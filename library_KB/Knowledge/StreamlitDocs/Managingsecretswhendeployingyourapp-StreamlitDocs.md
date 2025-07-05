Managing secrets when deploying your app - Streamlit Docs

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

    *remove*

    - [Dependencies](/deploy/concepts/dependencies)
    - [Secrets](/deploy/concepts/secrets)
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
* [Deploy](/deploy)/
* [Concepts](/deploy/concepts)/
* [Secrets](/deploy/concepts/secrets)

Managing secrets when deploying your app
========================================

If you are connecting to data sources or external services, you will likely be handling secret information like credentials or keys. Secret information should be stored and transmitted in a secure manner. When you deploy your app, ensure that you understand your platform's features and mechanisms for handling secrets so you can follow best practice.

Avoid saving secrets directly in your code and keep `.gitignore` updated to prevent accidentally committing a local secret to your repository. For helpful reminders, see [Security reminders](/develop/concepts/connections/security-reminders).

If you are using Streamlit Community Cloud, [Secrets management](/deploy/streamlit-community-cloud/deploy-your-app/secrets-management) allows you save environment variables and store secrets outside of your code. If you are using another platform designed for Streamlit, check if they have a built-in mechanism for working with secrets. In some cases, they may even support `st.secrets` or securely uploading your `secrets.toml` file.

For information about using `st.connection` with environment variables, see [Global secrets, managing multiple apps and multiple data stores](/develop/concepts/connections/connecting-to-data#global-secrets-managing-multiple-apps-and-multiple-data-stores).

[Previous: Dependencies](/deploy/concepts/dependencies)[Next: Streamlit Community Cloud](/deploy/streamlit-community-cloud)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
