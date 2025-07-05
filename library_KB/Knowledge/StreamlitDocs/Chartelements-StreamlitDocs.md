Chart elements - Streamlit Docs

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
* [Chart elements](/develop/api-reference/charts)

Chart elements
==============

Streamlit supports several different charting libraries, and our goal is to
continually add support for more. Right now, the most basic library in our
arsenal is [Matplotlib](https://matplotlib.org/). Then there are also
interactive charting libraries like [Vega
Lite](https://vega.github.io/vega-lite/) (2D charts) and
[deck.gl](https://github.com/uber/deck.gl) (maps and 3D charts). And
finally we also provide a few chart types that are "native" to Streamlit,
like `st.line_chart` and `st.area_chart`.

Simple chart elements
---------------------

[![screenshot](/images/api/area_chart.jpg)

#### Simple area charts

Display an area chart.

`st.area_chart(my_data_frame)`](/develop/api-reference/charts/st.area_chart)[![screenshot](/images/api/bar_chart.jpg)

#### Simple bar charts

Display a bar chart.

`st.bar_chart(my_data_frame)`](/develop/api-reference/charts/st.bar_chart)[![screenshot](/images/api/line_chart.jpg)

#### Simple line charts

Display a line chart.

`st.line_chart(my_data_frame)`](/develop/api-reference/charts/st.line_chart)[![screenshot](/images/api/scatter_chart.svg)

#### Simple scatter charts

Display a line chart.

`st.scatter_chart(my_data_frame)`](/develop/api-reference/charts/st.scatter_chart)[![screenshot](/images/api/map.jpg)

#### Scatterplots on maps

Display a map with points on it.

`st.map(my_data_frame)`](/develop/api-reference/charts/st.map)

Advanced chart elements
-----------------------

[![screenshot](/images/api/pyplot.jpg)

#### Matplotlib

Display a matplotlib.pyplot figure.

`st.pyplot(my_mpl_figure)`](/develop/api-reference/charts/st.pyplot)[![screenshot](/images/api/vega_lite_chart.jpg)

#### Altair

Display a chart using the Altair library.

`st.altair_chart(my_altair_chart)`](/develop/api-reference/charts/st.altair_chart)[![screenshot](/images/api/vega_lite_chart.jpg)

#### Vega-Lite

Display a chart using the Vega-Lite library.

`st.vega_lite_chart(my_vega_lite_chart)`](/develop/api-reference/charts/st.vega_lite_chart)[![screenshot](/images/api/plotly_chart.jpg)

#### Plotly

Display an interactive Plotly chart.

`st.plotly_chart(my_plotly_chart)`](/develop/api-reference/charts/st.plotly_chart)[![screenshot](/images/api/bokeh_chart.jpg)

#### Bokeh

Display an interactive Bokeh chart.

`st.bokeh_chart(my_bokeh_chart)`](/develop/api-reference/charts/st.bokeh_chart)[![screenshot](/images/api/pydeck_chart.jpg)

#### PyDeck

Display a chart using the PyDeck library.

`st.pydeck_chart(my_pydeck_chart)`](/develop/api-reference/charts/st.pydeck_chart)[![screenshot](/images/api/graphviz_chart.jpg)

#### GraphViz

Display a graph using the dagre-d3 library.

`st.graphviz_chart(my_graphviz_spec)`](/develop/api-reference/charts/st.graphviz_chart)

Third-party components

These are featured components created by our lovely community. For more examples and inspiration, check out our [Components Gallery](https://streamlit.io/components) and [Streamlit Extras](https://extras.streamlit.app)!

Previous

[![screenshot](/images/api/components/lottie.jpg)

#### Streamlit Lottie

Integrate [Lottie](https://lottiefiles.com/) animations inside your Streamlit app. Created by [@andfanilo](https://github.com/andfanilo).

`lottie_hello = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_V9t630.json")
st_lottie(lottie_hello, key="hello")`](https://github.com/andfanilo/streamlit-lottie)

[![screenshot](/images/api/components/plotly-events.jpg)

#### Plotly Events

Make Plotly charts interactive!. Created by [@null-jones](https://github.com/null-jones/).

`fig = px.line(x=[1], y=[1])
selected_points = plotly_events(fig)`](https://github.com/null-jones/streamlit-plotly-events)

[![screenshot](/images/api/components/extras-chart-annotations.jpg)

#### Streamlit Extras

A library with useful Streamlit extras. Created by [@arnaudmiribel](https://github.com/arnaudmiribel/).

`chart += get_annotations_chart(annotations=[("Mar 01, 2008", "Pretty good day for GOOG"), ("Dec 01, 2007", "Something's going wrong for GOOG & AAPL"), ("Nov 01, 2008", "Market starts again thanks to..."), ("Dec 01, 2009", "Small crash for GOOG after..."),],)
st.altair_chart(chart, use_container_width=True)`](https://extras.streamlit.app/)

[![screenshot](/images/api/components/plost.jpg)

#### Plost

A deceptively simple plotting library for Streamlit. Created by [@tvst](https://github.com/tvst).

`import plost
plost.line_chart(my_dataframe, x='time', y='stock_value', color='stock_name',)`](https://github.com/tvst/plost)

[![screenshot](/images/api/components/hiplot.jpg)

#### HiPlot

High dimensional Interactive Plotting. Created by [@facebookresearch](https://github.com/facebookresearch).

`data = [{'dropout':0.1, 'lr': 0.001, 'loss': 10.0, 'optimizer': 'SGD'}, {'dropout':0.15, 'lr': 0.01, 'loss': 3.5, 'optimizer': 'Adam'}, {'dropout':0.3, 'lr': 0.1, 'loss': 4.5, 'optimizer': 'Adam'}]
hip.Experiment.from_iterable(data).display()`](https://github.com/facebookresearch/hiplot)

[![screenshot](/images/api/components/echarts.jpg)

#### ECharts

High dimensional Interactive Plotting. Created by [@andfanilo](https://github.com/andfanilo).

`from streamlit_echarts import st_echarts
st_echarts(options=options)`](https://github.com/andfanilo/streamlit-echarts)

[![screenshot](/images/api/components/folium.jpg)

#### Streamlit Folium

Streamlit Component for rendering Folium maps. Created by [@randyzwitch](https://github.com/randyzwitch).

`m = folium.Map(location=[39.949610, -75.150282], zoom_start=16)
st_data = st_folium(m, width=725)`](https://github.com/randyzwitch/streamlit-folium)

[![screenshot](/images/api/components/spacy.jpg)

#### Spacy-Streamlit

spaCy building blocks and visualizers for Streamlit apps. Created by [@explosion](https://github.com/explosion).

`models = ["en_core_web_sm", "en_core_web_md"]
spacy_streamlit.visualize(models, "Sundar Pichai is the CEO of Google.")`](https://github.com/explosion/spacy-streamlit)

[![screenshot](/images/api/components/agraph.jpg)

#### Streamlit Agraph

A Streamlit Graph Vis, based on [react-grah-vis](https://github.com/crubier/react-graph-vis). Created by [@ChrisDelClea](https://github.com/ChrisDelClea).

`from streamlit_agraph import agraph, Node, Edge, Config
agraph(nodes=nodes, edges=edges, config=config)`](https://github.com/ChrisDelClea/streamlit-agraph)

[![screenshot](/images/api/components/lottie.jpg)

#### Streamlit Lottie

Integrate [Lottie](https://lottiefiles.com/) animations inside your Streamlit app. Created by [@andfanilo](https://github.com/andfanilo).

`lottie_hello = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_V9t630.json")
st_lottie(lottie_hello, key="hello")`](https://github.com/andfanilo/streamlit-lottie)

[![screenshot](/images/api/components/plotly-events.jpg)

#### Plotly Events

Make Plotly charts interactive!. Created by [@null-jones](https://github.com/null-jones/).

`fig = px.line(x=[1], y=[1])
selected_points = plotly_events(fig)`](https://github.com/null-jones/streamlit-plotly-events)

[![screenshot](/images/api/components/extras-chart-annotations.jpg)

#### Streamlit Extras

A library with useful Streamlit extras. Created by [@arnaudmiribel](https://github.com/arnaudmiribel/).

`chart += get_annotations_chart(annotations=[("Mar 01, 2008", "Pretty good day for GOOG"), ("Dec 01, 2007", "Something's going wrong for GOOG & AAPL"), ("Nov 01, 2008", "Market starts again thanks to..."), ("Dec 01, 2009", "Small crash for GOOG after..."),],)
st.altair_chart(chart, use_container_width=True)`](https://extras.streamlit.app/)

[![screenshot](/images/api/components/plost.jpg)

#### Plost

A deceptively simple plotting library for Streamlit. Created by [@tvst](https://github.com/tvst).

`import plost
plost.line_chart(my_dataframe, x='time', y='stock_value', color='stock_name',)`](https://github.com/tvst/plost)

[![screenshot](/images/api/components/hiplot.jpg)

#### HiPlot

High dimensional Interactive Plotting. Created by [@facebookresearch](https://github.com/facebookresearch).

`data = [{'dropout':0.1, 'lr': 0.001, 'loss': 10.0, 'optimizer': 'SGD'}, {'dropout':0.15, 'lr': 0.01, 'loss': 3.5, 'optimizer': 'Adam'}, {'dropout':0.3, 'lr': 0.1, 'loss': 4.5, 'optimizer': 'Adam'}]
hip.Experiment.from_iterable(data).display()`](https://github.com/facebookresearch/hiplot)

[![screenshot](/images/api/components/echarts.jpg)

#### ECharts

High dimensional Interactive Plotting. Created by [@andfanilo](https://github.com/andfanilo).

`from streamlit_echarts import st_echarts
st_echarts(options=options)`](https://github.com/andfanilo/streamlit-echarts)

[![screenshot](/images/api/components/folium.jpg)

#### Streamlit Folium

Streamlit Component for rendering Folium maps. Created by [@randyzwitch](https://github.com/randyzwitch).

`m = folium.Map(location=[39.949610, -75.150282], zoom_start=16)
st_data = st_folium(m, width=725)`](https://github.com/randyzwitch/streamlit-folium)

[![screenshot](/images/api/components/spacy.jpg)

#### Spacy-Streamlit

spaCy building blocks and visualizers for Streamlit apps. Created by [@explosion](https://github.com/explosion).

`models = ["en_core_web_sm", "en_core_web_md"]
spacy_streamlit.visualize(models, "Sundar Pichai is the CEO of Google.")`](https://github.com/explosion/spacy-streamlit)

[![screenshot](/images/api/components/agraph.jpg)

#### Streamlit Agraph

A Streamlit Graph Vis, based on [react-grah-vis](https://github.com/crubier/react-graph-vis). Created by [@ChrisDelClea](https://github.com/ChrisDelClea).

`from streamlit_agraph import agraph, Node, Edge, Config
agraph(nodes=nodes, edges=edges, config=config)`](https://github.com/ChrisDelClea/streamlit-agraph)

[![screenshot](/images/api/components/lottie.jpg)

#### Streamlit Lottie

Integrate [Lottie](https://lottiefiles.com/) animations inside your Streamlit app. Created by [@andfanilo](https://github.com/andfanilo).

`lottie_hello = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_V9t630.json")
st_lottie(lottie_hello, key="hello")`](https://github.com/andfanilo/streamlit-lottie)

[![screenshot](/images/api/components/plotly-events.jpg)

#### Plotly Events

Make Plotly charts interactive!. Created by [@null-jones](https://github.com/null-jones/).

`fig = px.line(x=[1], y=[1])
selected_points = plotly_events(fig)`](https://github.com/null-jones/streamlit-plotly-events)

[![screenshot](/images/api/components/extras-chart-annotations.jpg)

#### Streamlit Extras

A library with useful Streamlit extras. Created by [@arnaudmiribel](https://github.com/arnaudmiribel/).

`chart += get_annotations_chart(annotations=[("Mar 01, 2008", "Pretty good day for GOOG"), ("Dec 01, 2007", "Something's going wrong for GOOG & AAPL"), ("Nov 01, 2008", "Market starts again thanks to..."), ("Dec 01, 2009", "Small crash for GOOG after..."),],)
st.altair_chart(chart, use_container_width=True)`](https://extras.streamlit.app/)

 Next

[Previous: Data elements](/develop/api-reference/data)[Next: st.area\_chart](/develop/api-reference/charts/st.area_chart)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
