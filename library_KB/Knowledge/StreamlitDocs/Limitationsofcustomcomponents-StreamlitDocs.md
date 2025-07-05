Limitations of custom components - Streamlit Docs

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
* [Custom components](/develop/concepts/custom-components)/
* [Limitations](/develop/concepts/custom-components/limitations)

Limitations of custom components
================================

How do Streamlit Components differ from functionality provided in the base Streamlit package?
---------------------------------------------------------------------------------------------

* Streamlit Components are wrapped up in an iframe, which gives you the ability to do whatever you want (within the iframe) using any web technology you like.

What types of things aren't possible with Streamlit Components?
---------------------------------------------------------------

Because each Streamlit Component gets mounted into its own sandboxed iframe, this implies a few limitations on what is possible with Components:

* **Can't communicate with other Components**: Components can’t contain (or otherwise communicate with) other components, so Components cannot be used to build something like a grid layout.
* **Can't modify CSS**: A Component can’t modify the CSS that the rest of the Streamlit app uses, so you can't create something to put the app in dark mode, for example.
* **Can't add/remove elements**: A Component can’t add or remove other elements of a Streamlit app, so you couldn't make something to remove the app menu, for example.

My Component seems to be blinking/stuttering...how do I fix that?
-----------------------------------------------------------------

Currently, no automatic debouncing of Component updates is performed within Streamlit. The Component creator themselves can decide to rate-limit the updates they send back to Streamlit.

[Previous: Publish a Component](/develop/concepts/custom-components/publish)[Next: Component gallery](https://streamlit.io/components)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
