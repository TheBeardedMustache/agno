st.bokeh\_chart - Streamlit Docs

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
* [st.bokeh\_chart](/develop/api-reference/charts/st.bokeh_chart)

st.bokeh\_chart
---------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Display an interactive Bokeh chart.

Bokeh is a charting library for Python. The arguments to this function
closely follow the ones for Bokeh's show function. You can find
more about Bokeh at <https://bokeh.pydata.org>.

To show Bokeh charts in Streamlit, call st.bokeh\_chart
wherever you would call Bokeh's show.

Important

You must install bokeh==2.4.3 and numpy<2 to use this
command.

If you need a newer version of Bokeh, use our [streamlit-bokeh](https://github.com/streamlit/streamlit-bokeh)
custom component instead.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/elements/bokeh_chart.py#L36 "View st.bokeh_chart source code on GitHub") | |
| --- | --- |
| st.bokeh\_chart(figure, use\_container\_width=True) | |
| Parameters | |
| figure (bokeh.plotting.figure.Figure) | A Bokeh figure to plot. |
| use\_container\_width (bool) | Whether to override the figure's native width with the width of the parent container. If use\_container\_width is True (default), Streamlit sets the width of the figure to match the width of the parent container. If use\_container\_width is False, Streamlit sets the width of the chart to fit its contents according to the plotting library, up to the width of the parent container. |

#### Example

```

import streamlit as st
from bokeh.plotting import figure

x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

p = figure(title="simple line example", x_axis_label="x", y_axis_label="y")
p.line(x, y, legend_label="Trend", line_width=2)

st.bokeh_chart(p)

```

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen *open\_in\_new*](https://doc-bokeh-chart.streamlit.app//?utm_medium=oembed&)

[Previous: st.altair\_chart](/develop/api-reference/charts/st.altair_chart)[Next: st.graphviz\_chart](/develop/api-reference/charts/st.graphviz_chart)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
