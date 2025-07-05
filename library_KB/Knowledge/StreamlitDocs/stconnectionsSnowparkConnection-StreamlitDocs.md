st.connections.SnowparkConnection - Streamlit Docs

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

      *add*
    - [Connections and secrets](/develop/api-reference/connections)

      *remove*

      * SECRETS

        ---
      * [st.secrets](/develop/api-reference/connections/st.secrets)
      * [secrets.toml](/develop/api-reference/connections/secrets.toml)
      * CONNECTIONS

        ---
      * [st.connection](/develop/api-reference/connections/st.connection)
      * [SnowflakeConnection](/develop/api-reference/connections/st.connections.snowflakeconnection)
      * [SQLConnection](/develop/api-reference/connections/st.connections.sqlconnection)
      * [BaseConnection](/develop/api-reference/connections/st.connections.baseconnection)
      * [SnowparkConnection*delete*](/develop/api-reference/connections/st.connections.snowparkconnection)
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
* [Connections and secrets](/develop/api-reference/connections)/
* [SnowparkConnection](/develop/api-reference/connections/st.connections.snowparkconnection)

*star*

#### Tip

This page only contains the `st.connections.SnowparkConnection` class. For a deeper dive into creating and managing data connections within Streamlit apps, read [Connecting to data](/develop/concepts/connections/connecting-to-data).

st.connections.SnowparkConnection
---------------------------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

*delete*

#### Deprecation notice

`st.connections.SnowParkConnection` was deprecated in version 1.28.0. Use [`st.connections.SnowflakeConnection`](/develop/api-reference/connections/st.connections.snowflakeconnection) instead.

A connection to Snowpark using snowflake.snowpark.session.Session. Initialize using

st.connection("<name>", type="snowpark").

In addition to providing access to the Snowpark Session, SnowparkConnection supports
direct SQL querying using query("...") and thread safe access using
with conn.safe\_session():. See methods below for more information.
SnowparkConnections should always be created using st.connection(), **not**
initialized directly.

Note

We don't expect this iteration of SnowparkConnection to be able to scale
well in apps with many concurrent users due to the lock contention that will occur
over the single underlying Session object under high load.

| Class description[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/connections/snowpark_connection.py#L48 "View st.SnowparkConnection source code on GitHub") | |
| --- | --- |
| st.connections.SnowparkConnection(connection\_name, \*\*kwargs) | |
|  |  |
| --- | --- |
| Methods | |
| [query](/develop/api-reference/connections/st.connections.snowparkconnection#snowparkconnectionquery)(sql, ttl=None) | Run a read-only SQL query. |
| [reset](/develop/api-reference/connections/st.connections.snowparkconnection#snowparkconnectionreset)() | Reset this connection so that it gets reinitialized the next time it's used. |
| [safe\_session](/develop/api-reference/connections/st.connections.snowparkconnection#snowparkconnectionsafe_session)() | Grab the underlying Snowpark session in a thread-safe manner. |
| Attributes | |
| [session](/develop/api-reference/connections/st.connections.snowparkconnection#snowparkconnectionsession) | Access the underlying Snowpark session. |

SnowparkConnection.query
------------------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Run a read-only SQL query.

This method implements both query result caching (with caching behavior
identical to that of using @st.cache\_data) as well as simple error handling/retries.

Note

Queries that are run without a specified ttl are cached indefinitely.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/connections/snowpark_connection.py#L96 "View st.query source code on GitHub") | |
| --- | --- |
| SnowparkConnection.query(sql, ttl=None) | |
| Parameters | |
| sql (str) | The read-only SQL query to execute. |
| ttl (float, int, timedelta or None) | The maximum number of seconds to keep results in the cache, or None if cached results should not expire. The default is None. |
|  |  |
| --- | --- |
| Returns | |
| (pandas.DataFrame) | The result of running the query, formatted as a pandas DataFrame. |

#### Example

```

import streamlit as st

conn = st.connection("snowpark")
df = conn.query("SELECT * FROM pet_owners")
st.dataframe(df)

```

SnowparkConnection.reset
------------------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Reset this connection so that it gets reinitialized the next time it's used.

This method can be useful when a connection has become stale, an auth token has
expired, or in similar scenarios where a broken connection might be fixed by
reinitializing it. Note that some connection methods may already use reset()
in their error handling code.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/connections/base_connection.py#L121 "View st.reset source code on GitHub") | |
| --- | --- |
| SnowparkConnection.reset() | |
|  |  |
| --- | --- |
| Returns | |
| (None) | No description |

#### Example

```

import streamlit as st

conn = st.connection("my_conn")

# Reset the connection before using it if it isn't healthy
# Note: is_healthy() isn't a real method and is just shown for example here.
if not conn.is_healthy():
    conn.reset()

# Do stuff with conn...

```

SnowparkConnection.safe\_session
--------------------------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Grab the underlying Snowpark session in a thread-safe manner.

As operations on a Snowpark session are not thread safe, we need to take care
when using a session in the context of a Streamlit app where each script run
occurs in its own thread. Using the contextmanager pattern to do this ensures
that access on this connection's underlying Session is done in a thread-safe
manner.

Information on how to use Snowpark sessions can be found in the [Snowpark documentation](https://docs.snowflake.com/en/developer-guide/snowpark/python/working-with-dataframes).

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/connections/snowpark_connection.py#L189 "View st.safe_session source code on GitHub") | |
| --- | --- |
| SnowparkConnection.safe\_session() | |

#### Example

```

import streamlit as st

conn = st.connection("snowpark")
with conn.safe_session() as session:
    df = session.table("mytable").limit(10).to_pandas()

st.dataframe(df)

```

SnowparkConnection.session
--------------------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Access the underlying Snowpark session.

Note

Snowpark sessions are **not** thread safe. Users of this method are
responsible for ensuring that access to the session returned by this method is
done in a thread-safe manner. For most users, we recommend using the thread-safe
safe\_session() method and a with block.

Information on how to use Snowpark sessions can be found in the [Snowpark documentation](https://docs.snowflake.com/en/developer-guide/snowpark/python/working-with-dataframes).

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/connections/snowpark_connection.py#L166 "View st.session source code on GitHub") | |
| --- | --- |
| SnowparkConnection.session | |

#### Example

```

import streamlit as st

session = st.connection("snowpark").session
df = session.table("mytable").limit(10).to_pandas()
st.dataframe(df)

```

[Previous: st.experimental\_connection](/develop/api-reference/connections/st.experimental_connection)[Next: ExperimentalBaseConnection](/develop/api-reference/connections/st.connections.experimentalbaseconnection)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
