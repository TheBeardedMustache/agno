Connect Streamlit to Supabase - Streamlit Docs

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
* [Supabase](/develop/tutorials/databases/supabase)

Connect Streamlit to Supabase
=============================

Introduction
------------

This guide explains how to securely access a Supabase instance from Streamlit Community Cloud. It uses [st.connection](/develop/api-reference/connections/st.connection), [Streamlit Supabase Connector](https://github.com/SiddhantSadangi/st_supabase_connection/tree/main) (a community-built connection developed by [@SiddhantSadangi](https://github.com/SiddhantSadangi)) and Streamlit's [Secrets management](/develop/concepts/connections/secrets-management). Supabase is the open source Firebase alternative and is based on PostgreSQL.

*push\_pin*

#### Note

Community-built connections, such as the [Streamlit Supabase Connector](https://github.com/SiddhantSadangi/st_supabase_connection/tree/main), extend and build on the `st.connection` interface and make it easier than ever to build Streamlit apps with a wide variety of data sources. These type of connections work exactly the same as [the ones built into Streamlit](/develop/api-reference/connections) and have access to all the same capabilities.

Sign in to Supabase and create a project
----------------------------------------

First, head over to [Supabase](https://app.supabase.io/) and sign up for a free account using your GitHub.

![](/images/databases/supabase-1.png)

Sign in with GitHub

![](/images/databases/supabase-2.png)

Authorize Supabase

Once you're signed in, you can create a project.

![](/images/databases/supabase-3.png)

Your Supabase account

![](/images/databases/supabase-4.png)

Create a new project

Your screen should look like this once your project has been created:

![](/images/databases/supabase-5.png)

*priority\_high*

#### Important

Make sure to note down your Project API Key and Project URL highlighted in the above screenshot. ☝️

You will need these to connect to your Supabase instance from Streamlit.

Create a Supabase database
--------------------------

Now that you have a project, you can create a database and populate it with some sample data. To do so, click on the **SQL editor** button on the same project page, followed by the **New query** button in the SQL editor.

![](/images/databases/supabase-6.png)

Open the SQL editor

![](/images/databases/supabase-7.png)

Create a new query

In the SQL editor, enter the following queries to create a database and a table with some example values:

`CREATE TABLE mytable (
name varchar(80),
pet varchar(80)
);
INSERT INTO mytable VALUES ('Mary', 'dog'), ('John', 'cat'), ('Robert', 'bird');`

Click **Run** to execute the queries. To verify that the queries were executed successfully, click on the **Table Editor** button on the left menu, followed by your newly created table `mytable`.

![](/images/databases/supabase-8.png)

Write and run your queries

![](/images/databases/supabase-9.png)

View your table in the Table Editor

With your Supabase database created, you can now connect to it from Streamlit!

### Add Supabase Project URL and API key to your local app secrets

Your local Streamlit app will read secrets from a file `.streamlit/secrets.toml` in your app's root directory. Create this file if it doesn't exist yet and add the `SUPABASE_URL` and `SUPABASE_KEY` here:

`# .streamlit/secrets.toml
[connections.supabase]
SUPABASE_URL = "xxxx"
SUPABASE_KEY = "xxxx"`

Replace `xxxx` above with your Project URL and API key from [Step 1](/develop/tutorials/databases/supabase#sign-in-to-supabase-and-create-a-project).

*priority\_high*

#### Important

Add this file to `.gitignore` and don't commit it to your GitHub repo!

Copy your app secrets to the cloud
----------------------------------

As the `secrets.toml` file above is not committed to GitHub, you need to pass its content to your deployed app (on Streamlit Community Cloud) separately. Go to the [app dashboard](https://share.streamlit.io/) and in the app's dropdown menu, click on **Edit Secrets**. Copy the content of `secrets.toml` into the text area. More information is available at [Secrets management](/deploy/streamlit-community-cloud/deploy-your-app/secrets-management).

![Secrets manager screenshot](/images/databases/edit-secrets.png)

Add st-supabase-connection to your requirements file
----------------------------------------------------

Add the [`st-supabase-connection`](https://pypi.org/project/st-supabase-connection/) community-built connection library to your `requirements.txt` file, preferably pinning its version (replace `x.x.x` with the version you want installed):

`# requirements.txt
st-supabase-connection==x.x.x`

*star*

#### Tip

We've used the `st-supabase-connection` library here in combination with `st.connection` to benefit from the ease of setting up the data connection, managing your credentials, and Streamlit's caching capabilities that native and community-built connections provide.

You can however still directly use the [Supabase Python Client Library](https://pypi.org/project/supabase/) library if you prefer, but you'll need to write more code to set up the connection and cache the results. See [Using the Supabase Python Client Library](/develop/tutorials/databases/supabase#using-the-supabase-python-client-library) below for an example.

Write your Streamlit app
------------------------

Copy the code below to your Streamlit app and run it.

`# streamlit_app.py
import streamlit as st
from st_supabase_connection import SupabaseConnection
# Initialize connection.
conn = st.connection("supabase",type=SupabaseConnection)
# Perform query.
rows = conn.query("*", table="mytable", ttl="10m").execute()
# Print results.
for row in rows.data:
st.write(f"{row['name']} has a :{row['pet']}:")`

See `st.connection` above? This handles secrets retrieval, setup, query caching and retries. By default, `query()` results are cached without expiring. In this case, we set `ttl="10m"` to ensure the query result is cached for no longer than 10 minutes. You can also set `ttl=0` to disable caching. Learn more in [Caching](/develop/concepts/architecture/caching).

If everything worked out (and you used the example table we created above), your app should look like this:

![Finished app screenshot](/images/databases/supabase-10.png)

As Supabase uses PostgresSQL under the hood, you can also connect to Supabase by using the connection string Supabase provides under Settings > Databases. From there, you can refer to the [PostgresSQL tutorial](/develop/tutorials/databases/postgresql) to connect to your database.

Using the Supabase Python Client Library
----------------------------------------

If you prefer to use the [Supabase Python Client Library](https://pypi.org/project/supabase/) directly, you can do so by following the steps below.

1. Add your Supabase Project URL and API key to your local app secrets:

   Your local Streamlit app will read secrets from a file `.streamlit/secrets.toml` in your app's root directory. Create this file if it doesn't exist yet and add the SUPABASE\_URL and SUPABASE\_KEY here:

   `# .streamlit/secrets.toml
   SUPABASE_URL = "xxxx"
   SUPABASE_KEY = "xxxx"`
2. Add `supabase` to your requirements file:

   Add the [`supabase`](https://github.com/supabase-community/supabase-py) Python Client Library to your `requirements.txt` file, preferably pinning its version (replace `x.x.x` with the version you want installed):

   `# requirements.txt
   supabase==x.x.x`
3. Write your Streamlit app:

   Copy the code below to your Streamlit app and run it.

   `# streamlit_app.py
   import streamlit as st
   from supabase import create_client, Client
   # Initialize connection.
   # Uses st.cache_resource to only run once.
   @st.cache_resource
   def init_connection():
   url = st.secrets["SUPABASE_URL"]
   key = st.secrets["SUPABASE_KEY"]
   return create_client(url, key)
   supabase = init_connection()
   # Perform query.
   # Uses st.cache_data to only rerun when the query changes or after 10 min.
   @st.cache_data(ttl=600)
   def run_query():
   return supabase.table("mytable").select("*").execute()
   rows = run_query()
   # Print results.
   for row in rows.data:
   st.write(f"{row['name']} has a :{row['pet']}:")`

   See `st.cache_data` above? Without it, Streamlit would run the query every time the app reruns (e.g. on a widget interaction). With `st.cache_data`, it only runs when the query changes or after 10 minutes (that's what `ttl` is for). Watch out: If your database updates more frequently, you should adapt `ttl` or remove caching so viewers always see the latest data. Learn more in [Caching](/develop/concepts/architecture/caching).

[Previous: Snowflake](/develop/tutorials/databases/snowflake)[Next: Tableau](/develop/tutorials/databases/tableau)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
