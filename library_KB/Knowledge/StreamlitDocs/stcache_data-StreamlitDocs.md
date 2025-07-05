st.cache\_data - Streamlit Docs

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
* [st.cache\_data](/develop/api-reference/caching-and-state/st.cache_data)

*star*

#### Tip

This page only contains information on the `st.cache_data` API. For a deeper dive into caching and how to use it, check out [Caching](/develop/concepts/architecture/caching).

st.cache\_data
--------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Decorator to cache functions that return data (e.g. dataframe transforms, database queries, ML inference).

Cached objects are stored in "pickled" form, which means that the return
value of a cached function must be pickleable. Each caller of the cached
function gets its own copy of the cached data.

You can clear a function's cache with func.clear() or clear the entire
cache with st.cache\_data.clear().

A function's arguments must be hashable to cache it. If you have an
unhashable argument (like a database connection) or an argument you
want to exclude from caching, use an underscore prefix in the argument
name. In this case, Streamlit will return a cached value when all other
arguments match a previous function call. Alternatively, you can
declare custom hashing functions with hash\_funcs.

To cache global resources, use st.cache\_resource instead. Learn more
about caching at <https://docs.streamlit.io/develop/concepts/architecture/caching>.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/runtime/caching/cache_data_api.py#L382 "View st.cache_data source code on GitHub") | |
| --- | --- |
| st.cache\_data(func=None, \*, ttl, max\_entries, show\_spinner, persist, experimental\_allow\_widgets, hash\_funcs=None) | |
| Parameters | |
| func (callable) | The function to cache. Streamlit hashes the function's source code. |
| ttl (float, timedelta, str, or None) | The maximum time to keep an entry in the cache. Can be one of:   * None if cache entries should never expire (default). * A number specifying the time in seconds. * A string specifying the time in a format supported by [Pandas's   Timedelta constructor](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.html),   e.g. "1d", "1.5 days", or "1h23s". * A timedelta object from [Python's built-in datetime library](https://docs.python.org/3/library/datetime.html#timedelta-objects),   e.g. timedelta(days=1).   Note that ttl will be ignored if persist="disk" or persist=True. |
| max\_entries (int or None) | The maximum number of entries to keep in the cache, or None for an unbounded cache. When a new entry is added to a full cache, the oldest cached entry will be removed. Defaults to None. |
| show\_spinner (bool or str) | Enable the spinner. Default is True to show a spinner when there is a "cache miss" and the cached data is being created. If string, value of show\_spinner param will be used for spinner text. |
| persist ("disk", bool, or None) | Optional location to persist cached data to. Passing "disk" (or True) will persist the cached data to the local disk. None (or False) will disable persistence. The default is None. |
| experimental\_allow\_widgets (bool) | *delete* The cached widget replay functionality was removed in 1.38. Please remove the experimental\_allow\_widgets parameter from your caching decorators. This parameter will be removed in a future version.  Allow widgets to be used in the cached function. Defaults to False. |
| hash\_funcs (dict or None) | Mapping of types or fully qualified names to hash functions. This is used to override the behavior of the hasher inside Streamlit's caching mechanism: when the hasher encounters an object, it will first check to see if its type matches a key in this dict and, if so, will use the provided function to generate a hash for it. See below for an example of how this can be used. |

#### Example

```

import streamlit as st

@st.cache_data
def fetch_and_clean_data(url):
    # Fetch data from URL here, and then clean it up.
    return data

d1 = fetch_and_clean_data(DATA_URL_1)
# Actually executes the function, since this is the first time it was
# encountered.

d2 = fetch_and_clean_data(DATA_URL_1)
# Does not execute the function. Instead, returns its previously computed
# value. This means that now the data in d1 is the same as in d2.

d3 = fetch_and_clean_data(DATA_URL_2)
# This is a different URL, so the function executes.

```

To set the persist parameter, use this command as follows:

```

import streamlit as st

@st.cache_data(persist="disk")
def fetch_and_clean_data(url):
    # Fetch data from URL here, and then clean it up.
    return data

```

By default, all parameters to a cached function must be hashable.
Any parameter whose name begins with \_ will not be hashed. You can use
this as an "escape hatch" for parameters that are not hashable:

```

import streamlit as st

@st.cache_data
def fetch_and_clean_data(_db_connection, num_rows):
    # Fetch data from _db_connection here, and then clean it up.
    return data

connection = make_database_connection()
d1 = fetch_and_clean_data(connection, num_rows=10)
# Actually executes the function, since this is the first time it was
# encountered.

another_connection = make_database_connection()
d2 = fetch_and_clean_data(another_connection, num_rows=10)
# Does not execute the function. Instead, returns its previously computed
# value - even though the _database_connection parameter was different
# in both calls.

```

A cached function's cache can be procedurally cleared:

```

import streamlit as st

@st.cache_data
def fetch_and_clean_data(_db_connection, num_rows):
    # Fetch data from _db_connection here, and then clean it up.
    return data

fetch_and_clean_data.clear(_db_connection, 50)
# Clear the cached entry for the arguments provided.

fetch_and_clean_data.clear()
# Clear all cached entries for this function.

```

To override the default hashing behavior, pass a custom hash function.
You can do that by mapping a type (e.g. datetime.datetime) to a hash
function (lambda dt: dt.isoformat()) like this:

```

import streamlit as st
import datetime

@st.cache_data(hash_funcs={datetime.datetime: lambda dt: dt.isoformat()})
def convert_to_utc(dt: datetime.datetime):
    return dt.astimezone(datetime.timezone.utc)

```

Alternatively, you can map the type's fully-qualified name
(e.g. "datetime.datetime") to the hash function instead:

```

import streamlit as st
import datetime

@st.cache_data(hash_funcs={"datetime.datetime": lambda dt: dt.isoformat()})
def convert_to_utc(dt: datetime.datetime):
    return dt.astimezone(datetime.timezone.utc)

```

*priority\_high*

#### Warning

`st.cache_data` implicitly uses the `pickle` module, which is known to be insecure. Anything your cached function returns is pickled and stored, then unpickled on retrieval. Ensure your cached functions return trusted values because it is possible to construct malicious pickle data that will execute arbitrary code during unpickling. Never load data that could have come from an untrusted source in an unsafe mode or that could have been tampered with. **Only load data you trust**.

st.cache\_data.clear
--------------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Clear all in-memory and on-disk data caches.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/runtime/caching/cache_data_api.py#L599 "View st.cache_data.clear source code on GitHub") | |
| --- | --- |
| st.cache\_data.clear() | |

#### Example

In the example below, pressing the "Clear All" button will clear memoized values from all functions decorated with `@st.cache_data`.

`import streamlit as st
@st.cache_data
def square(x):
return x**2
@st.cache_data
def cube(x):
return x**3
if st.button("Clear All"):
# Clear values from *all* all in-memory and on-disk data caches:
# i.e. clear values from both square and cube
st.cache_data.clear()`

CachedFunc.clear
----------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Clear the cached function's associated cache.

If no arguments are passed, Streamlit will clear all values cached for
the function. If arguments are passed, Streamlit will clear the cached
value for these arguments only.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/runtime/caching/cache_utils.py#L349 "View st.clear source code on GitHub") | |
| --- | --- |
| CachedFunc.clear(\*args, \*\*kwargs) | |
| Parameters | |
| \*args (Any) | Arguments of the cached functions. |
| \*\*kwargs (Any) | Keyword arguments of the cached function. |

#### Example

```

import streamlit as st
import time

@st.cache_data
def foo(bar):
    time.sleep(2)
    st.write(f"Executed foo({bar}).")
    return bar

if st.button("Clear all cached values for `foo`", on_click=foo.clear):
    foo.clear()

if st.button("Clear the cached value of `foo(1)`"):
    foo.clear(1)

foo(1)
foo(2)

```

Using Streamlit commands in cached functions
--------------------------------------------

### Static elements

Since version 1.16.0, cached functions can contain Streamlit commands! For example, you can do this:

`@st.cache_data
def get_api_data():
data = api.get(...)
st.success("Fetched data from API!") # 👈 Show a success message
return data`

As we know, Streamlit only runs this function if it hasn’t been cached before. On this first run, the `st.success` message will appear in the app. But what happens on subsequent runs? It still shows up! Streamlit realizes that there is an `st.` command inside the cached function, saves it during the first run, and replays it on subsequent runs. Replaying static elements works for both caching decorators.

You can also use this functionality to cache entire parts of your UI:

`@st.cache_data
def show_data():
st.header("Data analysis")
data = api.get(...)
st.success("Fetched data from API!")
st.write("Here is a plot of the data:")
st.line_chart(data)
st.write("And here is the raw data:")
st.dataframe(data)`

### Input widgets

You can also use [interactive input widgets](/develop/api-reference/widgets) like `st.slider` or `st.text_input` in cached functions. Widget replay is an experimental feature at the moment. To enable it, you need to set the `experimental_allow_widgets` parameter:

`@st.cache_data(experimental_allow_widgets=True) # 👈 Set the parameter
def get_data():
num_rows = st.slider("Number of rows to get") # 👈 Add a slider
data = api.get(..., num_rows)
return data`

Streamlit treats the slider like an additional input parameter to the cached function. If you change the slider position, Streamlit will see if it has already cached the function for this slider value. If yes, it will return the cached value. If not, it will rerun the function using the new slider value.

Using widgets in cached functions is extremely powerful because it lets you cache entire parts of your app. But it can be dangerous! Since Streamlit treats the widget value as an additional input parameter, it can easily lead to excessive memory usage. Imagine your cached function has five sliders and returns a 100 MB DataFrame. Then we’ll add 100 MB to the cache for *every permutation* of these five slider values – even if the sliders do not influence the returned data! These additions can make your cache explode very quickly. Please be aware of this limitation if you use widgets in cached functions. We recommend using this feature only for isolated parts of your UI where the widgets directly influence the cached return value.

*priority\_high*

#### Warning

Support for widgets in cached functions is currently experimental. We may change or remove it anytime without warning. Please use it with care!

*push\_pin*

#### Note

Two widgets are currently not supported in cached functions: `st.file_uploader` and `st.camera_input`. We may support them in the future. Feel free to [open a GitHub issue](https://github.com/streamlit/streamlit/issues) if you need them!

[Previous: Caching and state](/develop/api-reference/caching-and-state)[Next: st.cache\_resource](/develop/api-reference/caching-and-state/st.cache_resource)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
