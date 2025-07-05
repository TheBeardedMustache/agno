st.set\_page\_config - Streamlit Docs

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
* [st.set\_page\_config](/develop/api-reference/configuration/st.set_page_config)

st.set\_page\_config
--------------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Configure the default settings of the page.

This command can be called multiple times in a script run to dynamically
change the page configuration. The calls are additive, with each successive
call overriding only the parameters that are specified.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/commands/page_config.py#L109 "View st.set_page_config source code on GitHub") | |
| --- | --- |
| st.set\_page\_config(page\_title=None, page\_icon=None, layout=None, initial\_sidebar\_state=None, menu\_items=None) | |
| Parameters | |
| page\_title (str or None) | The page title, shown in the browser tab. If this is None (default), the page title is inherited from the previous call of st.set\_page\_config. If this is None and no previous call exists, the page title is inferred from the page source.  If a page source is a Python file, its inferred title is derived from the filename. If a page source is a callable object, its inferred title is derived from the callable's name. |
| page\_icon (Anything supported by st.image (except list), str, or None) | The page favicon. If page\_icon is None (default), the page icon is inherited from the previous call of st.set\_page\_config. If this is None and no previous call exists, the favicon is a monochrome Streamlit logo.  In addition to the types supported by [st.image](https://docs.streamlit.io/develop/api-reference/media/st.image) (except list), the following strings are valid:   * A single-character emoji. For example, you can set page\_icon="🦈". * An emoji short code. For example, you can set page\_icon=":shark:".   For a list of all supported codes, see   <https://share.streamlit.io/streamlit/emoji-shortcodes>. * The string literal, "random". You can set page\_icon="random"   to set a random emoji from the supported list above. * An icon from the Material Symbols library (rounded style) in the   format ":material/icon\_name:" where "icon\_name" is the name   of the icon in snake case.  For example, page\_icon=":material/thumb\_up:" will display the   Thumb Up icon. Find additional icons in the [Material Symbols](https://fonts.google.com/icons?icon.set=Material+Symbols&icon.style=Rounded)   font library.   Note  Colors are not supported for Material icons. When you use a Material icon for favicon, it will be black, regardless of browser theme. |
| layout ("centered", "wide", or None) | How the page content should be laid out. If this is None (default), the page layout is inherited from the previous call of st.set\_page\_config. If this is None and no previous call exists, the page layout is "centered".  "centered" constrains the elements into a centered column of fixed width. "wide" uses the entire screen. |
| initial\_sidebar\_state ("auto", "expanded", "collapsed", or None) | How the sidebar should start out. If this is None (default), the sidebar state is inherited from the previous call of st.set\_page\_config. If no previous call exists, the sidebar state is "auto".  The following states are supported:   * "auto": The sidebar is hidden on small devices and shown otherwise. * "expanded": The sidebar is shown initially. * "collapsed": The sidebar is hidden initially.   In most cases, "auto" provides the best user experience across devices of different sizes. |
| menu\_items (dict) | Configure the menu that appears on the top-right side of this app. The keys in this dict denote the menu item you'd like to configure:   * "Get help": str or None  The URL this menu item should point to.   If None, hides this menu item. * "Report a Bug": str or None  The URL this menu item should point to.   If None, hides this menu item. * "About": str or None  A markdown string to show in the About dialog.   If None, only shows Streamlit's default About text.   The URL may also refer to an email address e.g. mailto:john@example.com. To remove an item that was specified in a previous call to st.set\_page\_config, set its value to None in the dictionary. |

#### Example

```

import streamlit as st

st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

```

[Previous: st.set\_option](/develop/api-reference/configuration/st.set_option)[Next: App testing](/develop/api-reference/app-testing)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
