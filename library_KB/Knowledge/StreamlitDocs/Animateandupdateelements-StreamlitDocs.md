Animate and update elements - Streamlit Docs

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
* [Animate and update elements](/develop/concepts/design/animate)

Animate and update elements
===========================

Sometimes you display a chart or dataframe and want to modify it live as the app
runs (for example, in a loop). Some elements have built-in methods to allow you
to update them in-place without rerunning the app.

Updatable elements include the following:

* `st.empty` containers can be written to in sequence and will always show the last thing written. They can also be cleared with an
  additional `.empty()` called like a method.
* `st.dataframe`, `st.table`, and many chart elements can be updated with the `.add_rows()` method which appends data.
* `st.progress` elements can be updated with additional `.progress()` calls. They can also be cleared with a `.empty()` method call.
* `st.status` containers have an `.update()` method to change their labels, expanded state, and status.
* `st.toast` messages can be updated in place with additional `.toast()` calls.

`st.empty` containers
---------------------

`st.empty` can hold a single element. When you write any element to an `st.empty` container, Streamlit discards its previous content
displays the new element. You can also `st.empty` containers by calling `.empty()` as a method. If you want to update a set of elements, use
a plain container (`st.container()`) inside `st.empty` and write contents to the plain container. Rewrite the plain container and its
contents as often as desired to update your app's display.

The `.add_rows()` method
------------------------

`st.dataframe`, `st.table`, and all chart functions can be mutated using the `.add_rows()` method on their output. In the following example, we use `my_data_element = st.line_chart(df)`. You can try the example with `st.table`, `st.dataframe`, and most of the other simple charts by just swapping out `st.line_chart`. Note that `st.dataframe` only shows the first ten rows by default and enables scrolling for additional rows. This means adding rows is not as visually apparent as it is with `st.table` or the chart elements.

`import streamlit as st
import pandas as pd
import numpy as np
import time
df = pd.DataFrame(np.random.randn(15, 3), columns=(["A", "B", "C"]))
my_data_element = st.line_chart(df)
for tick in range(10):
time.sleep(.5)
add_df = pd.DataFrame(np.random.randn(1, 3), columns=(["A", "B", "C"]))
my_data_element.add_rows(add_df)
st.button("Regenerate")`

[Previous: App design](/develop/concepts/design)[Next: Button behavior and examples](/develop/concepts/design/buttons)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
