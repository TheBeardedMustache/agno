st.multiselect - Streamlit Docs

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
* [st.multiselect](/develop/api-reference/widgets/st.multiselect)

st.multiselect
--------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Display a multiselect widget.

The multiselect widget starts as empty.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/elements/widgets/multiselect.py#L215 "View st.multiselect source code on GitHub") | |
| --- | --- |
| st.multiselect(label, options, default=None, format\_func=special\_internal\_function, key=None, help=None, on\_change=None, args=None, kwargs=None, \*, max\_selections=None, placeholder=None, disabled=False, label\_visibility="visible", accept\_new\_options=False) | |
| Parameters | |
| label (str) | A short label explaining to the user what this select widget is for. The label can optionally contain GitHub-flavored Markdown of the following types: Bold, Italics, Strikethroughs, Inline Code, Links, and Images. Images display like icons, with a max height equal to the font height.  Unsupported Markdown elements are unwrapped so only their children (text contents) render. Display unsupported elements as literal characters by backslash-escaping them. E.g., "1\. Not an ordered list".  See the body parameter of [st.markdown](https://docs.streamlit.io/develop/api-reference/text/st.markdown) for additional, supported Markdown directives.  For accessibility reasons, you should never set an empty label, but you can hide it with label\_visibility if needed. In the future, we may disallow empty labels by raising an exception. |
| options (Iterable) | Labels for the select options in an Iterable. This can be a list, set, or anything supported by st.dataframe. If options is dataframe-like, the first column will be used. Each label will be cast to str internally by default. |
| default (Iterable of V, V, or None) | List of default values. Can also be a single value. |
| format\_func (function) | Function to modify the display of the options. It receives the raw option as an argument and should output the label to be shown for that option. This has no impact on the return value of the command. |
| key (str or int) | An optional string or integer to use as the unique key for the widget. If this is omitted, a key will be generated for the widget based on its content. No two widgets may have the same key. |
| help (str or None) | A tooltip that gets displayed next to the widget label. Streamlit only displays the tooltip when label\_visibility="visible". If this is None (default), no tooltip is displayed.  The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of st.markdown. |
| on\_change (callable) | An optional callback invoked when this widget's value changes. |
| args (tuple) | An optional tuple of args to pass to the callback. |
| kwargs (dict) | An optional dict of kwargs to pass to the callback. |
| max\_selections (int) | The max selections that can be selected at a time. |
| placeholder (str or None) | A string to display when no options are selected. If this is None (default), the widget displays one of the two following placeholder strings:   * "Choose an option" is displayed if you set   accept\_new\_options=False. * "Choose or add an option" is displayed if you set   accept\_new\_options=True. |
| disabled (bool) | An optional boolean that disables the multiselect widget if set to True. The default is False. |
| label\_visibility ("visible", "hidden", or "collapsed") | The visibility of the label. The default is "visible". If this is "hidden", Streamlit displays an empty spacer instead of the label, which can help keep the widget aligned with other widgets. If this is "collapsed", Streamlit displays no label or spacer. |
| accept\_new\_options (bool) | Whether the user can add selections that aren't included in options. If this is False (default), the user can only select from the items in options. If this is True, the user can enter new items that don't exist in options.  When a user enters and selects a new item, it is included in the widget's returned list as a string. The new item is not added to the widget's drop-down menu. Streamlit will use a case-insensitive match from options before adding a new item, and a new item can't be added if a case-insensitive match is already selected. The max\_selections argument is still enforced. |
|  |  |
| --- | --- |
| Returns | |
| (list) | A list with the selected options |

#### Examples

**Example 1: Use a basic multiselect widget**

You can declare one or more initial selections with the default
parameter.

```

import streamlit as st

options = st.multiselect(
    "What are your favorite colors?",
    ["Green", "Yellow", "Red", "Blue"],
    default=["Yellow", "Red"],
)

st.write("You selected:", options)

```

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen *open\_in\_new*](https://doc-multiselect.streamlit.app//?utm_medium=oembed&)

**Example 2: Let users to add new options**

To allow users to enter and select new options that aren't included in
the options list, use the accept\_new\_options parameter. To
prevent users from adding an unbounded number of new options, use the
max\_selections parameter.

```

import streamlit as st

options = st.multiselect(
    "What are your favorite cat names?",
    ["Jellybeans", "Fish Biscuit", "Madam President"],
    max_selections=5,
    accept_new_options=True,
)

st.write("You selected:", options)

```

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen *open\_in\_new*](https://doc-multiselect-accept-new-options.streamlit.app//?utm_medium=oembed&)

[Previous: st.feedback](/develop/api-reference/widgets/st.feedback)[Next: st.pills](/develop/api-reference/widgets/st.pills)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
