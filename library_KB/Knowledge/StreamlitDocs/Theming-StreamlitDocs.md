Theming - Streamlit Docs

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

    *remove*

    - CORE

      ---
    - [Architecture and execution](/develop/concepts/architecture)

      *add*
    - [Multipage apps](/develop/concepts/multipage-apps)

      *add*
    - [App design](/develop/concepts/design)

      *add*
    - ADDITIONAL

      ---
    - [Connections, secrets, and authentication](/develop/concepts/connections)

      *add*
    - [Custom components](/develop/concepts/custom-components)

      *add*
    - [Configuration and theming](/develop/concepts/configuration)

      *remove*

      * [Configuration options](/develop/concepts/configuration/options)
      * [HTTPS support](/develop/concepts/configuration/https-support)
      * [Serving static files](/develop/concepts/configuration/serving-static-files)
      * THEMING

        ---
      * [Customize your theme](/develop/concepts/configuration/theming)
      * [Customize colors and borders](/develop/concepts/configuration/theming-customize-colors-and-borders)
      * [Customize fonts](/develop/concepts/configuration/theming-customize-fonts)
    - [App testing](/develop/concepts/app-testing)

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
* [Develop](/develop)/
* [Concepts](/develop/concepts)/
* [Configuration and theming](/develop/concepts/configuration)/
* [Customize your theme](/develop/concepts/configuration/theming)

Theming overview
================

In this guide, we provide an overview of theming and visual customization of Streamlit apps. Streamlit themes are defined using configuration options, which are most commonly defined in a `.streamlit/config.toml` file. For more information about setting configuration options, see [Working with configuration options](/develop/concepts/configuration/options). For a complete list of configuration options and definitions, see the API reference for [config.toml](/develop/api-reference/configuration/config.toml#theme).

The following options can be set once for your whole app:

* **Base color scheme**: Set your custom theme to inherit from Streamlit's light or dark theme.
* **Font size**: Set the base font size for your app.

The following options can be configured separately for the main body of your app and the sidebar:

* **Font**: Set the font family for body text, headers, and code.
* **Text color**: Set the color of body text and links.
* **Primary color**: Set the color of interactive elements and highlights.
* **Background color**: Set the color of app, widget, and code block backgrounds.
* **Border radius**: Set the roundness of elements and widgets.
* **Border color**: Set the color and visibility of element, widget, and sidebar borders.

Example themes
--------------

The following light theme is inspired by [Anthropic](https://docs.anthropic.com/en/home).

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen *open\_in\_new*](https://doc-theming-overview-anthropic-light-inspired.streamlit.app/?utm_medium=oembed)

The following dark theme is inspired by [Spotify](https://open.spotify.com/).

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen *open\_in\_new*](https://doc-theming-overview-spotify-inspired.streamlit.app/?utm_medium=oembed)

Working with theme configuration during development
---------------------------------------------------

Most theme configuration options can be updated while an app is running. This makes it easy to iterate on your custom theme. If you change your app's primary color, save your `config.toml` file, and rerun your app, you will immediately see the new color. However, some configuration options (like `[[theme.fontFace]]`) require you to restart the Streamlit server to reflect the updates. If in doubt, when updating your app's configuration, stop the Streamlit server in your terminal and restart your app with the `streamlit run` command.

[Previous: Serving static files](/develop/concepts/configuration/serving-static-files)[Next: Customize colors and borders](/develop/concepts/configuration/theming-customize-colors-and-borders)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
