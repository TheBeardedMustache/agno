streamlit hello - Streamlit Docs

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

    *remove*

    - PAGE ELEMENTS

      ---
    - [Write and magic](/develop/api-reference/write-magic)

      *add*
    - [Text elements](/develop/api-reference/text)

      *add*
    - [Data elements](/develop/api-reference/data)

      *add*
    - [Chart elements](/develop/api-reference/charts)

      *add*
    - [Input widgets](/develop/api-reference/widgets)

      *add*
    - [Media elements](/develop/api-reference/media)

      *add*
    - [Layouts and containers](/develop/api-reference/layout)

      *add*
    - [Chat elements](/develop/api-reference/chat)

      *add*
    - [Status elements](/develop/api-reference/status)

      *add*
    - [Third-party components*open\_in\_new*](https://streamlit.io/components)
    - APPLICATION LOGIC

      ---
    - [Authentication and user info](/develop/api-reference/user)

      *add*
    - [Navigation and pages](/develop/api-reference/navigation)

      *add*
    - [Execution flow](/develop/api-reference/execution-flow)

      *add*
    - [Caching and state](/develop/api-reference/caching-and-state)

      *add*
    - [Connections and secrets](/develop/api-reference/connections)

      *add*
    - [Custom components](/develop/api-reference/custom-components)

      *add*
    - [Configuration](/develop/api-reference/configuration)

      *add*
    - TOOLS

      ---
    - [App testing](/develop/api-reference/app-testing)

      *add*
    - [Command line](/develop/api-reference/cli)

      *remove*

      * [streamlit cache](/develop/api-reference/cli/cache)
      * [streamlit config](/develop/api-reference/cli/config)
      * [streamlit docs](/develop/api-reference/cli/docs)
      * [streamlit hello](/develop/api-reference/cli/hello)
      * [streamlit help](/develop/api-reference/cli/help)
      * [streamlit init](/develop/api-reference/cli/init)
      * [streamlit run](/develop/api-reference/cli/run)
      * [streamlit version](/develop/api-reference/cli/version)
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
* [API reference](/develop/api-reference)/
* [Command line](/develop/api-reference/cli)/
* [streamlit hello](/develop/api-reference/cli/hello)

`$ streamlit hello`
-------------------

Run the Hello app, an example Streamlit app included with the Streamlit library.

### Syntax

`streamlit hello`

### Options

The `hello` command accepts configuration options (just like the `run` command does). Configuration options are passed in the form of `--<section>.<option>=<value>`. For example, if you want to set the primary color of your app to blue, you could use one of the three equivalent options:

* `--theme.primaryColor=blue`
* `--theme.primaryColor="blue"`
* `--theme.primaryColor=#0000FF`

For a complete list of configuration options, see [`config.toml`](/develop/api-reference/configuration/config.toml) in the API reference. For examples, see below.

### Example

#### Example 1: Run the Hello app with default settings

To verify that Streamlit is installed correctly, this command runs an example app included in the Streamlit library. From any directory, execute the following:

`streamlit hello`

Streamlit will start the Hello app and open it in your default browser. The source for the Hello app can be [viewed in GitHub](https://github.com/streamlit/streamlit/tree/develop/lib/streamlit/hello).

#### Example 2: Run the Hello app with a custom config option value

To run the Hello app with a blue accent color, from any directory, execute the following:

`streamlit hello --theme.primaryColor=blue`

[Previous: streamlit docs](/develop/api-reference/cli/docs)[Next: streamlit help](/develop/api-reference/cli/help)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
