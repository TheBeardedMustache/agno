Connect Streamlit to AWS S3 - Streamlit Docs

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
* [AWS S3](/develop/tutorials/databases/aws-s3)

Connect Streamlit to AWS S3
===========================

Introduction
------------

This guide explains how to securely access files on AWS S3 from Streamlit Community Cloud. It uses [Streamlit FilesConnection](https://github.com/streamlit/files-connection), the [s3fs](https://github.com/dask/s3fs) library and optionally Streamlit's [Secrets management](/develop/concepts/connections/secrets-management).

Create an S3 bucket and add a file
----------------------------------

*push\_pin*

#### Note

If you already have a bucket that you want to use, feel free
to [skip to the next step](/develop/tutorials/databases/aws-s3#create-access-keys).

First, [sign up for AWS](https://aws.amazon.com/) or log in. Go to the [S3 console](https://s3.console.aws.amazon.com/s3/home) and create a new bucket:

![AWS screenshot 1](/images/databases/aws-1.png)

![AWS screenshot 2](/images/databases/aws-2.png)

Navigate to the upload section of your new bucket:

![AWS screenshot 3](/images/databases/aws-3.png)

![AWS screenshot 4](/images/databases/aws-4.png)

And note down the "AWS Region" for later. In this example, it's `us-east-1`, but it may differ for you.

Next, upload the following CSV file, which contains some example data:

[myfile.csv](/images/databases/myfile.csv)


Create access keys
------------------

Go to the [AWS console](https://console.aws.amazon.com/), create access keys as shown below and copy the "Access Key ID" and "Secret Access Key":

![AWS screenshot 5](/images/databases/aws-5.png)

![AWS screenshot 6](/images/databases/aws-6.png)

*star*

#### Tip

Access keys created as a root user have wide-ranging permissions. In order to make your AWS account
more secure, you should consider creating an IAM account with restricted permissions and using its
access keys. More information [here](https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html).

Set up your AWS credentials locally
-----------------------------------

Streamlit FilesConnection and s3fs will read and use your existing [AWS credentials and configuration](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html) if available - such as from an `~/.aws/credentials` file or environment variables.

If you don't already have this set up, or plan to host the app on Streamlit Community Cloud, you should specify the credentials from a file `.streamlit/secrets.toml` in your app's root directory or your home directory. Create this file if it doesn't exist yet and add to it the access key ID, access key secret, and the AWS default region you noted down earlier, as shown below:

`# .streamlit/secrets.toml
AWS_ACCESS_KEY_ID = "xxx"
AWS_SECRET_ACCESS_KEY = "xxx"
AWS_DEFAULT_REGION = "xxx"`

*priority\_high*

#### Important

Be sure to replace `xxx` above with the values you noted down earlier, and add this file to `.gitignore` so you don't commit it to your GitHub repo!

Copy your app secrets to the cloud
----------------------------------

To host your app on Streamlit Community Cloud, you will need to pass your credentials to your deployed app via secrets. Go to the [app dashboard](https://share.streamlit.io/) and in the app's dropdown menu, click on **Edit Secrets**. Copy the content of `secrets.toml` above into the text area. More information is available at [Secrets management](/deploy/streamlit-community-cloud/deploy-your-app/secrets-management).

![Secrets manager screenshot](/images/databases/edit-secrets.png)

Add FilesConnection and s3fs to your requirements file
------------------------------------------------------

Add the [FilesConnection](https://github.com/streamlit/files-connection) and [s3fs](https://github.com/dask/s3fs) packages to your `requirements.txt` file, preferably pinning the versions (replace `x.x.x` with the version you want installed):

`# requirements.txt
s3fs==x.x.x
st-files-connection`

Write your Streamlit app
------------------------

Copy the code below to your Streamlit app and run it. Make sure to adapt the name of your bucket and file. Note that Streamlit automatically turns the access keys from your secrets file into environment variables, where `s3fs` searches for them by default.

`# streamlit_app.py
import streamlit as st
from st_files_connection import FilesConnection
# Create connection object and retrieve file contents.
# Specify input format is a csv and to cache the result for 600 seconds.
conn = st.connection('s3', type=FilesConnection)
df = conn.read("testbucket-jrieke/myfile.csv", input_format="csv", ttl=600)
# Print results.
for row in df.itertuples():
st.write(f"{row.Owner} has a :{row.Pet}:")`

See `st.connection` above? This handles secrets retrieval, setup, result caching and retries. By default, `read()` results are cached without expiring. In this case, we set `ttl=600` to ensure the file contents is cached for no longer than 10 minutes. You can also set `ttl=0` to disable caching. Learn more in [Caching](/develop/concepts/architecture/caching).

If everything worked out (and you used the example file given above), your app should look like this:

![Finished app screenshot](/images/databases/streamlit-app.png)

[Previous: Connect to data sources](/develop/tutorials/databases)[Next: BigQuery](/develop/tutorials/databases/bigquery)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
