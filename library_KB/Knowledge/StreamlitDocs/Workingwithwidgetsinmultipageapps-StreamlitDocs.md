﻿Working with widgets in multipage apps - Streamlit Docs

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

      *remove*

      * [Overview](/develop/concepts/multipage-apps/overview)
      * [Page and navigation](/develop/concepts/multipage-apps/page-and-navigation)
      * [Pages directory](/develop/concepts/multipage-apps/pages-directory)
      * [Working with widgets](/develop/concepts/multipage-apps/widgets)
    - [App design](/develop/concepts/design)

      *add*
    - ADDITIONAL

      ---
    - [Connections, secrets, and authentication](/develop/concepts/connections)

      *add*
    - [Custom components](/develop/concepts/custom-components)

      *add*
    - [Configuration and theming](/develop/concepts/configuration)

      *add*
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
* [Multipage apps](/develop/concepts/multipage-apps)/
* [Working with widgets](/develop/concepts/multipage-apps/widgets)

Working with widgets in multipage apps
======================================

When you create a widget in a Streamlit app, Streamlit generates a widget ID and uses it to make your widget stateful. As your app reruns with user interaction, Streamlit keeps track of the widget's value by associating its value to its ID. In particular, a widget's ID depends on the page where it's created. If you define an identical widget on two different pages, then the widget will reset to its default value when you switch pages.

This guide explains three strategies to deal with the behavior if you'd like to have a widget remain stateful across all pages. If don't want a widget to appear on all pages, but you do want it to remain stateful when you navigate away from its page (and then back), Options 2 and 3 can be used. For detailed information about these strategies, see [Understanding widget behavior](/develop/concepts/architecture/widget-behavior).

Option 1 (preferred): Execute your widget command in your entrypoint file
-------------------------------------------------------------------------

When you define your multipage app with `st.Page` and `st.navigation`, your entrypoint file becomes a frame of common elements around your pages. When you execute a widget command in your entrypoint file, Streamlit associates the widget to your entrypoint file instead of a particular page. Since your entrypoint file is executed in every app rerun, any widget in your entrypoint file will remain stateful as your users switch between pages.

This method does not work if you define your app with the `pages/` directory.

The following example includes a selectbox and slider in the sidebar that are rendered and stateful on all pages. The widgets each have an assigned key so you can access their values through Session State within a page.

**Directory structure:**

`your-repository/
├── page_1.py
├── page_2.py
└── streamlit_app.py`

**`streamlit_app.py`:**

`import streamlit as st
pg = st.navigation([st.Page("page_1.py"), st.Page("page_2.py")])
st.sidebar.selectbox("Group", ["A","B","C"], key="group")
st.sidebar.slider("Size", 1, 5, key="size")
pg.run()`

Option 2: Save your widget values into a dummy key in Session State
-------------------------------------------------------------------

If you want to navigate away from a widget and return to it while keeping its value, or if you want to use the same widget on multiple pages, use a separate key in `st.session_state` to save the value independently from the widget. In this example, a temporary key is used with a widget. The temporary key uses an underscore prefix. Hence, `"_my_key"` is used as the widget key, but the data is copied to `"my_key"` to preserve it between pages.

`import streamlit as st
def store_value():
# Copy the value to the permanent key
st.session_state["my_key"] = st.session_state["_my_key"]
# Copy the saved value to the temporary key
st.session_state["_my_key"] = st.session_state["my_key"]
st.number_input("Number of filters", key="_my_key", on_change=store_value)`

If this is functionalized to work with multiple widgets, it could look something like this:

`import streamlit as st
def store_value(key):
st.session_state[key] = st.session_state["_"+key]
def load_value(key):
st.session_state["_"+key] = st.session_state[key]
load_value("my_key")
st.number_input("Number of filters", key="_my_key", on_change=store_value, args=["my_key"])`

Option 3: Interrupt the widget clean-up process
-----------------------------------------------

When Streamlit gets to the end of an app run, it will delete the data for any widgets that were not rendered. This includes data for any widget not associated to the current page. However, if you re-save a key-value pair in an app run, Streamlit will not associate the key-value pair to any widget until you execute a widget command again with that key.

As a result, if you have the following code at the top of every page, any widget with the key `"my_key"` will retain its value wherever it's rendered (or not). Alternatively, if you are using `st.navigation` and `st.Page`, you can include this once in your entrypoint file before executing your page.

`if "my_key" in st.session_state:
st.session_state.my_key = st.session_state.my_key`

[Previous: Pages directory](/develop/concepts/multipage-apps/pages-directory)[Next: App design](/develop/concepts/design)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
