st.connections.SnowflakeConnection - Streamlit Docs

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
* [SnowflakeConnection](/develop/api-reference/connections/st.connections.snowflakeconnection)

*star*

#### Tip

This page only contains the `st.connections.SnowflakeConnection` class. For a deeper dive into creating and managing data connections within Streamlit apps, see [Connect Streamlit to Snowflake](/develop/tutorials/databases/snowflake) and [Connecting to data](/develop/concepts/connections/connecting-to-data).

st.connections.SnowflakeConnection
----------------------------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

A connection to Snowflake using the Snowflake Connector for Python.

Initialize this connection object using st.connection("snowflake") or
st.connection("<name>", type="snowflake"). Connection parameters for a
SnowflakeConnection can be specified using secrets.toml and/or
\*\*kwargs. Connection parameters are passed to
snowflake.connector.connect().

When an app is running in Streamlit in Snowflake,
st.connection("snowflake") connects automatically using the app owner's
role without further configuration. \*\*kwargs will be ignored in this
case. Use secrets.toml and \*\*kwargs to configure your connection
for local development.

SnowflakeConnection includes several convenience methods. For example, you
can directly execute a SQL query with .query() or access the underlying
Snowflake Connector object with .raw\_connection.

Tip

[snowflake-snowpark-python](https://pypi.org/project/snowflake-snowpark-python/)
must be installed in your environment to use this connection. You can
install Snowflake extras along with Streamlit:

```

>>> pip install streamlit[snowflake]

```

Important

Account identifiers must be of the form <orgname>-<account\_name>
where <orgname> is the name of your Snowflake organization and
<account\_name> is the unique name of your account within your
organization. This is dash-separated, not dot-separated like when used
in SQL queries. For more information, see [Account identifiers](https://docs.snowflake.com/en/user-guide/admin-account-identifier).

| Class description[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/connections/snowflake_connection.py#L49 "View st.SnowflakeConnection source code on GitHub") | |
| --- | --- |
| st.connections.SnowflakeConnection(connection\_name, \*\*kwargs) | |
|  |  |
| --- | --- |
| Methods | |
| [cursor](/develop/api-reference/connections/st.connections.snowflakeconnection#snowflakeconnectioncursor)() | Create a new cursor object from this connection. |
| [query](/develop/api-reference/connections/st.connections.snowflakeconnection#snowflakeconnectionquery)(sql, \*, ttl=None, show\_spinner="Running `snowflake.query(...)`.", params=None, \*\*kwargs) | Run a read-only SQL query. |
| [reset](/develop/api-reference/connections/st.connections.snowflakeconnection#snowflakeconnectionreset)() | Reset this connection so that it gets reinitialized the next time it's used. |
| [session](/develop/api-reference/connections/st.connections.snowflakeconnection#snowflakeconnectionsession)() | Create a new Snowpark session from this connection. |
| [write\_pandas](/develop/api-reference/connections/st.connections.snowflakeconnection#snowflakeconnectionwrite_pandas)(df, table\_name, database=None, schema=None, chunk\_size=None, \*\*kwargs) | Write a pandas.DataFrame to a table in a Snowflake database. |
| Attributes | |
| [raw\_connection](/develop/api-reference/connections/st.connections.snowflakeconnection#snowflakeconnectionraw_connection) | Access the underlying connection object from the Snowflake Connector for Python. |

#### Examples

**Example 1: Configuration with Streamlit secrets**

You can configure your Snowflake connection using Streamlit's
[Secrets management](https://docs.streamlit.io/develop/concepts/connections/secrets-management).
For example, if you have MFA enabled on your account, you can connect using
[key-pair authentication](https://docs.snowflake.com/en/user-guide/key-pair-auth).

.streamlit/secrets.toml:

```

[connections.snowflake]
account = "xxx-xxx"
user = "xxx"
private_key_file = "/xxx/xxx/xxx.p8"
role = "xxx"
warehouse = "xxx"
database = "xxx"
schema = "xxx"

```

Your app code:

```

import streamlit as st
conn = st.connection("snowflake")
df = conn.query("SELECT * FROM my_table")

```

**Example 2: Configuration with keyword arguments and external authentication**

You can configure your Snowflake connection with keyword arguments. The
keyword arguments are merged with (and take precedence over) the values in
secrets.toml. However, if you name your connection "snowflake" and
don't have a [connections.snowflake] dictionary in your
secrets.toml file, Streamlit will ignore any keyword arguments and use
the default Snowflake connection as described in Example 5 and Example 6.
To configure your connection using only keyword arguments, declare a name
for the connection other than "snowflake".

For example, if your Snowflake account supports SSO, you can set up a quick
local connection for development using [browser-based SSO](https://docs.snowflake.com/en/user-guide/admin-security-fed-auth-use#how-browser-based-sso-works).
Because there is nothing configured in secrets.toml, the name is an
empty string and the type is set to "snowflake". This prevents
Streamlit from ignoring the keyword arguments and using a default
Snowflake connection.

```

import streamlit as st
conn = st.connection(
    "",
    type="snowflake",
    account="xxx-xxx",
    user="xxx",
    authenticator="externalbrowser",
)
df = conn.query("SELECT * FROM my_table")

```

**Example 3: Named connection with Snowflake's connection configuration file**

Snowflake's Python Connector supports a [connection configuration file](https://docs.snowflake.com/en/developer-guide/python-connector/python-connector-connect#connecting-using-the-connections-toml-file),
which is well integrated with Streamlit's SnowflakeConnection. If you
already have one or more connections configured, all you need to do is pass
the name of the connection to use.

~/.snowflake/connections.toml:

```

[my_connection]
account = "xxx-xxx"
user = "xxx"
password = "xxx"
warehouse = "xxx"
database = "xxx"
schema = "xxx"

```

Your app code:

```

import streamlit as st
conn = st.connection("my_connection", type="snowflake")
df = conn.query("SELECT * FROM my_table")

```

**Example 4: Named connection with Streamlit secrets and Snowflake's connection configuration file**

If you have a Snowflake configuration file with a connection named
my\_connection as in Example 3, you can pass the connection name through
secrets.toml.

.streamlit/secrets.toml:

```

[connections.snowflake]
connection_name = "my_connection"

```

Your app code:

```

import streamlit as st
conn = st.connection("snowflake")
df = conn.query("SELECT * FROM my_table")

```

**Example 5: Default connection with an environment variable**

If you don't have a [connections.snowflake] dictionary in your
secrets.toml file and use st.connection("snowflake"), Streamlit
will use the default connection for the [Snowflake Python Connector](https://docs.snowflake.cn/en/developer-guide/python-connector/python-connector-connect#setting-a-default-connection).

If you have a Snowflake configuration file with a connection named
my\_connection as in Example 3, you can set an environment variable to
declare it as the default Snowflake connection.

```

SNOWFLAKE_DEFAULT_CONNECTION_NAME = "my_connection"

```

Your app code:

```

import streamlit as st
conn = st.connection("snowflake")
df = conn.query("SELECT * FROM my_table")

```

**Example 6: Default connection in Snowflake's connection configuration file**

If you have a Snowflake configuration file that defines your default
connection, Streamlit will automatically use it if no other connection is
declared.

~/.snowflake/connections.toml:

```

[default]
account = "xxx-xxx"
user = "xxx"
password = "xxx"
warehouse = "xxx"
database = "xxx"
schema = "xxx"

```

Your app code:

```

import streamlit as st
conn = st.connection("snowflake")
df = conn.query("SELECT * FROM my_table")

```

SnowflakeConnection.cursor
--------------------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Create a new cursor object from this connection.

Snowflake Connector cursors implement the Python Database API v2.0
specification (PEP-249). For more information, see the
[Snowflake Connector for Python documentation](https://docs.snowflake.com/en/developer-guide/python-connector/python-connector-api#object-cursor).

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/connections/snowflake_connection.py#L457 "View st.cursor source code on GitHub") | |
| --- | --- |
| SnowflakeConnection.cursor() | |
|  |  |
| --- | --- |
| Returns | |
| (snowflake.connector.cursor.SnowflakeCursor) | A cursor object for the connection. |

#### Example

The following example uses a cursor to insert multiple rows into a
table. The qmark parameter style is specified as an optional
keyword argument. Alternatively, the parameter style can be declared in
your connection configuration file. For more information, see the
[Snowflake Connector for Python documentation](https://docs.snowflake.com/en/developer-guide/python-connector/python-connector-example#using-qmark-or-numeric-binding).

```

import streamlit as st

conn = st.connection("snowflake", "paramstyle"="qmark")
rows_to_insert = [("Mary", "dog"), ("John", "cat"), ("Robert", "bird")]
conn.cursor().executemany(
    "INSERT INTO mytable (name, pet) VALUES (?, ?)", rows_to_insert
)

```

SnowflakeConnection.query
-------------------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Run a read-only SQL query.

This method implements query result caching and simple error
handling/retries. The caching behavior is identical to that of using
@st.cache\_data.

Note

Queries that are run without a specified ttl are cached
indefinitely.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/connections/snowflake_connection.py#L282 "View st.query source code on GitHub") | |
| --- | --- |
| SnowflakeConnection.query(sql, \*, ttl=None, show\_spinner="Running `snowflake.query(...)`.", params=None, \*\*kwargs) | |
| Parameters | |
| sql (str) | The read-only SQL query to execute. |
| ttl (float, int, timedelta or None) | The maximum number of seconds to keep results in the cache. If this is None (default), cached results do not expire with time. |
| show\_spinner (boolean or string) | Whether to enable the spinner. When a cached query is executed, no spinner is displayed because the result is immediately available. When a new query is executed, the default is to show a spinner with the message "Running snowflake.query(...)."  If this is False, no spinner displays while executing the query. If this is a string, the string will be used as the message for the spinner. |
| params (list, tuple, dict or None) | List of parameters to pass to the Snowflake Connector for Python Cursor.execute() method. This connector supports binding data to a SQL statement using qmark bindings. For more information and examples, see the [Snowflake Connector for Python documentation](https://docs.snowflake.com/en/developer-guide/python-connector/python-connector-example#using-qmark-or-numeric-binding). This defaults to None. |
|  |  |
| --- | --- |
| Returns | |
| (pandas.DataFrame) | The result of running the query, formatted as a pandas DataFrame. |

#### Example

```

import streamlit as st

conn = st.connection("snowflake")
df = conn.query("SELECT * FROM my_table")
st.dataframe(df)

```

SnowflakeConnection.raw\_connection
-----------------------------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Access the underlying connection object from the Snowflake Connector for Python.

For information on how to use the Snowflake Connector for Python, see
the [Snowflake Connector for Python documentation](https://docs.snowflake.com/en/developer-guide/python-connector/python-connector-example).

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/connections/snowflake_connection.py#L490 "View st.raw_connection source code on GitHub") | |
| --- | --- |
| SnowflakeConnection.raw\_connection | |
|  |  |
| --- | --- |
| Returns | |
| (snowflake.connector.connection.SnowflakeConnection) | The connection object. |

#### Example

The following example uses a cursor to submit an asynchronous query,
saves the query ID, then periodically checks the query status through
the connection before retrieving the results.

```

import streamlit as st
import time

conn = st.connection("snowflake")
cur = conn.cursor()
cur.execute_async("SELECT * FROM my_table")
query_id = cur.sfqid
while True:
    status = conn.raw_connection.get_query_status(query_id)
    if conn.raw_connection.is_still_running(status):
        time.sleep(1)
    else:
        break
cur.get_results_from_sfqid(query_id)
df = cur.fetchall()

```

SnowflakeConnection.reset
-------------------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Reset this connection so that it gets reinitialized the next time it's used.

This method can be useful when a connection has become stale, an auth token has
expired, or in similar scenarios where a broken connection might be fixed by
reinitializing it. Note that some connection methods may already use reset()
in their error handling code.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/connections/base_connection.py#L121 "View st.reset source code on GitHub") | |
| --- | --- |
| SnowflakeConnection.reset() | |
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

SnowflakeConnection.session
---------------------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Create a new Snowpark session from this connection.

For information on how to use Snowpark sessions, see the
[Snowpark developer guide](https://docs.snowflake.com/en/developer-guide/snowpark/python/working-with-dataframes)
and [Snowpark API Reference](https://docs.snowflake.com/en/developer-guide/snowpark/reference/python/latest/snowpark/session).

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/connections/snowflake_connection.py#L529 "View st.session source code on GitHub") | |
| --- | --- |
| SnowflakeConnection.session() | |
|  |  |
| --- | --- |
| Returns | |
| (snowflake.snowpark.Session) | A new Snowpark session for this connection. |

#### Example

The following example creates a new Snowpark session and uses it to run
a query.

```

import streamlit as st

conn = st.connection("snowflake")
session = conn.session()
df = session.sql("SELECT * FROM my_table").collect()

```

SnowflakeConnection.write\_pandas
---------------------------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Write a pandas.DataFrame to a table in a Snowflake database.

This convenience method is a thin wrapper around
snowflake.connector.pandas\_tools.write\_pandas() using the
underlying connection. The conn parameter is passed automatically.
For more information and additional keyword arguments, see the
[Snowflake Connector for Python documentation](https://docs.snowflake.com/en/developer-guide/python-connector/python-connector-api#write_pandas).

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/connections/snowflake_connection.py#L375 "View st.write_pandas source code on GitHub") | |
| --- | --- |
| SnowflakeConnection.write\_pandas(df, table\_name, database=None, schema=None, chunk\_size=None, \*\*kwargs) | |
| Parameters | |
| df (pandas.DataFrame) | The pandas.DataFrame object containing the data to be copied into the table. |
| table\_name (str) | Name of the table where the data should be copied to. |
| database (str) | Name of the database containing the table. By default, the function writes to the database that is currently in use in the session.  Note  If you specify this parameter, you must also specify the schema parameter. |
| schema (str) | Name of the schema containing the table. By default, the function writes to the table in the schema that is currently in use in the session. |
| chunk\_size (int) | Number of elements to insert at a time. By default, the function inserts all elements in one chunk. |
| \*\*kwargs (Any) | Additional keyword arguments for snowflake.connector.pandas\_tools.write\_pandas(). |
|  |  |
| --- | --- |
| Returns | |
| (tuple[bool, int, int]) | A tuple containing three values:   1. A boolean value that is True if the write was successful. 2. An integer giving the number of chunks of data that were copied. 3. An integer giving the number of rows that were inserted. |

#### Example

The following example uses the database and schema currently in use in
the session and copies the data into a table named "my\_table."

```

import streamlit as st
import pandas as pd

df = pd.DataFrame(
    {"Name": ["Mary", "John", "Robert"], "Pet": ["dog", "cat", "bird"]}
)
conn = st.connection("snowflake")
conn.write_pandas(df, "my_table")

```

[Previous: st.connection](/develop/api-reference/connections/st.connection)[Next: SQLConnection](/develop/api-reference/connections/st.connections.sqlconnection)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
