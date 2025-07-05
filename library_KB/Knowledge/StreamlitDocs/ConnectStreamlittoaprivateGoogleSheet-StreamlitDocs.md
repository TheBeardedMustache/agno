Connect Streamlit to a private Google Sheet - Streamlit Docs

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
* [Private Google Sheet](/develop/tutorials/databases/private-gsheet)

Connect Streamlit to a private Google Sheet
===========================================

Introduction
------------

This guide explains how to securely access a private Google Sheet from Streamlit Community Cloud. It uses [st.connection](/develop/api-reference/connections/st.connection), [Streamlit GSheetsConnection](https://github.com/streamlit/gsheets-connection), and Streamlit's [Secrets management](/develop/concepts/connections/secrets-management).

If you are fine with enabling link sharing for your Google Sheet (i.e. everyone with the link can view it), the guide [Connect Streamlit to a public Google Sheet](/develop/tutorials/databases/public-gsheet) shows a simpler method of doing this. If your Sheet contains sensitive information and you cannot enable link sharing, keep on reading.

### Prerequisites

This tutorial requires `streamlit>=1.28` and `st-gsheets-connection` in your Python environment.

Create a Google Sheet
---------------------

If you already have a Sheet that you want to use, you can [skip to the next step](/develop/tutorials/databases/private-gsheet#enable-the-sheets-api).

Create a spreadsheet with this example data.

| name | pet |
| --- | --- |
| Mary | dog |
| John | cat |
| Robert | bird |

![Google sheet screenshot](/images/databases/private-gsheet-1.png)

Enable the Sheets API
---------------------

Programmatic access to Google Sheets is controlled through [Google Cloud Platform](https://cloud.google.com/). Create an account or sign in and head over to the [**APIs & Services** dashboard](https://console.cloud.google.com/apis/dashboard) (select or create a project if asked). As shown below, search for the Sheets API and enable it:

![GCP screenshot 1](/images/databases/private-gsheet-2.png)

![GCP screenshot 2](/images/databases/private-gsheet-3.png)

![GCP screenshot 3](/images/databases/private-gsheet-4.png)

Create a service account & key file
-----------------------------------

To use the Sheets API from Streamlit Community Cloud, you need a Google Cloud Platform service account (a special account type for programmatic data access). Go to the [**Service Accounts** page](https://console.cloud.google.com/iam-admin/serviceaccounts) and create an account with the **Viewer** permission (this will let the account access data but not change it):

![GCP screenshot 5](/images/databases/private-gsheet-5.png)

![GCP screenshot 6](/images/databases/private-gsheet-6.png)

![GCP screenshot 7](/images/databases/private-gsheet-7.png)

*push\_pin*

#### Note

The button "**CREATE SERVICE ACCOUNT**" is gray, you don't have the correct permissions. Ask the admin of your Google Cloud project for help.

After clicking "**DONE**", you should be back on the service accounts overview. First, note down the email address of the account you just created (**important for next step!**). Then, create a JSON key file for the new account and download it:

![GCP screenshot 8](/images/databases/private-gsheet-8.png)

![GCP screenshot 9](/images/databases/private-gsheet-9.png)

![GCP screenshot 10](/images/databases/private-gsheet-10.png)

Share the Google Sheet with the service account
-----------------------------------------------

By default, the service account you just created cannot access your Google Sheet. To give it access, click on the "**Share**" button in the Google Sheet, add the email of the service account (noted down in step 2), and choose the correct permission (if you just want to read the data, "**Viewer**" is enough):

![GCP screenshot 11](/images/databases/private-gsheet-11.png)

![GCP screenshot 12](/images/databases/private-gsheet-12.png)

Add the key file to your local app secrets
------------------------------------------

Your local Streamlit app will read secrets from a file `.streamlit/secrets.toml` in your app's root directory. Create this file if it doesn't exist yet and add the URL of your Google Sheet plus the content of the key file you downloaded to it as shown below:

`# .streamlit/secrets.toml
[connections.gsheets]
spreadsheet = "https://docs.google.com/spreadsheets/d/xxxxxxx/edit#gid=0"
# From your JSON key file
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

Write your Streamlit app
------------------------

Copy the code below to your Streamlit app and run it.

`# streamlit_app.py
import streamlit as st
from streamlit_gsheets import GSheetsConnection
# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)
df = conn.read()
# Print results.
for row in df.itertuples():
st.write(f"{row.name} has a :{row.pet}:")`

See `st.connection` above? This handles secrets retrieval, setup, query caching and retries. By default, `.read()` results are cached without expiring. You can pass optional parameters to `.read()` to customize your connection. For example, you can specify the name of a worksheet, cache expiration time, or pass-through parameters for [`pandas.read_csv`](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html) like this:

`df = conn.read(
worksheet="Sheet1",
ttl="10m",
usecols=[0, 1],
nrows=3,
)`

In this case, we set `ttl="10m"` to ensure the query result is cached for no longer than 10 minutes. You can also set `ttl=0` to disable caching. Learn more in [Caching](/develop/concepts/architecture/caching). We've declared optional parameters `usecols=[0,1]` and `nrows=3` for `pandas` to use under the hood.

If everything worked out (and you used the example table we created above), your app should look like this:

![Finished app screenshot](/images/databases/streamlit-app.png)

Connecting to a Google Sheet from Community Cloud
-------------------------------------------------

This tutorial assumes a local Streamlit app, however you can also connect to Google Sheets from apps hosted in Community Cloud. The main additional steps are:

* [Include information about dependencies](/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies) using a `requirements.txt` file with `st-gsheets-connection` and any other dependencies.
* [Add your secrets](/deploy/streamlit-community-cloud/deploy-your-app/secrets-management) to your Community Cloud app.

[Previous: PostgreSQL](/develop/tutorials/databases/postgresql)[Next: Public Google Sheet](/develop/tutorials/databases/public-gsheet)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
