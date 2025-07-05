Connect your GitHub account - Streamlit Docs

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
* [Connect your GitHub account](/deploy/streamlit-community-cloud/get-started/connect-your-github-account)

Connect your GitHub account
===========================

Connecting GitHub to your Streamlit Community Cloud account allows you to deploy apps directly from the files you store in your repositories. It also lets the system check for updates to those files and automatically update your apps. When you first connect your GitHub account to your Community Cloud account, you'll be able to deploy apps from your public repositories to Community Cloud. If you want to deploy from private repositories, you can give Community Cloud additional permissions to do so. For more information about these permissions, see [GitHub OAuth scope](/deploy/streamlit-community-cloud/status#github-oauth-scope).

*priority\_high*

#### Important

In order to deploy an app, you must have **admin** permissions to its repository. If you don't have admin access, contact the repository's owner or fork the repository to create your own copy. For more help, see our [community forum](https://discuss.streamlit.io/).

If you are a member of a GitHub organization, that organization is displayed at the bottom of each GitHub OAuth prompt. In this case, we recommend reading about [Organization access](/deploy/streamlit-community-cloud/get-started/connect-your-github-account#organization-access) at the end of this page before performing the steps to connect your GitHub account. You must be an organization's owner in GitHub to grant access to that organization.

Prerequisites
-------------

* You must have a Community Cloud account. See [Create your account](/deploy/streamlit-community-cloud/get-started/create-your-account).
* You must have a GitHub account.

Add access to public repositories
---------------------------------

1. In the upper-left corner, click "**Workspaces *warning***."

![Connect your GitHub account to a new Community Cloud account](/images/streamlit-community-cloud/workspace-unconnected-setup.png)

1. From the drop down, click "**Connect GitHub account**."
2. Enter your GitHub credentials and follow GitHub's authentication prompts.
3. Click "**Authorize streamlit**."

   ![Authorize Community Cloud to connect to your GitHub account](/images/streamlit-community-cloud/GitHub-auth1-none.png)

   This adds the "Streamlit" OAuth application to your GitHub account. This allows Community Cloud to work with your public repositories and create codespaces for you. In the next section, you can allow Community Cloud to access your private repositories, too. For more information about using and reviewing the OAuth applications on your account, see [Using OAuth apps](https://docs.github.com/en/apps/oauth-apps/using-oauth-apps) in GitHub's docs.

Optional: Add access to private repositories
--------------------------------------------

After your Community Cloud account has access to deploy from your public repositories, you can follow these additional steps to grant access to your private repositories.

1. In the upper-left corner, click on your GitHub username.

![Access your workspace settings](/images/streamlit-community-cloud/workspace-empty-menu.png)

1. From the drop down, click "**Settings**."
2. On the left side of the dialog, select "**Linked accounts**."
3. Under "Source control," click "**Connect here *arrow\_forward***."
4. Click "**Authorize streamlit**."

![Authorize Community Cloud to connect to your private GitHub repositories](/images/streamlit-community-cloud/GitHub-auth2-none.png)

Organization access
-------------------

To deploy apps from repositories owned by a GitHub organization, Community Cloud must have permission to access the organization's repositories. If you are a member of a GitHub organization when you connect your GitHub account, your OAuth prompts will include a section labeled "Organization access."

![GitHub Oauth prompt including organization access](/images/streamlit-community-cloud/GitHub-auth1-organizations.png)

If you have already connected your GitHub account and need to add access to an organization, follow the steps in [Manage your GitHub connection](/deploy/streamlit-community-cloud/manage-your-account/manage-your-github-connection) to disconnect your GitHub account and start over. Alternatively, if you are not the owner of an organization, you can ask the owner to create a Community Cloud account for themselves and add permission directly.

### Organizations you own

For any organization you own, if authorization has not been previously granted or denied, you can click "**Grant**" before you click "**Authorize streamlit**."

![Authorize your Streamlit on a GitHub organization you own](/images/streamlit-community-cloud/GitHub-auth-grant-XL.png)

### Organizations owned by others

For an organization you don't own, if authorization has not been previously granted or denied, you can click "**Request**" before you click "**Authorize streamlit**."

![Authorize your Streamlit on a GitHub organization owned by others](/images/streamlit-community-cloud/GitHub-auth-request-XL.png)

### Previous or pending authorization

If someone has already started the process of authorizing Streamlit for your organization, the OAuth prompt will show the current status.

#### Approved access

If an organization has already granted Streamlit access, the OAuth prompt shows a green check (*check*).

![Approved authorization for Streamlit on an organization](/images/streamlit-community-cloud/GitHub-auth-granted-XL.png)

#### Pending access

If a request has been previously sent but not yet approved, the OAuth prompt show "Access request pending." Follow up with the organization's owner to accept the request in GitHub.

![Pending authorization for Streamlit on an organization](/images/streamlit-community-cloud/GitHub-auth-pending-XL.png)

#### Denied access

If a request has been previously sent and denied, the OAuth prompt shows a red X (*close*). In this case, the organization owner will need to authorize Streamlit from GitHub. See GitHub's documentation on [OAuth apps and organizations](https://docs.github.com/en/apps/oauth-apps/using-oauth-apps/authorizing-oauth-apps#oauth-apps-and-organizations).

![Denied authorization for Streamlit on an organization](/images/streamlit-community-cloud/GitHub-auth-denied-XL.png)

What's next?
------------

Now that you have your account you can [Explore your workspace](/deploy/streamlit-community-cloud/get-started/explore-your-workspace). Or if you're ready to go, jump right in and [Deploy your app](/deploy/streamlit-community-cloud/deploy-your-app).

[Previous: Create your account](/deploy/streamlit-community-cloud/get-started/create-your-account)[Next: Explore your workspace](/deploy/streamlit-community-cloud/get-started/explore-your-workspace)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
