st.query\_params - Streamlit Docs

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
* [st.query\_params](/develop/api-reference/caching-and-state/st.query_params)

st.query\_params
----------------

`st.query_params` provides a dictionary-like interface to access query parameters in your app's URL and is available as of Streamlit 1.30.0. It behaves similarly to `st.session_state` with the notable exception that keys may be repeated in an app's URL. Handling of repeated keys requires special consideration as explained below.

`st.query_params` can be used with both key and attribute notation. For example, `st.query_params.my_key` and `st.query_params["my_key"]`. All keys and values will be set and returned as strings. When you write to `st.query_params`, key-value pair prefixed with `?` is added to the end of your app's URL. Each additional pair is prefixed with `&` instead of `?`. Query parameters are cleared when navigating between pages in a multipage app.

For example, consider the following URL:

`https://your_app.streamlit.app/?first_key=1&second_key=two&third_key=true`

The parameters in the URL above will be accessible in `st.query_params` as:

`{
"first_key" : "1",
"second_key" : "two",
"third_key" : "true"
}`

This means you can use those parameters in your app like this:

`# You can read query params using key notation
if st.query_params["first_key"] == "1":
do_something()
# ...or using attribute notation
if st.query_params.second_key == "two":
do_something_else()
# And you can change a param by just writing to it
st.query_params.first_key = 2 # This gets converted to str automatically`

### Repeated keys

When a key is repeated in your app's URL (`?a=1&a=2&a=3`), dict-like methods will return only the last value. In this example, `st.query_params["a"]` returns `"3"`. To get all keys as a list, use the [`.get_all()`](/develop/api-reference/caching-and-state/st.query_params#stquery_paramsget_all) method shown below. To set the value of a repeated key, assign the values as a list. For example, `st.query_params.a = ["1", "2", "3"]` produces the repeated key given at the beginning of this paragraph.

### Limitation

`st.query_params` can't get or set embedding settings as described in [Embed your app](/deploy/streamlit-community-cloud/share-your-app/embed-your-app#embed-options). `st.query_params.embed` and `st.query_params.embed_options` will raise an `AttributeError` or `StreamlitAPIException` when trying to get or set their values, respectively.

st.query\_params.clear
----------------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Clear all query parameters from the URL of the app.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/runtime/state/query_params_proxy.py#L135 "View st.clear source code on GitHub") | |
| --- | --- |
| st.query\_params.clear() | |
|  |  |
| --- | --- |
| Returns | |
| (None) | No description |

st.query\_params.from\_dict
---------------------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Set all of the query parameters from a dictionary or dictionary-like object.

This method primarily exists for advanced users who want to control
multiple query parameters in a single update. To set individual query
parameters, use key or attribute notation instead.

This method inherits limitations from st.query\_params and can't be
used to set embedding options as described in [Embed your app](https://docs.streamlit.io/deploy/streamlit-community-cloud/share-your-app/embed-your-app#embed-options).

To handle repeated keys, the value in a key-value pair should be a list.

Note

.from\_dict() is not a direct inverse of .to\_dict() if
you are working with repeated keys. A true inverse operation is
{key: st.query\_params.get\_all(key) for key in st.query\_params}.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/runtime/state/query_params_proxy.py#L175 "View st.from_dict source code on GitHub") | |
| --- | --- |
| st.query\_params.from\_dict(params) | |
| Parameters | |
| params (dict) | A dictionary used to replace the current query parameters. |

#### Example

```

import streamlit as st

st.query_params.from_dict({"foo": "bar", "baz": [1, "two"]})

```

st.query\_params.get\_all
-------------------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Get a list of all query parameter values associated to a given key.

When a key is repeated as a query parameter within the URL, this method
allows all values to be obtained. In contrast, dict-like methods only
retrieve the last value when a key is repeated in the URL.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/runtime/state/query_params_proxy.py#L112 "View st.get_all source code on GitHub") | |
| --- | --- |
| st.query\_params.get\_all(key) | |
| Parameters | |
| key (str) | The label of the query parameter in the URL. |
|  |  |
| --- | --- |
| Returns | |
| (List[str]) | A list of values associated to the given key. May return zero, one, or multiple values. |

st.query\_params.to\_dict
-------------------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Get all query parameters as a dictionary.

This method primarily exists for internal use and is not needed for
most cases. st.query\_params returns an object that inherits from
dict by default.

When a key is repeated as a query parameter within the URL, this method
will return only the last value of each unique key.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/runtime/state/query_params_proxy.py#L147 "View st.to_dict source code on GitHub") | |
| --- | --- |
| st.query\_params.to\_dict() | |
|  |  |
| --- | --- |
| Returns | |
| (Dict[str,str]) | A dictionary of the current query parameters in the app's URL. |

[Previous: st.context](/develop/api-reference/caching-and-state/st.context)[Next: st.experimental\_get\_query\_params](/develop/api-reference/caching-and-state/st.experimental_get_query_params)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
