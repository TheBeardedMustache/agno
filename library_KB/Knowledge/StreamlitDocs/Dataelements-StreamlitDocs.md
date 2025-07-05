Data elements - Streamlit Docs

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
* [Data elements](/develop/api-reference/data)

Data elements
=============

When you're working with data, it is extremely valuable to visualize that
data quickly, interactively, and from multiple different angles. That's what
Streamlit is actually built and optimized for.

You can display data via [charts](/develop/api-reference/data#display-charts), and you can display it in
raw form. These are the Streamlit commands you can use to display and interact with raw data.

[![screenshot](/images/api/dataframe.jpg)

#### Dataframes

Display a dataframe as an interactive table.

`st.dataframe(my_data_frame)`](/develop/api-reference/data/st.dataframe)[![screenshot](/images/api/data_editor.jpg)

#### Data editor

Display a data editor widget.

`edited = st.data_editor(df, num_rows="dynamic")`](/develop/api-reference/data/st.data_editor)[![screenshot](/images/api/column_config.jpg)

#### Column configuration

Configure the display and editing behavior of dataframes and data editors.

`st.column_config.NumberColumn("Price (in USD)", min_value=0, format="$%d")`](/develop/api-reference/data/st.column_config)[![screenshot](/images/api/table.jpg)

#### Static tables

Display a static table.

`st.table(my_data_frame)`](/develop/api-reference/data/st.table)[![screenshot](/images/api/metric.jpg)

#### Metrics

Display a metric in big bold font, with an optional indicator of how the metric changed.

`st.metric("My metric", 42, 2)`](/develop/api-reference/data/st.metric)[![screenshot](/images/api/json.jpg)

#### Dicts and JSON

Display object or string as a pretty-printed JSON string.

`st.json(my_dict)`](/develop/api-reference/data/st.json)

Third-party components

These are featured components created by our lovely community. For more examples and inspiration, check out our [Components Gallery](https://streamlit.io/components) and [Streamlit Extras](https://extras.streamlit.app)!

Previous

[![screenshot](/images/api/components/image-coordinates.jpg)

#### Image Coordinates

Get the coordinates of clicks on an image. Created by [@blackary](https://github.com/blackary/).

`from streamlit_image_coordinates import streamlit_image_coordinates
value = streamlit_image_coordinates("https://placekitten.com/200/300")
st.write(value)`](https://github.com/blackary/streamlit-image-coordinates)

[![screenshot](/images/api/components/plotly-events.jpg)

#### Plotly Events

Make Plotly charts interactive!. Created by [@null-jones](https://github.com/null-jones/).

`from streamlit_plotly_events import plotly_events
fig = px.line(x=[1], y=[1])
selected_points = plotly_events(fig)`](https://github.com/null-jones/streamlit-plotly-events)

[![screenshot](/images/api/components/extras-metric-cards.jpg)

#### Streamlit Extras

A library with useful Streamlit extras. Created by [@arnaudmiribel](https://github.com/arnaudmiribel/).

`from streamlit_extras.metric_cards import style_metric_cards
col3.metric(label="No Change", value=5000, delta=0)
style_metric_cards()`](https://extras.streamlit.app/)

[![screenshot](/images/api/components/aggrid.jpg)

#### Streamlit Aggrid

Implementation of Ag-Grid component for Streamlit. Created by [@PablocFonseca](https://github.com/PablocFonseca).

`df = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6]})
grid_return = AgGrid(df, editable=True)
new_df = grid_return['data']`](https://github.com/PablocFonseca/streamlit-aggrid)

[![screenshot](/images/api/components/folium.jpg)

#### Streamlit Folium

Streamlit Component for rendering Folium maps. Created by [@randyzwitch](https://github.com/randyzwitch).

`m = folium.Map(location=[39.949610, -75.150282], zoom_start=16)
folium.Marker([39.949610, -75.150282], popup="Liberty Bell", tooltip="Liberty Bell").add_to(m)
st_data = st_folium(m, width=725)`](https://github.com/randyzwitch/streamlit-folium)

[![screenshot](/images/api/components/pandas-profiling.jpg)

#### Pandas Profiling

Pandas profiling component for Streamlit. Created by [@okld](https://github.com/okld/).

`df = pd.read_csv("https://storage.googleapis.com/tf-datasets/titanic/train.csv")
pr = df.profile_report()
st_profile_report(pr)`](https://github.com/okld/streamlit-pandas-profiling)

[![screenshot](/images/api/components/image-coordinates.jpg)

#### Image Coordinates

Get the coordinates of clicks on an image. Created by [@blackary](https://github.com/blackary/).

`from streamlit_image_coordinates import streamlit_image_coordinates
value = streamlit_image_coordinates("https://placekitten.com/200/300")
st.write(value)`](https://github.com/blackary/streamlit-image-coordinates)

[![screenshot](/images/api/components/plotly-events.jpg)

#### Plotly Events

Make Plotly charts interactive!. Created by [@null-jones](https://github.com/null-jones/).

`from streamlit_plotly_events import plotly_events
fig = px.line(x=[1], y=[1])
selected_points = plotly_events(fig)`](https://github.com/null-jones/streamlit-plotly-events)

[![screenshot](/images/api/components/extras-metric-cards.jpg)

#### Streamlit Extras

A library with useful Streamlit extras. Created by [@arnaudmiribel](https://github.com/arnaudmiribel/).

`from streamlit_extras.metric_cards import style_metric_cards
col3.metric(label="No Change", value=5000, delta=0)
style_metric_cards()`](https://extras.streamlit.app/)

[![screenshot](/images/api/components/aggrid.jpg)

#### Streamlit Aggrid

Implementation of Ag-Grid component for Streamlit. Created by [@PablocFonseca](https://github.com/PablocFonseca).

`df = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6]})
grid_return = AgGrid(df, editable=True)
new_df = grid_return['data']`](https://github.com/PablocFonseca/streamlit-aggrid)

[![screenshot](/images/api/components/folium.jpg)

#### Streamlit Folium

Streamlit Component for rendering Folium maps. Created by [@randyzwitch](https://github.com/randyzwitch).

`m = folium.Map(location=[39.949610, -75.150282], zoom_start=16)
folium.Marker([39.949610, -75.150282], popup="Liberty Bell", tooltip="Liberty Bell").add_to(m)
st_data = st_folium(m, width=725)`](https://github.com/randyzwitch/streamlit-folium)

[![screenshot](/images/api/components/pandas-profiling.jpg)

#### Pandas Profiling

Pandas profiling component for Streamlit. Created by [@okld](https://github.com/okld/).

`df = pd.read_csv("https://storage.googleapis.com/tf-datasets/titanic/train.csv")
pr = df.profile_report()
st_profile_report(pr)`](https://github.com/okld/streamlit-pandas-profiling)

[![screenshot](/images/api/components/image-coordinates.jpg)

#### Image Coordinates

Get the coordinates of clicks on an image. Created by [@blackary](https://github.com/blackary/).

`from streamlit_image_coordinates import streamlit_image_coordinates
value = streamlit_image_coordinates("https://placekitten.com/200/300")
st.write(value)`](https://github.com/blackary/streamlit-image-coordinates)

[![screenshot](/images/api/components/plotly-events.jpg)

#### Plotly Events

Make Plotly charts interactive!. Created by [@null-jones](https://github.com/null-jones/).

`from streamlit_plotly_events import plotly_events
fig = px.line(x=[1], y=[1])
selected_points = plotly_events(fig)`](https://github.com/null-jones/streamlit-plotly-events)

[![screenshot](/images/api/components/extras-metric-cards.jpg)

#### Streamlit Extras

A library with useful Streamlit extras. Created by [@arnaudmiribel](https://github.com/arnaudmiribel/).

`from streamlit_extras.metric_cards import style_metric_cards
col3.metric(label="No Change", value=5000, delta=0)
style_metric_cards()`](https://extras.streamlit.app/)

 Next

[Previous: Text elements](/develop/api-reference/text)[Next: st.dataframe](/develop/api-reference/data/st.dataframe)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
