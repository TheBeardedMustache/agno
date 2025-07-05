# Hello Glyph

This tutorial shows how to translate a query into SIL frames and view the raw encoding.

1. **Install the package**

   ```bash
   pip install soul-language
   ```

2. **Run SQLy with a simple query**

   ```bash
   python -m sqly.cli "SELECT glyph FROM glyphs" --show-frames
   ```

3. **Inspect the hex-dump**

   The command will print the lowered frame encodings as a hex string.
