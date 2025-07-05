st.logo - Streamlit Docs

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

    *add*
  + [API reference](/develop/api-reference)

    *remove*

    - PAGE ELEMENTS

      ---
    - [Write and magic](/develop/api-reference/write-magic)

      *add*
    - [Text elements](/develop/api-reference/text)

      *add*
    - [Data elements](/develop/api-reference/data)

      *add*
    - [Chart elements](/develop/api-reference/charts)

      *add*
    - [Input widgets](/develop/api-reference/widgets)

      *add*
    - [Media elements](/develop/api-reference/media)

      *remove*

      * [st.audio](/develop/api-reference/media/st.audio)
      * [st.image](/develop/api-reference/media/st.image)
      * [st.logo](/develop/api-reference/media/st.logo)
      * [st.video](/develop/api-reference/media/st.video)
    - [Layouts and containers](/develop/api-reference/layout)

      *add*
    - [Chat elements](/develop/api-reference/chat)

      *add*
    - [Status elements](/develop/api-reference/status)

      *add*
    - [Third-party components*open\_in\_new*](https://streamlit.io/components)
    - APPLICATION LOGIC

      ---
    - [Authentication and user info](/develop/api-reference/user)

      *add*
    - [Navigation and pages](/develop/api-reference/navigation)

      *add*
    - [Execution flow](/develop/api-reference/execution-flow)

      *add*
    - [Caching and state](/develop/api-reference/caching-and-state)

      *add*
    - [Connections and secrets](/develop/api-reference/connections)

      *add*
    - [Custom components](/develop/api-reference/custom-components)

      *add*
    - [Configuration](/develop/api-reference/configuration)

      *add*
    - TOOLS

      ---
    - [App testing](/develop/api-reference/app-testing)

      *add*
    - [Command line](/develop/api-reference/cli)

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
* [API reference](/develop/api-reference)/
* [Media elements](/develop/api-reference/media)/
* [st.logo](/develop/api-reference/media/st.logo)

st.logo
-------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Renders a logo in the upper-left corner of your app and its sidebar.

If st.logo is called multiple times within a page, Streamlit will
render the image passed in the last call. For the most consistent results,
call st.logo early in your page script and choose an image that works
well in both light and dark mode. Avoid empty margins around your image.

If your logo does not work well for both light and dark mode, consider
setting the theme and hiding the settings menu from users with the
[configuration option](https://docs.streamlit.io/develop/api-reference/configuration/config.toml)
client.toolbarMode="minimal".

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/commands/logo.py#L37 "View st.logo source code on GitHub") | |
| --- | --- |
| st.logo(image, \*, size="medium", link=None, icon\_image=None) | |
| Parameters | |
| image (Anything supported by st.image (except list)) | The image to display in the upper-left corner of your app and its sidebar. This can be any of the types supported by [st.image](https://docs.streamlit.io/develop/api-reference/media/st.image) except a list. If icon\_image is also provided, then Streamlit will only display image in the sidebar.  Streamlit scales the image to a max height set by size and a max width to fit within the sidebar. |
| size ("small", "medium", or "large") | The size of the image displayed in the upper-left corner of the app and its sidebar. The possible values are as follows:   * "small": 20px max height * "medium" (default): 24px max height * "large": 32px max height |
| link (str or None) | The external URL to open when a user clicks on the logo. The URL must start with "http://" or "https://". If link is None (default), the logo will not include a hyperlink. |
| icon\_image (Anything supported by st.image (except list) or None) | An optional, typically smaller image to replace image in the upper-left corner when the sidebar is closed. This can be any of the types supported by st.image except a list. If icon\_image is None (default), Streamlit will always display image in the upper-left corner, regardless of whether the sidebar is open or closed. Otherwise, Streamlit will render icon\_image in the upper-left corner of the app when the sidebar is closed.  Streamlit scales the image to a max height set by size and a max width to fit within the sidebar. If the sidebar is closed, the max width is retained from when it was last open.  For best results, pass a wide or horizontal image to image and a square image to icon\_image. Or, pass a square image to image and leave icon\_image=None. |

#### Examples

A common design practice is to use a wider logo in the sidebar, and a
smaller, icon-styled logo in your app's main body.

```

import streamlit as st

st.logo(
    LOGO_URL_LARGE,
    link="https://streamlit.io/gallery",
    icon_image=LOGO_URL_SMALL,
)

```

Try switching logos around in the following example:

```

import streamlit as st

HORIZONTAL_RED = "images/horizontal_red.png"
ICON_RED = "images/icon_red.png"
HORIZONTAL_BLUE = "images/horizontal_blue.png"
ICON_BLUE = "images/icon_blue.png"

options = [HORIZONTAL_RED, ICON_RED, HORIZONTAL_BLUE, ICON_BLUE]
sidebar_logo = st.selectbox("Sidebar logo", options, 0)
main_body_logo = st.selectbox("Main body logo", options, 1)

st.logo(sidebar_logo, icon_image=main_body_logo)
st.sidebar.markdown("Hi!")

```

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen *open\_in\_new*](https://doc-logo.streamlit.app//?utm_medium=oembed&)

[Previous: st.image](/develop/api-reference/media/st.image)[Next: st.video](/develop/api-reference/media/st.video)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
