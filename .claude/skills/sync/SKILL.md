---
name: sync
description: Keep the repo codex and the claude.ai Codex v5 artifact in step — rebuild and republish the page from the repo, or pull in edits made on the claude.ai side. Use at the start of a session, after outside edits, or when Patrick asks if things are in sync.
---

# Sync workflow

The repo (`codex_v5/`) is the master. The Codex v5 artifact (https://claude.ai/artifact/DejDv6wZUCqZGEpZDonS4W) is the readable copy on claude.ai.

**Check:** read the artifact with the Artifact tool. Extract its `window.ARCHIVE` texts and compare each with `codex_v5/`. Use a short Python script with `json.JSONDecoder().raw_decode`, unescaping `<\/` to `</`.
- **They match:** nothing to do.
- **The artifact is newer** (edited on claude.ai): show Patrick the differing files and a short summary of each change. Write the artifact's text into `codex_v5/` only after he confirms, then update the affected study notes and commit.
- **The repo is newer:** run `python3 scripts/build_codex_page.py` and republish `build/codex_v5.html` to that URL.

Also check `codex_v5/` for files missing from `scripts/codex_manifest.json`, since the build script reports these. Add new ones to the manifest with a label and group.
