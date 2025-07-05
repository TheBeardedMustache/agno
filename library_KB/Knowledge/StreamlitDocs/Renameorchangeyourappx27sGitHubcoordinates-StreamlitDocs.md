Rename or change your app's GitHub coordinates - Streamlit Docs

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
* [Rename your app in GitHub](/deploy/streamlit-community-cloud/manage-your-app/rename-your-app)

Rename or change your app's GitHub coordinates
==============================================

Streamlit Community Cloud identifies apps by their GitHub coordinates (owner, repository, branch, entrypoint file path). If you move or rename one of these coordinates without preparation, you will lose access to administer any associated app.

Delete, rename, redeploy
------------------------

If you need to rename your repository, move your entrypoint file, or otherwise change a deployed app's GitHub coordinates, do the following:

1. Delete your app.
2. Make your desired changes in GitHub.
3. Redeploy your app.

Regain access when you've already made changes to your app's GitHub coordinates
-------------------------------------------------------------------------------

If you have changed a repository so that Community Cloud can no longer find your app on GitHub, your app will be missing or shown as view-only. View-only means that you can't edit, reboot, delete, or view settings for your app. You can only access analytics.

You may be able to regain control as follows:

1. Revert the change you made to your app so that Community Cloud can see the owner, repository, branch, and entrypoint file it expects.
2. Sign out of Community Cloud and GitHub.
3. Sign back in to Community Cloud and GitHub.
4. If you have regained access, delete your app. Proceed with your original change, and redeploy your app.

   If this does not restore access to your app, please [contact Snowflake support](/knowledge-base/deploy/how-to-submit-a-support-case-for-streamlit-community-cloud) for assistance. They can delete your disconnected apps so you can redeploy them. For the quickest help, please provide a complete list of your affected apps by URL.

[Previous: Reboot your app](/deploy/streamlit-community-cloud/manage-your-app/reboot-your-app)[Next: Upgrade Python](/deploy/streamlit-community-cloud/manage-your-app/upgrade-python)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
