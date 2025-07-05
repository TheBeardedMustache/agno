# SoulLanguage [![Docs](https://github.com/owner/SoulLanguage/actions/workflows/docs.yml/badge.svg)](https://owner.github.io/SoulLanguage/)

SoulLanguage is a tiny reference implementation of the Soul Interpreter Language (SIL) v2.1.  It focuses on providing encoders and decoders for the nine optional frame extensions described in the specification.

## Installation

Install the dependencies with pip:

```bash
pip install -r requirements/dev.txt
```

## Running Tests

Quality checks use **black**, **flake8** and **pytest**. Run them from the repository root:

```bash
black src tests --check
flake8 src tests
pytest
```

## Extension Modules

The extensions are implemented (or reserved) as modules under `src/`:

1. **Ternary Typed Token** – 3‑trit header handled by `ttt.py`.
2. **Δt window and QoS class** – implemented in `frame.py`.
3. **Extension 3** – reserved for future features.
4. **Extension 4** – reserved for future features.
5. **Extension 5** – reserved for future features.
6. **Extension 6** – reserved for future features.
7. **Run‑length text encoding** – provided by `extension7.py`.
8. **Extension 8** – reserved for future features.
9. **Ethical Exception Register** – planned for future implementation.


## Release

Releases are automated via GitHub Actions. Provide a `PYPI_TOKEN` secret for uploading to PyPI.

