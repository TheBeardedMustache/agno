Navigation and pages - Streamlit Docs

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

      *remove*

      * [st.navigation](/develop/api-reference/navigation/st.navigation)
      * [st.Page](/develop/api-reference/navigation/st.page)
      * [st.page\_link*link*](/develop/api-reference/widgets/st.page_link)
      * [st.switch\_page](/develop/api-reference/navigation/st.switch_page)
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
* [Navigation and pages](/develop/api-reference/navigation)

Navigation and pages
====================

[![screenshot](/images/api/navigation.jpg)

#### Navigation

Configure the available pages in a multipage app.

`st.navigation({
"Your account" : [log_out, settings],
"Reports" : [overview, usage],
"Tools" : [search]
})`](/develop/api-reference/navigation/st.navigation)[![screenshot](/images/api/page.jpg)

#### Page

Define a page in a multipage app.

`home = st.Page(
"home.py",
title="Home",
icon=":material/home:"
)`](/develop/api-reference/navigation/st.page)[![screenshot](/images/api/page_link.jpg)

#### Page link

Display a link to another page in a multipage app.

`st.page_link("app.py", label="Home", icon="🏠")
st.page_link("pages/profile.py", label="Profile")`](/develop/api-reference/widgets/st.page_link)[#### Switch page

Programmatically navigates to a specified page.

`st.switch_page("pages/my_page.py")`](/develop/api-reference/navigation/st.switch_page)

[Previous: Authentication and user info](/develop/api-reference/user)[Next: st.navigation](/develop/api-reference/navigation/st.navigation)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
