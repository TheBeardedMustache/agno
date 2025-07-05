Connect Streamlit to TiDB - Streamlit Docs

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

    *add*
  + [Tutorials](/develop/tutorials)

    *remove*

    - [Authentication and personalization](/develop/tutorials/authentication)

      *add*
    - [Chat and LLM apps](/develop/tutorials/chat-and-llm-apps)

      *add*
    - [Configuration and theming](/develop/tutorials/configuration-and-theming)

      *add*
    - [Connect to data sources](/develop/tutorials/databases)

      *remove*

      * [AWS S3](/develop/tutorials/databases/aws-s3)
      * [BigQuery](/develop/tutorials/databases/bigquery)
      * [Firestore*open\_in\_new*](https://blog.streamlit.io/streamlit-firestore/)
      * [Google Cloud Storage](/develop/tutorials/databases/gcs)
      * [Microsoft SQL Server](/develop/tutorials/databases/mssql)
      * [MongoDB](/develop/tutorials/databases/mongodb)
      * [MySQL](/develop/tutorials/databases/mysql)
      * [Neon](/develop/tutorials/databases/neon)
      * [PostgreSQL](/develop/tutorials/databases/postgresql)
      * [Private Google Sheet](/develop/tutorials/databases/private-gsheet)
      * [Public Google Sheet](/develop/tutorials/databases/public-gsheet)
      * [Snowflake](/develop/tutorials/databases/snowflake)
      * [Supabase](/develop/tutorials/databases/supabase)
      * [Tableau](/develop/tutorials/databases/tableau)
      * [TiDB](/develop/tutorials/databases/tidb)
      * [TigerGraph](/develop/tutorials/databases/tigergraph)
    - [Elements](/develop/tutorials/elements)

      *add*
    - [Execution flow](/develop/tutorials/execution-flow)

      *add*
    - [Multipage apps](/develop/tutorials/multipage)

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
* [Tutorials](/develop/tutorials)/
* [Connect to data sources](/develop/tutorials/databases)/
* [TiDB](/develop/tutorials/databases/tidb)

Connect Streamlit to TiDB
=========================

Introduction
------------

This guide explains how to securely access a ***remote*** TiDB database from Streamlit Community Cloud. It uses [st.connection](/develop/api-reference/connections/st.connection) and Streamlit's [Secrets management](/develop/concepts/connections/secrets-management). The below example code will **only work on Streamlit version >= 1.28**, when `st.connection` was added.

[TiDB](https://www.pingcap.com/tidb/) is an open-source, MySQL-compatible database that supports Hybrid Transactional and Analytical Processing (HTAP) workloads. TiDB introducs a [built-in vector search](https://www.pingcap.com/ai/) to the SQL database family, enabling support for your AI applications without requiring a new database or additional technical stacks. [TiDB Cloud](https://tidb.cloud/) is a fully managed cloud database service that simplifies the deployment and management of TiDB databases for developers.

Sign in to TiDB Cloud and create a cluster
------------------------------------------

First, head over to [TiDB Cloud](https://tidbcloud.com/free-trial) and sign up for a free account, using either Google, GitHub, Microsoft or E-mail:

![Sign up TiDB Cloud](/images/databases/tidb-1.png)

Once you've signed in, you will already have a TiDB cluster:

![List clusters](/images/databases/tidb-2.png)

You can create more clusters if you want to. Click the cluster name to enter cluster overview page:

![Cluster overview](/images/databases/tidb-3.png)

Then click **Connect** to easily get the connection arguments to access the cluster. On the popup, click **Generate Password** to set the password.

![Get connection arguments](/images/databases/tidb-4.png)

*priority\_high*

#### Important

Make sure to note down the password. It won't be available on TiDB Cloud after this step.

Create a TiDB database
----------------------

*push\_pin*

#### Note

If you already have a database that you want to use, feel free
to [skip to the next step](/develop/tutorials/databases/tidb#add-username-and-password-to-your-local-app-secrets).

Once your TiDB cluster is up and running, connect to it with the `mysql` client(or with **SQL Editor** tab on the console) and enter the following commands to create a database and a table with some example values:

`CREATE DATABASE pets;
USE pets;
CREATE TABLE mytable (
name varchar(80),
pet varchar(80)
);
INSERT INTO mytable VALUES ('Mary', 'dog'), ('John', 'cat'), ('Robert', 'bird');`

Add username and password to your local app secrets
---------------------------------------------------

Your local Streamlit app will read secrets from a file `.streamlit/secrets.toml` in your app's root directory. Learn more about [Streamlit secrets management here](/develop/concepts/connections/secrets-management). Create this file if it doesn't exist yet and add host, username and password of your TiDB cluster as shown below:

`# .streamlit/secrets.toml
[connections.tidb]
dialect = "mysql"
host = "<TiDB_cluster_host>"
port = 4000
database = "pets"
username = "<TiDB_cluster_user>"
password = "<TiDB_cluster_password>"`

*priority\_high*

#### Important

When copying your app secrets to Streamlit Community Cloud, be sure to replace the values of **host**, **username** and **password** with those of your *remote* TiDB cluster!

Add this file to `.gitignore` and don't commit it to your GitHub repo!

Copy your app secrets to the cloud
----------------------------------

As the `secrets.toml` file above is not committed to GitHub, you need to pass its content to your deployed app (on Streamlit Community Cloud) separately. Go to the [app dashboard](https://share.streamlit.io/) and in the app's dropdown menu, click on **Edit Secrets**. Copy the content of `secrets.toml` into the text area. More information is available at [Secrets management](/deploy/streamlit-community-cloud/deploy-your-app/secrets-management).

![Secrets manager screenshot](/images/databases/edit-secrets.png)

Add dependencies to your requirements file
------------------------------------------

Add the [mysqlclient](https://github.com/PyMySQL/mysqlclient) and [SQLAlchemy](https://github.com/sqlalchemy/sqlalchemy) packages to your `requirements.txt` file, preferably pinning its version (replace `x.x.x` with the version you want installed):

`# requirements.txt
mysqlclient==x.x.x
SQLAlchemy==x.x.x`

Write your Streamlit app
------------------------

Copy the code below to your Streamlit app and run it. Make sure to adapt `query` to use the name of your table.

`# streamlit_app.py
import streamlit as st
# Initialize connection.
conn = st.connection('tidb', type='sql')
# Perform query.
df = conn.query('SELECT * from mytable;', ttl=600)
# Print results.
for row in df.itertuples():
st.write(f"{row.name} has a :{row.pet}:")`

See `st.connection` above? This handles secrets retrieval, setup, query caching and retries. By default, `query()` results are cached without expiring. In this case, we set `ttl=600` to ensure the query result is cached for no longer than 10 minutes. You can also set `ttl=0` to disable caching. Learn more in [Caching](/develop/concepts/architecture/caching).

If everything worked out (and you used the example table we created above), your app should look like this:

![Finished app screenshot](/images/databases/streamlit-app.png)

Connect with PyMySQL
--------------------

Other than [mysqlclient](https://github.com/PyMySQL/mysqlclient), [PyMySQL](https://github.com/PyMySQL/PyMySQL) is another popular MySQL Python client. To use PyMySQL, first you need to adapt your requirements file:

`# requirements.txt
PyMySQL==x.x.x
SQLAlchemy==x.x.x`

Then adapt your secrets file:

`# .streamlit/secrets.toml
[connections.tidb]
dialect = "mysql"
driver = "pymysql"
host = "<TiDB_cluster_host>"
port = 4000
database = "pets"
username = "<TiDB_cluster_user>"
password = "<TiDB_cluster_password>"
create_engine_kwargs = { connect_args = { ssl = { ca = "<path_to_CA_store>" }}}`

[Previous: Tableau](/develop/tutorials/databases/tableau)[Next: TigerGraph](/develop/tutorials/databases/tigergraph)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
