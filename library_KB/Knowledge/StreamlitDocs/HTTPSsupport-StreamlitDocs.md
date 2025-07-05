HTTPS support - Streamlit Docs

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
* [HTTPS support](/develop/concepts/configuration/https-support)

HTTPS support
=============

Many apps need to be accessed with SSL / [TLS](https://en.wikipedia.org/wiki/Transport_Layer_Security) protocol or `https://`.

We recommend performing SSL termination in a reverse proxy or load balancer for self-hosted and production use cases, not directly in the app. [Streamlit Community Cloud](/deploy/streamlit-community-cloud) uses this approach, and every major cloud and app hosting platform should allow you to configure it and provide extensive documentation. You can find some of these platforms in our [Deployment tutorials](/deploy/tutorials).

To terminate SSL in your Streamlit app, you must configure `server.sslCertFile` and `server.sslKeyFile`. Learn how to set config options in [Configuration](/develop/concepts/configuration).

Details on usage
----------------

* The configuration value should be a local file path to a cert file and key file. These must be available at the time the app starts.
* Both `server.sslCertFile` and `server.sslKeyFile` must be specified. If only one is specified, your app will exit with an error.
* This feature will not work in Community Cloud. Community Cloud already serves your app with TLS.

*priority\_high*

#### Warning

In a production environment, we recommend performing SSL termination by the load balancer or the reverse proxy, not using this option. The use of this option in Streamlit has not gone through extensive security audits or performance tests.

Example usage
-------------

`# .streamlit/config.toml
[server]
sslCertFile = '/path/to/certchain.pem'
sslKeyFile = '/path/to/private.key'`

[Previous: Configuration options](/develop/concepts/configuration/options)[Next: Serving static files](/develop/concepts/configuration/serving-static-files)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
