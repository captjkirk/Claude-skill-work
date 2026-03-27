#!/bin/bash
# Blackthorn OBM Plugin — Quick Packager
# Run from anywhere: bash /path/to/blackthorn-obm/package.sh

set -e

PLUGIN_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
OUTPUT_DIR="$(find /sessions/*/mnt/Cowork-OS/outputs/skill-updates -maxdepth 0 -type d 2>/dev/null | head -1)"
PLUGIN_FILE="blackthorn-obm.plugin"
VALIDATE="$(find /sessions/*/mnt/.claude/skills/skill-creator/scripts/quick_validate.py -maxdepth 0 2>/dev/null | head -1)"

# Sync: pull updated AND new skills from .claude/skills/ into plugin source
# Skills in this list stay as standalones and are never added to the plugin
EXCLUDE=("brainstorming" "docx" "pdf" "pptx" "xlsx")

STANDALONE_DIR="$(find /sessions/*/mnt/.claude/skills -maxdepth 0 -type d 2>/dev/null | head -1)"
if [ -n "$STANDALONE_DIR" ]; then
    SYNCED=()
    ADDED=()
    for standalone_dir in "$STANDALONE_DIR"/*/; do
        skill=$(basename "$standalone_dir")
        standalone_skill="$standalone_dir/SKILL.md"
        plugin_skill="$PLUGIN_DIR/skills/$skill/SKILL.md"
        [ -f "$standalone_skill" ] || continue
        # Skip excluded skills
        [[ " ${EXCLUDE[*]} " =~ " $skill " ]] && continue
        if [ ! -f "$plugin_skill" ]; then
            mkdir -p "$PLUGIN_DIR/skills/$skill"
            cp "$standalone_skill" "$plugin_skill"
            ADDED+=("$skill")
        elif [ "$standalone_skill" -nt "$plugin_skill" ]; then
            cp "$standalone_skill" "$plugin_skill"
            SYNCED+=("$skill")
        fi
    done
    [ ${#ADDED[@]} -gt 0 ]  && echo "➕ New skills added to plugin: ${ADDED[*]}"
    [ ${#SYNCED[@]} -gt 0 ] && echo "🔄 Updated skills synced: ${SYNCED[*]}"
fi

echo ""
echo "🔍 Validating skills..."
PASS=true
for skill_dir in "$PLUGIN_DIR/skills"/*/; do
    skill=$(basename "$skill_dir")
    result=$(python3 "$VALIDATE" "$skill_dir" 2>&1)
    if [ $? -ne 0 ]; then
        echo "  ❌ FAIL: $skill — $result"
        PASS=false
    fi
done

if [ "$PASS" = false ]; then
    echo ""
    echo "Validation failed — fix errors above before packaging."
    exit 1
fi

echo "  ✅ All skills valid"
echo ""
echo "📦 Packaging..."
cd "$PLUGIN_DIR"
zip -r /tmp/"$PLUGIN_FILE" . -x "*.DS_Store" -x "__pycache__/*" -x "*.pyc" -x "package.sh" -q

SIZE=$(du -h /tmp/"$PLUGIN_FILE" | cut -f1)

if [ -n "$OUTPUT_DIR" ]; then
    cp /tmp/"$PLUGIN_FILE" "$OUTPUT_DIR/$PLUGIN_FILE"
    echo "  ✅ Saved to: $OUTPUT_DIR/$PLUGIN_FILE ($SIZE)"
else
    echo "  ✅ Packaged to: /tmp/$PLUGIN_FILE ($SIZE)"
    echo "  ⚠️  Could not find Cowork-OS outputs folder — copy manually from /tmp/"
fi

echo ""

# Report any standalone duplicates that should be removed via the Cowork UI
STANDALONE_DIR="$(find /sessions/*/mnt/.claude/skills -maxdepth 0 -type d 2>/dev/null | head -1)"
if [ -n "$STANDALONE_DIR" ]; then
    DUPES=()
    for skill_dir in "$PLUGIN_DIR/skills"/*/; do
        skill=$(basename "$skill_dir")
        if [ -d "$STANDALONE_DIR/$skill" ]; then
            DUPES+=("$skill")
        fi
    done
    if [ ${#DUPES[@]} -gt 0 ]; then
        echo "⚠️  Standalone duplicates still installed (remove via Cowork Skills UI):"
        for d in "${DUPES[@]}"; do echo "   - $d"; done
    else
        echo "✅ No standalone duplicates found"
    fi
fi

echo "Done. Install via Cowork → outputs/skill-updates/$PLUGIN_FILE"
