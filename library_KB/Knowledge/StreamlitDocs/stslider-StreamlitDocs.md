﻿st.slider - Streamlit Docs

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
* [st.slider](/develop/api-reference/widgets/st.slider)

st.slider
---------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Display a slider widget.

This supports int, float, date, time, and datetime types.

This also allows you to render a range slider by passing a two-element
tuple or list as the value.

The difference between st.slider and st.select\_slider is that
slider only accepts numerical or date/time data and takes a range as
input, while select\_slider accepts any datatype and takes an iterable
set of options.

Note

Integer values exceeding +/- (1<<53) - 1 cannot be accurately
stored or returned by the widget due to serialization constraints
between the Python server and JavaScript client. You must handle
such numbers as floats, leading to a loss in precision.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/elements/widgets/slider.py#L430 "View st.slider source code on GitHub") | |
| --- | --- |
| st.slider(label, min\_value=None, max\_value=None, value=None, step=None, format=None, key=None, help=None, on\_change=None, args=None, kwargs=None, \*, disabled=False, label\_visibility="visible", width="stretch") | |
| Parameters | |
| label (str) | A short label explaining to the user what this slider is for. The label can optionally contain GitHub-flavored Markdown of the following types: Bold, Italics, Strikethroughs, Inline Code, Links, and Images. Images display like icons, with a max height equal to the font height.  Unsupported Markdown elements are unwrapped so only their children (text contents) render. Display unsupported elements as literal characters by backslash-escaping them. E.g., "1\. Not an ordered list".  See the body parameter of [st.markdown](https://docs.streamlit.io/develop/api-reference/text/st.markdown) for additional, supported Markdown directives.  For accessibility reasons, you should never set an empty label, but you can hide it with label\_visibility if needed. In the future, we may disallow empty labels by raising an exception. |
| min\_value (a supported type or None) | The minimum permitted value. If this is None (default), the minimum value depends on the type as follows:   * integer: 0 * float: 0.0 * date or datetime: value - timedelta(days=14) * time: time.min |
| max\_value (a supported type or None) | The maximum permitted value. If this is None (default), the maximum value depends on the type as follows:   * integer: 100 * float: 1.0 * date or datetime: value + timedelta(days=14) * time: time.max |
| value (a supported type or a tuple/list of supported types or None) | The value of the slider when it first renders. If a tuple/list of two values is passed here, then a range slider with those lower and upper bounds is rendered. For example, if set to (1, 10) the slider will have a selectable range between 1 and 10. This defaults to min\_value. If the type is not otherwise specified in any of the numeric parameters, the widget will have an integer value. |
| step (int, float, timedelta, or None) | The stepping interval. Defaults to 1 if the value is an int, 0.01 if a float, timedelta(days=1) if a date/datetime, timedelta(minutes=15) if a time (or if max\_value - min\_value < 1 day) |
| format (str or None) | A printf-style format string controlling how the interface should display numbers. This does not impact the return value.  For information about formatting integers and floats, see [sprintf.js](https://github.com/alexei/sprintf.js?tab=readme-ov-file#format-specification). For example, format="%0.1f" adjusts the displayed decimal precision to only show one digit after the decimal.  For information about formatting datetimes, dates, and times, see [momentJS](https://momentjs.com/docs/#/displaying/format/). For example, format="ddd ha" adjusts the displayed datetime to show the day of the week and the hour ("Tue 8pm"). |
| key (str or int) | An optional string or integer to use as the unique key for the widget. If this is omitted, a key will be generated for the widget based on its content. No two widgets may have the same key. |
| help (str or None) | A tooltip that gets displayed next to the widget label. Streamlit only displays the tooltip when label\_visibility="visible". If this is None (default), no tooltip is displayed.  The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of st.markdown. |
| on\_change (callable) | An optional callback invoked when this slider's value changes. |
| args (tuple) | An optional tuple of args to pass to the callback. |
| kwargs (dict) | An optional dict of kwargs to pass to the callback. |
| disabled (bool) | An optional boolean that disables the slider if set to True. The default is False. |
| label\_visibility ("visible", "hidden", or "collapsed") | The visibility of the label. The default is "visible". If this is "hidden", Streamlit displays an empty spacer instead of the label, which can help keep the widget aligned with other widgets. If this is "collapsed", Streamlit displays no label or spacer. |
| width ("stretch" or int) | The width of the slider widget. This can be one of the following:   * "stretch" (default): The width of the widget matches the   width of the parent container. * An integer specifying the width in pixels: The widget has a   fixed width. If the specified width is greater than the width of   the parent container, the width of the widget matches the width   of the parent container. |
|  |  |
| --- | --- |
| Returns | |
| (int/float/date/time/datetime or tuple of int/float/date/time/datetime) | The current value of the slider widget. The return type will match the data type of the value parameter. |

#### Examples

```

import streamlit as st

age = st.slider("How old are you?", 0, 130, 25)
st.write("I'm ", age, "years old")

```

And here's an example of a range slider:

```

import streamlit as st

values = st.slider("Select a range of values", 0.0, 100.0, (25.0, 75.0))
st.write("Values:", values)

```

This is a range time slider:

```

import streamlit as st
from datetime import time

appointment = st.slider(
    "Schedule your appointment:", value=(time(11, 30), time(12, 45))
)
st.write("You're scheduled for:", appointment)

```

Finally, a datetime slider:

```

import streamlit as st
from datetime import datetime

start_time = st.slider(
    "When do you start?",
    value=datetime(2020, 1, 1, 9, 30),
    format="MM/DD/YY - hh:mm",
)
st.write("Start time:", start_time)

```

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen *open\_in\_new*](https://doc-slider.streamlit.app//?utm_medium=oembed&)

### Featured videos

Check out our video on how to use one of Streamlit's core functions, the slider!

In the video below, we'll take it a step further and make a double-ended slider.

[Previous: st.number\_input](/develop/api-reference/widgets/st.number_input)[Next: st.date\_input](/develop/api-reference/widgets/st.date_input)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
