st.dialog - Streamlit Docs

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
* [st.dialog](/develop/api-reference/execution-flow/st.dialog)

st.dialog
---------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Function decorator to create a modal dialog.

A function decorated with @st.dialog becomes a dialog
function. When you call a dialog function, Streamlit inserts a modal dialog
into your app. Streamlit element commands called within the dialog function
render inside the modal dialog.

The dialog function can accept arguments that can be passed when it is
called. Any values from the dialog that need to be accessed from the wider
app should generally be stored in Session State.

A user can dismiss a modal dialog by clicking outside of it, clicking the
"**X**" in its upper-right corner, or pressing ESC on their keyboard.
Dismissing a modal dialog does not trigger an app rerun. To close the modal
dialog programmatically, call st.rerun() explicitly inside of the
dialog function.

st.dialog inherits behavior from [st.fragment](https://docs.streamlit.io/develop/api-reference/execution-flow/st.fragment).
When a user interacts with an input widget created inside a dialog function,
Streamlit only reruns the dialog function instead of the full script.

Calling st.sidebar in a dialog function is not supported.

Dialog code can interact with Session State, imported modules, and other
Streamlit elements created outside the dialog. Note that these interactions
are additive across multiple dialog reruns. You are responsible for
handling any side effects of that behavior.

Warning

Only one dialog function may be called in a script run, which means
that only one dialog can be open at any given time.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/elements/dialog_decorator.py#L133 "View st.dialog source code on GitHub") | |
| --- | --- |
| st.dialog(title, \*, width="small") | |
| Parameters | |
| title (str) | The title to display at the top of the modal dialog. It cannot be empty. |
| width ("small", "large") | The width of the modal dialog. If width is "small (default), the modal dialog will be 500 pixels wide. If width is "large", the modal dialog will be about 750 pixels wide. |

#### Examples

The following example demonstrates the basic usage of @st.dialog.
In this app, clicking "**A**" or "**B**" will open a modal dialog and prompt you
to enter a reason for your vote. In the modal dialog, click "**Submit**" to record
your vote into Session State and rerun the app. This will close the modal dialog
since the dialog function is not called during the full-script rerun.

```

import streamlit as st

@st.dialog("Cast your vote")
def vote(item):
    st.write(f"Why is {item} your favorite?")
    reason = st.text_input("Because...")
    if st.button("Submit"):
        st.session_state.vote = {"item": item, "reason": reason}
        st.rerun()

if "vote" not in st.session_state:
    st.write("Vote for your favorite")
    if st.button("A"):
        vote("A")
    if st.button("B"):
        vote("B")
else:
    f"You voted for {st.session_state.vote['item']} because {st.session_state.vote['reason']}"

```

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen *open\_in\_new*](https://doc-modal-dialog.streamlit.app//?utm_medium=oembed&)

[Previous: Execution flow](/develop/api-reference/execution-flow)[Next: st.form](/develop/api-reference/execution-flow/st.form)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
