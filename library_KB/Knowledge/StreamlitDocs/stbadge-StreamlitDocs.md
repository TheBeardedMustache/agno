st.badge - Streamlit Docs

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

      *remove*

      * HEADINGS AND BODY

        ---
      * [st.title](/develop/api-reference/text/st.title)
      * [st.header](/develop/api-reference/text/st.header)
      * [st.subheader](/develop/api-reference/text/st.subheader)
      * [st.markdown](/develop/api-reference/text/st.markdown)
      * FORMATTED TEXT

        ---
      * [st.badge](/develop/api-reference/text/st.badge)
      * [st.caption](/develop/api-reference/text/st.caption)
      * [st.code](/develop/api-reference/text/st.code)
      * [st.divider](/develop/api-reference/text/st.divider)
      * [st.echo](/develop/api-reference/text/st.echo)
      * [st.latex](/develop/api-reference/text/st.latex)
      * [st.text](/develop/api-reference/text/st.text)
      * UTILITIES

        ---
      * [st.help](/develop/api-reference/text/st.help)
      * [st.html](/develop/api-reference/text/st.html)
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
* [Text elements](/develop/api-reference/text)/
* [st.badge](/develop/api-reference/text/st.badge)

st.badge
--------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Display a colored badge with an icon and label.

This is a thin wrapper around the color-badge Markdown directive.
The following are equivalent:

* st.markdown(":blue-badge[Home]")
* st.badge("Home", color="blue")

Note

You can insert badges everywhere Streamlit supports Markdown by
using the color-badge Markdown directive. See st.markdown for
more information.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/elements/markdown.py#L355 "View st.badge source code on GitHub") | |
| --- | --- |
| st.badge(label, \*, icon=None, color="blue", width="content") | |
| Parameters | |
| label (str) | The label to display in the badge. The label can optionally contain GitHub-flavored Markdown of the following types: Bold, Italics, Strikethroughs, Inline Code.  See the body parameter of [st.markdown](https://docs.streamlit.io/develop/api-reference/text/st.markdown) for additional, supported Markdown directives. Because this command escapes square brackets ([ ]) in this parameter, any directive requiring square brackets is not supported. |
| icon (str or None) | An optional emoji or icon to display next to the badge label. If icon is None (default), no icon is displayed. If icon is a string, the following options are valid:   * A single-character emoji. For example, you can set icon="🚨"   or icon="🔥". Emoji short codes are not supported. * An icon from the Material Symbols library (rounded style) in the   format ":material/icon\_name:" where "icon\_name" is the name   of the icon in snake case.  For example, icon=":material/thumb\_up:" will display the   Thumb Up icon. Find additional icons in the [Material Symbols](https://fonts.google.com/icons?icon.set=Material+Symbols&icon.style=Rounded)   font library. |
| color (str) | The color to use for the badge. This defaults to "blue".  This can be one of the following supported colors: blue, green, orange, red, violet, gray/grey, or primary. If you use "primary", Streamlit will use the default primary accent color unless you set the theme.primaryColor configuration option. |
| width ("content", "stretch", or int) | The width of the badge element. This can be one of the following:   * "content" (default): The width of the element matches the   width of its content, but doesn't exceed the width of the parent   container. * "stretch": The width of the element matches the width of the   parent container. * An integer specifying the width in pixels: The element has a   fixed width. If the specified width is greater than the width of   the parent container, the width of the element matches the width   of the parent container. |

#### Examples

Create standalone badges with st.badge (with or without icons). If
you want to have multiple, side-by-side badges, you can use the
Markdown directive in st.markdown.

```

import streamlit as st

st.badge("New")
st.badge("Success", icon=":material/check:", color="green")

st.markdown(
    ":violet-badge[:material/star: Favorite] :orange-badge[⚠️ Needs review] :gray-badge[Deprecated]"
)

```

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen *open\_in\_new*](https://doc-badge.streamlit.app//?utm_medium=oembed&)

[Previous: st.markdown](/develop/api-reference/text/st.markdown)[Next: st.caption](/develop/api-reference/text/st.caption)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
