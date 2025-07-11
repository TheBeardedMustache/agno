﻿Embed your app - Streamlit Docs

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
* [Share your app](/deploy/streamlit-community-cloud/share-your-app)/
* [Embed your app](/deploy/streamlit-community-cloud/share-your-app/embed-your-app)

Embed your app
==============

Embedding Streamlit Community Cloud apps enriches your content by integrating interactive, data-driven applications directly within your pages. Whether you're writing a blog post, a technical document, or sharing resources on platforms like Medium, Notion, or even StackOverflow, embedding Streamlit apps adds a dynamic component to your content. This allows your audience to interact with your ideas, rather than merely reading about them or looking at screenshots.

Streamlit Community Cloud supports both [iframe](/deploy/streamlit-community-cloud/share-your-app/embed-your-app#embedding-with-iframes) and [oEmbed](/deploy/streamlit-community-cloud/share-your-app/embed-your-app#embedding-with-oembed) methods for embedding **public** apps. This flexibility enables you to share your apps across a wide array of platforms, broadening your app's visibility and impact. In this guide, we'll cover how to use both methods effectively to share your Streamlit apps with the world.

Embedding with iframes
----------------------

Streamlit Community Cloud supports embedding **public** apps using the subdomain scheme. To embed a public app, add the query parameter `/?embed=true` to the end of the `*.streamlit.app` URL.

For example, say you want to embed the [30DaysOfStreamlit app](https://30days.streamlit.app/). The URL to include in your iframe is: `https://30days.streamlit.app/?embed=true`:

`<iframe
src="https://30days.streamlit.app?embed=true"
style="height: 450px; width: 100%;"
></iframe>`

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen *open\_in\_new*](https://30days.streamlit.app/?utm_medium=oembed)

*priority\_high*

#### Important

There will be no official support for embedding private apps.

In addition to allowing you to embed apps via iframes, the `?embed=true` query parameter also does the following:

* Removes the toolbar with the app menu icon (*more\_vert*).
* Removes the padding at the top and bottom of the app.
* Removes the footer.
* Removes the colored line from the top of the app.

For granular control over the embedding behavior, Streamlit allows you to specify one or more instances of the `?embed_options` query parameter (e.g. to show the toolbar, open the app in dark theme, etc). [Click here for a full list of Embed options.](/deploy/streamlit-community-cloud/share-your-app/embed-your-app#embed-options)

Embedding with oEmbed
---------------------

Streamlit's oEmbed support allows for a simpler embedding experience. You can directly drop a Streamlit app's URL into a Medium, Ghost, or Notion page (or any of more than 700 content providers that supports oEmbed or [embed.ly](https://embed.ly/)). The embedded app will automatically appear! This helps Streamlit Community Cloud apps seamlessly integrate into these platforms, improving the visibility and accessibility of your apps.

### Example

When creating content in a Notion page, Medium article, or Ghost blog, you only need to paste the app's URL and hit "**Enter**." The app will then render automatically at that spot in your content. You can use your undecorated app URL without the `?embed=true` query parameter.

`https://30days.streamlit.app/`

Here's an example of [@chrieke](https://github.com/chrieke)'s [Prettymapp app](https://chrieke-prettymapp-streamlit-prettymappapp-1k0qxh.streamlit.app/) embedded in a Medium article:

![Example: Embed an app in a Medium article with oEmbed](/images/streamlit-community-cloud/oembed.gif)

*star*

#### Tip

Ensure the platform hosting the embedded Streamlit app supports oEmbed or [embed.ly](https://embed.ly/).

### Key Sites for oEmbed

oEmbed should work out of the box for several platforms including but not limited to:

* [Medium](https://medium.com/)
* [Notion](https://notion.so/)
* [Looker](https://www.looker.com/)
* [Tableau](https://www.tableau.com/)
* [Ghost](https://ghost.org/)
* [Discourse](https://www.discourse.org/)
* [StackOverflow](https://stackoverflow.com/)
* [W3](https://www.w3schools.com/)
* [Reddit](https://www.reddit.com/)

Please check the specific platform's documentation to verify support for oEmbed.

### iframe versus oEmbed

The only noteworthy differences between the methods is that iframing allows you to customize the app's embedding behavior (e.g. showing the toolbar, opening the app in dark theme, etc) using the various `?embed_options` described in the next section.

Embed options
-------------

When [Embedding with iframes](/deploy/streamlit-community-cloud/share-your-app/embed-your-app#embedding-with-iframes), Streamlit allows you to specify one or more instances of the `?embed_options` query parameter for granular control over the embedding behavior.

Both `?embed` and `?embed_options` are invisible to [`st.query_params`](/develop/api-reference/caching-and-state/st.query_params) and its precursors, [`st.experimental_get_query_params`](/develop/api-reference/caching-and-state/st.experimental_get_query_params) and [`st.experimental_set_query_params`](/develop/api-reference/caching-and-state/st.experimental_set_query_params). You can't get or set their values.

The supported values for `?embed_options` are listed below:

1. Show the toolbar at the top right of the app which includes the app menu (*more\_vert*), running man, and link to GitHub.

   `/?embed=true&embed_options=show_toolbar`
2. Show padding at the top and bottom of the app.

   `/?embed=true&embed_options=show_padding`
3. Show the footer reading "Made with Streamlit." (This doesn't apply to Streamlit versions 1.29.0 and later since the footer was removed from the library.)

   `/?embed=true&embed_options=show_footer`
4. Show the colored line at the top of the app.

   `/?embed=true&embed_options=show_colored_line`
5. Hide the "skeleton" that appears while an app is loading.

   `/?embed=true&embed_options=hide_loading_screen`
6. Disable scrolling for the main body of the app. (The sidebar will still be scrollable.)

   `/?embed=true&embed_options=disable_scrolling`
7. Open the app with light theme.

   `/?embed=true&embed_options=light_theme`
8. Open the app with dark theme.

   `/?embed=true&embed_options=dark_theme`

You can also combine the params:

`/?embed=true&embed_options=show_toolbar&embed_options=show_padding&embed_options=show_footer&embed_options=show_colored_line&embed_options=disable_scrolling`

### Build an embed link

You can conveniently build an embed link for your app — right from your app!

1. From your app at `<your-custom-subdomain>.streamlit.app`, click "**Share**" in the upper-right corner.
2. Click "**Embed**" to access a list of selectable embed options.

   ![Access embed options from the share button](/images/streamlit-community-cloud/share-menu-embed.png)
3. Select your embed options and click "**Get embed link**" to copy the embed link to your clipboard.

   ![Build a customized embed link for your app from the share button](/images/streamlit-community-cloud/share-menu-embed-url.png)

[Previous: Share your app](/deploy/streamlit-community-cloud/share-your-app)[Next: Search indexability](/deploy/streamlit-community-cloud/share-your-app/indexability)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
