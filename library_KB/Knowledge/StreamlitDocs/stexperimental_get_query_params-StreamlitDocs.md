st.experimental\_get\_query\_params - Streamlit Docs

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

      *remove*

      * SERVER

        ---
      * [st.cache\_data](/develop/api-reference/caching-and-state/st.cache_data)
      * [st.cache\_resource](/develop/api-reference/caching-and-state/st.cache_resource)
      * [st.session\_state](/develop/api-reference/caching-and-state/st.session_state)
      * BROWSER

        ---
      * [st.context](/develop/api-reference/caching-and-state/st.context)
      * [st.query\_params](/develop/api-reference/caching-and-state/st.query_params)
      * [st.experimental\_get\_query\_params*delete*](/develop/api-reference/caching-and-state/st.experimental_get_query_params)
      * [st.experimental\_set\_query\_params*delete*](/develop/api-reference/caching-and-state/st.experimental_set_query_params)
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
* [Caching and state](/develop/api-reference/caching-and-state)/
* [st.experimental\_get\_query\_params](/develop/api-reference/caching-and-state/st.experimental_get_query_params)

st.experimental\_get\_query\_params
-----------------------------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

*delete*

#### Deprecation notice

`st.experimental_get_query_params` was deprecated in version 1.30.0. Use [`st.query_params`](/develop/api-reference/caching-and-state/st.query_params) instead.

Return the query parameters that is currently showing in the browser's URL bar.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/commands/experimental_query_params.py#L31 "View st.experimental_get_query_params source code on GitHub") | |
| --- | --- |
| st.experimental\_get\_query\_params() | |
|  |  |
| --- | --- |
| Returns | |
| (dict) | The current query parameters as a dict. "Query parameters" are the part of the URL that comes after the first "?". |

#### Example

Let's say the user's web browser is at
http://localhost:8501/?show\_map=True&selected=asia&selected=america.
Then, you can get the query parameters using the following:

```

import streamlit as st

st.experimental_get_query_params()
{"show_map": ["True"], "selected": ["asia", "america"]}

```

Note that the values in the returned dict are *always* lists. This is
because we internally use Python's urllib.parse.parse\_qs(), which behaves
this way. And this behavior makes sense when you consider that every item
in a query string is potentially a 1-element array.

[Previous: st.query\_params](/develop/api-reference/caching-and-state/st.query_params)[Next: st.experimental\_set\_query\_params](/develop/api-reference/caching-and-state/st.experimental_set_query_params)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
