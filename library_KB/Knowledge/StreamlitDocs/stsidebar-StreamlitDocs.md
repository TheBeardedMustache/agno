st.sidebar - Streamlit Docs

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
* [st.sidebar](/develop/api-reference/layout/st.sidebar)

st.sidebar
----------

Add widgets to sidebar
----------------------

Not only can you add interactivity to your app with widgets, you can organize them into a sidebar. Elements can be passed to `st.sidebar` using object notation and `with` notation.

The following two snippets are equivalent:

`# Object notation
st.sidebar.[element_name]`

`# "with" notation
with st.sidebar:
st.[element_name]`

Each element that's passed to `st.sidebar` is pinned to the left, allowing users to focus on the content in your app.

*star*

#### Tip

The sidebar is resizable! Drag and drop the right border of the sidebar to resize it! ↔️

Here's an example of how you'd add a selectbox and a radio button to your sidebar:

`import streamlit as st
# Using object notation
add_selectbox = st.sidebar.selectbox(
"How would you like to be contacted?",
("Email", "Home phone", "Mobile phone")
)
# Using "with" notation
with st.sidebar:
add_radio = st.radio(
"Choose a shipping method",
("Standard (5-15 days)", "Express (2-5 days)")
)`

*priority\_high*

#### Important

The only elements that aren't supported using object notation are `st.echo`, `st.spinner`, and `st.toast`. To use these elements, you must use `with` notation.

Here's an example of how you'd add [`st.echo`](/develop/api-reference/text/st.echo) and [`st.spinner`](/develop/api-reference/status/st.spinner) to your sidebar:

`import streamlit as st
import time
with st.sidebar:
with st.echo():
st.write("This code will be printed to the sidebar.")
with st.spinner("Loading..."):
time.sleep(5)
st.success("Done!")`

[Previous: st.popover](/develop/api-reference/layout/st.popover)[Next: st.tabs](/develop/api-reference/layout/st.tabs)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
