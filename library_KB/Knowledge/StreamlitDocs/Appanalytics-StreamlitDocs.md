App analytics - Streamlit Docs

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
* [App analytics](/deploy/streamlit-community-cloud/manage-your-app/app-analytics)

App analytics
=============

Streamlit Community Cloud allows you to see the viewership of each of your apps. Specifically, you can see:

* The total viewers count of your app (counted from April 2022).
* The most recent unique viewers (capped at the last 20 viewers).
* A relative timestamp of each unique viewer's last visit.

![App analytics on Streamlit Community Cloud](/images/streamlit-community-cloud/workspace-app-analytics-viewers.png)

Access your app analytics
-------------------------

You can get to your app's analytics:

* [From your workspace](/deploy/streamlit-community-cloud/manage-your-app/app-analytics#access-app-analytics-from-your-workspace).
* [From your Cloud logs](/deploy/streamlit-community-cloud/manage-your-app/app-analytics#access-app-analytics-from-your-cloud-logs).

### Access app analytics from your workspace

From your workspace at [share.streamlit.io](https://share.streamlit.io), click the overflow icon (*more\_vert*) next to your app. Click "**Analytics**."

![Access app analytics from your workspace through your app overflow menu](/images/streamlit-community-cloud/workspace-app-analytics.png)

### Access app analytics from your Cloud logs

From your app at `<your-custom-subdomain>.streamlit.app`, click "**Manage app**" in the lower-right corner.

![Access Streamlit Community Cloud logs from your app](/images/streamlit-community-cloud/cloud-logs-open.png)

Click the overflow menu icon (*more\_vert*) and click "**Analytics**."

![Access app analytics from your Cloud logs](/images/streamlit-community-cloud/cloud-logs-menu-analytics.png)

App viewers
-----------

For public apps, we anonymize all viewers outside your workspace to protect their privacy and display anonymous viewers as random pseudonyms. You'll still be able to see the identities of fellow members in your workspace, including any viewers you've invited (once they've accepted).

*priority\_high*

#### Important

When you invite a viewer to an app, they gain access to analytics as well. Additionally, if someone is invited as a viewer to *any* app in your workspace, they can see analytics for all public apps in your workspace and invite additional viewers themselves. A viewer in your workspace may see the emails of developers and other viewers in your workspace through analytics.

Meanwhile, for private apps where you control who has access, you will be able to see the specific users who recently viewed your apps.

Additionally, you may occasionally see anonymous users in a private app. Rest assured, these anonymous users *do* have authorized view access granted by you or your workspace members.

Common reasons why users show up anonymously are:

* The app was previously public.
* The given viewer viewed the app in April 2022, when the Streamlit team was honing user identification for this feature.

See Streamlit's general [Privacy Notice](https://streamlit.io/privacy-policy).

[Previous: Manage your app](/deploy/streamlit-community-cloud/manage-your-app)[Next: App settings](/deploy/streamlit-community-cloud/manage-your-app/app-settings)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
