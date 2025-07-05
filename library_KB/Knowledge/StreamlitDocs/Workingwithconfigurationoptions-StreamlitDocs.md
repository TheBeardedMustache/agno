Working with configuration options - Streamlit Docs

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
* [Configuration options](/develop/concepts/configuration/options)

Working with configuration options
==================================

Streamlit provides four different ways to set configuration options. This list is in reverse order of precedence, i.e. command line flags take precedence over environment variables when the same configuration option is provided multiple times.

*push\_pin*

#### Note

If you change theme settings in `.streamlit/config.toml` *while* the app is running, these changes will reflect immediately. If you change non-theme settings in `.streamlit/config.toml` *while* the app is running, the server needs to be restarted for changes to be reflected in the app.

1. In a **global config file** at `~/.streamlit/config.toml` for macOS/Linux or `%userprofile%/.streamlit/config.toml` for Windows:

   `[server]
   port = 80`
2. In a **per-project config file** at `$CWD/.streamlit/config.toml`, where
   `$CWD` is the folder you're running Streamlit from.
3. Through `STREAMLIT_*` **environment variables**, such as:

   `export STREAMLIT_SERVER_PORT=80
   export STREAMLIT_SERVER_COOKIE_SECRET=dontforgottochangeme`
4. As **flags on the command line** when running `streamlit run`:

   `streamlit run your_script.py --server.port 80`

Available options
-----------------

All available configuration options are documented in [`config.toml`](/develop/api-reference/configuration/config.toml). These options may be declared in a TOML file, as environment variables, or as command line options.

When using environment variables to override `config.toml`, convert the variable (including its section header) to upper snake case and add a `STREAMLIT_` prefix. For example, `STREAMLIT_CLIENT_SHOW_ERROR_DETAILS` is equivalent to the following in TOML:

`[client]
showErrorDetails = true`

When using command line options to override `config.toml` and environment variables, use the same case as you would in the TOML file and include the section header as a period-separated prefix. For example, the command line option `--server.enableStaticServing true` is equivalent to the following:

`[server]
enableStaticServing = true`

Telemetry
---------

As mentioned during the installation process, Streamlit collects usage statistics. You can find out
more by reading our [Privacy Notice](https://streamlit.io/privacy-policy), but the high-level
summary is that although we collect telemetry data we cannot see and do not store information
contained in Streamlit apps.

If you'd like to opt out of usage statistics, add the following to your config file:

`[browser]
gatherUsageStats = false`

Theming
-------

You can change the base colors of your app using the `[theme]` section of the configuration system.
To learn more, see [Theming.](/develop/concepts/configuration/theming)

View all configuration options
------------------------------

As described in [Command-line options](/develop/api-reference/cli), you can
view all available configuration options using:

`streamlit config show`

[Previous: Configuration and theming](/develop/concepts/configuration)[Next: HTTPS support](/develop/concepts/configuration/https-support)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
