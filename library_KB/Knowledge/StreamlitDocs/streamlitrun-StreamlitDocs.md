streamlit run - Streamlit Docs

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
* [streamlit run](/develop/api-reference/cli/run)

`$ streamlit run`
-----------------

This command starts your Streamlit app.

### Syntax

`streamlit run <entrypoint file> [-- config options] [script args]`

### Arguments

`<entrypoint file>`: The path to your entrypoint file for your Streamlit app. In a multipage app with `st.navigation`, your entrypoint file acts as a router between your pages. Otherwise, your entrypoint file is your app's homepage.

### Options

Configuration options are passed in the form of `--<section>.<option>=<value>`. For example, if you want to set the primary color of your app to blue, you could use one of the three equivalent options:

* `--theme.primaryColor=blue`
* `--theme.primaryColor="blue"`
* `--theme.primaryColor=#0000FF`

For a complete list of configuration options, see [`config.toml`](/develop/api-reference/configuration/config.toml) in the API reference. For examples, see below.

### Script arguments

If you need to pass arguments directly to your script, you can pass them as positional arguments. If you use `sys.argv` to read your arguments, `sys.arfgv` returns a list of all arugments and does *not* include any configuration options. Python interprets all arguments as strings.

* `sys.argv[0]` returns the provided path to your entrypoint file (`<entrypoint file>`).
* `sys.argv[1:]` returns a list of arguments in order and does not include any configuration options.

### Examples

* If your app is in your working directory, run it as follows:

  `streamlit run your_app.py`
* If your app is in a subdirectory, run it as follows:

  `streamlit run your_subdirectory/your_app.py`
* If your app is saved in a public GitHub repo or gist, run it as follows:

  `streamlit run https://raw.githubusercontent.com/streamlit/demo-uber-nyc-pickups/master/streamlit_app.py`
* If you need to set one or more configuration options, run it as follows:

  `streamlit run your_app.py --client.showErrorDetails=False --theme.primaryColor=blue`
* If you need to pass an argument to your script, run it as follows:

  `streamlit run your_app.py "my list" of arguments`

  Within your script, the following statement will be true:

  `sys.argv[0] == "your_app.py"
  sys.argv[1] == "my list"
  sys.argv[2] == "of"
  sys.argv[3] == "arguments"`

[Previous: streamlit init](/develop/api-reference/cli/init)[Next: streamlit version](/develop/api-reference/cli/version)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
