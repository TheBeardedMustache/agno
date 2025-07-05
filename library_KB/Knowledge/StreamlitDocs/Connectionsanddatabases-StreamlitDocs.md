Connections and databases - Streamlit Docs

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
* [Connections and secrets](/develop/api-reference/connections)

Connections and databases
=========================

Setup your connection
---------------------

[![screenshot](/images/api/connection.svg)

#### Create a connection

Connect to a data source or API

`conn = st.connection('pets_db', type='sql')
pet_owners = conn.query('select * from pet_owners')
st.dataframe(pet_owners)`](/develop/api-reference/connections/st.connection)

Built-in connections
--------------------

[![screenshot](/images/api/connections.SnowflakeConnection.svg)

#### SnowflakeConnection

A connection to Snowflake.

`conn = st.connection('snowflake')`](/develop/api-reference/connections/st.connections.snowflakeconnection)[![screenshot](/images/api/connections.SQLConnection.svg)

#### SQLConnection

A connection to a SQL database using SQLAlchemy.

`conn = st.connection('sql')`](/develop/api-reference/connections/st.connections.sqlconnection)

Third-party connections
-----------------------

[#### Connection base class

Build your own connection with `BaseConnection`.

`class MyConnection(BaseConnection[myconn.MyConnection]):
def _connect(self, **kwargs) -> MyConnection:
return myconn.connect(**self._secrets, **kwargs)
def query(self, query):
return self._instance.query(query)`](/develop/api-reference/connections/st.connections.baseconnection)

Secrets
-------

[#### Secrets singleton

Access secrets from a local TOML file.

`key = st.secrets["OpenAI_key"]`](/develop/api-reference/connections/st.secrets)[#### Secrets file

Save your secrets in a per-project or per-profile TOML file.

`OpenAI_key = "<YOUR_SECRET_KEY>"`](/develop/api-reference/connections/secrets.toml)

Deprecated classes
------------------

[*delete*

#### SnowparkConnection

A connection to Snowflake.

`conn = st.connection("snowpark")`](/develop/api-reference/connections/st.connections.snowparkconnection)

[Previous: Caching and state](/develop/api-reference/caching-and-state)[Next: st.secrets](/develop/api-reference/connections/st.secrets)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
