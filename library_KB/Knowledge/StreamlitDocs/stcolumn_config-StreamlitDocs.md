st.column\_config - Streamlit Docs

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
* [st.column\_config](/develop/api-reference/data/st.column_config)

Column configuration
====================

When working with data in Streamlit, the `st.column_config` class is a powerful tool for configuring data display and interaction. Specifically designed for the `column_config` parameter in [`st.dataframe`](/develop/api-reference/data/st.dataframe) and [`st.data_editor`](/develop/api-reference/data/st.data_editor), it provides a suite of methods to tailor your columns to various data types - from simple text and numbers to lists, URLs, images, and more.

Whether it's translating temporal data into user-friendly formats or utilizing charts and progress bars for clearer data visualization, column configuration not only provides the user with an enriched data viewing experience but also ensures that you're equipped with the tools to present and interact with your data, just the way you want it.

[![screenshot](/images/api/column_config.column.jpg)

#### Column

Configure a generic column.

`Column("Streamlit Widgets", width="medium", help="Streamlit **widget** commands 🎈")`](/develop/api-reference/data/st.column_config/st.column_config.column)[![screenshot](/images/api/column_config.textcolumn.jpg)

#### Text column

Configure a text column.

`TextColumn("Widgets", max_chars=50, validate="^st\.[a-z_]+$")`](/develop/api-reference/data/st.column_config/st.column_config.textcolumn)[![screenshot](/images/api/column_config.numbercolumn.jpg)

#### Number column

Configure a number column.

`NumberColumn("Price (in USD)", min_value=0, format="$%d")`](/develop/api-reference/data/st.column_config/st.column_config.numbercolumn)[![screenshot](/images/api/column_config.checkboxcolumn.jpg)

#### Checkbox column

Configure a checkbox column.

`CheckboxColumn("Your favorite?", help="Select your **favorite** widgets")`](/develop/api-reference/data/st.column_config/st.column_config.checkboxcolumn)[![screenshot](/images/api/column_config.selectboxcolumn.jpg)

#### Selectbox column

Configure a selectbox column.

`SelectboxColumn("App Category", options=["🤖 LLM", "📈 Data Viz"])`](/develop/api-reference/data/st.column_config/st.column_config.selectboxcolumn)[![screenshot](/images/api/column_config.datetimecolumn.jpg)

#### Datetime column

Configure a datetime column.

`DatetimeColumn("Appointment", min_value=datetime(2023, 6, 1), format="D MMM YYYY, h:mm a")`](/develop/api-reference/data/st.column_config/st.column_config.datetimecolumn)[![screenshot](/images/api/column_config.datecolumn.jpg)

#### Date column

Configure a date column.

`DateColumn("Birthday", max_value=date(2005, 1, 1), format="DD.MM.YYYY")`](/develop/api-reference/data/st.column_config/st.column_config.datecolumn)[![screenshot](/images/api/column_config.timecolumn.jpg)

#### Time column

Configure a time column.

`TimeColumn("Appointment", min_value=time(8, 0, 0), format="hh:mm a")`](/develop/api-reference/data/st.column_config/st.column_config.timecolumn)[![screenshot](/images/api/column_config.jsoncolumn.jpg)

#### JSON column

Configure a JSON column.

`JSONColumn("Properties", width="medium")`](/develop/api-reference/data/st.column_config/st.column_config.jsoncolumn)[![screenshot](/images/api/column_config.listcolumn.jpg)

#### List column

Configure a list column.

`ListColumn("Sales (last 6 months)", width="medium")`](/develop/api-reference/data/st.column_config/st.column_config.listcolumn)[![screenshot](/images/api/column_config.linkcolumn.jpg)

#### Link column

Configure a link column.

`LinkColumn("Trending apps", max_chars=100, validate="^https://.*$")`](/develop/api-reference/data/st.column_config/st.column_config.linkcolumn)[![screenshot](/images/api/column_config.imagecolumn.jpg)

#### Image column

Configure an image column.

`ImageColumn("Preview Image", help="The preview screenshots")`](/develop/api-reference/data/st.column_config/st.column_config.imagecolumn)[![screenshot](/images/api/column_config.areachartcolumn.jpg)

#### Area chart column

Configure an area chart column.

`AreaChartColumn("Sales (last 6 months)" y_min=0, y_max=100)`](/develop/api-reference/data/st.column_config/st.column_config.areachartcolumn)[![screenshot](/images/api/column_config.linechartcolumn.jpg)

#### Line chart column

Configure a line chart column.

`LineChartColumn("Sales (last 6 months)" y_min=0, y_max=100)`](/develop/api-reference/data/st.column_config/st.column_config.linechartcolumn)[![screenshot](/images/api/column_config.barchartcolumn.jpg)

#### Bar chart column

Configure a bar chart column.

`BarChartColumn("Marketing spend" y_min=0, y_max=100)`](/develop/api-reference/data/st.column_config/st.column_config.barchartcolumn)[![screenshot](/images/api/column_config.progresscolumn.jpg)

#### Progress column

Configure a progress column.

`ProgressColumn("Sales volume", min_value=0, max_value=1000, format="$%f")`](/develop/api-reference/data/st.column_config/st.column_config.progresscolumn)

[Previous: st.data\_editor](/develop/api-reference/data/st.data_editor)[Next: Column](/develop/api-reference/data/st.column_config/st.column_config.column)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
