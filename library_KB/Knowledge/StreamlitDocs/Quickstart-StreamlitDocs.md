Quickstart - Streamlit Docs

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
* [Quickstart](/deploy/streamlit-community-cloud/get-started/quickstart)

Quickstart
==========

This is a concise set of steps to create your Streamlit Community Cloud account, deploy a sample app, and start editing it with GitHub Codespaces. For other options and complete explanations, start with [Create your account](/deploy/streamlit-community-cloud/get-started/create-your-account).

You will sign in to your GitHub account during this process. Community Cloud will use the email from your GitHub account to create your Community Cloud account. For other sign-in options, see [Create your account](/deploy/streamlit-community-cloud/get-started/create-your-account).

Prerequisites
-------------

* You must have a GitHub account.

Sign up for Streamlit Community Cloud
-------------------------------------

1. Go to [share.streamlit.io](https://share.streamlit.io).
2. Click "**Continue to sign-in**."
3. Click "**Continue with GitHub**."
4. Enter your GitHub credentials and follow GitHub's authentication prompts.
5. Fill in your account information, and click "**I accept**" at the bottom.

Add access to your public repositories
--------------------------------------

1. In the upper-left corner, click "**Workspaces *warning***."

![Connect your GitHub account to a new Community Cloud account](/images/streamlit-community-cloud/workspace-unconnected-setup.png)

1. From the drop down, click "**Connect GitHub account**."
2. Enter your GitHub credentials and follow GitHub's authentication prompts.
3. Click "**Authorize streamlit**."

![Authorize Community Cloud to connect to your GitHub account](/images/streamlit-community-cloud/GitHub-auth1-none.png)

Optional: Add access to private repositories
--------------------------------------------

1. In the upper-left corner, click on your GitHub username.

![Access your workspace settings](/images/streamlit-community-cloud/workspace-empty-menu.png)

1. From the drop down, click "**Settings**."
2. On the left side of the dialog, select "**Linked accounts**."
3. Under "Source control," click "**Connect here *arrow\_forward***."
4. Click "**Authorize streamlit**."

![Authorize Community Cloud to connect to your private GitHub repositories](/images/streamlit-community-cloud/GitHub-auth2-none.png)

Create a new app from a template
--------------------------------

1. In the upper-right corner, click "**Create app**."

![Create a new app from your workspace in Streamlit Community Cloud](/images/streamlit-community-cloud/deploy-empty-new-app.png)

1. When asked "Do you already have an app?" click "**Nope, create one from a template**."
2. From the list of templates on the left, select "**Blank app**."
3. At the bottom, select the option to "**Open GitHub Codespaces...**"
4. At the bottom, click "**Deploy**."

Edit your app in GitHub Codespaces
----------------------------------

1. Wait for GitHub to set up your codespace.

   It can take several minutes to fully initialize your codespace. After the Visual Studio Code editor appears in your codespace, it can take several minutes to install Python and start the Streamlit server. When complete, a split screen view displays a code editor on the left and a running app on the right. The code editor opens two tabs by default: the repository's readme file and the app's entrypoint file.

   ![Your new GitHub Codespace](/images/streamlit-community-cloud/deploy-template-blank-codespace.png)
2. Go to the app's entrypoint file (`streamlit_app.py`) in the left pane, and change line 3 by adding "Streamlit" inside `st.title`.

   `-st.title("🎈 My new app")
   +st.title("🎈 My new Streamlit app")`

   Files are automatically saved in your codespace with each edit.
3. A moment after typing a change, your app on the right side will display a rerun prompt. Click "**Always rerun**."

   ![Edit the title of your sample Streamlit app](/images/streamlit-community-cloud/deploy-template-blank-codespace-edit.png)

   If the rerun prompt disappears before you click it, you can hover over the overflow menu icon (*more\_vert*) to bring it back.
4. Optional: Continue to make edits and observe the changes within seconds.

Publish your changes
--------------------

1. In the left navigation bar, click the source control icon.

![See your deployed Streamlit app](/images/streamlit-community-cloud/deploy-template-blank-codespace-edit-source-control.png)

1. In the source control sidebar on the left, enter a name for your commit.
2. Click "***check* Commit**."

![See your deployed Streamlit app](/images/streamlit-community-cloud/deploy-template-blank-codespace-edit-commit.png)

1. To stage and commit all your changes, in the confirmation dialog, click "**Yes**." Your changes are committed locally in your codespace.
2. To push your commit to GitHub, in the source control sidebar on the left, click "***cached* 1 *arrow\_upward***."
3. To push commits to "origin/main," in the confirmation dialog, click "**OK**."

   Your changes are now saved to your GitHub repository. Community Cloud will immediately reflect the changes in your deployed app.
4. Optional: To see your updated, published app, return to the "**My apps**" section of your workspace at [share.streamlit.io](https://share.streamlit.io), and click on your app.

Stop or delete your codespace
-----------------------------

When you stop interacting with your codespace, GitHub will generally stop your codespace for you. However, the surest way to avoid undesired use of your capacity is to stop or delete your codespace when you are done.

1. Go to [github.com/codespaces](https://github.com/codespaces). At the bottom of the page, all your codespaces are listed. Click the overflow menu icon (*more\_horiz*) for your codespace.

![Stop or delete your GitHub Codespace](/images/streamlit-community-cloud/deploy-hello-codespace-manage.png)

2. If you want to return to your work later, click "**Stop codespace**." Otherwise, click "**Delete**."

   ![Stop your GitHub codespace](/images/streamlit-community-cloud/codespace-menu.png)
3. Congratulations! You just deployed an app to Streamlit Community Cloud. 🎉 Return to your workspace at [share.streamlit.io/](https://share.streamlit.io/) and [deploy another Streamlit app](/deploy/streamlit-community-cloud/deploy-your-app).

   ![See your deployed Streamlit app](/images/streamlit-community-cloud/deploy-template-blank-edited.png)

[Previous: Get started](/deploy/streamlit-community-cloud/get-started)[Next: Create your account](/deploy/streamlit-community-cloud/get-started/create-your-account)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
