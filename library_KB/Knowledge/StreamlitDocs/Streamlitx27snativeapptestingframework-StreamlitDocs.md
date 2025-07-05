Streamlit's native app testing framework - Streamlit Docs

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

      *add*
    - [Configuration and theming](/develop/concepts/configuration)

      *add*
    - [App testing](/develop/concepts/app-testing)

      *remove*

      * [Get started](/develop/concepts/app-testing/get-started)
      * [Beyond the basics](/develop/concepts/app-testing/beyond-the-basics)
      * [Automate your tests](/develop/concepts/app-testing/automate-tests)
      * [Example](/develop/concepts/app-testing/examples)
      * [Cheat sheet](/develop/concepts/app-testing/cheat-sheet)
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
* [App testing](/develop/concepts/app-testing)

Streamlit's native app testing framework
========================================

Streamlit app testing enables developers to build and run automated tests. Bring your favorite test automation software and enjoy simple syntax to simulate user input and inspect rendered output.

The provided class, AppTest, simulates a running app and provides methods to set up, manipulate, and inspect the app contents via API instead of a browser UI. AppTest provides similar functionality to browser automation tools like Selenium or Playwright, but with less overhead to write and execute tests. Use our testing framework with a tool like [pytest](https://docs.pytest.org/) to execute or automate your tests. A typical pattern is to build a suite of tests for an app to ensure consistent functionality as the app evolves. The tests run locally and/or in a CI environment like GitHub Actions.

[*science*](/develop/concepts/app-testing/get-started)

[Get started](/develop/concepts/app-testing/get-started) introduces you to the app testing framework and how to execute tests using `pytest`. Learn how to initialize and run simulated apps, including how to retrieve, manipulate, and inspect app elements.

[*password*](/develop/concepts/app-testing/beyond-the-basics)

[Beyond the basics](/develop/concepts/app-testing/beyond-the-basics) explains how to work with secrets and Session State within app tests, including how to test multipage apps.

[*play\_circle*](/develop/concepts/app-testing/automate-tests)

[Automate your tests](/develop/concepts/app-testing/automate-tests) with Continuous Integration (CI) to validate app changes over time.

[*quiz*](/develop/concepts/app-testing/examples)

[Example](/develop/concepts/app-testing/examples) puts together the concepts explained above. Check out an app with multiple tests in place.

[*saved\_search*](/develop/concepts/app-testing/cheat-sheet)

[Cheat sheet](/develop/concepts/app-testing/cheat-sheet) is a compact reference summarizing the available syntax.

[Previous: Configuration and theming](/develop/concepts/configuration)[Next: Get started](/develop/concepts/app-testing/get-started)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
