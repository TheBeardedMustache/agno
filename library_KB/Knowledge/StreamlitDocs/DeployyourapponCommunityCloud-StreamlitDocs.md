Deploy your app on Community Cloud - Streamlit Docs

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
* [Deploy!](/deploy/streamlit-community-cloud/deploy-your-app/deploy)

Deploy your app on Community Cloud
==================================

After you've [organized your files](/deploy/streamlit-community-cloud/deploy-your-app/file-organization) and [added your dependencies](/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies) as described on the previous pages, you're ready to deploy your app to Community Cloud!

Select your repository and entrypoint file
------------------------------------------

1. From your workspace at [share.streamlit.io](https://share.streamlit.io), in the upper-right corner, click "**Create app**."

   ![Deploy a new app from your workspace](/images/streamlit-community-cloud/deploy-empty-new-app.png)
2. When asked "Do you already have an app?" click "**Yup, I have an app**."
3. Fill in your repository, branch, and file path. Alternatively, to paste a link directly to `your_app.py` on GitHub, click "**Paste GitHub URL**."
4. Optional: In the "App URL" field, choose a subdomain for your new app.

   Every Community Cloud app is deployed to a subdomain on `streamlit.app`, but you can change your app's subdomain at any time. For more information, see [App settings](/deploy/streamlit-community-cloud/manage-your-app/app-settings). In the following example, Community Cloud will deploy an app to `https://red-balloon.streamlit.app/`.

   ![Fill in your app's information to deploy your app](/images/streamlit-community-cloud/deploy-an-app.png)

   Although Community Cloud attempts to suggest available repositories and files, these suggestions are not always complete. If the desired information is not listed for any field, enter it manually.

Optional: Configure secrets and Python version
----------------------------------------------

*push\_pin*

#### Note

Streamlit Community Cloud supports all released [versions of Python that are still receiving security updates](https://devguide.python.org/versions/). Streamlit Community Cloud defaults to version 3.12. You can select a version of your choice from the "Python version" dropdown in the "Advanced settings" modal. If an app is running a version of Python that becomes unsupported, it will be forcibly upgraded to the oldest supported version of Python and may break.

1. Click "**Advanced settings**."
2. Select your desired version of Python.
3. To define environment variables and secrets, in the "Secrets" field, paste the contents of your `secrets.toml` file.

   For more information, see [Community Cloud secrets management](/deploy/streamlit-community-cloud/deploy-your-app/secrets-management).
4. Click "**Save**."

![Advanced settings for deploying your app](/images/streamlit-community-cloud/deploy-an-app-advanced.png)

Watch your app launch
---------------------

Your app is now being deployed, and you can watch while it launches. Most apps are deployed within a few minutes, but if your app has a lot of dependencies, it may take longer. After the initial deployment, changes to your code should be reflected immediately in your app. Changes to your dependencies will be processed immediately, but may take a few minutes to install.

![Watch your app launch](/images/streamlit-community-cloud/deploy-an-app-provisioning.png)

*push\_pin*

#### Note

The Streamlit Community Cloud logs on the right-hand side of your app are only viewable to users with write access to your repository. These logs help you debug any issues with the app. Learn more about [Streamlit Community Cloud logs](/deploy/streamlit-community-cloud/manage-your-app#cloud-logs).



View your app
-------------

That's it—you're done! Your app now has a unique URL that you can share with others. Read more about how to [Share your app](/deploy/streamlit-community-cloud/share-your-app) with viewers.

### Unique subdomains

If the "**Custom subdomain (optional)**" field is blank when you deploy your app, a URL is assigned following a structure based on your GitHub repo. The subdomain of the URL is a dash-separated list of the following:

* Repository owner (GitHub user or organization)
* Repository name
* Entrypoint file path
* Branch name, if other than `main` or `master`
* A random hash

`https://[GitHub username or organization]-[repo name]-[app path]-[branch name]-[short hash].streamlit.app`

For example, the following app is deployed from the `streamlit` organization. The repo is `demo-self-driving` and the app name is `streamlit_app.py` in the root directory. The branch name is `master` and therefore not included.

`https://streamlit-demo-self-driving-streamlit-app-8jya0g.streamlit.app`

### Custom subdomains

Setting a custom subdomain makes it much easier to share your app because you can choose something memorable. To learn how to change the subdomain of a deployed app, see [View or change your app's URL](/deploy/streamlit-community-cloud/manage-your-app/app-settings#view-or-change-your-apps-url).

[Previous: Secrets management](/deploy/streamlit-community-cloud/deploy-your-app/secrets-management)[Next: Manage your app](/deploy/streamlit-community-cloud/manage-your-app)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
