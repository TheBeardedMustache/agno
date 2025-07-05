st.cache\_resource - Streamlit Docs

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
* [st.cache\_resource](/develop/api-reference/caching-and-state/st.cache_resource)

*star*

#### Tip

This page only contains information on the `st.cache_resource` API. For a deeper dive into caching and how to use it, check out [Caching](/develop/concepts/architecture/caching).

st.cache\_resource
------------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Decorator to cache functions that return global resources (e.g. database connections, ML models).

Cached objects are shared across all users, sessions, and reruns. They
must be thread-safe because they can be accessed from multiple threads
concurrently. If thread safety is an issue, consider using st.session\_state
to store resources per session instead.

You can clear a function's cache with func.clear() or clear the entire
cache with st.cache\_resource.clear().

A function's arguments must be hashable to cache it. If you have an
unhashable argument (like a database connection) or an argument you
want to exclude from caching, use an underscore prefix in the argument
name. In this case, Streamlit will return a cached value when all other
arguments match a previous function call. Alternatively, you can
declare custom hashing functions with hash\_funcs.

To cache data, use st.cache\_data instead. Learn more about caching at
<https://docs.streamlit.io/develop/concepts/architecture/caching>.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/runtime/caching/cache_resource_api.py#L248 "View st.cache_resource source code on GitHub") | |
| --- | --- |
| st.cache\_resource(func, \*, ttl, max\_entries, show\_spinner, validate, experimental\_allow\_widgets, hash\_funcs=None) | |
| Parameters | |
| func (callable) | The function that creates the cached resource. Streamlit hashes the function's source code. |
| ttl (float, timedelta, str, or None) | The maximum time to keep an entry in the cache. Can be one of:   * None if cache entries should never expire (default). * A number specifying the time in seconds. * A string specifying the time in a format supported by [Pandas's   Timedelta constructor](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.html),   e.g. "1d", "1.5 days", or "1h23s". * A timedelta object from [Python's built-in datetime library](https://docs.python.org/3/library/datetime.html#timedelta-objects),   e.g. timedelta(days=1). |
| max\_entries (int or None) | The maximum number of entries to keep in the cache, or None for an unbounded cache. When a new entry is added to a full cache, the oldest cached entry will be removed. Defaults to None. |
| show\_spinner (bool or str) | Enable the spinner. Default is True to show a spinner when there is a "cache miss" and the cached resource is being created. If string, value of show\_spinner param will be used for spinner text. |
| validate (callable or None) | An optional validation function for cached data. validate is called each time the cached value is accessed. It receives the cached value as its only parameter and it must return a boolean. If validate returns False, the current cached value is discarded, and the decorated function is called to compute a new value. This is useful e.g. to check the health of database connections. |
| experimental\_allow\_widgets (bool) | *delete* The cached widget replay functionality was removed in 1.38. Please remove the experimental\_allow\_widgets parameter from your caching decorators. This parameter will be removed in a future version.  Allow widgets to be used in the cached function. Defaults to False. |
| hash\_funcs (dict or None) | Mapping of types or fully qualified names to hash functions. This is used to override the behavior of the hasher inside Streamlit's caching mechanism: when the hasher encounters an object, it will first check to see if its type matches a key in this dict and, if so, will use the provided function to generate a hash for it. See below for an example of how this can be used. |

#### Example

```

import streamlit as st

@st.cache_resource
def get_database_session(url):
    # Create a database session object that points to the URL.
    return session

s1 = get_database_session(SESSION_URL_1)
# Actually executes the function, since this is the first time it was
# encountered.

s2 = get_database_session(SESSION_URL_1)
# Does not execute the function. Instead, returns its previously computed
# value. This means that now the connection object in s1 is the same as in s2.

s3 = get_database_session(SESSION_URL_2)
# This is a different URL, so the function executes.

```

By default, all parameters to a cache\_resource function must be hashable.
Any parameter whose name begins with \_ will not be hashed. You can use
this as an "escape hatch" for parameters that are not hashable:

```

import streamlit as st

@st.cache_resource
def get_database_session(_sessionmaker, url):
    # Create a database connection object that points to the URL.
    return connection

s1 = get_database_session(create_sessionmaker(), DATA_URL_1)
# Actually executes the function, since this is the first time it was
# encountered.

s2 = get_database_session(create_sessionmaker(), DATA_URL_1)
# Does not execute the function. Instead, returns its previously computed
# value - even though the _sessionmaker parameter was different
# in both calls.

```

A cache\_resource function's cache can be procedurally cleared:

```

import streamlit as st

@st.cache_resource
def get_database_session(_sessionmaker, url):
    # Create a database connection object that points to the URL.
    return connection

fetch_and_clean_data.clear(_sessionmaker, "https://streamlit.io/")
# Clear the cached entry for the arguments provided.

get_database_session.clear()
# Clear all cached entries for this function.

```

To override the default hashing behavior, pass a custom hash function.
You can do that by mapping a type (e.g. Person) to a hash
function (str) like this:

```

import streamlit as st
from pydantic import BaseModel

class Person(BaseModel):
    name: str

@st.cache_resource(hash_funcs={Person: str})
def get_person_name(person: Person):
    return person.name

```

Alternatively, you can map the type's fully-qualified name
(e.g. "\_\_main\_\_.Person") to the hash function instead:

```

import streamlit as st
from pydantic import BaseModel

class Person(BaseModel):
    name: str

@st.cache_resource(hash_funcs={"__main__.Person": str})
def get_person_name(person: Person):
    return person.name

```

st.cache\_resource.clear
------------------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Clear all cache\_resource caches.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/runtime/caching/cache_resource_api.py#L442 "View st.cache_resource.clear source code on GitHub") | |
| --- | --- |
| st.cache\_resource.clear() | |

#### Example

In the example below, pressing the "Clear All" button will clear *all* cache\_resource caches. i.e. Clears cached global resources from all functions decorated with `@st.cache_resource`.

`import streamlit as st
from transformers import BertModel
@st.cache_resource
def get_database_session(url):
# Create a database session object that points to the URL.
return session
@st.cache_resource
def get_model(model_type):
# Create a model of the specified type.
return BertModel.from_pretrained(model_type)
if st.button("Clear All"):
# Clears all st.cache_resource caches:
st.cache_resource.clear()`

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

`from transformers import pipeline
@st.cache_resource
def load_model():
model = pipeline("sentiment-analysis")
st.success("Loaded NLP model from Hugging Face!") # 👈 Show a success message
return model`

As we know, Streamlit only runs this function if it hasn’t been cached before. On this first run, the `st.success` message will appear in the app. But what happens on subsequent runs? It still shows up! Streamlit realizes that there is an `st.` command inside the cached function, saves it during the first run, and replays it on subsequent runs. Replaying static elements works for both caching decorators.

You can also use this functionality to cache entire parts of your UI:

`@st.cache_resource
def load_model():
st.header("Data analysis")
model = torchvision.models.resnet50(weights=ResNet50_Weights.DEFAULT)
st.success("Loaded model!")
st.write("Turning on evaluation mode...")
model.eval()
st.write("Here's the model:")
return model`

### Input widgets

You can also use [interactive input widgets](/develop/api-reference/widgets) like `st.slider` or `st.text_input` in cached functions. Widget replay is an experimental feature at the moment. To enable it, you need to set the `experimental_allow_widgets` parameter:

`@st.cache_resource(experimental_allow_widgets=True) # 👈 Set the parameter
def load_model():
pretrained = st.checkbox("Use pre-trained model:") # 👈 Add a checkbox
model = torchvision.models.resnet50(weights=ResNet50_Weights.DEFAULT, pretrained=pretrained)
return model`

Streamlit treats the checkbox like an additional input parameter to the cached function. If you uncheck it, Streamlit will see if it has already cached the function for this checkbox state. If yes, it will return the cached value. If not, it will rerun the function using the new slider value.

Using widgets in cached functions is extremely powerful because it lets you cache entire parts of your app. But it can be dangerous! Since Streamlit treats the widget value as an additional input parameter, it can easily lead to excessive memory usage. Imagine your cached function has five sliders and returns a 100 MB DataFrame. Then we’ll add 100 MB to the cache for *every permutation* of these five slider values – even if the sliders do not influence the returned data! These additions can make your cache explode very quickly. Please be aware of this limitation if you use widgets in cached functions. We recommend using this feature only for isolated parts of your UI where the widgets directly influence the cached return value.

*priority\_high*

#### Warning

Support for widgets in cached functions is currently experimental. We may change or remove it anytime without warning. Please use it with care!

*push\_pin*

#### Note

Two widgets are currently not supported in cached functions: `st.file_uploader` and `st.camera_input`. We may support them in the future. Feel free to [open a GitHub issue](https://github.com/streamlit/streamlit/issues) if you need them!

[Previous: st.cache\_data](/develop/api-reference/caching-and-state/st.cache_data)[Next: st.experimental\_memo](/develop/api-reference/caching-and-state/st.experimental_memo)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
