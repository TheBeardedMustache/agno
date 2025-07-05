st.connections.SQLConnection - Streamlit Docs

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
* [SQLConnection](/develop/api-reference/connections/st.connections.sqlconnection)

*star*

#### Tip

This page only contains the `st.connections.SQLConnection` class. For a deeper dive into creating and managing data connections within Streamlit apps, read [Connecting to data](/develop/concepts/connections/connecting-to-data).

st.connections.SQLConnection
----------------------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

A connection to a SQL database using a SQLAlchemy Engine.

Initialize this connection object using st.connection("sql") or
st.connection("<name>", type="sql"). Connection parameters for a
SQLConnection can be specified using secrets.toml and/or \*\*kwargs.
Possible connection parameters include:

* url or keyword arguments for [sqlalchemy.engine.URL.create()](https://docs.sqlalchemy.org/en/20/core/engines.html#sqlalchemy.engine.URL.create), except
  drivername. Use dialect and driver instead of drivername.
* Keyword arguments for [sqlalchemy.create\_engine()](https://docs.sqlalchemy.org/en/20/core/engines.html#sqlalchemy.create_engine), including custom
  connect() arguments used by your specific dialect or driver.
* autocommit. If this is False (default), the connection operates
  in manual commit (transactional) mode. If this is True, the
  connection operates in autocommit (non-transactional) mode.

If url exists as a connection parameter, Streamlit will pass it to
sqlalchemy.engine.make\_url(). Otherwise, Streamlit requires (at a
minimum) dialect, username, and host. Streamlit will use
dialect and driver (if defined) to derive drivername, then pass
the relevant connection parameters to sqlalchemy.engine.URL.create().

In addition to the default keyword arguments for sqlalchemy.create\_engine(),
your dialect may accept additional keyword arguments. For example, if you
use dialect="snowflake" with [Snowflake SQLAlchemy](https://github.com/snowflakedb/snowflake-sqlalchemy#key-pair-authentication-support),
you can pass a value for private\_key to use key-pair authentication. If
you use dialect="bigquery" with [Google BigQuery](https://github.com/googleapis/python-bigquery-sqlalchemy#authentication),
you can pass a value for location.

SQLConnection provides the .query() convenience method, which can be
used to run simple, read-only queries with both caching and simple error
handling/retries. More complex database interactions can be performed by
using the .session property to receive a regular SQLAlchemy Session.

Important

[SQLAlchemy](https://pypi.org/project/SQLAlchemy/) must be installed
in your environment to use this connection. You must also install your
driver, such as pyodbc or psycopg2.

| Class description[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/connections/sql_connection.py#L54 "View st.SQLConnection source code on GitHub") | |
| --- | --- |
| st.connections.SQLConnection(connection\_name, \*\*kwargs) | |
|  |  |
| --- | --- |
| Methods | |
| [connect](/develop/api-reference/connections/st.connections.sqlconnection#sqlconnectionconnect)() | Call .connect() on the underlying SQLAlchemy Engine, returning a new connection object. |
| [query](/develop/api-reference/connections/st.connections.sqlconnection#sqlconnectionquery)(sql, \*, show\_spinner="Running `sql.query(...)`.", ttl=None, index\_col=None, chunksize=None, params=None, \*\*kwargs) | Run a read-only query. |
| [reset](/develop/api-reference/connections/st.connections.sqlconnection#sqlconnectionreset)() | Reset this connection so that it gets reinitialized the next time it's used. |
| Attributes | |
| [driver](/develop/api-reference/connections/st.connections.sqlconnection#sqlconnectiondriver) | The name of the driver used by the underlying SQLAlchemy Engine. |
| [engine](/develop/api-reference/connections/st.connections.sqlconnection#sqlconnectionengine) | The underlying SQLAlchemy Engine. |
| [session](/develop/api-reference/connections/st.connections.sqlconnection#sqlconnectionsession) | Return a SQLAlchemy Session. |

#### Examples

**Example 1: Configuration with URL**

You can configure your SQL connection using Streamlit's
[Secrets management](https://docs.streamlit.io/develop/concepts/connections/secrets-management).
The following example specifies a SQL connection URL.

.streamlit/secrets.toml:

```

[connections.sql]
url = "xxx+xxx://xxx:xxx@xxx:xxx/xxx"

```

Your app code:

```

import streamlit as st

conn = st.connection("sql")
df = conn.query("SELECT * FROM pet_owners")
st.dataframe(df)

```

**Example 2: Configuration with dialect, host, and username**

If you do not specify url, you must at least specify dialect,
host, and username instead. The following example also includes
password.

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
df = conn.query("SELECT * FROM pet_owners")
st.dataframe(df)

```

**Example 3: Configuration with keyword arguments**

You can configure your SQL connection with keyword arguments (with or
without secrets.toml). For example, if you use Microsoft Entra ID with
a Microsoft Azure SQL server, you can quickly set up a local connection for
development using [interactive authentication](https://learn.microsoft.com/en-us/sql/connect/odbc/using-azure-active-directory?view=sql-server-ver16#new-andor-modified-dsn-and-connection-string-keywords).

This example requires the [Microsoft ODBC Driver for SQL Server](https://learn.microsoft.com/en-us/sql/connect/odbc/microsoft-odbc-driver-for-sql-server?view=sql-server-ver16)
for *Windows* in addition to the sqlalchemy and pyodbc packages for
Python.

```

import streamlit as st

conn = st.connection(
    "sql",
    dialect="mssql",
    driver="pyodbc",
    host="xxx.database.windows.net",
    database="xxx",
    username="xxx",
    query={
        "driver": "ODBC Driver 18 for SQL Server",
        "authentication": "ActiveDirectoryInteractive",
        "encrypt": "yes",
    },
)

df = conn.query("SELECT * FROM pet_owners")
st.dataframe(df)

```

SQLConnection.connect
---------------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Call .connect() on the underlying SQLAlchemy Engine, returning a new connection object.

Calling this method is equivalent to calling self.\_instance.connect().

NOTE: This method should not be confused with the internal \_connect method used
to implement a Streamlit Connection.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/connections/sql_connection.py#L355 "View st.connect source code on GitHub") | |
| --- | --- |
| SQLConnection.connect() | |
|  |  |
| --- | --- |
| Returns | |
| (sqlalchemy.engine.Connection) | A new SQLAlchemy connection object. |

SQLConnection.query
-------------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Run a read-only query.

This method implements query result caching and simple error
handling/retries. The caching behavior is identical to that of using
@st.cache\_data.

Note

Queries that are run without a specified ttl are cached indefinitely.

All keyword arguments passed to this function are passed down to
[pandas.read\_sql](https://pandas.pydata.org/docs/reference/api/pandas.read_sql.html), except ttl.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/connections/sql_connection.py#L222 "View st.query source code on GitHub") | |
| --- | --- |
| SQLConnection.query(sql, \*, show\_spinner="Running `sql.query(...)`.", ttl=None, index\_col=None, chunksize=None, params=None, \*\*kwargs) | |
| Parameters | |
| sql (str) | The read-only SQL query to execute. |
| show\_spinner (boolean or string) | Enable the spinner. The default is to show a spinner when there is a "cache miss" and the cached resource is being created. If a string, the value of the show\_spinner param will be used for the spinner text. |
| ttl (float, int, timedelta or None) | The maximum number of seconds to keep results in the cache, or None if cached results should not expire. The default is None. |
| index\_col (str, list of str, or None) | Column(s) to set as index(MultiIndex). Default is None. |
| chunksize (int or None) | If specified, return an iterator where chunksize is the number of rows to include in each chunk. Default is None. |
| params (list, tuple, dict or None) | List of parameters to pass to the execute method. The syntax used to pass parameters is database driver dependent. Check your database driver documentation for which of the five syntax styles, described in [PEP 249 paramstyle](https://peps.python.org/pep-0249/#paramstyle), is supported. Default is None. |
| \*\*kwargs (dict) | Additional keyword arguments are passed to [pandas.read\_sql](https://pandas.pydata.org/docs/reference/api/pandas.read_sql.html). |
|  |  |
| --- | --- |
| Returns | |
| (pandas.DataFrame) | The result of running the query, formatted as a pandas DataFrame. |

#### Example

```

import streamlit as st

conn = st.connection("sql")
df = conn.query(
    "SELECT * FROM pet_owners WHERE owner = :owner",
    ttl=3600,
    params={"owner": "barbara"},
)
st.dataframe(df)

```

SQLConnection.reset
-------------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Reset this connection so that it gets reinitialized the next time it's used.

This method can be useful when a connection has become stale, an auth token has
expired, or in similar scenarios where a broken connection might be fixed by
reinitializing it. Note that some connection methods may already use reset()
in their error handling code.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/connections/base_connection.py#L121 "View st.reset source code on GitHub") | |
| --- | --- |
| SQLConnection.reset() | |
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

SQLConnection.driver
--------------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

The name of the driver used by the underlying SQLAlchemy Engine.

This is equivalent to accessing self.\_instance.driver.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/connections/sql_connection.py#L384 "View st.driver source code on GitHub") | |
| --- | --- |
| SQLConnection.driver | |
|  |  |
| --- | --- |
| Returns | |
| (str) | The name of the driver. For example, "pyodbc" or "psycopg2". |

SQLConnection.engine
--------------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

The underlying SQLAlchemy Engine.

This is equivalent to accessing self.\_instance.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/connections/sql_connection.py#L371 "View st.engine source code on GitHub") | |
| --- | --- |
| SQLConnection.engine | |
|  |  |
| --- | --- |
| Returns | |
| (sqlalchemy.engine.base.Engine) | The underlying SQLAlchemy Engine. |

SQLConnection.session
---------------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Return a SQLAlchemy Session.

Users of this connection should use the contextmanager pattern for writes,
transactions, and anything more complex than simple read queries.

See the usage example below, which assumes we have a table numbers with a
single integer column val. The [SQLAlchemy](https://docs.sqlalchemy.org/en/20/orm/session_basics.html) docs also contain
much more information on the usage of sessions.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/connections/sql_connection.py#L397 "View st.session source code on GitHub") | |
| --- | --- |
| SQLConnection.session | |
|  |  |
| --- | --- |
| Returns | |
| (sqlalchemy.orm.Session) | A SQLAlchemy Session. |

#### Example

```

import streamlit as st
conn = st.connection("sql")
n = st.slider("Pick a number")
if st.button("Add the number!"):
    with conn.session as session:
        session.execute("INSERT INTO numbers (val) VALUES (:n);", {"n": n})
        session.commit()

```

[Previous: SnowflakeConnection](/develop/api-reference/connections/st.connections.snowflakeconnection)[Next: BaseConnection](/develop/api-reference/connections/st.connections.baseconnection)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
