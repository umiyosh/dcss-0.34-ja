#!/bin/bash
# Sign an app bundle from the inside out.

set -euo pipefail

BUNDLE=${1:?Usage: sign-app.sh <app-bundle>}
IDENTITY=${MACOS_SIGN_IDENTITY:--}

[ -d "$BUNDLE" ] || { echo "No such bundle: $BUNDLE" >&2; exit 1; }

OPTS=(--force --sign "$IDENTITY")
if [ "$IDENTITY" != "-" ]; then
    OPTS+=(--options runtime --timestamp)
fi

main_exe=$(/usr/libexec/PlistBuddy -c 'Print :CFBundleExecutable' \
           "$BUNDLE/Contents/Info.plist" 2>/dev/null || true)

while IFS= read -r file_path; do
    [ "$file_path" = "$BUNDLE/Contents/MacOS/$main_exe" ] && continue
    file "$file_path" | grep -q 'Mach-O' || continue
    codesign "${OPTS[@]}" "$file_path"
done < <(find "$BUNDLE" -type f \( -perm +111 -o -name '*.dylib' \))

codesign "${OPTS[@]}" "$BUNDLE"
codesign --verify --deep --strict "$BUNDLE"
