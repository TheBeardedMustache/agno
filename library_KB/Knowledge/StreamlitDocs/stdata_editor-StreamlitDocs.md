st.data\_editor - Streamlit Docs

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

      *remove*

      * [st.dataframe](/develop/api-reference/data/st.dataframe)
      * [st.data\_editor](/develop/api-reference/data/st.data_editor)
      * [st.column\_config](/develop/api-reference/data/st.column_config)

        *add*
      * [st.table](/develop/api-reference/data/st.table)
      * [st.metric](/develop/api-reference/data/st.metric)
      * [st.json](/develop/api-reference/data/st.json)
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
* [Data elements](/develop/api-reference/data)/
* [st.data\_editor](/develop/api-reference/data/st.data_editor)

*star*

#### Tip

This page only contains information on the `st.data_editor` API. For an overview of working with dataframes and to learn more about the data editor's capabilities and limitations, read [Dataframes](/develop/concepts/design/dataframes).

st.data\_editor
---------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Display a data editor widget.

The data editor widget allows you to edit dataframes and many other data structures in a table-like UI.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/elements/widgets/data_editor.py#L618 "View st.data_editor source code on GitHub") | |
| --- | --- |
| st.data\_editor(data, \*, width=None, height=None, use\_container\_width=None, hide\_index=None, column\_order=None, column\_config=None, num\_rows="fixed", disabled=False, key=None, on\_change=None, args=None, kwargs=None, row\_height=None) | |
| Parameters | |
| data (Anything supported by st.dataframe) | The data to edit in the data editor.  Note   * Styles from pandas.Styler will only be applied to non-editable columns. * Text and number formatting from column\_config always takes   precedence over text and number formatting from pandas.Styler. * Mixing data types within a column can make the column uneditable. * Additionally, the following data types are not yet supported for editing:   complex, list, tuple, bytes, bytearray,   memoryview, dict, set, frozenset,   fractions.Fraction, pandas.Interval, and   pandas.Period. * To prevent overflow in JavaScript, columns containing   datetime.timedelta and pandas.Timedelta values will   default to uneditable, but this can be changed through column   configuration. |
| width (int or None) | Desired width of the data editor expressed in pixels. If width is None (default), Streamlit sets the data editor width to fit its contents up to the width of the parent container. If width is greater than the width of the parent container, Streamlit sets the data editor width to match the width of the parent container. |
| height (int or None) | Desired height of the data editor expressed in pixels. If height is None (default), Streamlit sets the height to show at most ten rows. Vertical scrolling within the data editor element is enabled when the height does not accommodate all rows. |
| use\_container\_width (bool) | Whether to override width with the width of the parent container. If this is True (default), Streamlit sets the width of the data editor to match the width of the parent container. If this is False, Streamlit sets the data editor's width according to width. |
| hide\_index (bool or None) | Whether to hide the index column(s). If hide\_index is None (default), the visibility of index columns is automatically determined based on the data. |
| column\_order (Iterable of str or None) | Specifies the display order of columns. This also affects which columns are visible. For example, column\_order=("col2", "col1") will display 'col2' first, followed by 'col1', and will hide all other non-index columns. If None (default), the order is inherited from the original data structure. |
| column\_config (dict or None) | Configures how columns are displayed, e.g. their title, visibility, type, or format, as well as editing properties such as min/max value or step. This needs to be a dictionary where each key is a column name and the value is one of:   * None to hide the column. * A string to set the display label of the column. * One of the column types defined under st.column\_config, e.g.   st.column\_config.NumberColumn("Dollar values", format="$ %d") to show   a column as dollar amounts. See more info on the available column types   and config options [here](https://docs.streamlit.io/develop/api-reference/data/st.column_config).   To configure the index column(s), use \_index as the column name. |
| num\_rows ("fixed" or "dynamic") | Specifies if the user can add and delete rows in the data editor. If "fixed", the user cannot add or delete rows. If "dynamic", the user can add and delete rows in the data editor, but column sorting is disabled. Defaults to "fixed". |
| disabled (bool or Iterable of str) | Controls the editing of columns. If True, editing is disabled for all columns. If an Iterable of column names is provided (e.g., disabled=("col1", "col2")), only the specified columns will be disabled for editing. If False (default), all columns that support editing are editable. |
| key (str) | An optional string to use as the unique key for this widget. If this is omitted, a key will be generated for the widget based on its content. No two widgets may have the same key. |
| on\_change (callable) | An optional callback invoked when this data\_editor's value changes. |
| args (tuple) | An optional tuple of args to pass to the callback. |
| kwargs (dict) | An optional dict of kwargs to pass to the callback. |
| row\_height (int or None) | The height of each row in the data editor in pixels. If row\_height is None (default), Streamlit will use a default row height, which fits one line of text. |
|  |  |
| --- | --- |
| Returns | |
| (pandas.DataFrame, pandas.Series, pyarrow.Table, numpy.ndarray, list, set, tuple, or dict.) | The edited data. The edited data is returned in its original data type if it corresponds to any of the supported return types. All other data types are returned as a pandas.DataFrame. |

#### Examples

```

import streamlit as st
import pandas as pd

df = pd.DataFrame(
    [
       {"command": "st.selectbox", "rating": 4, "is_widget": True},
       {"command": "st.balloons", "rating": 5, "is_widget": False},
       {"command": "st.time_input", "rating": 3, "is_widget": True},
   ]
)
edited_df = st.data_editor(df)

favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
st.markdown(f"Your favorite command is **{favorite_command}** 🎈")

```

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen *open\_in\_new*](https://doc-data-editor.streamlit.app//?utm_medium=oembed&)

You can also allow the user to add and delete rows by setting num\_rows to "dynamic":

```

import streamlit as st
import pandas as pd

df = pd.DataFrame(
    [
       {"command": "st.selectbox", "rating": 4, "is_widget": True},
       {"command": "st.balloons", "rating": 5, "is_widget": False},
       {"command": "st.time_input", "rating": 3, "is_widget": True},
   ]
)
edited_df = st.data_editor(df, num_rows="dynamic")

favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
st.markdown(f"Your favorite command is **{favorite_command}** 🎈")

```

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen *open\_in\_new*](https://doc-data-editor1.streamlit.app//?utm_medium=oembed&)

Or you can customize the data editor via column\_config, hide\_index,
column\_order, or disabled:

```

import pandas as pd
import streamlit as st

df = pd.DataFrame(
    [
        {"command": "st.selectbox", "rating": 4, "is_widget": True},
        {"command": "st.balloons", "rating": 5, "is_widget": False},
        {"command": "st.time_input", "rating": 3, "is_widget": True},
    ]
)
edited_df = st.data_editor(
    df,
    column_config={
        "command": "Streamlit Command",
        "rating": st.column_config.NumberColumn(
            "Your rating",
            help="How much do you like this command (1-5)?",
            min_value=1,
            max_value=5,
            step=1,
            format="%d ⭐",
        ),
        "is_widget": "Widget ?",
    },
    disabled=["command", "is_widget"],
    hide_index=True,
)

favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
st.markdown(f"Your favorite command is **{favorite_command}** 🎈")

```

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen *open\_in\_new*](https://doc-data-editor-config.streamlit.app//?utm_medium=oembed&)

### Configuring columns

You can configure the display and editing behavior of columns in `st.dataframe` and `st.data_editor` via the [Column configuration API](/develop/api-reference/data/st.column_config). We have developed the API to let you add images, charts, and clickable URLs in dataframe and data editor columns. Additionally, you can make individual columns editable, set columns as categorical and specify which options they can take, hide the index of the dataframe, and much more.

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen *open\_in\_new*](https://doc-column-config-overview.streamlit.app/?utm_medium=oembed&)

[Previous: st.dataframe](/develop/api-reference/data/st.dataframe)[Next: st.column\_config](/develop/api-reference/data/st.column_config)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
