﻿config.toml - Streamlit Docs

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

      *remove*

      * [config.toml](/develop/api-reference/configuration/config.toml)
      * [st.get\_option](/develop/api-reference/configuration/st.get_option)
      * [st.set\_option](/develop/api-reference/configuration/st.set_option)
      * [st.set\_page\_config](/develop/api-reference/configuration/st.set_page_config)
    - TOOLS

      ---
    - [App testing](/develop/api-reference/app-testing)

      *add*
    - [Command line](/develop/api-reference/cli)

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
* [API reference](/develop/api-reference)/
* [Configuration](/develop/api-reference/configuration)/
* [config.toml](/develop/api-reference/configuration/config.toml)

config.toml
-----------

`config.toml` is an optional file you can define for your working directory or global development environment. When `config.toml` is defined both globally and in your working directory, Streamlit combines the configuration options and gives precedence to the working-directory configuration. Additionally, you can use environment variables and command-line options to override additional configuration options. For more information, see [Configuration options](/develop/concepts/configuration/options).

### File location

To define your configuration locally or per-project, add `.streamlit/config.toml` to your working directory. Your working directory is wherever you call `streamlit run`. If you haven't previously created the `.streamlit` directory, you will need to add it.

To define your configuration globally, you must first locate your global `.streamlit` directory. Streamlit adds this hidden directory to your OS user profile during installation. For MacOS/Linux, this will be `~/.streamlit/config.toml`. For Windows, this will be `%userprofile%/.streamlit/config.toml`.

### File format

`config.toml` is a [TOML](https://toml.io/en/) file.

#### Example

`[client]
showErrorDetails = "none"
[theme]
primaryColor = "#F63366"
backgroundColor = "black"`

### Available configuration options

Below are all the sections and options you can have in your `.streamlit/config.toml` file. To see all configurations, use the following command in your terminal or CLI:

`streamlit config show`

#### Global

`[global]
# By default, Streamlit displays a warning when a user sets both a widget
# default value in the function defining the widget and a widget value via
# the widget's key in `st.session_state`.
# If you'd like to turn off this warning, set this to True.
# Default: false
disableWidgetStateDuplicationWarning = false
# If True, will show a warning when you run a Streamlit-enabled script
# via "python my_script.py".
# Default: true
showWarningOnDirectExecution = true`

#### Logger

`[logger]
# Level of logging for Streamlit's internal logger: "error", "warning",
# "info", or "debug".
# Default: "info"
level = "info"
# String format for logging messages. If logger.datetimeFormat is set,
# logger messages will default to `%(asctime)s.%(msecs)03d %(message)s`.
# See Python's documentation for available attributes:
# https://docs.python.org/3/library/logging.html#formatter-objects
# Default: "%(asctime)s %(message)s"
messageFormat = "%(asctime)s %(message)s"`

#### Client

`[client]
# Controls whether uncaught app exceptions and deprecation warnings
# are displayed in the browser. This can be one of the following:
# - "full" : In the browser, Streamlit displays app deprecation
# warnings and exceptions, including exception types,
# exception messages, and associated tracebacks.
# - "stacktrace" : In the browser, Streamlit displays exceptions,
# including exception types, generic exception messages,
# and associated tracebacks. Deprecation warnings and
# full exception messages will only print to the
# console.
# - "type" : In the browser, Streamlit displays exception types and
# generic exception messages. Deprecation warnings, full
# exception messages, and associated tracebacks only
# print to the console.
# - "none" : In the browser, Streamlit displays generic exception
# messages. Deprecation warnings, full exception
# messages, associated tracebacks, and exception types
# will only print to the console.
# - True : This is deprecated. Streamlit displays "full"
# error details.
# - False : This is deprecated. Streamlit displays "stacktrace"
# error details.
# Default: "full"
showErrorDetails = "full"
# Change the visibility of items in the toolbar, options menu,
# and settings dialog (top right of the app).
# Allowed values:
# - "auto" : Show the developer options if the app is accessed through
# localhost or through Streamlit Community Cloud as a developer.
# Hide them otherwise.
# - "developer" : Show the developer options.
# - "viewer" : Hide the developer options.
# - "minimal" : Show only options set externally (e.g. through
# Streamlit Community Cloud) or through st.set_page_config.
# If there are no options left, hide the menu.
# Default: "auto"
toolbarMode = "auto"
# Controls whether to display the default sidebar page navigation in a
# multi-page app. This only applies when app's pages are defined by the
# `pages/` directory.
# Default: true
showSidebarNavigation = true`

#### Runner

`[runner]
# Allows you to type a variable or string by itself in a single line of
# Python code to write it to the app.
# Default: true
magicEnabled = true
# Handle script rerun requests immediately, rather than waiting for
# script execution to reach a yield point.
# This makes Streamlit much more responsive to user interaction, but it
# can lead to race conditions in apps that mutate session_state data
# outside of explicit session_state assignment statements.
# Default: true
fastReruns = true
# Raise an exception after adding unserializable data to Session State.
# Some execution environments may require serializing all data in Session
# State, so it may be useful to detect incompatibility during development,
# or when the execution environment will stop supporting it in the future.
# Default: false
enforceSerializableSessionState = false
# Adjust how certain 'options' widgets like radio, selectbox, and
# multiselect coerce Enum members.
# This is useful when the Enum class gets re-defined during a script
# re-run. For more information, check out the docs:
# https://docs.streamlit.io/develop/concepts/design/custom-classes#enums
# Allowed values:
# - "off" : Disables Enum coercion.
# - "nameOnly" : Enum classes can be coerced if their member names match.
# - "nameAndValue" : Enum classes can be coerced if their member names AND
# member values match.
# Default: "nameOnly"
enumCoercion = "nameOnly"`

#### Server

`[server]
# List of directories to watch for changes.
# By default, Streamlit watches files in the current working directory
# and its subdirectories. Use this option to specify additional
# directories to watch. Paths must be absolute.
# Default: []
folderWatchList = []
# List of directories to ignore for changes.
# By default, Streamlit watches files in the current working directory
# and its subdirectories. Use this option to specify exceptions within
# watched directories. Paths can be absolute or relative to the current
# working directory.
# Example: ['/home/user1/env', 'relative/path/to/folder']
# Default: []
folderWatchBlacklist = []
# Change the type of file watcher used by Streamlit, or turn it off
# completely.
# Allowed values:
# - "auto" : Streamlit will attempt to use the watchdog module, and
# falls back to polling if watchdog is not available.
# - "watchdog" : Force Streamlit to use the watchdog module.
# - "poll" : Force Streamlit to always use polling.
# - "none" : Streamlit will not watch files.
# Default: "auto"
fileWatcherType = "auto"
# Symmetric key used to produce signed cookies. If deploying on multiple
# replicas, this should be set to the same value across all replicas to ensure
# they all share the same secret.
# Default: randomly generated secret key.
cookieSecret = "a-random-key-appears-here"
# If false, will attempt to open a browser window on start.
# Default: false unless (1) we are on a Linux box where DISPLAY is unset, or
# (2) we are running in the Streamlit Atom plugin.
headless = false
# Automatically rerun script when the file is modified on disk.
# Default: false
runOnSave = false
# The address where the server will listen for client and browser
# connections.
# Use this if you want to bind the server to a specific address.
# If set, the server will only be accessible from this address, and not from
# any aliases (like localhost).
# Default: (unset)
address =
# The port where the server will listen for browser connections.
# Default: 8501
port = 8501
# The base path for the URL where Streamlit should be served from.
# Default: ""
baseUrlPath = ""
# Enables support for Cross-Origin Resource Sharing (CORS) protection,
# for added security.
# If XSRF protection is enabled and CORS protection is disabled at the
# same time, Streamlit will enable them both instead.
# Default: true
enableCORS = true
# Allowed list of origins.
# If CORS protection is enabled (`server.enableCORS=True`), use this
# option to set a list of allowed origins that the Streamlit server will
# accept traffic from.
# This config option does nothing if CORS protection is disabled.
# Example: ['http://example.com', 'https://streamlit.io']
# Default: []
corsAllowedOrigins = []
# Enables support for Cross-Site Request Forgery (XSRF) protection, for
# added security.
# If XSRF protection is enabled and CORS protection is disabled at the
# same time, Streamlit will enable them both instead.
# Default: true
enableXsrfProtection = true
# Max size, in megabytes, for files uploaded with the file_uploader.
# Default: 200
maxUploadSize = 200
# Max size, in megabytes, of messages that can be sent via the WebSocket
# connection.
# Default: 200
maxMessageSize = 200
# Enables support for websocket compression.
# Default: false
enableWebsocketCompression = false
# Enable serving files from a `static` directory in the running app's
# directory.
# Default: false
enableStaticServing = false
# TTL in seconds for sessions whose websockets have been disconnected.
# The server may choose to clean up session state, uploaded files, etc
# for a given session with no active websocket connection at any point
# after this time has passed.
# Default: 120
disconnectedSessionTTL = 120
# Server certificate file for connecting via HTTPS.
# Must be set at the same time as "server.sslKeyFile".
# ['DO NOT USE THIS OPTION IN A PRODUCTION ENVIRONMENT. It has not gone through
# security audits or performance tests. For the production environment, we
# recommend performing SSL termination by the load balancer or the reverse
# proxy.']
sslCertFile =
# Cryptographic key file for connecting via HTTPS.
# Must be set at the same time as "server.sslCertFile".
# ['DO NOT USE THIS OPTION IN A PRODUCTION ENVIRONMENT. It has not gone through
# security audits or performance tests. For the production environment, we
# recommend performing SSL termination by the load balancer or the reverse
# proxy.']
sslKeyFile =`

#### Browser

`[browser]
# Internet address where users should point their browsers in order to
# connect to the app. Can be IP address or DNS name and path.
# This is used to:
# - Set the correct URL for CORS and XSRF protection purposes.
# - Show the URL on the terminal
# - Open the browser
# Default: "localhost"
serverAddress = "localhost"
# Whether to send usage statistics to Streamlit.
# Default: true
gatherUsageStats = true
# Port where users should point their browsers in order to connect to the
# app.
# This is used to:
# - Set the correct URL for XSRF protection purposes.
# - Show the URL on the terminal (part of `streamlit run`).
# - Open the browser automatically (part of `streamlit run`).
# This option is for advanced use cases. To change the port of your app, use
# `server.Port` instead.
# Default: whatever value is set in server.port.
serverPort = 8501`

#### Mapbox

`[mapbox]
# If you'd like to show maps using Mapbox rather than Carto, use this
# to pass the Mapbox API token.
# THIS IS DEPRECATED.
# Instead of this, you should use either the MAPBOX_API_KEY environment
variable or PyDeck's `api_keys` argument.
# This option will be removed on or after 2026-05-01.
# Default: ""
token = ""`

#### Theme

`[theme]
# The preset Streamlit theme that your custom theme inherits from.
# This can be one of the following: "light" or "dark".
base =
# Primary accent color.
primaryColor =
# Background color of the app.
backgroundColor =
# Background color used for most interactive widgets.
secondaryBackgroundColor =
# Color used for almost all text.
textColor =
# Color used for all links.
linkColor =
# Background color used for code blocks.
codeBackgroundColor =
# The font family for all text, except code blocks.
# This can be one of the following:
# - "sans-serif"
# - "serif"
# - "monospace"
# - The `family` value for a custom font table under [[theme.fontFaces]]
# - A comma-separated list of these (as a single string) to specify
# fallbacks
# For example, you can use the following:
# font = "cool-font, fallback-cool-font, sans-serif"
font =
# The font family to use for code (monospace) in the sidebar.
# This can be one of the following:
# - "sans-serif"
# - "serif"
# - "monospace"
# - The `family` value for a custom font table under [[theme.fontFaces]]
# - A comma-separated list of these (as a single string) to specify
# fallbacks
codeFont =
# Sets the font size (in pixels or rem) for code blocks and code text.
# This applies to `st.code`, `st.json`, and `st.help`.
# It does not apply to inline code, which is set by default to 0.75em.
# When unset, the code font size will be 0.875rem.
codeFontSize =
# The font family to use for headings.
# This can be one of the following:
# - "sans-serif"
# - "serif"
# - "monospace"
# - The `family` value for a custom font table under [[theme.fontFaces]]
# - A comma-separated list of these (as a single string) to specify
# fallbacks
# If no heading font is set, Streamlit uses `theme.font` for headings.
headingFont =
# An array of fonts to use in your app.
# Each font in the array is a table (dictionary) that can have the
# following attributes, closely resembling CSS font-face definitions:
# - family
# - url
# - weight (optional)
# - style (optional)
# - unicodeRange (optional)
# To host a font with your app, enable static file serving with
# `server.enableStaticServing=true`.
# You can define multiple [[theme.fontFaces]] tables, including multiple
# tables with the same family if your font is defined by multiple files.
# For example, a font hosted with your app may have a [[theme.fontFaces]]
# table as follows:
# [[theme.fontFaces]]
# family = "font_name"
# url = "app/static/font_file.woff"
# weight = "400"
# style = "normal"
fontFaces =
# The radius used as basis for the corners of most UI elements.
# This can be one of the following:
# - "none"
# - "small"
# - "medium"
# - "large"
# - "full"
# - The number in pixels or rem.
# For example, you can use "10px", "0.5rem", or "2rem". To follow best
# practices, use rem instead of pixels when specifying a numeric size.
baseRadius =
# The radius used as basis for the corners of buttons.
# This can be one of the following:
# - "none"
# - "small"
# - "medium"
# - "large"
# - "full"
# - The number in pixels or rem.
# For example, you can use "10px", "0.5rem", or "2rem". To follow best
# practices, use rem instead of pixels when specifying a numeric size.
# If no button radius is set, Streamlit uses `theme.baseRadius` instead.
buttonRadius =
# The color of the border around elements.
borderColor =
# The color of the border around dataframes and tables.
# If no dataframe border color is set, Streamlit uses `theme.borderColor`
# instead.
dataframeBorderColor =
# Whether to show a border around input widgets.
showWidgetBorder =
# Sets the root font size (in pixels) for the app.
# This determines the overall scale of text and UI elements.
# When unset, the font size will be 16px.
baseFontSize =
# Whether to show a vertical separator between the sidebar and the main
# content area.
showSidebarBorder =`

#### Sidebar theme

`[theme.sidebar]
# Primary accent color.
primaryColor =
# Background color of the app.
backgroundColor =
# Background color used for most interactive widgets.
secondaryBackgroundColor =
# Color used for almost all text.
textColor =
# Color used for all links.
linkColor =
# Background color used for code blocks.
codeBackgroundColor =
# The font family for all text, except code blocks.
# This can be one of the following:
# - "sans-serif"
# - "serif"
# - "monospace"
# - The `family` value for a custom font table under [[theme.fontFaces]]
# - A comma-separated list of these (as a single string) to specify
# fallbacks
# For example, you can use the following:
# font = "cool-font, fallback-cool-font, sans-serif"
font =
# The font family to use for code (monospace) in the sidebar.
# This can be one of the following:
# - "sans-serif"
# - "serif"
# - "monospace"
# - The `family` value for a custom font table under [[theme.fontFaces]]
# - A comma-separated list of these (as a single string) to specify
# fallbacks
codeFont =
# Sets the font size (in pixels or rem) for code blocks and code text.
# This applies to `st.code`, `st.json`, and `st.help`.
# It does not apply to inline code, which is set by default to 0.75em.
# When unset, the code font size will be 0.875rem.
codeFontSize =
# The font family to use for headings.
# This can be one of the following:
# - "sans-serif"
# - "serif"
# - "monospace"
# - The `family` value for a custom font table under [[theme.fontFaces]]
# - A comma-separated list of these (as a single string) to specify
# fallbacks
# If no heading font is set, Streamlit uses `theme.font` for headings.
headingFont =
# The radius used as basis for the corners of most UI elements.
# This can be one of the following:
# - "none"
# - "small"
# - "medium"
# - "large"
# - "full"
# - The number in pixels or rem.
# For example, you can use "10px", "0.5rem", or "2rem". To follow best
# practices, use rem instead of pixels when specifying a numeric size.
baseRadius =
# The radius used as basis for the corners of buttons.
# This can be one of the following:
# - "none"
# - "small"
# - "medium"
# - "large"
# - "full"
# - The number in pixels or rem.
# For example, you can use "10px", "0.5rem", or "2rem". To follow best
# practices, use rem instead of pixels when specifying a numeric size.
# If no button radius is set, Streamlit uses `theme.baseRadius` instead.
buttonRadius =
# The color of the border around elements.
borderColor =
# The color of the border around dataframes and tables.
# If no dataframe border color is set, Streamlit uses `theme.borderColor`
# instead.
dataframeBorderColor =
# Whether to show a border around input widgets.
showWidgetBorder =`

#### Secrets

`[secrets]
# List of locations where secrets are searched.
# An entry can be a path to a TOML file or directory path where
# Kubernetes style secrets are saved. Order is important, import is
# first to last, so secrets in later files will take precedence over
# earlier ones.
# Default: [ <path to local environment's secrets.toml file>, <path to project's secrets.toml file>,]
files = [ "~/.streamlit/secrets.toml", "~/project directory/.streamlit/secrets.toml",]`

[Previous: Configuration](/develop/api-reference/configuration)[Next: st.get\_option](/develop/api-reference/configuration/st.get_option)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
