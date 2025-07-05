st.pydeck\_chart - Streamlit Docs

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
* [st.pydeck\_chart](/develop/api-reference/charts/st.pydeck_chart)

st.pydeck\_chart
----------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Draw a chart using the PyDeck library.

This supports 3D maps, point clouds, and more! More info about PyDeck
at <https://deckgl.readthedocs.io/en/latest/>.

These docs are also quite useful:

* DeckGL docs: <https://github.com/uber/deck.gl/tree/master/docs>
* DeckGL JSON docs: <https://github.com/uber/deck.gl/tree/master/modules/json>

When using this command, a service called [Carto](https://carto.com) provides the map tiles to render
map content. If you're using advanced PyDeck features you may need to obtain
an API key from Carto first. You can do that as
pydeck.Deck(api\_keys={"carto": YOUR\_KEY}) or by setting the CARTO\_API\_KEY
environment variable. See [PyDeck's documentation](https://deckgl.readthedocs.io/en/latest/deck.html) for more information.

Another common provider for map tiles is [Mapbox](https://mapbox.com). If you prefer to use that,
you'll need to create an account at <https://mapbox.com> and specify your Mapbox
key when creating the pydeck.Deck object. You can do that as
pydeck.Deck(api\_keys={"mapbox": YOUR\_KEY}) or by setting the MAPBOX\_API\_KEY
environment variable.

Carto and Mapbox are third-party products and Streamlit accepts no responsibility
or liability of any kind for Carto or Mapbox, or for any content or information
made available by Carto or Mapbox. The use of Carto or Mapbox is governed by
their respective Terms of Use.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/elements/deck_gl_json_chart.py#L290 "View st.pydeck_chart source code on GitHub") | |
| --- | --- |
| st.pydeck\_chart(pydeck\_obj=None, \*, use\_container\_width=True, width=None, height=None, selection\_mode="single-object", on\_select="ignore", key=None) | |
| Parameters | |
| pydeck\_obj (pydeck.Deck or None) | Object specifying the PyDeck chart to draw. |
| use\_container\_width (bool) | Whether to override the figure's native width with the width of the parent container. If use\_container\_width is True (default), Streamlit sets the width of the figure to match the width of the parent container. If use\_container\_width is False, Streamlit sets the width of the chart to fit its contents according to the plotting library, up to the width of the parent container. |
| width (int or None) | Desired width of the chart expressed in pixels. If width is None (default), Streamlit sets the width of the chart to fit its contents according to the plotting library, up to the width of the parent container. If width is greater than the width of the parent container, Streamlit sets the chart width to match the width of the parent container.  To use width, you must set use\_container\_width=False. |
| height (int or None) | Desired height of the chart expressed in pixels. If height is None (default), Streamlit sets the height of the chart to fit its contents according to the plotting library. |
| on\_select ("ignore" or "rerun" or callable) | How the figure should respond to user selection events. This controls whether or not the chart behaves like an input widget. on\_select can be one of the following:   * "ignore" (default): Streamlit will not react to any selection   events in the chart. The figure will not behave like an   input widget. * "rerun": Streamlit will rerun the app when the user selects   data in the chart. In this case, st.pydeck\_chart will return   the selection data as a dictionary. * A callable: Streamlit will rerun the app and execute the callable   as a callback function before the rest of the app. In this case,   st.pydeck\_chart will return the selection data as a   dictionary.   If on\_select is not "ignore", all layers must have a declared id to keep the chart stateful across reruns. |
| selection\_mode ("single-object" or "multi-object") | The selection mode of the chart. This can be one of the following:   * "single-object" (default): Only one object can be selected at   a time. * "multi-object": Multiple objects can be selected at a time. |
| key (str) | An optional string to use for giving this element a stable identity. If key is None (default), this element's identity will be determined based on the values of the other parameters.  Additionally, if selections are activated and key is provided, Streamlit will register the key in Session State to store the selection state. The selection state is read-only. |
|  |  |
| --- | --- |
| Returns | |
| (element or dict) | If on\_select is "ignore" (default), this command returns an internal placeholder for the chart element. Otherwise, this method returns a dictionary-like object that supports both key and attribute notation. The attributes are described by the PydeckState dictionary schema. |

#### Example

Here's a chart using a HexagonLayer and a ScatterplotLayer. It uses either the
light or dark map style, based on which Streamlit theme is currently active:

```

import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

chart_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=["lat", "lon"],
)

st.pydeck_chart(
    pdk.Deck(
        map_style=None,  # Use Streamlit theme to pick map style
        initial_view_state=pdk.ViewState(
            latitude=37.76,
            longitude=-122.4,
            zoom=11,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
                "HexagonLayer",
                data=chart_data,
                get_position="[lon, lat]",
                radius=200,
                elevation_scale=4,
                elevation_range=[0, 1000],
                pickable=True,
                extruded=True,
            ),
            pdk.Layer(
                "ScatterplotLayer",
                data=chart_data,
                get_position="[lon, lat]",
                get_color="[200, 30, 0, 160]",
                get_radius=200,
            ),
        ],
    )
)

```

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen *open\_in\_new*](https://doc-pydeck-chart.streamlit.app//?utm_medium=oembed&)

Note

To make the PyDeck chart's style consistent with Streamlit's theme,
you can set map\_style=None in the pydeck.Deck object.

Chart selections
----------------

### PydeckState

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

The schema for the PyDeck event state.

The event state is stored in a dictionary-like object that supports both
key and attribute notation. Event states cannot be programmatically changed
or set through Session State.

Only selection events are supported at this time.

|  |  |
| --- | --- |
| Attributes | |
| selection (dict) | The state of the on\_select event. This attribute returns a dictionary-like object that supports both key and attribute notation. The attributes are described by the PydeckSelectionState dictionary schema. |

### PydeckSelectionState

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

The schema for the PyDeck chart selection state.

The selection state is stored in a dictionary-like object that supports
both key and attribute notation. Selection states cannot be
programmatically changed or set through Session State.

You must define id in pydeck.Layer to ensure statefulness when
using selections with st.pydeck\_chart.

|  |  |
| --- | --- |
| Attributes | |
| indices (dict[str, list[int]]) | A dictionary of selected objects by layer. Each key in the dictionary is a layer id, and each value is a list of object indices within that layer. |
| objects (dict[str, list[dict[str, Any]]]) | A dictionary of object attributes by layer. Each key in the dictionary is a layer id, and each value is a list of metadata dictionaries for the selected objects in that layer. |

#### Examples

The following example has multi-object selection enabled. The chart
displays US state capitals by population (2023 US Census estimate). You
can access this [data](https://github.com/streamlit/docs/blob/main/python/api-examples-source/data/capitals.csv)
from GitHub.

```

import streamlit as st
import pydeck
import pandas as pd

capitals = pd.read_csv(
    "capitals.csv",
    header=0,
    names=[
        "Capital",
        "State",
        "Abbreviation",
        "Latitude",
        "Longitude",
        "Population",
    ],
)
capitals["size"] = capitals.Population / 10

point_layer = pydeck.Layer(
    "ScatterplotLayer",
    data=capitals,
    id="capital-cities",
    get_position=["Longitude", "Latitude"],
    get_color="[255, 75, 75]",
    pickable=True,
    auto_highlight=True,
    get_radius="size",
)

view_state = pydeck.ViewState(
    latitude=40, longitude=-117, controller=True, zoom=2.4, pitch=30
)

chart = pydeck.Deck(
    point_layer,
    initial_view_state=view_state,
    tooltip={"text": "{Capital}, {Abbreviation}\nPopulation: {Population}"},
)

event = st.pydeck_chart(chart, on_select="rerun", selection_mode="multi-object")

event.selection

```

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen *open\_in\_new*](https://doc-pydeck-event-state-selections.streamlit.app//?utm_medium=oembed&)

This is an example of the selection state when selecting a single object
from a layer with id, "captial-cities":

```

{
  "indices":{
    "capital-cities":[
      2
    ]
  },
  "objects":{
    "capital-cities":[
      {
        "Abbreviation":" AZ"
        "Capital":"Phoenix"
        "Latitude":33.448457
        "Longitude":-112.073844
        "Population":1650070
        "State":" Arizona"
        "size":165007.0
      }
    ]
  }
}

```

[Previous: st.plotly\_chart](/develop/api-reference/charts/st.plotly_chart)[Next: st.pyplot](/develop/api-reference/charts/st.pyplot)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
