# ForgeFlow Agent Studio

Phase-ordered desktop-native multi-agent orchestration platform.

## Local run
```bash
python -m ui.desktop.app
```

## Local tests
```bash
python -m pytest -q
```

## CI
- `.github/workflows/ci.yml` runs lint + tests on pushes and PRs.

## CD / Release executables
- `.github/workflows/release.yml` builds desktop bundles for Windows, macOS, Linux using PyInstaller.
- Tag a release as `vX.Y.Z` (example: `v0.1.0`).
- GitHub Actions will build binaries and upload them to the GitHub Release page as installable artifacts.
