Static file serving - Streamlit Docs

[![](/logo.svg)

#### Documentation](/)

*search*

Search

* [*rocket\_launch*

  Get started](/get-started)
  + [Installation](/get-started/installation)

    *add*
  + [Fundamentals](/get-started/fundamentals)

    *add*
  + [First steps](/get-started/tutorials)

    *add*
* [*code*

  Develop](/develop)
  + [Concepts](/develop/concepts)

    *remove*

    - CORE

      ---
    - [Architecture and execution](/develop/concepts/architecture)

      *add*
    - [Multipage apps](/develop/concepts/multipage-apps)

      *add*
    - [App design](/develop/concepts/design)

      *add*
    - ADDITIONAL

      ---
    - [Connections, secrets, and authentication](/develop/concepts/connections)

      *add*
    - [Custom components](/develop/concepts/custom-components)

      *add*
    - [Configuration and theming](/develop/concepts/configuration)

      *remove*

      * [Configuration options](/develop/concepts/configuration/options)
      * [HTTPS support](/develop/concepts/configuration/https-support)
      * [Serving static files](/develop/concepts/configuration/serving-static-files)
      * THEMING

        ---
      * [Customize your theme](/develop/concepts/configuration/theming)
      * [Customize colors and borders](/develop/concepts/configuration/theming-customize-colors-and-borders)
      * [Customize fonts](/develop/concepts/configuration/theming-customize-fonts)
    - [App testing](/develop/concepts/app-testing)

      *add*
  + [API reference](/develop/api-reference)

    *add*
  + [Tutorials](/develop/tutorials)

    *add*
  + [Quick reference](/develop/quick-reference)

    *add*
* [*web\_asset*

  Deploy](/deploy)
  + [Concepts](/deploy/concepts)

    *add*
  + [Streamlit Community Cloud](/deploy/streamlit-community-cloud)

    *add*
  + [Snowflake](/deploy/snowflake)
  + [Other platforms](/deploy/tutorials)

    *add*
* [*school*

  Knowledge base](/knowledge-base)
  + [FAQ](/knowledge-base/using-streamlit)
  + [Installing dependencies](/knowledge-base/dependencies)
  + [Deployment issues](/knowledge-base/deploy)

* [Home](/)/
* [Develop](/develop)/
* [Concepts](/develop/concepts)/
* [Configuration and theming](/develop/concepts/configuration)/
* [Serving static files](/develop/concepts/configuration/serving-static-files)

Static file serving
===================

Streamlit apps can host and serve small, static media files to support media embedding use cases that
won't work with the normal [media elements](/develop/api-reference/media).

To enable this feature, set `enableStaticServing = true` under `[server]` in your config file,
or environment variable `STREAMLIT_SERVER_ENABLE_STATIC_SERVING=true`.

Media stored in the folder `./static/` relative to the running app file is served at path
`app/static/[filename]`, such as `http://localhost:8501/app/static/cat.png`.

Details on usage
----------------

* Files with the following extensions will be served normally:
  + Common image types: `.jpg`, `.jpeg`, `.png`, `.gif`
  + Common font types: `.otf`, `.ttf`, `.woff`, `.woff2`
  + Other types: `.pdf`, `.xml`, `.json`
    Any other file will be sent with header `Content-Type:text/plain` which will cause browsers to render in plain text.
    This is included for security - other file types that need to render should be hosted outside the app.
* Streamlit also sets `X-Content-Type-Options:nosniff` for all files rendered from the static directory.
* For apps running on Streamlit Community Cloud:
  + Files available in the Github repo will always be served. Any files generated while the app is running,
    such as based on user interaction (file upload, etc), are not guaranteed to persist across user sessions.
  + Apps which store and serve many files, or large files, may run into resource limits and be shut down.

Example usage
-------------

* Put an image `cat.png` in the folder `./static/`
* Add `enableStaticServing = true` under `[server]` in your `.streamlit/config.toml`
* Any media in the `./static/` folder is served at the relative URL like `app/static/cat.png`

`# .streamlit/config.toml
[server]
enableStaticServing = true`

`# app.py
import streamlit as st
with st.echo():
st.title("CAT")
st.markdown("[![Click me](app/static/cat.png)](https://streamlit.io)")`

Additional resources:

* <https://docs.streamlit.io/develop/concepts/configuration>
* <https://static-file-serving.streamlit.app/>

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen *open\_in\_new*](https://static-file-serving.streamlit.app/?utm_medium=oembed)

[Previous: HTTPS support](/develop/concepts/configuration/https-support)[Next: Customize your theme](/develop/concepts/configuration/theming)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
