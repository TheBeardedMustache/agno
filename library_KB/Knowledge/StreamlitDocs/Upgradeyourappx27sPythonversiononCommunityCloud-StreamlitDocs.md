Upgrade your app's Python version on Community Cloud - Streamlit Docs

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

      *add*
    - [Manage your app](/deploy/streamlit-community-cloud/manage-your-app)

      *remove*

      * [App analytics](/deploy/streamlit-community-cloud/manage-your-app/app-analytics)
      * [App settings](/deploy/streamlit-community-cloud/manage-your-app/app-settings)
      * [Delete your app](/deploy/streamlit-community-cloud/manage-your-app/delete-your-app)
      * [Edit your app](/deploy/streamlit-community-cloud/manage-your-app/edit-your-app)
      * [Favorite your app](/deploy/streamlit-community-cloud/manage-your-app/favorite-your-app)
      * [Reboot your app](/deploy/streamlit-community-cloud/manage-your-app/reboot-your-app)
      * [Rename your app in GitHub](/deploy/streamlit-community-cloud/manage-your-app/rename-your-app)
      * [Upgrade Python](/deploy/streamlit-community-cloud/manage-your-app/upgrade-python)
      * [Upgrade Streamlit](/deploy/streamlit-community-cloud/manage-your-app/upgrade-streamlit)
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
* [Manage your app](/deploy/streamlit-community-cloud/manage-your-app)/
* [Upgrade Python](/deploy/streamlit-community-cloud/manage-your-app/upgrade-python)

Upgrade your app's Python version on Community Cloud
====================================================

Dependencies within Python can be upgraded in place by simply changing your environment configuration file (typically `requirements.txt`). However, Python itself can't be changed after deployment.

When you deploy an app, you can select the version of Python through the "**Advanced settings**" dialog. After you have deployed an app, you must delete it and redeploy it to change the version of Python it uses.

1. Take note of your app's settings:

   * Current, custom subdomain.
   * GitHub coordinates (repository, branch, and entrypoint file path).
   * Secrets.

   When you delete an app, its custom subdomain is immediately available for reuse.
2. [Delete your app](/deploy/streamlit-community-cloud/manage-your-app/delete-your-app).
3. [Deploy your app](/deploy/streamlit-community-cloud/deploy-your-app).

   1. On the deployment page, select your app's GitHub coordinates.
   2. Set your custom domain to match your deleted instance.
   3. Click "**Advanced settings**."
   4. Choose your desired version of Python.
   5. Optional: If your app had secrets, re-enter them.
   6. Click "**Save**."
   7. Click "**Deploy**."

In a few minutes, Community Cloud will redirect you to your redployed app.

[Previous: Rename your app in GitHub](/deploy/streamlit-community-cloud/manage-your-app/rename-your-app)[Next: Upgrade Streamlit](/deploy/streamlit-community-cloud/manage-your-app/upgrade-streamlit)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
