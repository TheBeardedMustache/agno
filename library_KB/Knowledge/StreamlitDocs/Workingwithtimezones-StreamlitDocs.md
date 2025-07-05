Working with timezones - Streamlit Docs

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

      *remove*

      * [Animate and update elements](/develop/concepts/design/animate)
      * [Button behavior and examples](/develop/concepts/design/buttons)
      * [Dataframes](/develop/concepts/design/dataframes)
      * [Multithreading](/develop/concepts/design/multithreading)
      * [Using custom classes](/develop/concepts/design/custom-classes)
      * [Working with timezones](/develop/concepts/design/timezone-handling)
    - ADDITIONAL

      ---
    - [Connections, secrets, and authentication](/develop/concepts/connections)

      *add*
    - [Custom components](/develop/concepts/custom-components)

      *add*
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
* [App design](/develop/concepts/design)/
* [Working with timezones](/develop/concepts/design/timezone-handling)

Working with timezones
======================

In general, working with timezones can be tricky. Your Streamlit app users are not necessarily in the same timezone as the server running your app. It is especially true of public apps, where anyone in the world (in any timezone) can access your app. As such, it is crucial to understand how Streamlit handles timezones, so you can avoid unexpected behavior when displaying `datetime` information.

How Streamlit handles timezones
-------------------------------

Streamlit always shows `datetime` information on the frontend with the same information as its corresponding `datetime` instance in the backend. I.e., date or time information does not automatically adjust to the users' timezone. We distinguish between the following two cases:

### **`datetime` instance without a timezone (naive)**

When you provide a `datetime` instance *without specifying a timezone*, the frontend shows the `datetime` instance without timezone information. For example (this also applies to other widgets like [`st.dataframe`](/develop/api-reference/data/st.dataframe)):

`import streamlit as st
from datetime import datetime
st.write(datetime(2020, 1, 10, 10, 30))
# Outputs: 2020-01-10 10:30:00`

Users of the above app always see the output as `2020-01-10 10:30:00`.

### **`datetime` instance with a timezone**

When you provide a `datetime` instance *and specify a timezone*, the frontend shows the `datetime` instance in that same timezone. For example (this also applies to other widgets like [`st.dataframe`](/develop/api-reference/data/st.dataframe)):

`import streamlit as st
from datetime import datetime
import pytz
st.write(datetime(2020, 1, 10, 10, 30, tzinfo=pytz.timezone("EST")))
# Outputs: 2020-01-10 10:30:00-05:00`

Users of the above app always see the output as `2020-01-10 10:30:00-05:00`.

In both cases, neither the date nor time information automatically adjusts to the users' timezone on the frontend. What users see is identical to the corresponding `datetime` instance in the backend. It is currently not possible to automatically adjust the date or time information to the timezone of the users viewing the app.

*push\_pin*

#### Note

The legacy version of the `st.dataframe` has issues with timezones. We do not plan to roll out additional fixes or enhancements for the legacy dataframe. If you need stable timezone support, please consider switching to the arrow serialization by changing the [config setting](/develop/concepts/configuration), *config.dataFrameSerialization = "arrow"*.

[Previous: Using custom classes](/develop/concepts/design/custom-classes)[Next: Connections, secrets, and authentication](/develop/concepts/connections)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
