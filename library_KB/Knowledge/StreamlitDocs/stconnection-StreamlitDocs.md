st.connection - Streamlit Docs

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
* [st.connection](/develop/api-reference/connections/st.connection)

*star*

#### Tip

This page only contains the `st.connection` API. For a deeper dive into creating and managing data connections within Streamlit apps, read [Connecting to data](/develop/concepts/connections/connecting-to-data).

st.connection
-------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Create a new connection to a data store or API, or return an existing one.

Configuration options, credentials, and secrets for connections are
combined from the following sources:

* The keyword arguments passed to this command.
* The app's secrets.toml files.
* Any connection-specific configuration files.

The connection returned from st.connection is internally cached with
st.cache\_resource and is therefore shared between sessions.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/runtime/connection_factory.py#L206 "View st.connection source code on GitHub") | |
| --- | --- |
| st.connection(name, type=None, max\_entries=None, ttl=None, \*\*kwargs) | |
| Parameters | |
| name (str) | The connection name used for secrets lookup in secrets.toml. Streamlit uses secrets under [connections.<name>] for the connection. type will be inferred if name is one of the following: "snowflake", "snowpark", or "sql". |
| type (str, connection class, or None) | The type of connection to create. This can be one of the following:   * None (default): Streamlit will infer the connection type from   name. If the type is not inferable from name, the type must   be specified in secrets.toml instead. * "snowflake": Streamlit will initialize a connection with   [SnowflakeConnection](https://docs.streamlit.io/develop/api-reference/connections/st.connections.snowflakeconnection). * "snowpark": Streamlit will initialize a connection with   [SnowparkConnection](https://docs.streamlit.io/develop/api-reference/connections/st.connections.snowparkconnection). This is deprecated. * "sql": Streamlit will initialize a connection with   [SQLConnection](https://docs.streamlit.io/develop/api-reference/connections/st.connections.sqlconnection). * A string path to an importable class: This must be a dot-separated   module path ending in the importable class. Streamlit will import the   class and initialize a connection with it. The class must extend   st.connections.BaseConnection. * An imported class reference: Streamlit will initialize a connection   with the referenced class, which must extend   st.connections.BaseConnection. |
| max\_entries (int or None) | The maximum number of connections to keep in the cache. If this is None (default), the cache is unbounded. Otherwise, when a new entry is added to a full cache, the oldest cached entry is removed. |
| ttl (float, timedelta, or None) | The maximum number of seconds to keep results in the cache. If this is None (default), cached results do not expire with time. |
| \*\*kwargs (any) | Connection-specific keyword arguments that are passed to the connection's .\_connect() method. \*\*kwargs are typically combined with (and take precedence over) key-value pairs in secrets.toml. To learn more, see the specific connection's documentation. |
|  |  |
| --- | --- |
| Returns | |
| (Subclass of BaseConnection) | An initialized connection object of the specified type. |

#### Examples

**Example 1: Inferred connection type**

The easiest way to create a first-party (SQL, Snowflake, or Snowpark) connection is
to use their default names and define corresponding sections in your secrets.toml
file. The following example creates a "sql"-type connection.

.streamlit/secrets.toml:

```

[connections.sql]
dialect = "xxx"
host = "xxx"
username = "xxx"
password = "xxx"

```

Your app code:

```

import streamlit as st
conn = st.connection("sql")

```

**Example 2: Named connections**

Creating a connection with a custom name requires you to explicitly
specify the type. If type is not passed as a keyword argument, it must
be set in the appropriate section of secrets.toml. The following
example creates two "sql"-type connections, each with their own
custom name. The first defines type in the st.connection command;
the second defines type in secrets.toml.

.streamlit/secrets.toml:

```

[connections.first_connection]
dialect = "xxx"
host = "xxx"
username = "xxx"
password = "xxx"

[connections.second_connection]
type = "sql"
dialect = "yyy"
host = "yyy"
username = "yyy"
password = "yyy"

```

Your app code:

```

import streamlit as st
conn1 = st.connection("first_connection", type="sql")
conn2 = st.connection("second_connection")

```

**Example 3: Using a path to the connection class**

Passing the full module path to the connection class can be useful,
especially when working with a custom connection. Although this is not the
typical way to create first party connections, the following example
creates the same type of connection as one with type="sql". Note that
type is a string path.

.streamlit/secrets.toml:

```

[connections.my_sql_connection]
url = "xxx+xxx://xxx:xxx@xxx:xxx/xxx"

```

Your app code:

```

import streamlit as st
conn = st.connection(
    "my_sql_connection", type="streamlit.connections.SQLConnection"
)

```

**Example 4: Importing the connection class**

You can pass the connection class directly to the st.connection
command. Doing so allows static type checking tools such as mypy to
infer the exact return type of st.connection. The following example
creates the same connection as in Example 3.

.streamlit/secrets.toml:

```

[connections.my_sql_connection]
url = "xxx+xxx://xxx:xxx@xxx:xxx/xxx"

```

Your app code:

```

import streamlit as st
from streamlit.connections import SQLConnection
conn = st.connection("my_sql_connection", type=SQLConnection)

```

For a comprehensive overview of this feature, check out this video tutorial by Joshua Carroll, Streamlit's Product Manager for Developer Experience. You'll learn about the feature's utility in creating and managing data connections within your apps by using real-world examples.

[Previous: secrets.toml](/develop/api-reference/connections/secrets.toml)[Next: SnowflakeConnection](/develop/api-reference/connections/st.connections.snowflakeconnection)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
