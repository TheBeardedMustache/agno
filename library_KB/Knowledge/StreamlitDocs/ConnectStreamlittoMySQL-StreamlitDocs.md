﻿Connect Streamlit to MySQL - Streamlit Docs

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
* [MySQL](/develop/tutorials/databases/mysql)

Connect Streamlit to MySQL
==========================

Introduction
------------

This guide explains how to securely access a ***remote*** MySQL database from Streamlit Community Cloud. It uses [st.connection](/develop/api-reference/connections/st.connection) and Streamlit's [Secrets management](/develop/concepts/connections/secrets-management). The below example code will **only work on Streamlit version >= 1.28**, when `st.connection` was added.

Create a MySQL database
-----------------------

*push\_pin*

#### Note

If you already have a database that you want to use, feel free
to [skip to the next step](/develop/tutorials/databases/mysql#add-username-and-password-to-your-local-app-secrets).

First, follow [this tutorial](https://dev.mysql.com/doc/mysql-getting-started/en/) to install MySQL and start the MySQL server (note down the username and password!). Once your MySQL server is up and running, connect to it with the `mysql` client and enter the following commands to create a database and a table with some example values:

`CREATE DATABASE pets;
USE pets;
CREATE TABLE mytable (
name varchar(80),
pet varchar(80)
);
INSERT INTO mytable VALUES ('Mary', 'dog'), ('John', 'cat'), ('Robert', 'bird');`

Add username and password to your local app secrets
---------------------------------------------------

Your local Streamlit app will read secrets from a file `.streamlit/secrets.toml` in your app's root directory. Learn more about [Streamlit secrets management here](/develop/concepts/connections/secrets-management). Create this file if it doesn't exist yet and add the database name, user, and password of your MySQL server as shown below:

`# .streamlit/secrets.toml
[connections.mysql]
dialect = "mysql"
host = "localhost"
port = 3306
database = "xxx"
username = "xxx"
password = "xxx"
query = { charset = "xxx" }`

If you use `query` when defining your connection, you must use `streamlit>=1.35.0`.

*priority\_high*

#### Important

When copying your app secrets to Streamlit Community Cloud, be sure to replace the values of **host**, **port**, **database**, **username**, and **password** with those of your *remote* MySQL database!

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
conn = st.connection('mysql', type='sql')
# Perform query.
df = conn.query('SELECT * from mytable;', ttl=600)
# Print results.
for row in df.itertuples():
st.write(f"{row.name} has a :{row.pet}:")`

See `st.connection` above? This handles secrets retrieval, setup, query caching and retries. By default, `query()` results are cached without expiring. In this case, we set `ttl=600` to ensure the query result is cached for no longer than 10 minutes. You can also set `ttl=0` to disable caching. Learn more in [Caching](/develop/concepts/architecture/caching).

If everything worked out (and you used the example table we created above), your app should look like this:

![Finished app screenshot](/images/databases/streamlit-app.png)

[Previous: MongoDB](/develop/tutorials/databases/mongodb)[Next: Neon](/develop/tutorials/databases/neon)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
