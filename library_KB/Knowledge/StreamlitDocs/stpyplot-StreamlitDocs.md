st.pyplot - Streamlit Docs

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
* [st.pyplot](/develop/api-reference/charts/st.pyplot)

st.pyplot
---------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Display a matplotlib.pyplot figure.

Important

You must install matplotlib to use this command.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/elements/pyplot.py#L34 "View st.pyplot source code on GitHub") | |
| --- | --- |
| st.pyplot(fig=None, clear\_figure=None, use\_container\_width=True, \*\*kwargs) | |
| Parameters | |
| fig (Matplotlib Figure) | The Matplotlib Figure object to render. See <https://matplotlib.org/stable/gallery/index.html> for examples.  Note  When this argument isn't specified, this function will render the global Matplotlib figure object. However, this feature is deprecated and will be removed in a later version. |
| clear\_figure (bool) | If True, the figure will be cleared after being rendered. If False, the figure will not be cleared after being rendered. If left unspecified, we pick a default based on the value of fig.   * If fig is set, defaults to False. * If fig is not set, defaults to True. This simulates Jupyter's   approach to matplotlib rendering. |
| use\_container\_width (bool) | Whether to override the figure's native width with the width of the parent container. If use\_container\_width is True (default), Streamlit sets the width of the figure to match the width of the parent container. If use\_container\_width is False, Streamlit sets the width of the chart to fit its contents according to the plotting library, up to the width of the parent container. |
| \*\*kwargs (any) | Arguments to pass to Matplotlib's savefig function. |

#### Example

```

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)

```

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen *open\_in\_new*](https://doc-pyplot.streamlit.app//?utm_medium=oembed&)

Matplotlib supports several types of "backends". If you're getting an
error using Matplotlib with Streamlit, try setting your backend to "TkAgg":

```

echo "backend: TkAgg" >> ~/.matplotlib/matplotlibrc

```

For more information, see <https://matplotlib.org/faq/usage_faq.html>.

*priority\_high*

#### Warning

Matplotlib [doesn't work well with threads](https://matplotlib.org/3.3.2/faq/howto_faq.html#working-with-threads). So if you're using Matplotlib you should wrap your code with locks. This Matplotlib bug is more prominent when you deploy and share your apps because you're more likely to get concurrent users then. The following example uses [`Rlock`](https://docs.python.org/3/library/threading.html#rlock-objects) from the `threading` module.

`import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from threading import RLock
_lock = RLock()
x = np.random.normal(1, 1, 100)
y = np.random.normal(1, 1, 100)
with _lock:
fig, ax = plt.subplots()
ax.scatter(x, y)
st.pyplot(fig)`

[Previous: st.pydeck\_chart](/develop/api-reference/charts/st.pydeck_chart)[Next: st.vega\_lite\_chart](/develop/api-reference/charts/st.vega_lite_chart)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
