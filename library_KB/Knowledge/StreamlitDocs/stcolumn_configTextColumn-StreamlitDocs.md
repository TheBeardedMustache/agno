st.column\_config.TextColumn - Streamlit Docs

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

        *remove*

        + [Column](/develop/api-reference/data/st.column_config/st.column_config.column)
        + [Text column](/develop/api-reference/data/st.column_config/st.column_config.textcolumn)
        + [Number column](/develop/api-reference/data/st.column_config/st.column_config.numbercolumn)
        + [Checkbox column](/develop/api-reference/data/st.column_config/st.column_config.checkboxcolumn)
        + [Selectbox column](/develop/api-reference/data/st.column_config/st.column_config.selectboxcolumn)
        + [Datetime column](/develop/api-reference/data/st.column_config/st.column_config.datetimecolumn)
        + [Date column](/develop/api-reference/data/st.column_config/st.column_config.datecolumn)
        + [Time column](/develop/api-reference/data/st.column_config/st.column_config.timecolumn)
        + [JSON column](/develop/api-reference/data/st.column_config/st.column_config.jsoncolumn)
        + [List column](/develop/api-reference/data/st.column_config/st.column_config.listcolumn)
        + [Link column](/develop/api-reference/data/st.column_config/st.column_config.linkcolumn)
        + [Image column](/develop/api-reference/data/st.column_config/st.column_config.imagecolumn)
        + [Area chart column](/develop/api-reference/data/st.column_config/st.column_config.areachartcolumn)
        + [Line chart column](/develop/api-reference/data/st.column_config/st.column_config.linechartcolumn)
        + [Bar chart column](/develop/api-reference/data/st.column_config/st.column_config.barchartcolumn)
        + [Progress column](/develop/api-reference/data/st.column_config/st.column_config.progresscolumn)
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
* [st.column\_config](/develop/api-reference/data/st.column_config)/
* [Text column](/develop/api-reference/data/st.column_config/st.column_config.textcolumn)

st.column\_config.TextColumn
----------------------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Configure a text column in st.dataframe or st.data\_editor.

This is the default column type for string values. This command needs to be used in the
column\_config parameter of st.dataframe or st.data\_editor. When used with
st.data\_editor, editing will be enabled with a text input widget.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/elements/lib/column_types.py#L510 "View st.TextColumn source code on GitHub") | |
| --- | --- |
| st.column\_config.TextColumn(label=None, \*, width=None, help=None, disabled=None, required=None, pinned=None, default=None, max\_chars=None, validate=None) | |
| Parameters | |
| label (str or None) | The label shown at the top of the column. If this is None (default), the column name is used. |
| width ("small", "medium", "large", or None) | The display width of the column. If this is None (default), the column will be sized to fit the cell contents. Otherwise, this can be one of the following:   * "small": 75px wide * "medium": 200px wide * "large": 400px wide |
| help (str or None) | A tooltip that gets displayed when hovering over the column label. If this is None (default), no tooltip is displayed.  The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of st.markdown. |
| disabled (bool or None) | Whether editing should be disabled for this column. If this is None (default), Streamlit will decide: indices are disabled and data columns are not.  If a column has mixed types, it may become uneditable regardless of disabled. |
| required (bool or None) | Whether edited cells in the column need to have a value. If this is False (default), the user can submit empty values for this column. If this is True, an edited cell in this column can only be submitted if its value is not None, and a new row will only be submitted after the user fills in this column. |
| pinned (bool or None) | Whether the column is pinned. A pinned column will stay visible on the left side no matter where the user scrolls. If this is None (default), Streamlit will decide: index columns are pinned, and data columns are not pinned. |
| default (str or None) | Specifies the default value in this column when a new row is added by the user. This defaults to None. |
| max\_chars (int or None) | The maximum number of characters that can be entered. If this is None (default), there will be no maximum. |
| validate (str or None) | A JS-flavored regular expression (e.g. "^[a-z]+$") that edited values are validated against. If the user input is invalid, it will not be submitted. |

#### Examples

```

import pandas as pd
import streamlit as st

data_df = pd.DataFrame(
    {
        "widgets": ["st.selectbox", "st.number_input", "st.text_area", "st.button"],
    }
)

st.data_editor(
    data_df,
    column_config={
        "widgets": st.column_config.TextColumn(
            "Widgets",
            help="Streamlit **widget** commands 🎈",
            default="st.",
            max_chars=50,
            validate=r"^st\.[a-z_]+$",
        )
    },
    hide_index=True,
)

```

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen *open\_in\_new*](https://doc-text-column.streamlit.app//?utm_medium=oembed&)

[Previous: Column](/develop/api-reference/data/st.column_config/st.column_config.column)[Next: Number column](/develop/api-reference/data/st.column_config/st.column_config.numbercolumn)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
