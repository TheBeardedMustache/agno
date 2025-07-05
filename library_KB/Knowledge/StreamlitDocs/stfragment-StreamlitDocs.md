﻿st.fragment - Streamlit Docs

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
* [st.fragment](/develop/api-reference/execution-flow/st.fragment)

st.fragment
-----------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Decorator to turn a function into a fragment which can rerun independently of the full app.

When a user interacts with an input widget created inside a fragment,
Streamlit only reruns the fragment instead of the full app. If
run\_every is set, Streamlit will also rerun the fragment at the
specified interval while the session is active, even if the user is not
interacting with your app.

To trigger an app rerun from inside a fragment, call st.rerun()
directly. To trigger a fragment rerun from within itself, call
st.rerun(scope="fragment"). Any values from the fragment that need to
be accessed from the wider app should generally be stored in Session State.

When Streamlit element commands are called directly in a fragment, the
elements are cleared and redrawn on each fragment rerun, just like all
elements are redrawn on each app rerun. The rest of the app is persisted
during a fragment rerun. When a fragment renders elements into externally
created containers, the elements will not be cleared with each fragment
rerun. Instead, elements will accumulate in those containers with each
fragment rerun, until the next app rerun.

Calling st.sidebar in a fragment is not supported. To write elements to
the sidebar with a fragment, call your fragment function inside a
with st.sidebar context manager.

Fragment code can interact with Session State, imported modules, and
other Streamlit elements created outside the fragment. Note that these
interactions are additive across multiple fragment reruns. You are
responsible for handling any side effects of that behavior.

Warning

* Fragments can only contain widgets in their main body. Fragments
  can't render widgets to externally created containers.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/runtime/fragment.py#L306 "View st.fragment source code on GitHub") | |
| --- | --- |
| st.fragment(func=None, \*, run\_every=None) | |
| Parameters | |
| func (callable) | The function to turn into a fragment. |
| run\_every (int, float, timedelta, str, or None) | The time interval between automatic fragment reruns. This can be one of the following:  * None (default). * An int or float specifying the interval in seconds. * A string specifying the time in a format supported by [Pandas'   Timedelta constructor](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.html),   e.g. "1d", "1.5 days", or "1h23s". * A timedelta object from [Python's built-in datetime library](https://docs.python.org/3/library/datetime.html#timedelta-objects),   e.g. timedelta(days=1).  If run\_every is None, the fragment will only rerun from user-triggered events. |

#### Examples

The following example demonstrates basic usage of
@st.fragment. As an analogy, "inflating balloons" is a slow process that happens
outside of the fragment. "Releasing balloons" is a quick process that happens inside
of the fragment.

```

import streamlit as st
import time

@st.fragment
def release_the_balloons():
    st.button("Release the balloons", help="Fragment rerun")
    st.balloons()

with st.spinner("Inflating balloons..."):
    time.sleep(5)
release_the_balloons()
st.button("Inflate more balloons", help="Full rerun")

```

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen *open\_in\_new*](https://doc-fragment-balloons.streamlit.app//?utm_medium=oembed&)

This next example demonstrates how elements both inside and outside of a
fragement update with each app or fragment rerun. In this app, clicking
"Rerun full app" will increment both counters and update all values
displayed in the app. In contrast, clicking "Rerun fragment" will only
increment the counter within the fragment. In this case, the st.write
command inside the fragment will update the app's frontend, but the two
st.write commands outside the fragment will not update the frontend.

```

import streamlit as st

if "app_runs" not in st.session_state:
    st.session_state.app_runs = 0
    st.session_state.fragment_runs = 0

@st.fragment
def my_fragment():
    st.session_state.fragment_runs += 1
    st.button("Rerun fragment")
    st.write(f"Fragment says it ran {st.session_state.fragment_runs} times.")

st.session_state.app_runs += 1
my_fragment()
st.button("Rerun full app")
st.write(f"Full app says it ran {st.session_state.app_runs} times.")
st.write(f"Full app sees that fragment ran {st.session_state.fragment_runs} times.")

```

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen *open\_in\_new*](https://doc-fragment.streamlit.app//?utm_medium=oembed&)

You can also trigger an app rerun from inside a fragment by calling
st.rerun.

```

import streamlit as st

if "clicks" not in st.session_state:
    st.session_state.clicks = 0

@st.fragment
def count_to_five():
    if st.button("Plus one!"):
        st.session_state.clicks += 1
        if st.session_state.clicks % 5 == 0:
            st.rerun()
    return

count_to_five()
st.header(f"Multiples of five clicks: {st.session_state.clicks // 5}")

if st.button("Check click count"):
    st.toast(f"## Total clicks: {st.session_state.clicks}")

```

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen *open\_in\_new*](https://doc-fragment-rerun.streamlit.app//?utm_medium=oembed&)

[Previous: st.form\_submit\_button](/develop/api-reference/execution-flow/st.form_submit_button)[Next: st.rerun](/develop/api-reference/execution-flow/st.rerun)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
