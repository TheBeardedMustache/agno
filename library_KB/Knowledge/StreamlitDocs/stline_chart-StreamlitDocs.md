st.line\_chart - Streamlit Docs

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

      *remove*

      * SIMPLE

        ---
      * [st.area\_chart](/develop/api-reference/charts/st.area_chart)
      * [st.bar\_chart](/develop/api-reference/charts/st.bar_chart)
      * [st.line\_chart](/develop/api-reference/charts/st.line_chart)
      * [st.map](/develop/api-reference/charts/st.map)
      * [st.scatter\_chart](/develop/api-reference/charts/st.scatter_chart)
      * ADVANCED

        ---
      * [st.altair\_chart](/develop/api-reference/charts/st.altair_chart)
      * [st.bokeh\_chart](/develop/api-reference/charts/st.bokeh_chart)
      * [st.graphviz\_chart](/develop/api-reference/charts/st.graphviz_chart)
      * [st.plotly\_chart](/develop/api-reference/charts/st.plotly_chart)
      * [st.pydeck\_chart](/develop/api-reference/charts/st.pydeck_chart)
      * [st.pyplot](/develop/api-reference/charts/st.pyplot)
      * [st.vega\_lite\_chart](/develop/api-reference/charts/st.vega_lite_chart)
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
* [Chart elements](/develop/api-reference/charts)/
* [st.line\_chart](/develop/api-reference/charts/st.line_chart)

st.line\_chart
--------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Display a line chart.

This is syntax-sugar around st.altair\_chart. The main difference
is this command uses the data's own column and indices to figure out
the chart's Altair spec. As a result this is easier to use for many
"just plot this" scenarios, while being less customizable.

If st.line\_chart does not guess the data specification
correctly, try specifying your desired chart using st.altair\_chart.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/elements/vega_charts.py#L585 "View st.line_chart source code on GitHub") | |
| --- | --- |
| st.line\_chart(data=None, \*, x=None, y=None, x\_label=None, y\_label=None, color=None, width=None, height=None, use\_container\_width=True) | |
| Parameters | |
| data (Anything supported by st.dataframe) | Data to be plotted. |
| x (str or None) | Column name or key associated to the x-axis data. If x is None (default), Streamlit uses the data index for the x-axis values. |
| y (str, Sequence of str, or None) | Column name(s) or key(s) associated to the y-axis data. If this is None (default), Streamlit draws the data of all remaining columns as data series. If this is a Sequence of strings, Streamlit draws several series on the same chart by melting your wide-format table into a long-format table behind the scenes. |
| x\_label (str or None) | The label for the x-axis. If this is None (default), Streamlit will use the column name specified in x if available, or else no label will be displayed. |
| y\_label (str or None) | The label for the y-axis. If this is None (default), Streamlit will use the column name(s) specified in y if available, or else no label will be displayed. |
| color (str, tuple, Sequence of str, Sequence of tuple, or None) | The color to use for different lines in this chart.  For a line chart with just one line, this can be:   * None, to use the default color. * A hex string like "#ffaa00" or "#ffaa0088". * An RGB or RGBA tuple with the red, green, blue, and alpha   components specified as ints from 0 to 255 or floats from 0.0 to   1.0.   For a line chart with multiple lines, where the dataframe is in long format (that is, y is None or just one column), this can be:   * None, to use the default colors. * The name of a column in the dataset. Data points will be grouped   into lines of the same color based on the value of this column.   In addition, if the values in this column match one of the color   formats above (hex string or color tuple), then that color will   be used.  For example: if the dataset has 1000 rows, but this column only   contains the values "adult", "child", and "baby", then those 1000   datapoints will be grouped into three lines whose colors will be   automatically selected from the default palette.  But, if for the same 1000-row dataset, this column contained   the values "#ffaa00", "#f0f", "#0000ff", then then those 1000   datapoints would still be grouped into three lines, but their   colors would be "#ffaa00", "#f0f", "#0000ff" this time around.   For a line chart with multiple lines, where the dataframe is in wide format (that is, y is a Sequence of columns), this can be:   * None, to use the default colors. * A list of string colors or color tuples to be used for each of   the lines in the chart. This list should have the same length   as the number of y values (e.g. color=["#fd0", "#f0f", "#04f"]   for three lines). |
| width (int or None) | Desired width of the chart expressed in pixels. If width is None (default), Streamlit sets the width of the chart to fit its contents according to the plotting library, up to the width of the parent container. If width is greater than the width of the parent container, Streamlit sets the chart width to match the width of the parent container.  To use width, you must set use\_container\_width=False. |
| height (int or None) | Desired height of the chart expressed in pixels. If height is None (default), Streamlit sets the height of the chart to fit its contents according to the plotting library. |
| use\_container\_width (bool) | Whether to override width with the width of the parent container. If use\_container\_width is True (default), Streamlit sets the width of the chart to match the width of the parent container. If use\_container\_width is False, Streamlit sets the chart's width according to width. |

#### Examples

```

import streamlit as st
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.line_chart(chart_data)

```

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen *open\_in\_new*](https://doc-line-chart.streamlit.app//?utm_medium=oembed&)

You can also choose different columns to use for x and y, as well as set
the color dynamically based on a 3rd column (assuming your dataframe is in
long format):

```

import streamlit as st
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(
    {
        "col1": np.random.randn(20),
        "col2": np.random.randn(20),
        "col3": np.random.choice(["A", "B", "C"], 20),
    }
)

st.line_chart(chart_data, x="col1", y="col2", color="col3")

```

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen *open\_in\_new*](https://doc-line-chart1.streamlit.app//?utm_medium=oembed&)

Finally, if your dataframe is in wide format, you can group multiple
columns under the y argument to show multiple lines with different
colors:

```

import streamlit as st
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(
    np.random.randn(20, 3), columns=["col1", "col2", "col3"]
)

st.line_chart(
    chart_data,
    x="col1",
    y=["col2", "col3"],
    color=["#FF0000", "#0000FF"],  # Optional
)

```

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen *open\_in\_new*](https://doc-line-chart2.streamlit.app//?utm_medium=oembed&)

element.add\_rows
-----------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Concatenate a dataframe to the bottom of the current one.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/elements/arrow.py#L735 "View st.add_rows source code on GitHub") | |
| --- | --- |
| element.add\_rows(data=None, \*\*kwargs) | |
| Parameters | |
| data (pandas.DataFrame, pandas.Styler, pyarrow.Table, numpy.ndarray, pyspark.sql.DataFrame, snowflake.snowpark.dataframe.DataFrame, Iterable, dict, or None) | Table to concat. Optional. |
| \*\*kwargs (pandas.DataFrame, numpy.ndarray, Iterable, dict, or None) | The named dataset to concat. Optional. You can only pass in 1 dataset (including the one in the data parameter). |

#### Example

```

import streamlit as st
import pandas as pd
import numpy as np

df1 = pd.DataFrame(
    np.random.randn(50, 20), columns=("col %d" % i for i in range(20))
)

my_table = st.table(df1)

df2 = pd.DataFrame(
    np.random.randn(50, 20), columns=("col %d" % i for i in range(20))
)

my_table.add_rows(df2)
# Now the table shown in the Streamlit app contains the data for
# df1 followed by the data for df2.

```

You can do the same thing with plots. For example, if you want to add
more data to a line chart:

```

# Assuming df1 and df2 from the example above still exist...
my_chart = st.line_chart(df1)
my_chart.add_rows(df2)
# Now the chart shown in the Streamlit app contains the data for
# df1 followed by the data for df2.

```

And for plots whose datasets are named, you can pass the data with a
keyword argument where the key is the name:

```

my_chart = st.vega_lite_chart(
    {
        "mark": "line",
        "encoding": {"x": "a", "y": "b"},
        "datasets": {
            "some_fancy_name": df1,  # <-- named dataset
        },
        "data": {"name": "some_fancy_name"},
    }
)
my_chart.add_rows(some_fancy_name=df2)  # <-- name used as keyword

```

[Previous: st.bar\_chart](/develop/api-reference/charts/st.bar_chart)[Next: st.map](/develop/api-reference/charts/st.map)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
