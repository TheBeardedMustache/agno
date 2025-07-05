Manage your GitHub connection - Streamlit Docs

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

      *add*
    - [Share your app](/deploy/streamlit-community-cloud/share-your-app)

      *add*
    - [Manage your account](/deploy/streamlit-community-cloud/manage-your-account)

      *remove*

      * [Sign in and sign out](/deploy/streamlit-community-cloud/manage-your-account/sign-in-sign-out)
      * [Workspace settings](/deploy/streamlit-community-cloud/manage-your-account/workspace-settings)
      * [Manage your GitHub connection](/deploy/streamlit-community-cloud/manage-your-account/manage-your-github-connection)
      * [Update your email](/deploy/streamlit-community-cloud/manage-your-account/update-your-email)
      * [Delete your account](/deploy/streamlit-community-cloud/manage-your-account/delete-your-account)
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
* [Manage your account](/deploy/streamlit-community-cloud/manage-your-account)/
* [Manage your GitHub connection](/deploy/streamlit-community-cloud/manage-your-account/manage-your-github-connection)

Manage your GitHub connection
=============================

If you have created an account but not yet connected GitHub, see [Connect your GitHub account](/deploy/streamlit-community-cloud/get-started/connect-your-github-account).

If you have already connected your GitHub account but still need to allow Streamlit Community Cloud to access private repositories, see [Optional: Add access to private repositories](/deploy/streamlit-community-cloud/get-started/connect-your-github-account#optional-add-access-to-private-repositories).

Add access to an organization
-----------------------------

If you are in an organization, you can grant or request access to that organization when you connect your GitHub account. For more information, see [Organization access](/deploy/streamlit-community-cloud/get-started/connect-your-github-account#organization-access).

If your GitHub account is already connected, you can remove permissions in your GitHub settings and force Streamlit to reprompt for GitHub authorization the next time you sign in to Community Cloud.

### Revoke and reauthorize

1. From your workspace, click on your workspace name in the upper-right corner. To sign out of Community Cloud, click "**Sign out**."

   ![Sign out of Streamlit Community Cloud](/images/streamlit-community-cloud/account-sign-out.png)
2. Go to your GitHub application settings at [github.com/settings/applications](https://github.com/settings/applications).
3. Find the "Streamlit" application, and click on the three dots (*more\_horiz*) to open the overflow menu.

   If you have ever signed in to Community Cloud using GitHub, you will also see the "Streamlit Community Cloud" application in your GitHub account. The "Streamlit" application manages repository access. The "Streamlit Community Cloud" application is only for managing your identity (email) on Community Cloud. You only need to revoke access to the "Streamlit" application.
4. Click "**Revoke**."

   ![Revoke access for Streamlit to access your GitHub account](/images/streamlit-community-cloud/GitHub-revoke.png)
5. Click "**I understand, revoke access**."

![Confirm to revoke access for Streamlit to your GitHub account](/images/streamlit-community-cloud/GitHub-revoke-confirm.png)

1. Return to [share.streamlit.io](https://share.streamlit.io) and sign in. You will be prompted to authorize GitHub as explained in [Connect GitHub](/deploy/streamlit-community-cloud/get-started/connect-your-github-account#organization-access).

### Granting previously denied access

If an organization owner has restricted Streamlit's access or restricted all OAuth applications, they may need to directly modify their permissions in GitHub. If an organization has restricted Streamlit's access, a red X (*close*) will appear next to the organization when you are prompted to authorize with your GitHub account.

![Denied authorization for Streamlit to access your GitHub account](/images/streamlit-community-cloud/GitHub-auth-denied-XL.png)

See GitHub's documentation on [OAuth apps and organizations](https://docs.github.com/en/apps/oauth-apps/using-oauth-apps/authorizing-oauth-apps#oauth-apps-and-organizations).

Rename your GitHub account or repositories
------------------------------------------

Community Cloud identifies apps by their GitHub coordinates (owner, repository, branch, entrypoint file path). If you rename your account or repository from which you've deployed an app, you will lose access to administer the app. To learn more, see [Rename your app in GitHub](/deploy/streamlit-community-cloud/manage-your-app/rename-your-app).

[Previous: Workspace settings](/deploy/streamlit-community-cloud/manage-your-account/workspace-settings)[Next: Update your email](/deploy/streamlit-community-cloud/manage-your-account/update-your-email)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
