﻿Use Streamlit in Snowflake - Streamlit Docs

[![](/logo.svg)

#### Documentation](/)

*search*

Search

* [*rocket\_launch*

  Get started](/get-started)
  + [Installation](/get-started/installation)

    *remove*

    - [Use command line](/get-started/installation/command-line)
    - [Use Anaconda Distribution](/get-started/installation/anaconda-distribution)
    - [Use GitHub Codespaces](/get-started/installation/community-cloud)
    - [Use Snowflake](/get-started/installation/streamlit-in-snowflake)
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

    *add*
  + [Snowflake](/deploy/snowflake)
  + [Other platforms](/deploy/tutorials)

    *add*
* [*school*

  Knowledge base](/knowledge-base)
  + [FAQ](/knowledge-base/using-streamlit)
  + [Installing dependencies](/knowledge-base/dependencies)
  + [Deployment issues](/knowledge-base/deploy)

* [Home](/)/
* [Get started](/get-started)/
* [Installation](/get-started/installation)/
* [Use Snowflake](/get-started/installation/streamlit-in-snowflake)

Use Streamlit in Snowflake to code in a secure environment
==========================================================

Snowflake is a single, global platform that powers the Data Cloud. If you want to use a secure platform with role-based access control, this is the option for you! This page walks you through creating a trial Snowflake account and building a "Hello world" app. Your trial account comes with an account credit so you can try out the service without entering any payment information.

*push\_pin*

#### Note

For more information, see [Limitations and unsupported features](https://docs.snowflake.com/en/developer-guide/streamlit/limitations) in the Snowflake documentation.

Prerequisites
-------------

All you need is an email address! Everything else happens in your 30-day trial account.

Create an account
-----------------

1. Go to [signup.snowflake.com](https://signup.snowflake.com/?utm_source=streamlit&utm_medium=referral&utm_campaign=na-us-en-&utm_content=-ss-streamlit-docs). (This link will open in a new tab.)
2. Fill in your information, and click "**CONTINUE**."
3. Select "**Standard**" for your Snowflake edition and "**Amazon Web Services**" for your cloud provider.
4. Choose the region nearest you, accept the terms, and click "**GET STARTED**."

![Choose your Snowflake edition, provider, and region](/images/get-started/SiS-region.png)

1. Answer a few questions to let us know more about yourself, or skip them.
2. A message will display: "You're now signed up!" Go to your email, and click on the activation link. (Within your link, note the subdomain. This is your Snowflake account identifier. `https://<account_identifier>.snowflakecomputing.com`)
3. Set your username and password. This will be an admin user account within your Snowflake account. Your Snowflake account can have multiple users within it.
4. If you are not signed in after setting your password, follow the instructions to enter your Snowflake account identifier, and then enter your username and password. If you've accidentally closed your browser, you can sign in at [app.snowflake.com](https://app.snowflake.com/).

Congratulations! You have a trial Snowflake account.

The displayed interface is called Snowsight. Snowsight provides a web-based, graphical user interface for your Snowflake account. The default page is "**Home**," which provides popular quick actions to get started. You can access your "**Projects**" in the left navigation or at the bottom of your "**Home**" page. "**Projects**" include worksheets, notebooks, Streamlit apps, and dashboards. Check out the Snowflake docs for a [quick tour](https://docs.snowflake.com/en/user-guide/ui-snowsight-quick-tour).)

![Sample databases in your new trial Snowflake account](/images/get-started/SiS-1-landing-page.png)

Optional: Create a warehouse
----------------------------

Warehouses provide compute resources for tasks and apps in your Snowflake account. Your trial account already has an XS warehouse which you can use. This is named "COMPUTE\_WH." However, if you want to use more compute resources, you can create another warehouse.

1. In the lower-left corner under your name, confirm that your current role is "ACCOUNTADMIN." If it isn't, click your name, hover over "**Switch Role**," and select "**ACCOUNTADMIN**."
2. In the left navigation, select "**Admin**" → "**Warehouses**."
3. In the upper-right corner, click the blue "*add* **Warehouse**" button.
4. Enter "STREAMLIT\_WH" for the name and select a type and size. The default type and size are "Standard" and "X-Small," respectively. Click "**Create Warehouse**."

Create a database
-----------------

Databases provide storage for data and apps in your Snowflake account. Your trial account comes with a shared database of sample data, but you must create a new database in your account to store your app files.

1. In the left navigation, select "**Data**" → "**Databases**."
2. In the upper-right corner, click the blue "*add* **Database**" button.
3. Enter "STREAMLIT\_DB" for the name, and click "**Create**."

Yay! You now have a new database to hold all your Streamlit apps.

![New database in your new trial Snowflake account](/images/get-started/SiS-2-databases.png)

The databases in the above screenshot are as follows:

* "SNOWFLAKE:" A built-in database that stores meta data for your account.
* "SNOWFLAKE\_SAMPLE\_DATA:" A shared database with sample data.
* "STREAMLIT\_DB:" Your new database where you'll put your Streamlit files.

Create a "Hello World" Streamlit app
------------------------------------

1. In the left navigation, select "**Projects**" → "**Streamlit**."
2. In the upper-right corner, click the blue "*add* **Streamlit App**" button.
3. Enter your app details as follows:

   * App title: "Hello World"
   * App location: "STREAMLIT\_DB" and "PUBLIC"
   * App warehouse: "COMPUTE\_WH" (default) or "STREAMLIT\_WH" (if you created a new warehouse)

   If you can't select your database, refresh the page to ensure that the interface is displaying current information.
4. Click "**Create**." (Note that the app will run with the rights of "ACCOUNTADMIN" for simplicity. You can curate your roles and permissions to choose who can create and access apps.)

   ![Create your first Streamlit in Snowflake app](/images/get-started/SiS-3-create-app.png)

   Your new app is prefilled with example code and opens in editing mode. The left panel shows your code. The right panel shows the resulting app.
5. Optional: Explore the example app.
6. In the left code editor, delete everything, and replace it with the following:

   `import streamlit as st
   st.write("Hello World")`

   If you want to return to the sample code later, you can always make another app to edit the same example again.
7. In the upper-right corner, click the blue "*play\_arrow* **Run**" button to make the running app reflect your changes.

   Hooray! You just wrote a Streamlit app.

   ![Hello World in Streamlit in Snowflake app](/images/get-started/SiS-4-hello-world.png)

   *star*

   #### Tip

   In the lower-left corner of the editing interface, you can click the splitscreen icons to toggle the visibility of your file navigation, code editor, and app preview.
8. Change `st.write` to `st.title`:

   `import streamlit as st
   st.title("Hello World")`
9. In the upper-right corner, click the blue "*play\_arrow* **Run**" button to make the running app reflect your changes.

   Your app now displays the larger title text.
10. Optional: Make more edits to your app. You must interact with your app or click the blue "*play\_arrow* **Run**" button to display the changes. This is different from a local environment where you can save your changes to trigger a rerun.
11. To return to Snowsight, in the upper-left corner, click "*chevron\_left* **Streamlit Apps**."

Return to your app
------------------

When you want to view or edit your app again, you can return to it through Snowsight. If you are returning to the site, you can sign in at [app.snowflake.com](https://app.snowflake.com/).

1. In the left navigation, select "**Projects**" → "**Streamlit**."
2. In your list of apps, click "**Hello World**."

   If you don't see your app, check that your role is set to "ACCOUNTADMIN" as described in [Optional: Create a warehouse](/get-started/installation/streamlit-in-snowflake#optional-create-a-warehouse).
3. Your app will open in viewing mode. To edit your app, in the upper-right corner, click "**Edit**."

   ![Change to editing mode in Streamlit in Snowflake](/images/get-started/SiS-5-hello-world-edit.png)

What's next?
------------

Read about our [Basic concepts](/get-started/fundamentals/main-concepts) and try out more commands in your app. Or, create more apps in Snowflake! You can reuse your warehouse and database, so you don't need to repeat those steps.

For more information about creating and managing Streamlit in Snowflake apps, check out the [Snowflake docs](https://docs.snowflake.com/en/developer-guide/streamlit/about-streamlit).

[Previous: Use GitHub Codespaces](/get-started/installation/community-cloud)[Next: Fundamentals](/get-started/fundamentals)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
