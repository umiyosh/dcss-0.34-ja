#!/bin/bash
# Submit a signed app bundle for notarization and staple the result.

set -euo pipefail

BUNDLE=${1:?Usage: notarize-app.sh <app-bundle>}

: "${NOTARY_KEY_PATH:?NOTARY_KEY_PATH is required}"
: "${NOTARY_KEY_ID:?NOTARY_KEY_ID is required}"
: "${NOTARY_ISSUER_ID:?NOTARY_ISSUER_ID is required}"

[ -d "$BUNDLE" ] || { echo "No such bundle: $BUNDLE" >&2; exit 1; }

submission="${TMPDIR:-/tmp}/notarize-$$.zip"
trap 'rm -f "$submission"' EXIT

ditto -c -k --keepParent "$BUNDLE" "$submission"
xcrun notarytool submit "$submission" \
    --key "$NOTARY_KEY_PATH" \
    --key-id "$NOTARY_KEY_ID" \
    --issuer "$NOTARY_ISSUER_ID" \
    --wait
xcrun stapler staple "$BUNDLE"
xcrun stapler validate "$BUNDLE"
