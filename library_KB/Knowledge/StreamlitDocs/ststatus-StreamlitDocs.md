st.status - Streamlit Docs

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
* [st.status](/develop/api-reference/status/st.status)

st.status
---------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Insert a status container to display output from long-running tasks.

Inserts a container into your app that is typically used to show the status and
details of a process or task. The container can hold multiple elements and can
be expanded or collapsed by the user similar to st.expander.
When collapsed, all that is visible is the status icon and label.

The label, state, and expanded state can all be updated by calling .update()
on the returned object. To add elements to the returned container, you can
use with notation (preferred) or just call methods directly on the returned
object.

By default, st.status() initializes in the "running" state. When called using
with notation, it automatically updates to the "complete" state at the end
of the "with" block. See examples below for more details.

Note

All content within the status container is computed and sent to the
frontend, even if the status container is closed.

To follow best design practices and maintain a good appearance on
all screen sizes, don't nest status containers.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/elements/layouts.py#L816 "View st.status source code on GitHub") | |
| --- | --- |
| st.status(label, \*, expanded=False, state="running", width="stretch") | |
| Parameters | |
| label (str) | The initial label of the status container. The label can optionally contain GitHub-flavored Markdown of the following types: Bold, Italics, Strikethroughs, Inline Code, Links, and Images. Images display like icons, with a max height equal to the font height.  Unsupported Markdown elements are unwrapped so only their children (text contents) render. Display unsupported elements as literal characters by backslash-escaping them. E.g., "1\. Not an ordered list".  See the body parameter of [st.markdown](https://docs.streamlit.io/develop/api-reference/text/st.markdown) for additional, supported Markdown directives. |
| expanded (bool) | If True, initializes the status container in "expanded" state. Defaults to False (collapsed). |
| state ("running", "complete", or "error") | The initial state of the status container which determines which icon is shown:   * running (default): A spinner icon is shown. * complete: A checkmark icon is shown. * error: An error icon is shown. |
| width ("stretch" or int) | The width of the status container. This can be one of the following:   * "stretch" (default): The width of the container matches the   width of the parent container. * An integer specifying the width in pixels: The container has a   fixed width. If the specified width is greater than the width of   the parent container, the width of the container matches the width   of the parent container. |
|  |  |
| --- | --- |
| Returns | |
| (StatusContainer) | A mutable status container that can hold multiple elements. The label, state, and expanded state can be updated after creation via .update(). |

#### Examples

You can use the with notation to insert any element into an status container:

```

import time
import streamlit as st

with st.status("Downloading data..."):
    st.write("Searching for data...")
    time.sleep(2)
    st.write("Found URL.")
    time.sleep(1)
    st.write("Downloading data...")
    time.sleep(1)

st.button("Rerun")

```

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen *open\_in\_new*](https://doc-status.streamlit.app//?utm_medium=oembed&)

You can also use .update() on the container to change the label, state,
or expanded state:

```

import time
import streamlit as st

with st.status("Downloading data...", expanded=True) as status:
    st.write("Searching for data...")
    time.sleep(2)
    st.write("Found URL.")
    time.sleep(1)
    st.write("Downloading data...")
    time.sleep(1)
    status.update(
        label="Download complete!", state="complete", expanded=False
    )

st.button("Rerun")

```

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen *open\_in\_new*](https://doc-status-update.streamlit.app//?utm_medium=oembed&)

StatusContainer.update
----------------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Update the status container.

Only specified arguments are updated. Container contents and unspecified
arguments remain unchanged.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/elements/lib/mutable_status_container.py#L108 "View st.update source code on GitHub") | |
| --- | --- |
| StatusContainer.update(\*, label=None, expanded=None, state=None) | |
| Parameters | |
| label (str or None) | A new label of the status container. If None, the label is not changed. |
| expanded (bool or None) | The new expanded state of the status container. If None, the expanded state is not changed. |
| state ("running", "complete", "error", or None) | The new state of the status container. This mainly changes the icon. If None, the state is not changed. |

[Previous: st.spinner](/develop/api-reference/status/st.spinner)[Next: st.toast](/develop/api-reference/status/st.toast)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
