st.rerun - Streamlit Docs

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

      *remove*

      * [st.dialog](/develop/api-reference/execution-flow/st.dialog)
      * [st.form](/develop/api-reference/execution-flow/st.form)
      * [st.form\_submit\_button](/develop/api-reference/execution-flow/st.form_submit_button)
      * [st.fragment](/develop/api-reference/execution-flow/st.fragment)
      * [st.rerun](/develop/api-reference/execution-flow/st.rerun)
      * [st.stop](/develop/api-reference/execution-flow/st.stop)
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
* [Execution flow](/develop/api-reference/execution-flow)/
* [st.rerun](/develop/api-reference/execution-flow/st.rerun)

st.rerun
--------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Rerun the script immediately.

When st.rerun() is called, Streamlit halts the current script run and
executes no further statements. Streamlit immediately queues the script to
rerun.

When using st.rerun in a fragment, you can scope the rerun to the
fragment. However, if a fragment is running as part of a full-app rerun,
a fragment-scoped rerun is not allowed.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/commands/execution_control.py#L102 "View st.rerun source code on GitHub") | |
| --- | --- |
| st.rerun(\*, scope="app") | |
| Parameters | |
| scope ("app" or "fragment") | Specifies what part of the app should rerun. If scope is "app" (default), the full app reruns. If scope is "fragment", Streamlit only reruns the fragment from which this command is called.  Setting scope="fragment" is only valid inside a fragment during a fragment rerun. If st.rerun(scope="fragment") is called during a full-app rerun or outside of a fragment, Streamlit will raise a StreamlitAPIException. |

### Caveats for `st.rerun`

`st.rerun` is one of the tools to control the logic of your app. While it is great for prototyping, there can be adverse side effects:

* Additional script runs may be inefficient and slower.
* Excessive reruns may complicate your app's logic and be harder to follow.
* If misused, infinite looping may crash your app.

In many cases where `st.rerun` works, [callbacks](/develop/api-reference/caching-and-state/st.session_state#use-callbacks-to-update-session-state) may be a cleaner alternative. [Containers](/develop/api-reference/layout) may also be helpful.

### A simple example in three variations

###### Using `st.rerun` to update an earlier header

`import streamlit as st
if "value" not in st.session_state:
st.session_state.value = "Title"
##### Option using st.rerun #####
st.header(st.session_state.value)
if st.button("Foo"):
st.session_state.value = "Foo"
st.rerun()`

###### Using a callback to update an earlier header

`##### Option using a callback #####
st.header(st.session_state.value)
def update_value():
st.session_state.value = "Bar"
st.button("Bar", on_click=update_value)`

###### Using containers to update an earlier header

`##### Option using a container #####
container = st.container()
if st.button("Baz"):
st.session_state.value = "Baz"
container.header(st.session_state.value)`

[Previous: st.fragment](/develop/api-reference/execution-flow/st.fragment)[Next: st.stop](/develop/api-reference/execution-flow/st.stop)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
