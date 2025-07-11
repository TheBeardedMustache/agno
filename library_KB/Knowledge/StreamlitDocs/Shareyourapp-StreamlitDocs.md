﻿Share your app - Streamlit Docs

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

      *remove*

      * [Embed your app](/deploy/streamlit-community-cloud/share-your-app/embed-your-app)
      * [Search indexability](/deploy/streamlit-community-cloud/share-your-app/indexability)
      * [Share previews](/deploy/streamlit-community-cloud/share-your-app/share-previews)
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
* [Share your app](/deploy/streamlit-community-cloud/share-your-app)

Share your app
==============

Now that your app is deployed you can easily share it and collaborate on it. But first, let's take a moment and do a little joy dance for getting that app deployed! 🕺💃

Your app is now live at a fixed URL, so go wild and share it with whomever you want. Your app will inherit permissions from your GitHub repo, meaning that if your repo is private your app will be private and if your repo is public your app will be public. If you want to change that you can simply do so from the app settings menu.

You are only allowed one private app at a time. If you've deployed from a private repository, you will have to make that app public or delete it before you can deploy another app from a private repository. Only developers can change your app between public and private.

* [Make your app public or private](/deploy/streamlit-community-cloud/share-your-app#make-your-app-public-or-private)
* [Share your public app](/deploy/streamlit-community-cloud/share-your-app#share-your-public-app)
* [Share your private app](/deploy/streamlit-community-cloud/share-your-app#share-your-private-app)

Make your app public or private
-------------------------------

If you deployed your app from a public repository, your app will be public by default. If you deployed your app from a private repository, you will need to make the app public if you want to freely share it with the community at large.

### Set privacy from your app settings

1. Access your [App settings](/deploy/streamlit-community-cloud/manage-your-app/app-settings) and go to the "**Sharing**" section.

   ![Share settings on Streamlit Community Cloud](/images/streamlit-community-cloud/workspace-app-settings-sharing.png)
2. Set your app's privacy under "Who can view this app." Select "**This app is public and searchable**" to make your app public. Select "**Only specific people can view this app**" to make your app private.

   ![Set your app's privacy in share settings](/images/streamlit-community-cloud/workspace-app-settings-sharing-change.png)

### Set privacy from the share button

1. From your app at `<your-custom-subdomain>.streamlit.app`, click "**Share**" in the upper-right corner.

   ![Access the share button from your app](/images/streamlit-community-cloud/share-open.png)
2. Toggle your app between public and private by clicking "**Make this app public**."

   ![Toggle your app between public and private from the share button](/images/streamlit-community-cloud/share-menu-public-toggle.png)

Share your public app
---------------------

Once your app is public, just give anyone your app's URL and they view it! Streamlit Community Cloud has several convenient shortcuts for sharing your app.

### Share your app on social media

1. From your app at `<your-custom-subdomain>.streamlit.app`, click "**Share**" in the upper-right corner.
2. Click "**Social**" to access convenient social media share buttons.

   ![Social media sharing links from the share button](/images/streamlit-community-cloud/share-menu-social.png)

*star*

#### Tip

Use the social media sharing buttons to post your app on our forum! We'd love to see what you make and perhaps feature your app as our app of the month. 💖

### Invite viewers by email

Whether your app is public or private, you can send an email invite to your app directly from Streamlit Community Cloud. This grants the viewer access to analytics for all your public apps and the ability to invite other viewers to your workspace. Developers and invited viewers are identified by their email in analytics instead of appearing anonymously (if they view any of your apps while signed in). Read more about viewers in [App analytics](/deploy/streamlit-community-cloud/manage-your-app/app-analytics).

1. From your app at `<your-custom-subdomain>.streamlit.app`, click "**Share**" in the upper-right corner.
2. Enter an email address and click "**Invite**."

   ![Invite viewers from the share button](/images/streamlit-community-cloud/share-invite-public.png)
3. Invited users will get a direct link to your app in their inbox.

   ![Invitation email sent to viewers](/images/streamlit-community-cloud/share-invite-email.png)

### Copy your app's URL

From your app click "**Share**" in the upper-right corner then click "**Copy link**."

![Copy your app's URL from the share button](/images/streamlit-community-cloud/share-copy.png)

### Add a badge to your GitHub repository

To help others find and play with your Streamlit app, you can add Streamlit's GitHub badge to your repo. Below is an enlarged example of what the badge looks like. Clicking on the badge takes you to—in this case—Streamlit's Roadmap.

[![Open in Streamlit badge for GitHub](/images/streamlit-community-cloud/github-badge.svg)](https://roadmap.streamlit.app/)

Once you deploy your app, you can embed this badge right into your GitHub README.md by adding the following Markdown:

`[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://<your-custom-subdomain>.streamlit.app)`

*push\_pin*

#### Note

Be sure to replace `https://<your-custom-subdomain>.streamlit.app` with the URL of your deployed app!

Share your private app
----------------------

By default an app deployed from a private repository will be private to the developers in the workspace. A private app will not be visible to anyone else unless you grant them explicit permission. You can grant permission by adding them as a developer on GitHub or by adding them as a viewer on Streamlit Community Cloud.

Once you have added someone's email address to your app's viewer list, that person will be able to sign in and view your private app. If their email is associated with a Google account, they will be able to sign in with Google OAuth. Otherwise, they will be able to sign in with single-use, emailed links. Streamlit sends an email invitation with a link to your app every time you invite someone.

*priority\_high*

#### Important

When you add a viewer to any app in your workspace, they are granted access to analytics for that app as well as analytics for all your public apps. They can also pass these permissions to others by inviting more viewers. All viewers and developers in your workspace are identified by their email in analytics. Furthermore, their emails show in analytics for every app in your workspace and not just apps they are explicitly invited to. Read more about viewers in [App analytics](/deploy/streamlit-community-cloud/manage-your-app/app-analytics)

### Invite viewers from the share button

1. From your app at `<your-custom-subdomain>.streamlit.app`, click "**Share**" in the upper-right corner.

   ![Access the share button from your app](/images/streamlit-community-cloud/share-open.png)
2. Enter the email to send an invitation to and click "**Invite**."

   ![Invite viewers from the share button](/images/streamlit-community-cloud/share-invite.png)
3. Invited users appear in the list below.

   ![View invited users from the share button](/images/streamlit-community-cloud/share-invited.png)
4. Invited users will get a direct link to your app in their inbox.

   ![Invitation email sent to viewers](/images/streamlit-community-cloud/share-invite-email.png)

* To remove a viewer, simply access the share menu as above and click the *close* next to their name.

  ![Remove viewers from the share button](/images/streamlit-community-cloud/share-remove.png)

### Invite viewers from your app settings

1. Access your [App settings](/deploy/streamlit-community-cloud/manage-your-app/app-settings) and go to the "**Sharing**" section.

   ![Access sharing settings from your app settings](/images/streamlit-community-cloud/workspace-app-settings-sharing.png)
2. Add or remove users from the list of viewers. Click "**Save**."

   ![Invite and remove viewers from your app settings](/images/streamlit-community-cloud/workspace-app-settings-sharing-invite.png)

[Previous: Manage your app](/deploy/streamlit-community-cloud/manage-your-app)[Next: Embed your app](/deploy/streamlit-community-cloud/share-your-app/embed-your-app)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
