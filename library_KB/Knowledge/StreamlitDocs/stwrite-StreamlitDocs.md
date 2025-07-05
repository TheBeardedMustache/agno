st.write - Streamlit Docs

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

      *remove*

      * [st.write](/develop/api-reference/write-magic/st.write)
      * [st.write\_stream](/develop/api-reference/write-magic/st.write_stream)
      * [magic](/develop/api-reference/write-magic/magic)
    - [Text elements](/develop/api-reference/text)

      *add*
    - [Data elements](/develop/api-reference/data)

      *add*
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
* [Write and magic](/develop/api-reference/write-magic)/
* [st.write](/develop/api-reference/write-magic/st.write)

st.write
--------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Displays arguments in the app.

This is the Swiss Army knife of Streamlit commands: it does different
things depending on what you throw at it. Unlike other Streamlit
commands, st.write() has some unique properties:

* You can pass in multiple arguments, all of which will be displayed.
* Its behavior depends on the input type(s).

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/elements/write.py#L255 "View st.write source code on GitHub") | |
| --- | --- |
| st.write(\*args, unsafe\_allow\_html=False, \*\*kwargs) | |
| Parameters | |
| \*args (any) | One or many objects to display in the app.   Each type of argument is handled as follows:     | Type | Handling | | --- | --- | | str | Uses st.markdown(). | | dataframe-like, dict, or list | Uses st.dataframe(). | | Exception | Uses st.exception(). | | function, module, or class | Uses st.help(). | | DeltaGenerator | Uses st.help(). | | Altair chart | Uses st.altair\_chart(). | | Bokeh figure | Uses st.bokeh\_chart(). | | Graphviz graph | Uses st.graphviz\_chart(). | | Keras model | Converts model and uses st.graphviz\_chart(). | | Matplotlib figure | Uses st.pyplot(). | | Plotly figure | Uses st.plotly\_chart(). | | PIL.Image | Uses st.image(). | | generator or stream (like openai.Stream) | Uses st.write\_stream(). | | SymPy expression | Uses st.latex(). | | An object with .\_repr\_html() | Uses st.html(). | | Database cursor | Displays DB API 2.0 cursor results in a table. | | Any | Displays str(arg) as inline code. | |
| unsafe\_allow\_html (bool) | Whether to render HTML within \*args. This only applies to strings or objects falling back on \_repr\_html\_(). If this is False (default), any HTML tags found in body will be escaped and therefore treated as raw text. If this is True, any HTML expressions within body will be rendered.  Adding custom HTML to your app impacts safety, styling, and maintainability.  Note  If you only want to insert HTML or CSS without Markdown text, we recommend using st.html instead. |
| \*\*kwargs (any) | *delete* \*\*kwargs is deprecated and will be removed in a later version. Use other, more specific Streamlit commands to pass additional keyword arguments.  Keyword arguments. Not used. |
|  |  |
| --- | --- |
| Returns | |
| (None) | No description |

#### Examples

Its basic use case is to draw Markdown-formatted text, whenever the
input is a string:

```

import streamlit as st

st.write("Hello, *World!* :sunglasses:")

```

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen *open\_in\_new*](https://doc-write1.streamlit.app//?utm_medium=oembed&)

As mentioned earlier, st.write() also accepts other data formats, such as
numbers, data frames, styled data frames, and assorted objects:

```

import streamlit as st
import pandas as pd

st.write(1234)
st.write(
    pd.DataFrame(
        {
            "first column": [1, 2, 3, 4],
            "second column": [10, 20, 30, 40],
        }
    )
)

```

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen *open\_in\_new*](https://doc-write2.streamlit.app//?utm_medium=oembed&)

Finally, you can pass in multiple arguments to do things like:

```

import streamlit as st

st.write("1 + 1 = ", 2)
st.write("Below is a DataFrame:", data_frame, "Above is a dataframe.")

```

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen *open\_in\_new*](https://doc-write3.streamlit.app//?utm_medium=oembed&)

Oh, one more thing: st.write accepts chart objects too! For example:

```

import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

df = pd.DataFrame(np.random.randn(200, 3), columns=["a", "b", "c"])
c = (
    alt.Chart(df)
    .mark_circle()
    .encode(x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])
)

st.write(c)

```

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen *open\_in\_new*](https://doc-vega-lite-chart.streamlit.app//?utm_medium=oembed&)

### Featured video

Learn what the [`st.write`](/develop/api-reference/write-magic/st.write) and [magic](/develop/api-reference/write-magic/magic) commands are and how to use them.

[Previous: Write and magic](/develop/api-reference/write-magic)[Next: st.write\_stream](/develop/api-reference/write-magic/st.write_stream)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
