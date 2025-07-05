Components - Streamlit Docs

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

      *remove*

      * [Intro to custom components](/develop/concepts/custom-components/intro)
      * [Create a Component](/develop/concepts/custom-components/create)
      * [Publish a Component](/develop/concepts/custom-components/publish)
      * [Limitations](/develop/concepts/custom-components/limitations)
      * [Component gallery*open\_in\_new*](https://streamlit.io/components)
    - [Configuration and theming](/develop/concepts/configuration)

      *add*
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
* [Custom components](/develop/concepts/custom-components)

Custom Components
=================

Components are third-party Python modules that extend what's possible with Streamlit.

How to use a Component
----------------------

Components are super easy to use:

1. Start by finding the Component you'd like to use. Two great resources for this are:

   * The [Component gallery](https://streamlit.io/components)
   * [This thread](https://discuss.streamlit.io/t/streamlit-components-community-tracker/4634),
     by Fanilo A. from our forums.
2. Install the Component using your favorite Python package manager. This step and all following
   steps are described in your component's instructions.

   For example, to use the fantastic [AgGrid
   Component](https://github.com/PablocFonseca/streamlit-aggrid), you first install it with:

   `pip install streamlit-aggrid`
3. In your Python code, import the Component as described in its instructions. For AgGrid, this step
   is:

   `from st_aggrid import AgGrid`
4. ...now you're ready to use it! For AgGrid, that's:

   `AgGrid(my_dataframe)`

Making your own Component
-------------------------

If you're interested in making your own component, check out the following resources:

* [Create a Component](/develop/concepts/custom-components/create)
* [Publish a Component](/develop/concepts/custom-components/publish)
* [Components API](/develop/concepts/custom-components/intro)
* [Blog post for when we launched Components!](https://blog.streamlit.io/introducing-streamlit-components/)

Alternatively, if you prefer to learn using videos, our engineer Tim Conkling has put together some
amazing tutorials:

##### Video tutorial, part 1

##### Video tutorial, part 2

[Previous: Connections, secrets, and authentication](/develop/concepts/connections)[Next: Intro to custom components](/develop/concepts/custom-components/intro)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
