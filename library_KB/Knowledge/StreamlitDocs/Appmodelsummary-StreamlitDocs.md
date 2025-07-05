App model summary - Streamlit Docs

[![](/logo.svg)

#### Documentation](/)

*search*

Search

* [*rocket\_launch*

  Get started](/get-started)
  + [Installation](/get-started/installation)

    *add*
  + [Fundamentals](/get-started/fundamentals)

    *remove*

    - [Basic concepts](/get-started/fundamentals/main-concepts)
    - [Advanced concepts](/get-started/fundamentals/advanced-concepts)
    - [Additional features](/get-started/fundamentals/additional-features)
    - [Summary](/get-started/fundamentals/summary)
  + [First steps](/get-started/tutorials)

    *add*
* [*code*

  Develop](/develop)
  + [Concepts](/develop/concepts)

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
* [Get started](/get-started)/
* [Fundamentals](/get-started/fundamentals)/
* [Summary](/get-started/fundamentals/summary)

App model summary
=================

Now that you know a little more about all the individual pieces, let's close
the loop and review how it works together:

1. Streamlit apps are Python scripts that run from top to bottom.
2. Every time a user opens a browser tab pointing to your app, the script is executed and a new session starts.
3. As the script executes, Streamlit draws its output live in a browser.
4. Every time a user interacts with a widget, your script is re-executed and Streamlit redraws its output in the browser.
   * The output value of that widget matches the new value during that rerun.
5. Scripts use the Streamlit cache to avoid recomputing expensive functions, so updates happen very fast.
6. Session State lets you save information that persists between reruns when you need more than a simple widget.
7. Streamlit apps can contain multiple pages, which are defined in separate `.py` files in a `pages` folder.

![The Streamlit app model](/images/app_model.png)

[Previous: Additional features](/get-started/fundamentals/additional-features)[Next: First steps](/get-started/tutorials)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
