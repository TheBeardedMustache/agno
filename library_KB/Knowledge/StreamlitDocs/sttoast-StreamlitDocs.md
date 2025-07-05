st.toast - Streamlit Docs

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

      *remove*

      * CALLOUTS

        ---
      * [st.success](/develop/api-reference/status/st.success)
      * [st.info](/develop/api-reference/status/st.info)
      * [st.warning](/develop/api-reference/status/st.warning)
      * [st.error](/develop/api-reference/status/st.error)
      * [st.exception](/develop/api-reference/status/st.exception)
      * OTHER

        ---
      * [st.progress](/develop/api-reference/status/st.progress)
      * [st.spinner](/develop/api-reference/status/st.spinner)
      * [st.status](/develop/api-reference/status/st.status)
      * [st.toast](/develop/api-reference/status/st.toast)
      * [st.balloons](/develop/api-reference/status/st.balloons)
      * [st.snow](/develop/api-reference/status/st.snow)
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
* [Status elements](/develop/api-reference/status)/
* [st.toast](/develop/api-reference/status/st.toast)

st.toast
--------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Display a short message, known as a notification "toast".

The toast appears in the app's top-right corner and disappears after four seconds.

Warning

st.toast is not compatible with Streamlit's [caching](https://docs.streamlit.io/develop/concepts/architecture/caching) and
cannot be called within a cached function.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/elements/toast.py#L38 "View st.toast source code on GitHub") | |
| --- | --- |
| st.toast(body, \*, icon=None) | |
| Parameters | |
| body (str) | The string to display as GitHub-flavored Markdown. Syntax information can be found at: <https://github.github.com/gfm>.  See the body parameter of [st.markdown](https://docs.streamlit.io/develop/api-reference/text/st.markdown) for additional, supported Markdown directives. |
| icon (str, None) | An optional emoji or icon to display next to the alert. If icon is None (default), no icon is displayed. If icon is a string, the following options are valid:   * A single-character emoji. For example, you can set icon="🚨"   or icon="🔥". Emoji short codes are not supported. * An icon from the Material Symbols library (rounded style) in the   format ":material/icon\_name:" where "icon\_name" is the name   of the icon in snake case.  For example, icon=":material/thumb\_up:" will display the   Thumb Up icon. Find additional icons in the [Material Symbols](https://fonts.google.com/icons?icon.set=Material+Symbols&icon.style=Rounded)   font library. |

#### Example

```

import streamlit as st

st.toast('Your edited image was saved!', icon='😍')

```

When multiple toasts are generated, they will stack. Hovering over a toast will
stop it from disappearing. When hovering ends, the toast will disappear after
four more seconds.

`import streamlit as st
import time
if st.button('Three cheers'):
st.toast('Hip!')
time.sleep(.5)
st.toast('Hip!')
time.sleep(.5)
st.toast('Hooray!', icon='🎉')`

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen *open\_in\_new*](https://doc-status-toast1.streamlit.app/?utm_medium=oembed)

Toast messages can also be updated. Assign `st.toast(my_message)` to a variable
and use the `.toast()` method to update it. Note: if a toast has already disappeared
or been dismissed, the update will not be seen.

`import streamlit as st
import time
def cook_breakfast():
msg = st.toast('Gathering ingredients...')
time.sleep(1)
msg.toast('Cooking...')
time.sleep(1)
msg.toast('Ready!', icon = "🥞")
if st.button('Cook breakfast'):
cook_breakfast()`

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen *open\_in\_new*](https://doc-status-toast2.streamlit.app/?utm_medium=oembed)

[Previous: st.status](/develop/api-reference/status/st.status)[Next: st.balloons](/develop/api-reference/status/st.balloons)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
