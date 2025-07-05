Connect Streamlit to TigerGraph - Streamlit Docs

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
* [TigerGraph](/develop/tutorials/databases/tigergraph)

Connect Streamlit to TigerGraph
===============================

Introduction
------------

This guide explains how to securely access a TigerGraph database from Streamlit Community Cloud. It uses the [pyTigerGraph](https://pytigergraph.github.io/pyTigerGraph/GettingStarted/) library and Streamlit's [Secrets management](/develop/concepts/connections/secrets-management).

Create a TigerGraph Cloud Database
----------------------------------

First, follow the official tutorials to create a TigerGraph instance in TigerGraph Cloud, either as a [blog](https://www.tigergraph.com/blog/getting-started-with-tigergraph-3-0/) or a [video](https://www.youtube.com/watch?v=NtNW2e8MfCQ). Note your username, password, and subdomain.

For this tutorial, we will be using the COVID-19 starter kit. When setting up your solution, select the “COVID-19 Analysis" option.

![TG_Cloud_COVID19](/images/databases/tigergraph-1.png)

Once it is started, ensure your data is downloaded and queries are installed.

![TG_Cloud_Schema](/images/databases/tigergraph-2.png)

Add username and password to your local app secrets
---------------------------------------------------

Your local Streamlit app will read secrets from a file `.streamlit/secrets.toml` in your app’s root directory. Create this file if it doesn’t exist yet and add your TigerGraph Cloud instance username, password, graph name, and subdomain as shown below:

`# .streamlit/secrets.toml
[tigergraph]
host = "https://xxx.i.tgcloud.io/"
username = "xxx"
password = "xxx"
graphname = "xxx"`

*priority\_high*

#### Important

Add this file to `.gitignore` and don't commit it to your GitHub repo!

Copy your app secrets to the cloud
----------------------------------

As the `secrets.toml` file above is not committed to GitHub, you need to pass its content to your deployed app (on Streamlit Community Cloud) separately. Go to the [app dashboard](https://share.streamlit.io/) and in the app's dropdown menu, click on Edit Secrets. Copy the content of `secrets.toml` into the text area. More information is available at [Secrets management](/deploy/streamlit-community-cloud/deploy-your-app/secrets-management).

![Secrets manager screenshot](/images/databases/edit-secrets.png)

Add PyTigerGraph to your requirements file
------------------------------------------

Add the pyTigerGraph package to your `requirements.txt` file, preferably pinning its version (replace `x.x.x` with the version you want installed):

`# requirements.txt
pyTigerGraph==x.x.x`

Write your Streamlit app
------------------------

Copy the code below to your Streamlit app and run it. Make sure to adapt the name of your graph and query.

`# streamlit_app.py
import streamlit as st
import pyTigerGraph as tg
# Initialize connection.
conn = tg.TigerGraphConnection(**st.secrets["tigergraph"])
conn.apiToken = conn.getToken(conn.createSecret())
# Pull data from the graph by running the "mostDirectInfections" query.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def get_data():
most_infections = conn.runInstalledQuery("mostDirectInfections")[0]["Answer"][0]
return most_infections["v_id"], most_infections["attributes"]
items = get_data()
# Print results.
st.title(f"Patient {items[0]} has the most direct infections")
for key, val in items[1].items():
st.write(f"Patient {items[0]}'s {key} is {val}.")`

See `st.cache_data` above? Without it, Streamlit would run the query every time the app reruns (e.g. on a widget interaction). With `st.cache_data`, it only runs when the query changes or after 10 minutes (that's what `ttl` is for). Watch out: If your database updates more frequently, you should adapt `ttl` or remove caching so viewers always see the latest data. Learn more in [Caching](/develop/concepts/architecture/caching).

If everything worked out (and you used the example data we created above), your app should look like this:

![Final_App](/images/databases/tigergraph-3.png)

[Previous: TiDB](/develop/tutorials/databases/tidb)[Next: Elements](/develop/tutorials/elements)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
