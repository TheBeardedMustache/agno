st.container - Streamlit Docs

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

      *add*
    - [Layouts and containers](/develop/api-reference/layout)

      *remove*

      * [st.columns](/develop/api-reference/layout/st.columns)
      * [st.container](/develop/api-reference/layout/st.container)
      * [st.dialog*link*](/develop/api-reference/execution-flow/st.dialog)
      * [st.empty](/develop/api-reference/layout/st.empty)
      * [st.expander](/develop/api-reference/layout/st.expander)
      * [st.form*link*](/develop/api-reference/execution-flow/st.form)
      * [st.popover](/develop/api-reference/layout/st.popover)
      * [st.sidebar](/develop/api-reference/layout/st.sidebar)
      * [st.tabs](/develop/api-reference/layout/st.tabs)
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
* [Layouts and containers](/develop/api-reference/layout)/
* [st.container](/develop/api-reference/layout/st.container)

st.container
------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Insert a multi-element container.

Inserts an invisible container into your app that can be used to hold
multiple elements. This allows you to, for example, insert multiple
elements into your app out of order.

To add elements to the returned container, you can use the with notation
(preferred) or just call methods directly on the returned object. See
examples below.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/elements/layouts.py#L50 "View st.container source code on GitHub") | |
| --- | --- |
| st.container(\*, height=None, border=None, key=None) | |
| Parameters | |
| height (int or None) | Desired height of the container expressed in pixels. If None (default) the container grows to fit its content. If a fixed height, scrolling is enabled for large content and a grey border is shown around the container to visually separate its scroll surface from the rest of the app.  Note  Use scrolling containers sparingly. If you use scrolling containers, avoid heights that exceed 500 pixels. Otherwise, the scroll surface of the container might cover the majority of the screen on mobile devices, which makes it hard to scroll the rest of the app. |
| border (bool or None) | Whether to show a border around the container. If None (default), a border is shown if the container is set to a fixed height and not shown otherwise. |
| key (str or None) | An optional string to give this container a stable identity.  Additionally, if key is provided, it will be used as CSS class name prefixed with st-key-. |

#### Examples

Inserting elements using with notation:

```

import streamlit as st

with st.container():
    st.write("This is inside the container")

    # You can call any Streamlit command, including custom components:
    st.bar_chart(np.random.randn(50, 3))

st.write("This is outside the container")

```

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen *open\_in\_new*](https://doc-container1.streamlit.app//?utm_medium=oembed&)

Inserting elements out of order:

```

import streamlit as st

container = st.container(border=True)
container.write("This is inside the container")
st.write("This is outside the container")

# Now insert some more in the container
container.write("This is inside too")

```

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen *open\_in\_new*](https://doc-container2.streamlit.app//?utm_medium=oembed&)

Using height to make a grid:

```

import streamlit as st

row1 = st.columns(3)
row2 = st.columns(3)

for col in row1 + row2:
    tile = col.container(height=120)
    tile.title(":balloon:")

```

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen *open\_in\_new*](https://doc-container3.streamlit.app//?utm_medium=oembed&)

Using height to create a scrolling container for long content:

```

import streamlit as st

long_text = "Lorem ipsum. " * 1000

with st.container(height=300):
    st.markdown(long_text)

```

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen *open\_in\_new*](https://doc-container4.streamlit.app//?utm_medium=oembed&)

[Previous: st.columns](/develop/api-reference/layout/st.columns)[Next: st.dialog](https://docs.streamlit.io/develop/api-reference/execution-flow/st.dialog)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
