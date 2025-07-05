Connect Streamlit to MongoDB - Streamlit Docs

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
* [MongoDB](/develop/tutorials/databases/mongodb)

Connect Streamlit to MongoDB
============================

Introduction
------------

This guide explains how to securely access a ***remote*** MongoDB database from Streamlit Community Cloud. It uses the [PyMongo](https://github.com/mongodb/mongo-python-driver) library and Streamlit's [Secrets management](/develop/concepts/connections/secrets-management).

Create a MongoDB Database
-------------------------

*push\_pin*

#### Note

If you already have a database that you want to use, feel free
to [skip to the next step](/develop/tutorials/databases/mongodb#add-username-and-password-to-your-local-app-secrets).

First, follow the official tutorials to [install MongoDB](https://docs.mongodb.com/guides/server/install/), [set up authentication](https://docs.mongodb.com/guides/server/auth/) (note down the username and password!), and [connect to the MongoDB instance](https://docs.mongodb.com/guides/server/drivers/). Once you are connected, open the `mongo` shell and enter the following two commands to create a collection with some example values:

`use mydb
db.mycollection.insertMany([{"name" : "Mary", "pet": "dog"}, {"name" : "John", "pet": "cat"}, {"name" : "Robert", "pet": "bird"}])`

Add username and password to your local app secrets
---------------------------------------------------

Your local Streamlit app will read secrets from a file `.streamlit/secrets.toml` in your app's root directory. Create this file if it doesn't exist yet and add the database information as shown below:

`# .streamlit/secrets.toml
[mongo]
host = "localhost"
port = 27017
username = "xxx"
password = "xxx"`

*priority\_high*

#### Important

When copying your app secrets to Streamlit Community Cloud, be sure to replace the values of **host**, **port**, **username**, and **password** with those of your *remote* MongoDB database!

Add this file to `.gitignore` and don't commit it to your GitHub repo!

Copy your app secrets to the cloud
----------------------------------

As the `secrets.toml` file above is not committed to GitHub, you need to pass its content to your deployed app (on Streamlit Community Cloud) separately. Go to the [app dashboard](https://share.streamlit.io/) and in the app's dropdown menu, click on **Edit Secrets**. Copy the content of `secrets.toml` into the text area. More information is available at [Secrets management](/deploy/streamlit-community-cloud/deploy-your-app/secrets-management).

![Secrets manager screenshot](/images/databases/edit-secrets.png)

Add PyMongo to your requirements file
-------------------------------------

Add the [PyMongo](https://github.com/mongodb/mongo-python-driver) package to your `requirements.txt` file, preferably pinning its version (replace `x.x.x` with the version you want installed):

`# requirements.txt
pymongo==x.x.x`

Write your Streamlit app
------------------------

Copy the code below to your Streamlit app and run it. Make sure to adapt the name of your database and collection.

`# streamlit_app.py
import streamlit as st
import pymongo
# Initialize connection.
# Uses st.cache_resource to only run once.
@st.cache_resource
def init_connection():
return pymongo.MongoClient(**st.secrets["mongo"])
client = init_connection()
# Pull data from the collection.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def get_data():
db = client.mydb
items = db.mycollection.find()
items = list(items) # make hashable for st.cache_data
return items
items = get_data()
# Print results.
for item in items:
st.write(f"{item['name']} has a :{item['pet']}:")`

See `st.cache_data` above? Without it, Streamlit would run the query every time the app reruns (e.g. on a widget interaction). With `st.cache_data`, it only runs when the query changes or after 10 minutes (that's what `ttl` is for). Watch out: If your database updates more frequently, you should adapt `ttl` or remove caching so viewers always see the latest data. Learn more in [Caching](/develop/concepts/architecture/caching).

If everything worked out (and you used the example data we created above), your app should look like this:

![Finished app screenshot](/images/databases/streamlit-app.png)

[Previous: Microsoft SQL Server](/develop/tutorials/databases/mssql)[Next: MySQL](/develop/tutorials/databases/mysql)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
