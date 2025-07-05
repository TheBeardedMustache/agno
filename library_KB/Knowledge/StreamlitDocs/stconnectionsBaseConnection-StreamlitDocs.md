st.connections.BaseConnection - Streamlit Docs

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
* [BaseConnection](/develop/api-reference/connections/st.connections.baseconnection)

*star*

#### Tip

This page only contains information on the `st.connections.BaseConnection` class. For a deeper dive into creating and managing data connections within Streamlit apps, read [Connecting to data](/develop/concepts/connections/connecting-to-data).

st.connections.BaseConnection
-----------------------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

The abstract base class that all Streamlit Connections must inherit from.

This base class provides connection authors with a standardized way to hook into the
st.connection() factory function: connection authors are required to provide an
implementation for the abstract method \_connect in their subclasses.

Additionally, it also provides a few methods/properties designed to make
implementation of connections more convenient. See the docstrings for each of the
methods of this class for more information

Note

While providing an implementation of \_connect is technically all that's
required to define a valid connection, connections should also provide the user
with context-specific ways of interacting with the underlying connection object.
For example, the first-party SQLConnection provides a query() method for
reads and a session property for more complex operations.

| Class description[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/connections/base_connection.py#L27 "View st.BaseConnection source code on GitHub") | |
| --- | --- |
| st.connections.BaseConnection(connection\_name, \*\*kwargs) | |
|  |  |
| --- | --- |
| Methods | |
| [reset](/develop/api-reference/connections/st.connections.baseconnection#baseconnectionreset)() | Reset this connection so that it gets reinitialized the next time it's used. |

BaseConnection.reset
--------------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Reset this connection so that it gets reinitialized the next time it's used.

This method can be useful when a connection has become stale, an auth token has
expired, or in similar scenarios where a broken connection might be fixed by
reinitializing it. Note that some connection methods may already use reset()
in their error handling code.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/connections/base_connection.py#L121 "View st.reset source code on GitHub") | |
| --- | --- |
| BaseConnection.reset() | |
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

[Previous: SQLConnection](/develop/api-reference/connections/st.connections.sqlconnection)[Next: st.experimental\_connection](/develop/api-reference/connections/st.experimental_connection)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
