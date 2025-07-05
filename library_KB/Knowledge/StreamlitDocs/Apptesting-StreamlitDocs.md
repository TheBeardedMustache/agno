﻿App testing - Streamlit Docs

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

      *add*
    - TOOLS

      ---
    - [App testing](/develop/api-reference/app-testing)

      *remove*

      * [st.testing.v1.AppTest](/develop/api-reference/app-testing/st.testing.v1.apptest)
      * [Testing element classes](/develop/api-reference/app-testing/testing-element-classes)
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
* [App testing](/develop/api-reference/app-testing)

App testing
===========

Streamlit app testing framework enables developers to build and run headless tests that execute their app code directly, simulate user input, and inspect rendered outputs for correctness.

The provided class, AppTest, simulates a running app and provides methods to set up, manipulate, and inspect the app contents via API instead of a browser UI. It can be used to write automated tests of an app in various scenarios. These can then be run using a tool like pytest. A typical pattern is to build a suite of tests for an app that ensure consistent functionality as the app evolves, and run the tests locally and/or in a CI environment like Github Actions.

The AppTest class
-----------------

[### st.testing.v1.AppTest

`st.testing.v1.AppTest` simulates a running Streamlit app for testing.

`from streamlit.testing.v1 import AppTest
at = AppTest.from_file("streamlit_app.py")
at.secrets["WORD"] = "Foobar"
at.run()
assert not at.exception
at.text_input("word").input("Bazbat").run()
assert at.warning[0].value == "Try again."`](/develop/api-reference/app-testing/st.testing.v1.apptest)[### AppTest.from\_file

`st.testing.v1.AppTest.from_file` initializes a simulated app from a file.

`from streamlit.testing.v1 import AppTest
at = AppTest.from_file("streamlit_app.py")
at.secrets["WORD"] = "Foobar"
at.run()
assert not at.exception`](/develop/api-reference/app-testing/st.testing.v1.apptest#apptestfrom_file)[### AppTest.from\_string

`st.testing.v1.AppTest.from_string` initializes a simulated app from a string.

`from streamlit.testing.v1 import AppTest
app_script = """
import streamlit as st
word_of_the_day = st.text_input("What's the word of the day?", key="word")
if word_of_the_day == st.secrets["WORD"]:
st.success("That's right!")
elif word_of_the_day and word_of_the_day != st.secrets["WORD"]:
st.warn("Try again.")
"""
at = AppTest.from_string(app_script)
at.secrets["WORD"] = "Foobar"
at.run()
assert not at.exception`](/develop/api-reference/app-testing/st.testing.v1.apptest#apptestfrom_string)[### AppTest.from\_function

`st.testing.v1.AppTest.from_function` initializes a simulated app from a function.

`from streamlit.testing.v1 import AppTest
def app_script ():
import streamlit as st
word_of_the_day = st.text_input("What's the word of the day?", key="word")
if word_of_the_day == st.secrets["WORD"]:
st.success("That's right!")
elif word_of_the_day and word_of_the_day != st.secrets["WORD"]:
st.warn("Try again.")
at = AppTest.from_function(app_script)
at.secrets["WORD"] = "Foobar"
at.run()
assert not at.exception`](/develop/api-reference/app-testing/st.testing.v1.apptest#apptestfrom_function)

Testing-element classes
-----------------------

[#### Block

A representation of container elements, including:

* `st.chat_message`
* `st.columns`
* `st.sidebar`
* `st.tabs`
* The main body of the app.

`# at.sidebar returns a Block
at.sidebar.button[0].click().run()
assert not at.exception`](/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treeblock)[#### Element

The base class for representation of all elements, including:

* `st.title`
* `st.header`
* `st.markdown`
* `st.dataframe`

`# at.title returns a sequence of Title
# Title inherits from Element
assert at.title[0].value == "My awesome app"`](/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treeelement)[#### Button

A representation of `st.button` and `st.form_submit_button`.

`at.button[0].click().run()`](/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treebutton)[#### ChatInput

A representation of `st.chat_input`.

`at.chat_input[0].set_value("What is Streamlit?").run()`](/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treechatinput)[#### Checkbox

A representation of `st.checkbox`.

`at.checkbox[0].check().run()`](/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treecheckbox)[#### ColorPicker

A representation of `st.color_picker`.

`at.color_picker[0].pick("#FF4B4B").run()`](/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treecolorpicker)[#### DateInput

A representation of `st.date_input`.

`release_date = datetime.date(2023, 10, 26)
at.date_input[0].set_value(release_date).run()`](/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treedateinput)[#### Multiselect

A representation of `st.multiselect`.

`at.multiselect[0].select("New York").run()`](/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treemultiselect)[#### NumberInput

A representation of `st.number_input`.

`at.number_input[0].increment().run()`](/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treenumberinput)[#### Radio

A representation of `st.radio`.

`at.radio[0].set_value("New York").run()`](/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treeradio)[#### SelectSlider

A representation of `st.select_slider`.

`at.select_slider[0].set_range("A","C").run()`](/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treeselectslider)[#### Selectbox

A representation of `st.selectbox`.

`at.selectbox[0].select("New York").run()`](/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treeselectbox)[#### Slider

A representation of `st.slider`.

`at.slider[0].set_range(2,5).run()`](/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treeslider)[#### TextArea

A representation of `st.text_area`.

`at.text_area[0].input("Streamlit is awesome!").run()`](/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treetextarea)[#### TextInput

A representation of `st.text_input`.

`at.text_input[0].input("Streamlit").run()`](/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treetextinput)[#### TimeInput

A representation of `st.time_input`.

`at.time_input[0].increment().run()`](/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treetimeinput)[#### Toggle

A representation of `st.toggle`.

`at.toggle[0].set_value("True").run()`](/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treetoggle)

[Previous: Configuration](/develop/api-reference/configuration)[Next: st.testing.v1.AppTest](/develop/api-reference/app-testing/st.testing.v1.apptest)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
