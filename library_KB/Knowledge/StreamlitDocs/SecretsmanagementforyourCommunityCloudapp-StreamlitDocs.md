Secrets management for your Community Cloud app - Streamlit Docs

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

    *add*
  + [Quick reference](/develop/quick-reference)

    *add*
* [*web\_asset*

  Deploy](/deploy)
  + [Concepts](/deploy/concepts)

    *add*
  + [Streamlit Community Cloud](/deploy/streamlit-community-cloud)

    *remove*

    - [Get started](/deploy/streamlit-community-cloud/get-started)

      *add*
    - [Deploy your app](/deploy/streamlit-community-cloud/deploy-your-app)

      *remove*

      * [File organization](/deploy/streamlit-community-cloud/deploy-your-app/file-organization)
      * [App dependencies](/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies)
      * [Secrets management](/deploy/streamlit-community-cloud/deploy-your-app/secrets-management)
      * [Deploy!](/deploy/streamlit-community-cloud/deploy-your-app/deploy)
    - [Manage your app](/deploy/streamlit-community-cloud/manage-your-app)

      *add*
    - [Share your app](/deploy/streamlit-community-cloud/share-your-app)

      *add*
    - [Manage your account](/deploy/streamlit-community-cloud/manage-your-account)

      *add*
    - [Status and limitations](/deploy/streamlit-community-cloud/status)
  + [Snowflake](/deploy/snowflake)
  + [Other platforms](/deploy/tutorials)

    *add*
* [*school*

  Knowledge base](/knowledge-base)
  + [FAQ](/knowledge-base/using-streamlit)
  + [Installing dependencies](/knowledge-base/dependencies)
  + [Deployment issues](/knowledge-base/deploy)

* [Home](/)/
* [Deploy](/deploy)/
* [Streamlit Community Cloud](/deploy/streamlit-community-cloud)/
* [Deploy your app](/deploy/streamlit-community-cloud/deploy-your-app)/
* [Secrets management](/deploy/streamlit-community-cloud/deploy-your-app/secrets-management)

Secrets management for your Community Cloud app
===============================================

Introduction
------------

If you are [connecting to data sources](/develop/tutorials/databases), you will likely need to handle credentials or secrets. Storing unencrypted secrets in a git repository is a bad practice. If your application needs access to sensitive credentials, the recommended solution is to store those credentials in a file that is not committed to the repository and to pass them as environment variables.

How to use secrets management
-----------------------------

Community Cloud lets you save your secrets within your app's settings. When developing locally, you can use `st.secrets` in your code to read secrets from a `.streamlit/secrets.toml` file. However, this `secrets.toml` file should never be committed to your repository. Instead, when you deploy your app, you can paste the contents of your `secrets.toml` file into the "**Advanced settings**" dialog. You can update your secrets at any time through your app's settings in your workspace.

### Prerequisites

* You should understand how to use `st.secrets` and `secrets.toml`. See [Secrets management](/develop/concepts/connections/secrets-management).

### Advanced settings

While deploying your app, you can access "**Advanced settings**" to set your secrets. After your app is deployed, you can view or update your secrets through the app's settings. The deployment workflow is fully described on the next page, but the "**Advanced settings**" dialog looks like this:

![Advanced settings for deploying your app](/images/streamlit-community-cloud/deploy-an-app-advanced.png)

Simply copy and paste the contents of your local `secrets.toml` file into the "Secrets" field within the dialog. After you click "**Save**" to commit the changes, that's it!

### Edit your app's secrets

If you need to add or edit your secrets for an app that is already deployed, you can access secrets through your [App settings](/deploy/streamlit-community-cloud/manage-your-app/app-settings). See [View or update your secrets](/deploy/streamlit-community-cloud/manage-your-app/app-settings#view-or-update-your-secrets).

[Previous: App dependencies](/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies)[Next: Deploy!](/deploy/streamlit-community-cloud/deploy-your-app/deploy)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
