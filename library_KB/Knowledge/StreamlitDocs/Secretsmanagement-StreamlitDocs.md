﻿Secrets management - Streamlit Docs

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

    *remove*

    - CORE

      ---
    - [Architecture and execution](/develop/concepts/architecture)

      *add*
    - [Multipage apps](/develop/concepts/multipage-apps)

      *add*
    - [App design](/develop/concepts/design)

      *add*
    - ADDITIONAL

      ---
    - [Connections, secrets, and authentication](/develop/concepts/connections)

      *remove*

      * [Connecting to data](/develop/concepts/connections/connecting-to-data)
      * [Secrets management](/develop/concepts/connections/secrets-management)
      * [User authentication](/develop/concepts/connections/authentication)
      * [Security reminders](/develop/concepts/connections/security-reminders)
    - [Custom components](/develop/concepts/custom-components)

      *add*
    - [Configuration and theming](/develop/concepts/configuration)

      *add*
    - [App testing](/develop/concepts/app-testing)

      *add*
  + [API reference](/develop/api-reference)

    *add*
  + [Tutorials](/develop/tutorials)

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
* [Concepts](/develop/concepts)/
* [Connections, secrets, and authentication](/develop/concepts/connections)/
* [Secrets management](/develop/concepts/connections/secrets-management)

Secrets management
==================

Storing unencrypted secrets in a git repository is a bad practice. For applications that require access to sensitive credentials, the recommended solution is to store those credentials outside the repository - such as using a credentials file not committed to the repository or passing them as environment variables.

Streamlit provides native file-based secrets management to easily store and securely access your secrets in your Streamlit app.

*push\_pin*

#### Note

Existing secrets management tools, such as [dotenv files](https://pypi.org/project/python-dotenv/), [AWS credentials files](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html#configuring-credentials), [Google Cloud Secret Manager](https://pypi.org/project/google-cloud-secret-manager/), or [Hashicorp Vault](https://www.vaultproject.io/use-cases/secrets-management), will work fine in Streamlit. We just add native secrets management for times when it's useful.

How to use secrets management
-----------------------------

### Develop locally and set up secrets

Streamlit provides two ways to set up secrets locally using [TOML](https://toml.io/en/latest) format:

1. In a **global secrets file** at `~/.streamlit/secrets.toml` for macOS/Linux or `%userprofile%/.streamlit/secrets.toml` for Windows:

   `# Everything in this section will be available as an environment variable
   db_username = "Jane"
   db_password = "mypassword"
   # You can also add other sections if you like.
   # The contents of sections as shown below will not become environment variables,
   # but they'll be easily accessible from within Streamlit anyway as we show
   # later in this doc.
   [my_other_secrets]
   things_i_like = ["Streamlit", "Python"]`

   If you use the global secrets file, you don't have to duplicate secrets across several project-level files if multiple Streamlit apps share the same secrets.
2. In a **per-project secrets file** at `$CWD/.streamlit/secrets.toml`, where `$CWD` is the folder you're running Streamlit from. If both a global secrets file and a per-project secrets file exist, *secrets in the per-project file overwrite those defined in the global file*.

*priority\_high*

#### Important

Add this file to your `.gitignore` so you don't commit your secrets!

### Use secrets in your app

Access your secrets by querying the `st.secrets` dict, or as environment variables. For example, if you enter the secrets from the section above, the code below shows you how to access them within your Streamlit app.

`import streamlit as st
# Everything is accessible via the st.secrets dict:
st.write("DB username:", st.secrets["db_username"])
st.write("DB password:", st.secrets["db_password"])
# And the root-level secrets are also accessible as environment variables:
import os
st.write(
"Has environment variables been set:",
os.environ["db_username"] == st.secrets["db_username"],
)`

*star*

#### Tip

You can access `st.secrets` via attribute notation (e.g. `st.secrets.key`), in addition to key notation (e.g. `st.secrets["key"]`) — like [st.session\_state](/develop/api-reference/caching-and-state/st.session_state).

You can even compactly use TOML sections to pass multiple secrets as a single attribute. Consider the following secrets:

`[db_credentials]
username = "my_username"
password = "my_password"`

Rather than passing each secret as attributes in a function, you can more compactly pass the section to achieve the same result. See the notional code below, which uses the secrets above:

`# Verbose version
my_db.connect(username=st.secrets.db_credentials.username, password=st.secrets.db_credentials.password)
# Far more compact version!
my_db.connect(**st.secrets.db_credentials)`

### Error handling

Here are some common errors you might encounter when using secrets management.

* If a `.streamlit/secrets.toml` is created *while* the app is running, the server needs to be restarted for changes to be reflected in the app.
* If you try accessing a secret, but no `secrets.toml` file exists, Streamlit will raise a `FileNotFoundError` exception:

  ![Secrets management FileNotFoundError](/images/secrets-filenotfounderror.png)
* If you try accessing a secret that doesn't exist, Streamlit will raise a `KeyError` exception:

  `import streamlit as st
  st.write(st.secrets["nonexistent_key"])`

  ![Secrets management KeyError](/images/secrets-keyerror.png)

### Use secrets on Streamlit Community Cloud

When you deploy your app to [Streamlit Community Cloud](https://streamlit.io/cloud), you can use the same secrets management workflow as you would locally. However, you'll need to also set up your secrets in the Community Cloud Secrets Management console. Learn how to do so via the Cloud-specific [Secrets management](/deploy/streamlit-community-cloud/deploy-your-app/secrets-management) documentation.

[Previous: Connecting to data](/develop/concepts/connections/connecting-to-data)[Next: User authentication](/develop/concepts/connections/authentication)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
