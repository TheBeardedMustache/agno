Caching and state - Streamlit Docs

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
* [Caching and state](/develop/api-reference/caching-and-state)

Caching and state
=================

Optimize performance and add statefulness to your app!

Caching
-------

Streamlit provides powerful [cache primitives](/develop/concepts/architecture/caching) for data and global resources. They allow your app to stay performant even when loading data from the web, manipulating large datasets, or performing expensive computations.

[#### Cache data

Function decorator to cache functions that return data (e.g. dataframe transforms, database queries, ML inference).

`@st.cache_data
def long_function(param1, param2):
# Perform expensive computation here or
# fetch data from the web here
return data`](/develop/api-reference/caching-and-state/st.cache_data)[#### Cache resource

Function decorator to cache functions that return global resources (e.g. database connections, ML models).

`@st.cache_resource
def init_model():
# Return a global resource here
return pipeline(
"sentiment-analysis",
model="distilbert-base-uncased-finetuned-sst-2-english"
)`](/develop/api-reference/caching-and-state/st.cache_resource)

Browser and server state
------------------------

Streamlit re-executes your script with each user interaction. Widgets have built-in statefulness between reruns, but Session State lets you do more!

[#### Context

`st.context` provides a read-only interface to access cookies, headers, locale, and other browser-session information.

`st.context.cookies
st.context.headers`](/develop/api-reference/caching-and-state/st.context)[#### Session State

Save data between reruns and across pages.

`st.session_state["foo"] = "bar"`](/develop/api-reference/caching-and-state/st.session_state)[#### Query parameters

Get, set, or clear the query parameters that are shown in the browser's URL bar.

`st.query_params[key] = value
st.query_params.clear()`](/develop/api-reference/caching-and-state/st.query_params)

Deprecated commands
-------------------

[*delete*

#### Get query parameters

Get query parameters that are shown in the browser's URL bar.

`param_dict = st.experimental_get_query_params()`](/develop/api-reference/caching-and-state/st.experimental_get_query_params)[*delete*

#### Set query parameters

Set query parameters that are shown in the browser's URL bar.

`st.experimental_set_query_params(
{"show_all"=True, "selected"=["asia", "america"]}
)`](/develop/api-reference/caching-and-state/st.experimental_set_query_params)

[Previous: Execution flow](/develop/api-reference/execution-flow)[Next: st.cache\_data](/develop/api-reference/caching-and-state/st.cache_data)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
