st.components.v1.html - Streamlit Docs

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

      *remove*

      * [st.components.v1​.declare\_component](/develop/api-reference/custom-components/st.components.v1.declare_component)
      * [st.components.v1.html](/develop/api-reference/custom-components/st.components.v1.html)
      * [st.components.v1.iframe](/develop/api-reference/custom-components/st.components.v1.iframe)
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
* [Custom components](/develop/api-reference/custom-components)/
* [st.components.v1.html](/develop/api-reference/custom-components/st.components.v1.html)

st.components.v1.html
---------------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Display an HTML string in an iframe.

To use this function, import it from the streamlit.components.v1
module.

If you want to insert HTML text into your app without an iframe, try
st.html instead.

Warning

Using st.components.v1.html directly (instead of importing
its module) is deprecated and will be disallowed in a later version.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/elements/iframe.py#L105 "View st.html source code on GitHub") | |
| --- | --- |
| st.components.v1.html(html, width=None, height=None, scrolling=False, \*, tab\_index=None) | |
| Parameters | |
| html (str) | The HTML string to embed in the iframe. |
| width (int) | The width of the iframe in CSS pixels. By default, this is the app's default element width. |
| height (int) | The height of the frame in CSS pixels. By default, this is 150. |
| scrolling (bool) | Whether to allow scrolling in the iframe. If this False (default), Streamlit crops any content larger than the iframe and does not show a scrollbar. If this is True, Streamlit shows a scrollbar when the content is larger than the iframe. |
| tab\_index (int or None) | Specifies how and if the iframe is sequentially focusable. Users typically use the Tab key for sequential focus navigation.  This can be one of the following values:   * None (default): Uses the browser's default behavior. * -1: Removes the iframe from sequential navigation, but still   allows it to be focused programmatically. * 0: Includes the iframe in sequential navigation in the order   it appears in the document but after all elements with a positive   tab\_index. * Positive integer: Includes the iframe in sequential navigation.   Elements are navigated in ascending order of their positive   tab\_index.   For more information, see the [tabindex](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/tabindex) documentation on MDN. |

#### Example

```

import streamlit.components.v1 as components

components.html(
    "<p><span style='text-decoration: line-through double red;'>Oops</span>!</p>"
)

```

[Previous: st.components.v1​.declare\_component](/develop/api-reference/custom-components/st.components.v1.declare_component)[Next: st.components.v1.iframe](/develop/api-reference/custom-components/st.components.v1.iframe)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
