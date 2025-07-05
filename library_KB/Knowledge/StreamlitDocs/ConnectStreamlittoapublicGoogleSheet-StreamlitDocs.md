Connect Streamlit to a public Google Sheet - Streamlit Docs

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
* [Public Google Sheet](/develop/tutorials/databases/public-gsheet)

Connect Streamlit to a public Google Sheet
==========================================

Introduction
------------

This guide explains how to securely access a public Google Sheet from Streamlit. It uses [st.connection](/develop/api-reference/connections/st.connection), [Streamlit GSheetsConnection](https://github.com/streamlit/gsheets-connection), and Streamlit's [Secrets management](/develop/concepts/connections/secrets-management).

This method requires you to enable link sharing for your Google Sheet. While the sharing link will not appear in your code (and actually acts as sort of a password!), someone with the link can get all the data in the Sheet. If you don't want this, follow the (more complicated) guide to [Connect Streamlit to a private Google Sheet](/private-gsheet).

### Prerequisites

This tutorial requires `streamlit>=1.28` and `st-gsheets-connection` in your Python environment.

Create a Google Sheet and turn on link sharing
----------------------------------------------

If you already have a Sheet that you want to access, you can [skip to the next step](/develop/tutorials/databases/public-gsheet#add-the-sheets-url-to-your-local-app-secrets). See Google's documentation on how to [share spreadsheets](https://support.google.com/docs/answer/9331169?hl=en#6.1) for more information.

Create a spreadsheet with this example data and create a share link. The link should have "Anyone with the link" set as a "Viewer."

| name | pet |
| --- | --- |
| Mary | dog |
| John | cat |
| Robert | bird |

![screenshot 1](/images/databases/public-gsheet-1.png)

![screenshot 1](/images/databases/public-gsheet-2.png)

Add the Sheets URL to your local app secrets
--------------------------------------------

Your local Streamlit app will read secrets from a file `.streamlit/secrets.toml` in your app's root directory. Create this file if it doesn't exist yet and add the share link of your Google Sheet to it as shown below:

`# .streamlit/secrets.toml
[connections.gsheets]
spreadsheet = "https://docs.google.com/spreadsheets/d/xxxxxxx/edit#gid=0"`

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

[Previous: Private Google Sheet](/develop/tutorials/databases/private-gsheet)[Next: Snowflake](/develop/tutorials/databases/snowflake)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
