Upgrade your app's Streamlit version on Streamlit Community Cloud - Streamlit Docs

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
* [Upgrade Streamlit](/deploy/streamlit-community-cloud/manage-your-app/upgrade-streamlit)

Upgrade your app's Streamlit version on Streamlit Community Cloud
=================================================================

Want to use a cool new Streamlit feature but your app on Streamlit Community Cloud is running an old version of the Streamlit library? If that's you, don't worry! Here's how to upgrade your app's Streamlit version, based on how you manage your [app dependencies](/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies):

No dependency file
------------------

When there is no dependencies file in your repository, your app will use the lastest Streamlit version that existed when it was last rebooted. In this case, simply [reboot your app](/deploy/streamlit-community-cloud/manage-your-app/reboot-your-app) and Community Cloud will install the latest version.

You may want to avoid getting into this situation if your app depends on a specific version of Streamlit. That is why we encourage you to use a dependency file and pin your desired version of Streamlit.

With a dependency file
----------------------

When your app includes a dependency file, reboot your app or change your dependency file as follows:

* If Streamlit is not included in your dependency file, reboot the app as described above.

  Note that we don't recommend having an incomplete dependency file since `pip` won't be able to include `streamlit` when resolving compatible versions of your dependencies.
* If Streamlit is included in your dependency file, but the version is not pinned or capped, reboot the app as described above.

  When Community Cloud reboots your app, it will re-resolve your dependency file. Your app will then have the latest version of all dependencies that are consistent with your dependency file.
* If Streamlit is included in your dependency file, and the version is pinned (e.g., `streamlit==1.37.0`), update your dependency file.

  When you commit a change to your dependency file in your repository, Community Cloud will detect the change and automatically resolve the new dependencies. This is how you add, remove, or change all Python dependencies in general. You don't need to manually reboot your app, but you can if you want to.

[Previous: Upgrade Python](/deploy/streamlit-community-cloud/manage-your-app/upgrade-python)[Next: Share your app](/deploy/streamlit-community-cloud/share-your-app)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
