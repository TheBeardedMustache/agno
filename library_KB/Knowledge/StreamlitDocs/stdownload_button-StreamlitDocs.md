﻿st.download\_button - Streamlit Docs

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

      *remove*

      * BUTTONS

        ---
      * [st.button](/develop/api-reference/widgets/st.button)
      * [st.download\_button](/develop/api-reference/widgets/st.download_button)
      * [st.form\_submit\_button*link*](/develop/api-reference/execution-flow/st.form_submit_button)
      * [st.link\_button](/develop/api-reference/widgets/st.link_button)
      * [st.page\_link](/develop/api-reference/widgets/st.page_link)
      * SELECTIONS

        ---
      * [st.checkbox](/develop/api-reference/widgets/st.checkbox)
      * [st.color\_picker](/develop/api-reference/widgets/st.color_picker)
      * [st.feedback](/develop/api-reference/widgets/st.feedback)
      * [st.multiselect](/develop/api-reference/widgets/st.multiselect)
      * [st.pills](/develop/api-reference/widgets/st.pills)
      * [st.radio](/develop/api-reference/widgets/st.radio)
      * [st.segmented\_control](/develop/api-reference/widgets/st.segmented_control)
      * [st.selectbox](/develop/api-reference/widgets/st.selectbox)
      * [st.select\_slider](/develop/api-reference/widgets/st.select_slider)
      * [st.toggle](/develop/api-reference/widgets/st.toggle)
      * NUMERIC

        ---
      * [st.number\_input](/develop/api-reference/widgets/st.number_input)
      * [st.slider](/develop/api-reference/widgets/st.slider)
      * DATE AND TIME

        ---
      * [st.date\_input](/develop/api-reference/widgets/st.date_input)
      * [st.time\_input](/develop/api-reference/widgets/st.time_input)
      * TEXT

        ---
      * [st.chat\_input*link*](/develop/api-reference/chat/st.chat_input)
      * [st.text\_area](/develop/api-reference/widgets/st.text_area)
      * [st.text\_input](/develop/api-reference/widgets/st.text_input)
      * MEDIA AND FILES

        ---
      * [st.audio\_input](/develop/api-reference/widgets/st.audio_input)
      * [st.camera\_input](/develop/api-reference/widgets/st.camera_input)
      * [st.data\_editor*link*](/develop/api-reference/data/st.data_editor)
      * [st.file\_uploader](/develop/api-reference/widgets/st.file_uploader)
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
* [Input widgets](/develop/api-reference/widgets)/
* [st.download\_button](/develop/api-reference/widgets/st.download_button)

st.download\_button
-------------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Display a download button widget.

This is useful when you would like to provide a way for your users
to download a file directly from your app.

Note that the data to be downloaded is stored in-memory while the
user is connected, so it's a good idea to keep file sizes under a
couple hundred megabytes to conserve memory.

If you want to prevent your app from rerunning when a user clicks the
download button, wrap the download button in a [fragment](https://docs.streamlit.io/develop/concepts/architecture/fragments).

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/elements/widgets/button.py#L258 "View st.download_button source code on GitHub") | |
| --- | --- |
| st.download\_button(label, data, file\_name=None, mime=None, key=None, help=None, on\_click="rerun", args=None, kwargs=None, \*, type="secondary", icon=None, disabled=False, use\_container\_width=False) | |
| Parameters | |
| label (str) | A short label explaining to the user what this button is for. The label can optionally contain GitHub-flavored Markdown of the following types: Bold, Italics, Strikethroughs, Inline Code, Links, and Images. Images display like icons, with a max height equal to the font height.  Unsupported Markdown elements are unwrapped so only their children (text contents) render. Display unsupported elements as literal characters by backslash-escaping them. E.g., "1\. Not an ordered list".  See the body parameter of [st.markdown](https://docs.streamlit.io/develop/api-reference/text/st.markdown) for additional, supported Markdown directives. |
| data (str, bytes, or file) | The contents of the file to be downloaded.  To prevent unncecessary recomputation, use caching when converting your data for download. For more information, see the Example 1 below. |
| file\_name (str) | An optional string to use as the name of the file to be downloaded, such as "my\_file.csv". If not specified, the name will be automatically generated. |
| mime (str or None) | The MIME type of the data. If this is None (default), Streamlit sets the MIME type depending on the value of data as follows:   * If data is a string or textual file (i.e. str or   io.TextIOWrapper object), Streamlit uses the "text/plain"   MIME type. * If data is a binary file or bytes (i.e. bytes,   io.BytesIO, io.BufferedReader, or io.RawIOBase   object), Streamlit uses the "application/octet-stream" MIME type.   For more information about MIME types, see <https://www.iana.org/assignments/media-types/media-types.xhtml>. |
| key (str or int) | An optional string or integer to use as the unique key for the widget. If this is omitted, a key will be generated for the widget based on its content. No two widgets may have the same key. |
| help (str or None) | A tooltip that gets displayed when the button is hovered over. If this is None (default), no tooltip is displayed.  The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of st.markdown. |
| on\_click (callable, "rerun", "ignore", or None) | How the button should respond to user interaction. This controls whether or not the button triggers a rerun and if a callback function is called. This can be one of the following values:   * "rerun" (default): The user downloads the file and the app   reruns. No callback function is called. * "ignore": The user downloads the file and the app doesn't   rerun. No callback function is called. * A callable: The user downloads the file and app reruns. The   callable is called before the rest of the app. * None: This is same as on\_click="rerun". This value exists   for backwards compatibility and shouldn't be used. |
| args (tuple) | An optional tuple of args to pass to the callback. |
| kwargs (dict) | An optional dict of kwargs to pass to the callback. |
| type ("primary", "secondary", or "tertiary") | An optional string that specifies the button type. This can be one of the following:   * "primary": The button's background is the app's primary color   for additional emphasis. * "secondary" (default): The button's background coordinates   with the app's background color for normal emphasis. * "tertiary": The button is plain text without a border or   background for subtly. |
| icon (str or None) | An optional emoji or icon to display next to the button label. If icon is None (default), no icon is displayed. If icon is a string, the following options are valid:   * A single-character emoji. For example, you can set icon="🚨"   or icon="🔥". Emoji short codes are not supported. * An icon from the Material Symbols library (rounded style) in the   format ":material/icon\_name:" where "icon\_name" is the name   of the icon in snake case.  For example, icon=":material/thumb\_up:" will display the   Thumb Up icon. Find additional icons in the [Material Symbols](https://fonts.google.com/icons?icon.set=Material+Symbols&icon.style=Rounded)    font library. |
| disabled (bool) | An optional boolean that disables the download button if set to True. The default is False. |
| use\_container\_width (bool) | Whether to expand the button's width to fill its parent container. If use\_container\_width is False (default), Streamlit sizes the button to fit its contents. If use\_container\_width is True, the width of the button matches its parent container.  In both cases, if the contents of the button are wider than the parent container, the contents will line wrap. |
|  |  |
| --- | --- |
| Returns | |
| (bool) | True if the button was clicked on the last run of the app, False otherwise. |

#### Examples

**Example 1: Download a dataframe as a CSV file**

When working with a large dataframe, it's recommended to fetch your
data with a cached function. When working with a download button, it's
similarly recommended to convert your data into a downloadable format
with a cached function. Caching ensures that the app reruns
efficiently.

```

import streamlit as st
import pandas as pd
import numpy as np

@st.cache_data
def get_data():
    df = pd.DataFrame(
        np.random.randn(50, 20), columns=("col %d" % i for i in range(20))
    )
    return df

@st.cache_data
def convert_for_download(df):
    return df.to_csv().encode("utf-8")

df = get_data()
csv = convert_for_download(df)

st.download_button(
    label="Download CSV",
    data=csv,
    file_name="data.csv",
    mime="text/csv",
    icon=":material/download:",
)

```

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen *open\_in\_new*](https://doc-download-button-csv.streamlit.app//?utm_medium=oembed&)

**Example 2: Download a string as a text file**

If you pass a string to the data argument, Streamlit will
automatically use the "text/plain" MIME type.

When you have a widget (like a text area) affecting the value of your
download, it's recommended to use another button to prepare the
download. In this case, use on\_click="ignore" in your download
button to prevent the download button from rerunning your app. This
turns the download button into a frontend-only element that can be
nested in another button.

Without a preparation button, a user can type something into the text
area and immediately click the download button. Because a download is
initiated concurrently with the app rerun, this can create a race-like
condition where the user doesn't see the updated data in their
download.

Important

Even when you prevent your download button from triggering a rerun,
another widget with a pending change can still trigger a rerun. For
example, if a text area has a pending change when a user clicks a
download button, the text area will trigger a rerun.

```

import streamlit as st

message = st.text_area("Message", value="Lorem ipsum.\nStreamlit is cool.")

if st.button("Prepare download"):
    st.download_button(
        label="Download text",
        data=message,
        file_name="message.txt",
        on_click="ignore",
        type="primary",
        icon=":material/download:",
    )

```

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen *open\_in\_new*](https://doc-download-button-text.streamlit.app//?utm_medium=oembed&)

**Example 3: Download a file**

Use a context manager to open and read a local file on your Streamlit
server. Pass the io.BufferedReader object directly to data.
Remember to specify the MIME type if you don't want the default
type of "application/octet-stream" for generic binary data. In the
example below, the MIME type is set to "image/png" for a PNG file.

```

import streamlit as st

with open("flower.png", "rb") as file:
    st.download_button(
        label="Download image",
        data=file,
        file_name="flower.png",
        mime="image/png",
    )

```

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen *open\_in\_new*](https://doc-download-button-file.streamlit.app//?utm_medium=oembed&)

[Previous: st.button](/develop/api-reference/widgets/st.button)[Next: st.form\_submit\_button](https://docs.streamlit.io/develop/api-reference/execution-flow/st.form_submit_button)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
