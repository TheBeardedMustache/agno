Connect Streamlit to Google BigQuery - Streamlit Docs

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
* [BigQuery](/develop/tutorials/databases/bigquery)

Connect Streamlit to Google BigQuery
====================================

Introduction
------------

This guide explains how to securely access a BigQuery database from Streamlit Community Cloud. It uses the
[google-cloud-bigquery](https://googleapis.dev/python/bigquery/latest/index.html) library and
Streamlit's [Secrets management](/develop/concepts/connections/secrets-management).

Create a BigQuery database
--------------------------

*push\_pin*

#### Note

If you already have a database that you want to use, feel free
to [skip to the next step](/develop/tutorials/databases/bigquery#enable-the-bigquery-api).

For this example, we will use one of the [sample datasets](https://cloud.google.com/bigquery/public-data#sample_tables) from BigQuery (namely the `shakespeare` table). If you want to create a new dataset instead, follow [Google's quickstart guide](https://cloud.google.com/bigquery/docs/quickstarts/quickstart-web-ui).

Enable the BigQuery API
-----------------------

Programmatic access to BigQuery is controlled through [Google Cloud Platform](https://cloud.google.com). Create an account or sign in and head over to the [APIs & Services dashboard](https://console.cloud.google.com/apis/dashboard) (select or create a project if asked). As shown below, search for the BigQuery API and enable it:

![Bigquery screenshot 1](/images/databases/big-query-1.png)

![Bigquery screenshot 2](/images/databases/big-query-2.png)

![Bigquery screenshot 3](/images/databases/big-query-3.png)

Create a service account & key file
-----------------------------------

To use the BigQuery API from Streamlit Community Cloud, you need a Google Cloud Platform service account (a special account type for programmatic data access). Go to the [Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts) page and create an account with the **Viewer** permission (this will let the account access data but not change it):

![Bigquery screenshot 4](/images/databases/big-query-4.png)

![Bigquery screenshot 5](/images/databases/big-query-5.png)

![Bigquery screenshot 6](/images/databases/big-query-6.png)

*push\_pin*

#### Note

If the button **CREATE SERVICE ACCOUNT** is gray, you don't have the correct permissions. Ask the
admin of your Google Cloud project for help.

After clicking **DONE**, you should be back on the service accounts overview. Create a JSON key file for the new account and download it:

![Bigquery screenshot 7](/images/databases/big-query-7.png)

![Bigquery screenshot 8](/images/databases/big-query-8.png)

![Bigquery screenshot 9](/images/databases/big-query-9.png)

Add the key file to your local app secrets
------------------------------------------

Your local Streamlit app will read secrets from a file `.streamlit/secrets.toml` in your app's root
directory. Create this file if it doesn't exist yet and add the content of the key file you just
downloaded to it as shown below:

`# .streamlit/secrets.toml
[gcp_service_account]
type = "service_account"
project_id = "xxx"
private_key_id = "xxx"
private_key = "xxx"
client_email = "xxx"
client_id = "xxx"
auth_uri = "https://accounts.google.com/o/oauth2/auth"
token_uri = "https://oauth2.googleapis.com/token"
auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
client_x509_cert_url = "xxx"`

*priority\_high*

#### Important

Add this file to `.gitignore` and don't commit it to your GitHub repo!

Copy your app secrets to the cloud
----------------------------------

As the `secrets.toml` file above is not committed to GitHub, you need to pass its content to your deployed app (on Streamlit Community Cloud) separately. Go to the [app dashboard](https://share.streamlit.io/) and in the app's dropdown menu, click on **Edit Secrets**. Copy the content of `secrets.toml` into the text area. More information is available at [Secrets management](/deploy/streamlit-community-cloud/deploy-your-app/secrets-management).

![Secrets manager screenshot](/images/databases/edit-secrets.png)

Add google-cloud-bigquery to your requirements file
---------------------------------------------------

Add the [google-cloud-bigquery](https://googleapis.dev/python/bigquery/latest/index.html) package to your `requirements.txt` file, preferably pinning its version (replace `x.x.x` with the version want installed):

`# requirements.txt
google-cloud-bigquery==x.x.x`

Write your Streamlit app
------------------------

Copy the code below to your Streamlit app and run it. Make sure to adapt the query if you don't use the sample table.

`# streamlit_app.py
import streamlit as st
from google.oauth2 import service_account
from google.cloud import bigquery
# Create API client.
credentials = service_account.Credentials.from_service_account_info(
st.secrets["gcp_service_account"]
)
client = bigquery.Client(credentials=credentials)
# Perform query.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def run_query(query):
query_job = client.query(query)
rows_raw = query_job.result()
# Convert to list of dicts. Required for st.cache_data to hash the return value.
rows = [dict(row) for row in rows_raw]
return rows
rows = run_query("SELECT word FROM `bigquery-public-data.samples.shakespeare` LIMIT 10")
# Print results.
st.write("Some wise words from Shakespeare:")
for row in rows:
st.write("✍️ " + row['word'])`

See `st.cache_data` above? Without it, Streamlit would run the query every time the app reruns (e.g. on a widget interaction). With `st.cache_data`, it only runs when the query changes or after 10 minutes (that's what `ttl` is for). Watch out: If your database updates more frequently, you should adapt `ttl` or remove caching so viewers always see the latest data. Learn more in [Caching](/develop/concepts/architecture/caching).

Alternatively, you can use pandas to read from BigQuery right into a dataframe! Follow all the above steps, install the [pandas-gbq](https://pandas-gbq.readthedocs.io/en/latest/index.html) library (don't forget to add it to `requirements.txt`!), and call `pandas.read_gbq(query, credentials=credentials)`. More info [in the pandas docs](https://pandas.pydata.org/docs/reference/api/pandas.read_gbq.html).

If everything worked out (and you used the sample table), your app should look like this:

![Final app screenshot](/images/databases/big-query-10.png)

[Previous: AWS S3](/develop/tutorials/databases/aws-s3)[Next: Firestore](https://blog.streamlit.io/streamlit-firestore/)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
