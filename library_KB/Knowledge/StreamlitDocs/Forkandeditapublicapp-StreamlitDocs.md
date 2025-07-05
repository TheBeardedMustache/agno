Fork and edit a public app - Streamlit Docs

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

      *remove*

      * [Quickstart](/deploy/streamlit-community-cloud/get-started/quickstart)
      * [Create your account](/deploy/streamlit-community-cloud/get-started/create-your-account)
      * [Connect your GitHub account](/deploy/streamlit-community-cloud/get-started/connect-your-github-account)
      * [Explore your workspace](/deploy/streamlit-community-cloud/get-started/explore-your-workspace)
      * [Deploy from a template](/deploy/streamlit-community-cloud/get-started/deploy-from-a-template)
      * [Fork and edit a public app](/deploy/streamlit-community-cloud/get-started/fork-and-edit-a-public-app)
      * [Trust and security](/deploy/streamlit-community-cloud/get-started/trust-and-security)
    - [Deploy your app](/deploy/streamlit-community-cloud/deploy-your-app)

      *add*
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
* [Get started](/deploy/streamlit-community-cloud/get-started)/
* [Fork and edit a public app](/deploy/streamlit-community-cloud/get-started/fork-and-edit-a-public-app)

Fork and edit a public app
==========================

Community Cloud is all about learning, sharing, and exploring the world of Streamlit. For apps with public repositories, you can quickly fork copies to your GitHub account, deploy your own version, and jump into a codespace on GitHub to start editing and exploring Streamlit code.

1. From a forkable app, in the upper-right corner, click "**Fork**."

   ![Click Fork in the upper-right corner of a public app](/images/streamlit-community-cloud/fork-public-hello.png)
2. Optional: In the "App URL" field, choose a custom subdomain for your app.

   Every Community Cloud app is deployed to a subdomain on `streamlit.app`, but you can change your app's subdomain at any time. For more information, see [App settings](/deploy/streamlit-community-cloud/manage-your-app/app-settings).
3. Click "**Fork!**"

   The repository will be forked to your GitHub account. If you have already forked the repository, Community Cloud will use the existing fork. If your existing fork already has an associated codespace, the codespace will be reused.

   *priority\_high*

   #### Warning

   Do not use this method in the following situations:

   * You have an existing repository that matches the fork name (but isn't a fork of this app).
   * You have an existing fork of this app, but you've changed the name of the repository.

   If you have an existing fork of this app and kept the original repository name, Community Cloud will use your existing fork. If you've previously deployed the app and opened a codespace, Community Cloud will open your existing codespace.

   ![Click Fork to confirm and deploy your app](/images/streamlit-community-cloud/fork-public-hello-deploy.png)
4. Wait for GitHub to set up your codespace.

   It can take several minutes to fully initialize your codespace. After the Visual Studio Code editor appears in your codespace, it can take several minutes to install Python and start the Streamlit server. When complete, a split screen view displays a code editor on the left and a running app on the right. The code editor opens two tabs by default: the repository's readme file and the app's entrypoint file.

   ![Click Fork to confirm and deploy your app](/images/streamlit-community-cloud/fork-public-hello-codespace.png)

   *priority\_high*

   #### Important

   The app displayed in your codespace is not the same instance you deployed on Community Cloud. Your codespace is a self-contained development environment. When you make edits inside a codespace, those edits don't leave the codespace until you commit them to your repository. When you commit your changes to your repository, Community Cloud detects the changes and updates your deployed app. To learn more, see [Edit your app](/deploy/streamlit-community-cloud/manage-your-app/edit-your-app).
5. Edit your newly forked app as desired. For more instructions on working with GitHub Codespaces, see [Edit your app](/deploy/streamlit-community-cloud/manage-your-app/edit-your-app).

[Previous: Deploy from a template](/deploy/streamlit-community-cloud/get-started/deploy-from-a-template)[Next: Trust and security](/deploy/streamlit-community-cloud/get-started/trust-and-security)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
