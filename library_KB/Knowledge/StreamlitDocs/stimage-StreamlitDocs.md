st.image - Streamlit Docs

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
* [st.image](/develop/api-reference/media/st.image)

st.image
--------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Display an image or list of images.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/elements/image.py#L47 "View st.image source code on GitHub") | |
| --- | --- |
| st.image(image, caption=None, width=None, use\_column\_width=None, clamp=False, channels="RGB", output\_format="auto", \*, use\_container\_width=False) | |
| Parameters | |
| image (numpy.ndarray, BytesIO, str, Path, or list of these) | The image to display. This can be one of the following:   * A URL (string) for a hosted image. * A path to a local image file. The path can be a str   or Path object. Paths can be absolute or relative to the   working directory (where you execute streamlit run). * An SVG string like <svg xmlns=...</svg>. * A byte array defining an image. This includes monochrome images of   shape (w,h) or (w,h,1), color images of shape (w,h,3), or RGBA   images of shape (w,h,4), where w and h are the image width and   height, respectively. * A list of any of the above. Streamlit displays the list as a   row of images that overflow to additional rows as needed. |
| caption (str or list of str) | Image caption(s). If this is None (default), no caption is displayed. If image is a list of multiple images, caption must be a list of captions (one caption for each image) or None.  Captions can optionally contain GitHub-flavored Markdown. Syntax information can be found at: <https://github.github.com/gfm>.  See the body parameter of [st.markdown](https://docs.streamlit.io/develop/api-reference/text/st.markdown) for additional, supported Markdown directives. |
| width (int or None) | Image width. If this is None (default), Streamlit will use the image's native width, up to the width of the parent container. When using an SVG image without a default width, you should declare width or use use\_container\_width=True. |
| use\_column\_width ("auto", "always", "never", or bool) | *delete* use\_column\_width is deprecated and will be removed in a future release. Please use the use\_container\_width parameter instead.  If "auto", set the image's width to its natural size, but do not exceed the width of the column. If "always" or True, set the image's width to the column width. If "never" or False, set the image's width to its natural size. Note: if set, use\_column\_width takes precedence over the width parameter. |
| clamp (bool) | Whether to clamp image pixel values to a valid range (0-255 per channel). This is only used for byte array images; the parameter is ignored for image URLs and files. If this is False (default) and an image has an out-of-range value, a RuntimeError will be raised. |
| channels ("RGB" or "BGR") | The color format when image is an nd.array. This is ignored for other image types. If this is "RGB" (default), image[:, :, 0] is the red channel, image[:, :, 1] is the green channel, and image[:, :, 2] is the blue channel. For images coming from libraries like OpenCV, you should set this to "BGR" instead. |
| output\_format ("JPEG", "PNG", or "auto") | The output format to use when transferring the image data. If this is "auto" (default), Streamlit identifies the compression type based on the type and format of the image. Photos should use the "JPEG" format for lossy compression while diagrams should use the "PNG" format for lossless compression. |
| use\_container\_width (bool) | Whether to override width with the width of the parent container. If use\_container\_width is False (default), Streamlit sets the image's width according to width. If use\_container\_width is True, Streamlit sets the width of the image to match the width of the parent container. |

#### Example

```

import streamlit as st
st.image("sunrise.jpg", caption="Sunrise by the mountains")

```

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen *open\_in\_new*](https://doc-image.streamlit.app//?utm_medium=oembed&)

[Previous: st.audio](/develop/api-reference/media/st.audio)[Next: st.logo](/develop/api-reference/media/st.logo)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
