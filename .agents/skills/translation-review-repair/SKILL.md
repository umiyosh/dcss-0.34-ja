---
name: translation-review-repair
description: >-
  Diagnose and repair a failing DCSS "Verify generated views" CI check when
  translation-review files are changed, missing, unexpected, or generated
  non-deterministically. Do not use for translation quality review.
---

# Translation Review Repair

Restore agreement between the translation resources, the deterministic
generator, and the committed `translation-review/` views. Treat files below
`crawl-ref/source/dat/descript/`, `crawl-ref/source/dat/database/`, and the
C++/Lua message call sites as source data; do not hand-edit generated Markdown
to make the check pass. Code-message translations live in
`crawl-ref/source/dat/database/ja/messages.txt`; dialogue views are under
`translation-review/database/` and code-message views under
`translation-review/code/`.

## Diagnose

Run this from the repository root:

```sh
python3 crawl-ref/source/util/translation_review.py --check
```

Use the reported category and file paths to choose the repair:

- `changed` or `missing`: run the generator, then inspect the generated diff.
- `unexpected`: establish why the current generator no longer emits the file.
  Common causes are a renamed or removed English resource, a reduced generator
  scope, or a file manually added below `translation-review/`.
- `non-deterministic`: fix the generator. Do not repeatedly regenerate or
  choose one output arbitrarily.

If the failure cannot be reproduced, compare the checked-out commit with the
CI commit before changing anything.

## Repair current views

For `changed` or `missing` output, run:

```sh
python3 crawl-ref/source/util/translation_review.py
git diff -- translation-review
```

Confirm that every generated change follows from the source or generator
change. Keep the source and its generated views in the same commit.

For `unexpected` output, remove only a reported file that is proven to be an
obsolete generated view. Regeneration does not delete old files. Do not delete
an English or Japanese resource to silence this error. If ownership of the
file is unclear, stop and report the ambiguity instead of deleting it.

## Repair non-deterministic generation

Reproduce the two-run mismatch and inspect
`crawl-ref/source/util/translation_review.py` and `code_message_review.py`
in the same directory for unstable inputs such as
unsorted traversal, timestamps, randomness, temporary paths, locale or
environment-dependent formatting, external data, or concurrency. Add a
focused regression test, fix the generating logic, and regenerate the views.
Do not normalize away a meaningful source difference.

## Verify and deliver

Run the focused checks:

```sh
PYTHONPATH=crawl-ref/source/util python3 -m unittest discover -s crawl-ref/source/util/tests -p '*_review.py'
python3 crawl-ref/source/util/translation_review.py --check
crawl-ref/source/util/checkwhite -n crawl-ref/source/util/translation_review.py crawl-ref/source/util/tests/test_translation_review.py
git diff HEAD --check
```

Inspect the full source and generated diff. Follow `AGENTS.md` for commit,
push, and pull-request handling. Report which category occurred, its cause,
the files repaired, the checks run, and any remaining uncertainty.
