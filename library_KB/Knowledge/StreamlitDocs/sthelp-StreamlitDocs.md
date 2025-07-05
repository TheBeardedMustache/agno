st.help - Streamlit Docs

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

      *remove*

      * HEADINGS AND BODY

        ---
      * [st.title](/develop/api-reference/text/st.title)
      * [st.header](/develop/api-reference/text/st.header)
      * [st.subheader](/develop/api-reference/text/st.subheader)
      * [st.markdown](/develop/api-reference/text/st.markdown)
      * FORMATTED TEXT

        ---
      * [st.badge](/develop/api-reference/text/st.badge)
      * [st.caption](/develop/api-reference/text/st.caption)
      * [st.code](/develop/api-reference/text/st.code)
      * [st.divider](/develop/api-reference/text/st.divider)
      * [st.echo](/develop/api-reference/text/st.echo)
      * [st.latex](/develop/api-reference/text/st.latex)
      * [st.text](/develop/api-reference/text/st.text)
      * UTILITIES

        ---
      * [st.help](/develop/api-reference/text/st.help)
      * [st.html](/develop/api-reference/text/st.html)
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
* [Text elements](/develop/api-reference/text)/
* [st.help](/develop/api-reference/text/st.help)

st.help
-------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Display help and other information for a given object.

Depending on the type of object that is passed in, this displays the
object's name, type, value, signature, docstring, and member variables,
methods — as well as the values/docstring of members and methods.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/elements/doc_string.py#L46 "View st.help source code on GitHub") | |
| --- | --- |
| st.help(obj=, \*, width="stretch") | |
| Parameters | |
| obj (any) | The object whose information should be displayed. If left unspecified, this call will display help for Streamlit itself. |
| width ("stretch" or int) | The width of the help element. This can be one of the following:   * "stretch" (default): The width of the element matches the   width of the parent container. * An integer specifying the width in pixels: The element has a   fixed width. If the specified width is greater than the width of   the parent container, the width of the element matches the width   of the parent container. |

#### Example

Don't remember how to initialize a dataframe? Try this:

```

import streamlit as st
import pandas

st.help(pandas.DataFrame)

```

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen *open\_in\_new*](https://doc-string.streamlit.app//?utm_medium=oembed&)

Want to quickly check what data type is output by a certain function?
Try:

```

import streamlit as st

x = my_poorly_documented_function()
st.help(x)

```

Want to quickly inspect an object? No sweat:

```

class Dog:
  '''A typical dog.'''

  def __init__(self, breed, color):
    self.breed = breed
    self.color = color

  def bark(self):
    return 'Woof!'


fido = Dog("poodle", "white")

st.help(fido)

```

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen *open\_in\_new*](https://doc-string1.streamlit.app//?utm_medium=oembed&)

And if you're using Magic, you can get help for functions, classes,
and modules without even typing st.help:

```

import streamlit as st
import pandas

# Get help for Pandas read_csv:
pandas.read_csv

# Get help for Streamlit itself:
st

```

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen *open\_in\_new*](https://doc-string2.streamlit.app//?utm_medium=oembed&)

[Previous: st.text](/develop/api-reference/text/st.text)[Next: st.html](/develop/api-reference/text/st.html)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
