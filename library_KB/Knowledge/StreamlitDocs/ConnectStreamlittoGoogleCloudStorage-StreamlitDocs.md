Connect Streamlit to Google Cloud Storage - Streamlit Docs

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
* [Google Cloud Storage](/develop/tutorials/databases/gcs)

Connect Streamlit to Google Cloud Storage
=========================================

Introduction
------------

This guide explains how to securely access files on Google Cloud Storage from Streamlit Community Cloud. It uses [Streamlit FilesConnection](https://github.com/streamlit/files-connection), the [gcsfs](https://github.com/fsspec/gcsfs) library and Streamlit's [Secrets management](/develop/concepts/connections/secrets-management).

Create a Google Cloud Storage bucket and add a file
---------------------------------------------------

*push\_pin*

#### Note

If you already have a bucket that you want to use, feel free
to [skip to the next step](/develop/tutorials/databases/gcs#enable-the-google-cloud-storage-api).

First, [sign up for Google Cloud Platform](https://console.cloud.google.com/) or log in. Go to the [Google Cloud Storage console](https://console.cloud.google.com/storage/) and create a new bucket.

![GCS screenshot 1](/images/databases/gcs-1.png)

![GCS screenshot 2](/images/databases/gcs-2.png)

Navigate to the upload section of your new bucket:

![GCS screenshot 3](/images/databases/gcs-3.png)

![GCS screenshot 4](/images/databases/gcs-4.png)

And upload the following CSV file, which contains some example data:

[myfile.csv](/images/databases/myfile.csv)


Enable the Google Cloud Storage API
-----------------------------------

The Google Cloud Storage API is [enabled by default](https://cloud.google.com/service-usage/docs/enabled-service#default) when you create a project through the Google Cloud Console or CLI. Feel free to [skip to the next step](/develop/tutorials/databases/gcs#create-a-service-account-and-key-file).

If you do need to enable the API for programmatic access in your project, head over to the [APIs & Services dashboard](https://console.cloud.google.com/apis/dashboard) (select or create a project if asked). Search for the Cloud Storage API and enable it. The screenshot below has a blue "Manage" button and indicates the "API is enabled" which means no further action needs to be taken. This is very likely what you have since the API is enabled by default. However, if that is not what you see and you have an "Enable" button, you'll need to enable the API:

![GCS screenshot 5](/images/databases/gcs-5.png)

![GCS screenshot 6](/images/databases/gcs-6.png)

![GCS screenshot 7](/images/databases/gcs-7.png)

Create a service account and key file
-------------------------------------

To use the Google Cloud Storage API from Streamlit, you need a Google Cloud Platform service account (a special type for programmatic data access). Go to the Service Accounts page and create an account with **Viewer** permission.

![GCS screenshot 8](/images/databases/gcs-8.png)

![GCS screenshot 9](/images/databases/gcs-9.png)

![GCS screenshot 10](/images/databases/gcs-10.png)

*push\_pin*

#### Note

If the button **CREATE SERVICE ACCOUNT** is gray, you don't have the correct permissions. Ask the
admin of your Google Cloud project for help.

After clicking **DONE**, you should be back on the service accounts overview. Create a JSON key file for the new account and download it:

![GCS screenshot 11](/images/databases/gcs-11.png)

![GCS screenshot 12](/images/databases/gcs-12.png)

![GCS screenshot 13](/images/databases/gcs-13.png)

Add the key to your local app secrets
-------------------------------------

Your local Streamlit app will read secrets from a file `.streamlit/secrets.toml` in your app's root directory. Create this file if it doesn't exist yet and add the access key to it as shown below:

`# .streamlit/secrets.toml
[connections.gcs]
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

Add FilesConnection and gcsfs to your requirements file
-------------------------------------------------------

Add the [FilesConnection](https://github.com/streamlit/files-connection) and [gcsfs](https://github.com/fsspec/gcsfs) packages to your `requirements.txt` file, preferably pinning the versions (replace `x.x.x` with the version you want installed):

`# requirements.txt
gcsfs==x.x.x
st-files-connection`

Write your Streamlit app
------------------------

Copy the code below to your Streamlit app and run it. Make sure to adapt the name of your bucket and file. Note that Streamlit automatically turns the access keys from your secrets file into environment variables.

`# streamlit_app.py
import streamlit as st
from st_files_connection import FilesConnection
# Create connection object and retrieve file contents.
# Specify input format is a csv and to cache the result for 600 seconds.
conn = st.connection('gcs', type=FilesConnection)
df = conn.read("streamlit-bucket/myfile.csv", input_format="csv", ttl=600)
# Print results.
for row in df.itertuples():
st.write(f"{row.Owner} has a :{row.Pet}:")`

See `st.connection` above? This handles secrets retrieval, setup, result caching and retries. By default, `read()` results are cached without expiring. In this case, we set `ttl=600` to ensure the file contents is cached for no longer than 10 minutes. You can also set `ttl=0` to disable caching. Learn more in [Caching](/develop/concepts/architecture/caching).

If everything worked out (and you used the example file given above), your app should look like this:

![Finished app screenshot](/images/databases/streamlit-app.png)

[Previous: Firestore](https://blog.streamlit.io/streamlit-firestore/)[Next: Microsoft SQL Server](/develop/tutorials/databases/mssql)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
