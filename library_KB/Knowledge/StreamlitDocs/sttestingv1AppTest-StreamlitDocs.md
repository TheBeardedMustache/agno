st.testing.v1.AppTest - Streamlit Docs

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
* [App testing](/develop/api-reference/app-testing)/
* [st.testing.v1.AppTest](/develop/api-reference/app-testing/st.testing.v1.apptest)

The AppTest class
=================

st.testing.v1.AppTest
---------------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

A simulated Streamlit app to check the correctness of displayed elements and outputs.

An instance of AppTest simulates a running Streamlit app. This class
provides methods to set up, manipulate, and inspect the app contents via
API instead of a browser UI. It can be used to write automated tests of an
app in various scenarios. These can then be run using a tool like pytest.

AppTest can be initialized by one of three class methods:

* [st.testing.v1.AppTest.from\_file](#apptestfrom_file) (recommended)
* [st.testing.v1.AppTest.from\_string](#apptestfrom_string)
* [st.testing.v1.AppTest.from\_function](#apptestfrom_function)

Once initialized, Session State and widget values can be updated and the
script can be run. Unlike an actual live-running Streamlit app, you need to
call AppTest.run() explicitly to re-run the app after changing a widget
value. Switching pages also requires an explicit, follow-up call to
AppTest.run().

AppTest enables developers to build tests on their app as-is, in the
familiar python test format, without major refactoring or abstracting out
logic to be tested separately from the UI. Tests can run quickly with very
low overhead. A typical pattern is to build a suite of tests for an app
that ensure consistent functionality as the app evolves, and run the tests
locally and/or in a CI environment like Github Actions.

Note

AppTest only supports testing a single page of an app per
instance. For multipage apps, each page will need to be tested
separately. AppTest is not yet compatible with multipage apps
using st.navigation and st.Page.

| Class description[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/testing/v1/app_test.py#L98 "View st.AppTest source code on GitHub") | |
| --- | --- |
| st.testing.v1.AppTest(script\_path, \*, default\_timeout, args=None, kwargs=None) | |
|  |  |
| --- | --- |
| Methods | |
| [get](/develop/api-reference/app-testing/st.testing.v1.apptest#apptestget)(element\_type) | Get elements or widgets of the specified type. |
| [run](/develop/api-reference/app-testing/st.testing.v1.apptest#apptestrun)(\*, timeout=None) | Run the script from the current state. |
| [switch\_page](/develop/api-reference/app-testing/st.testing.v1.apptest#apptestswitch_page)(page\_path) | Switch to another page of the app. |
| Attributes | |
| secrets (dict[str, Any]) | Dictionary of secrets to be used the simulated app. Use dict-like syntax to set secret values for the simulated app. |
| session\_state (SafeSessionState) | Session State for the simulated app. SafeSessionState object supports read and write operations as usual for Streamlit apps. |
| query\_params (dict[str, Any]) | Dictionary of query parameters to be used by the simluated app. Use dict-like syntax to set query\_params values for the simulated app. |
| [button](/develop/api-reference/app-testing/st.testing.v1.apptest#apptestbutton) | Sequence of all st.button and st.form\_submit\_button widgets. |
| [button\_group](/develop/api-reference/app-testing/st.testing.v1.apptest#apptestbutton_group) | Sequence of all st.feedback widgets. |
| [caption](/develop/api-reference/app-testing/st.testing.v1.apptest#apptestcaption) | Sequence of all st.caption elements. |
| [chat\_input](/develop/api-reference/app-testing/st.testing.v1.apptest#apptestchat_input) | Sequence of all st.chat\_input widgets. |
| [chat\_message](/develop/api-reference/app-testing/st.testing.v1.apptest#apptestchat_message) | Sequence of all st.chat\_message elements. |
| [checkbox](/develop/api-reference/app-testing/st.testing.v1.apptest#apptestcheckbox) | Sequence of all st.checkbox widgets. |
| [code](/develop/api-reference/app-testing/st.testing.v1.apptest#apptestcode) | Sequence of all st.code elements. |
| [color\_picker](/develop/api-reference/app-testing/st.testing.v1.apptest#apptestcolor_picker) | Sequence of all st.color\_picker widgets. |
| [columns](/develop/api-reference/app-testing/st.testing.v1.apptest#apptestcolumns) | Sequence of all columns within st.columns elements. |
| [dataframe](/develop/api-reference/app-testing/st.testing.v1.apptest#apptestdataframe) | Sequence of all st.dataframe elements. |
| [date\_input](/develop/api-reference/app-testing/st.testing.v1.apptest#apptestdate_input) | Sequence of all st.date\_input widgets. |
| [divider](/develop/api-reference/app-testing/st.testing.v1.apptest#apptestdivider) | Sequence of all st.divider elements. |
| [error](/develop/api-reference/app-testing/st.testing.v1.apptest#apptesterror) | Sequence of all st.error elements. |
| [exception](/develop/api-reference/app-testing/st.testing.v1.apptest#apptestexception) | Sequence of all st.exception elements. |
| [expander](/develop/api-reference/app-testing/st.testing.v1.apptest#apptestexpander) | Sequence of all st.expander elements. |
| [header](/develop/api-reference/app-testing/st.testing.v1.apptest#apptestheader) | Sequence of all st.header elements. |
| [info](/develop/api-reference/app-testing/st.testing.v1.apptest#apptestinfo) | Sequence of all st.info elements. |
| [json](/develop/api-reference/app-testing/st.testing.v1.apptest#apptestjson) | Sequence of all st.json elements. |
| [latex](/develop/api-reference/app-testing/st.testing.v1.apptest#apptestlatex) | Sequence of all st.latex elements. |
| [main](/develop/api-reference/app-testing/st.testing.v1.apptest#apptestmain) | Sequence of elements within the main body of the app. |
| [markdown](/develop/api-reference/app-testing/st.testing.v1.apptest#apptestmarkdown) | Sequence of all st.markdown elements. |
| [metric](/develop/api-reference/app-testing/st.testing.v1.apptest#apptestmetric) | Sequence of all st.metric elements. |
| [multiselect](/develop/api-reference/app-testing/st.testing.v1.apptest#apptestmultiselect) | Sequence of all st.multiselect widgets. |
| [number\_input](/develop/api-reference/app-testing/st.testing.v1.apptest#apptestnumber_input) | Sequence of all st.number\_input widgets. |
| [radio](/develop/api-reference/app-testing/st.testing.v1.apptest#apptestradio) | Sequence of all st.radio widgets. |
| [select\_slider](/develop/api-reference/app-testing/st.testing.v1.apptest#apptestselect_slider) | Sequence of all st.select\_slider widgets. |
| [selectbox](/develop/api-reference/app-testing/st.testing.v1.apptest#apptestselectbox) | Sequence of all st.selectbox widgets. |
| [sidebar](/develop/api-reference/app-testing/st.testing.v1.apptest#apptestsidebar) | Sequence of all elements within st.sidebar. |
| [slider](/develop/api-reference/app-testing/st.testing.v1.apptest#apptestslider) | Sequence of all st.slider widgets. |
| [status](/develop/api-reference/app-testing/st.testing.v1.apptest#appteststatus) | Sequence of all st.status elements. |
| [subheader](/develop/api-reference/app-testing/st.testing.v1.apptest#apptestsubheader) | Sequence of all st.subheader elements. |
| [success](/develop/api-reference/app-testing/st.testing.v1.apptest#apptestsuccess) | Sequence of all st.success elements. |
| [table](/develop/api-reference/app-testing/st.testing.v1.apptest#apptesttable) | Sequence of all st.table elements. |
| [tabs](/develop/api-reference/app-testing/st.testing.v1.apptest#apptesttabs) | Sequence of all tabs within st.tabs elements. |
| [text](/develop/api-reference/app-testing/st.testing.v1.apptest#apptesttext) | Sequence of all st.text elements. |
| [text\_area](/develop/api-reference/app-testing/st.testing.v1.apptest#apptesttext_area) | Sequence of all st.text\_area widgets. |
| [text\_input](/develop/api-reference/app-testing/st.testing.v1.apptest#apptesttext_input) | Sequence of all st.text\_input widgets. |
| [time\_input](/develop/api-reference/app-testing/st.testing.v1.apptest#apptesttime_input) | Sequence of all st.time\_input widgets. |
| [title](/develop/api-reference/app-testing/st.testing.v1.apptest#apptesttitle) | Sequence of all st.title elements. |
| [toast](/develop/api-reference/app-testing/st.testing.v1.apptest#apptesttoast) | Sequence of all st.toast elements. |
| [toggle](/develop/api-reference/app-testing/st.testing.v1.apptest#apptesttoggle) | Sequence of all st.toggle widgets. |
| [warning](/develop/api-reference/app-testing/st.testing.v1.apptest#apptestwarning) | Sequence of all st.warning elements. |

Initialize a simulated app using AppTest
========================================

AppTest.from\_file
------------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Create an instance of AppTest to simulate an app page defined within a file.

This option is most convenient for CI workflows and testing of
published apps. The script must be executable on its own and so must
contain all necessary imports.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/testing/v1/app_test.py#L272 "View st.from_file source code on GitHub") | |
| --- | --- |
| AppTest.from\_file(cls, script\_path, \*, default\_timeout=3) | |
| Parameters | |
| script\_path (str | Path) | Path to a script file. The path should be absolute or relative to the file calling .from\_file. |
| default\_timeout (float) | Default time in seconds before a script run is timed out. Can be overridden for individual .run() calls. |
|  |  |
| --- | --- |
| Returns | |
| (AppTest) | A simulated Streamlit app for testing. The simulated app can be executed via .run(). |

AppTest.from\_string
--------------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Create an instance of AppTest to simulate an app page defined within a string.

This is useful for testing short scripts that fit comfortably as an
inline string in the test itself, without having to create a separate
file for it. The script must be executable on its own and so must
contain all necessary imports.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/testing/v1/app_test.py#L178 "View st.from_string source code on GitHub") | |
| --- | --- |
| AppTest.from\_string(cls, script, \*, default\_timeout=3) | |
| Parameters | |
| script (str) | The string contents of the script to be run. |
| default\_timeout (float) | Default time in seconds before a script run is timed out. Can be overridden for individual .run() calls. |
|  |  |
| --- | --- |
| Returns | |
| (AppTest) | A simulated Streamlit app for testing. The simulated app can be executed via .run(). |

AppTest.from\_function
----------------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Create an instance of AppTest to simulate an app page defined within a function.

This is similar to AppTest.from\_string(), but more convenient to
write with IDE assistance. The script must be executable on its own and
so must contain all necessary imports.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/testing/v1/app_test.py#L225 "View st.from_function source code on GitHub") | |
| --- | --- |
| AppTest.from\_function(cls, script, \*, default\_timeout=3, args=None, kwargs=None) | |
| Parameters | |
| script (Callable) | A function whose body will be used as a script. Must be runnable in isolation, so it must include any necessary imports. |
| default\_timeout (float) | Default time in seconds before a script run is timed out. Can be overridden for individual .run() calls. |
| args (tuple) | An optional tuple of args to pass to the script function. |
| kwargs (dict) | An optional dict of kwargs to pass to the script function. |
|  |  |
| --- | --- |
| Returns | |
| (AppTest) | A simulated Streamlit app for testing. The simulated app can be executed via .run(). |

Run an AppTest script
=====================

AppTest.run
-----------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Run the script from the current state.

This is equivalent to manually rerunning the app or the rerun that
occurs upon user interaction. AppTest.run() must be manually called
after updating a widget value or switching pages as script reruns do
not occur automatically as they do for live-running Streamlit apps.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/testing/v1/app_test.py#L372 "View st.run source code on GitHub") | |
| --- | --- |
| AppTest.run(\*, timeout=None) | |
| Parameters | |
| timeout (float or None) | The maximum number of seconds to run the script. If timeout is None (default), Streamlit uses the default timeout set for the instance of AppTest. |
|  |  |
| --- | --- |
| Returns | |
| (AppTest) | self |

AppTest.switch\_page
--------------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Switch to another page of the app.

This method does not automatically rerun the app. Use a follow-up call
to AppTest.run() to obtain the elements on the selected page.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/testing/v1/app_test.py#L395 "View st.switch_page source code on GitHub") | |
| --- | --- |
| AppTest.switch\_page(page\_path) | |
| Parameters | |
| page\_path (str) | Path of the page to switch to. The path must be relative to the main script's location (e.g. "pages/my\_page.py"). |
|  |  |
| --- | --- |
| Returns | |
| (AppTest) | self |

Get AppTest script elements
===========================

The main value of `AppTest` is providing an API to programmatically inspect and interact with the elements and widgets produced by a running Streamlit app. Using the `AppTest.<element type>` properties or `AppTest.get()` method returns a collection of all the elements or widgets of the specified type that would have been displayed by running the app.

Note that you can also retrieve elements within a specific container in the same way - first retrieve the container, then retrieve the elements just in that container.

AppTest.get
-----------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Get elements or widgets of the specified type.

This method returns the collection of all elements or widgets of
the specified type on the current page. Retrieve a specific element by
using its index (order on page) or key lookup.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/testing/v1/app_test.py#L1029 "View st.get source code on GitHub") | |
| --- | --- |
| AppTest.get(element\_type) | |
| Parameters | |
| element\_type (str) | An element attribute of AppTest. For example, "button", "caption", or "chat\_input". |
|  |  |
| --- | --- |
| Returns | |
| (Sequence of Elements) | Sequence of elements of the given type. Individual elements can be accessed from a Sequence by index (order on the page). When getting and element\_type that is a widget, individual widgets can be accessed by key. For example, at.get("text")[0] for the first st.text element or at.get("slider")(key="my\_key") for the st.slider widget with a given key. |

AppTest.button
--------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Sequence of all st.button and st.form\_submit\_button widgets.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/testing/v1/app_test.py#L450 "View st.button source code on GitHub") | |
| --- | --- |
| AppTest.button | |
|  |  |
| --- | --- |
| Returns | |
| (WidgetList of Button) | Sequence of all st.button and st.form\_submit\_button widgets. Individual widgets can be accessed from a WidgetList by index (order on the page) or key. For example, at.button[0] for the first widget or at.button(key="my\_key") for a widget with a given key. |

AppTest.caption
---------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Sequence of all st.caption elements.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/testing/v1/app_test.py#L479 "View st.caption source code on GitHub") | |
| --- | --- |
| AppTest.caption | |
|  |  |
| --- | --- |
| Returns | |
| (ElementList of Caption) | Sequence of all st.caption elements. Individual elements can be accessed from an ElementList by index (order on the page). For example, at.caption[0] for the first element. Caption is an extension of the Element class. |

AppTest.chat\_input
-------------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Sequence of all st.chat\_input widgets.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/testing/v1/app_test.py#L493 "View st.chat_input source code on GitHub") | |
| --- | --- |
| AppTest.chat\_input | |
|  |  |
| --- | --- |
| Returns | |
| (WidgetList of ChatInput) | Sequence of all st.chat\_input widgets. Individual widgets can be accessed from a WidgetList by index (order on the page) or key. For example, at.chat\_input[0] for the first widget or at.chat\_input(key="my\_key") for a widget with a given key. |

AppTest.chat\_message
---------------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Sequence of all st.chat\_message elements.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/testing/v1/app_test.py#L507 "View st.chat_message source code on GitHub") | |
| --- | --- |
| AppTest.chat\_message | |
|  |  |
| --- | --- |
| Returns | |
| (Sequence of ChatMessage) | Sequence of all st.chat\_message elements. Individual elements can be accessed from an ElementList by index (order on the page). For example, at.chat\_message[0] for the first element. ChatMessage is an extension of the Block class. |

AppTest.checkbox
----------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Sequence of all st.checkbox widgets.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/testing/v1/app_test.py#L521 "View st.checkbox source code on GitHub") | |
| --- | --- |
| AppTest.checkbox | |
|  |  |
| --- | --- |
| Returns | |
| (WidgetList of Checkbox) | Sequence of all st.checkbox widgets. Individual widgets can be accessed from a WidgetList by index (order on the page) or key. For example, at.checkbox[0] for the first widget or at.checkbox(key="my\_key") for a widget with a given key. |

AppTest.code
------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Sequence of all st.code elements.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/testing/v1/app_test.py#L535 "View st.code source code on GitHub") | |
| --- | --- |
| AppTest.code | |
|  |  |
| --- | --- |
| Returns | |
| (ElementList of Code) | Sequence of all st.code elements. Individual elements can be accessed from an ElementList by index (order on the page). For example, at.code[0] for the first element. Code is an extension of the Element class. |

AppTest.color\_picker
---------------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Sequence of all st.color\_picker widgets.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/testing/v1/app_test.py#L549 "View st.color_picker source code on GitHub") | |
| --- | --- |
| AppTest.color\_picker | |
|  |  |
| --- | --- |
| Returns | |
| (WidgetList of ColorPicker) | Sequence of all st.color\_picker widgets. Individual widgets can be accessed from a WidgetList by index (order on the page) or key. For example, at.color\_picker[0] for the first widget or at.color\_picker(key="my\_key") for a widget with a given key. |

AppTest.columns
---------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Sequence of all columns within st.columns elements.

Each column within a single st.columns will be returned as a
separate Column in the Sequence.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/testing/v1/app_test.py#L563 "View st.columns source code on GitHub") | |
| --- | --- |
| AppTest.columns | |
|  |  |
| --- | --- |
| Returns | |
| (Sequence of Column) | Sequence of all columns within st.columns elements. Individual columns can be accessed from an ElementList by index (order on the page). For example, at.columns[0] for the first column. Column is an extension of the Block class. |

AppTest.dataframe
-----------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Sequence of all st.dataframe elements.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/testing/v1/app_test.py#L580 "View st.dataframe source code on GitHub") | |
| --- | --- |
| AppTest.dataframe | |
|  |  |
| --- | --- |
| Returns | |
| (ElementList of Dataframe) | Sequence of all st.dataframe elements. Individual elements can be accessed from an ElementList by index (order on the page). For example, at.dataframe[0] for the first element. Dataframe is an extension of the Element class. |

AppTest.date\_input
-------------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Sequence of all st.date\_input widgets.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/testing/v1/app_test.py#L594 "View st.date_input source code on GitHub") | |
| --- | --- |
| AppTest.date\_input | |
|  |  |
| --- | --- |
| Returns | |
| (WidgetList of DateInput) | Sequence of all st.date\_input widgets. Individual widgets can be accessed from a WidgetList by index (order on the page) or key. For example, at.date\_input[0] for the first widget or at.date\_input(key="my\_key") for a widget with a given key. |

AppTest.divider
---------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Sequence of all st.divider elements.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/testing/v1/app_test.py#L608 "View st.divider source code on GitHub") | |
| --- | --- |
| AppTest.divider | |
|  |  |
| --- | --- |
| Returns | |
| (ElementList of Divider) | Sequence of all st.divider elements. Individual elements can be accessed from an ElementList by index (order on the page). For example, at.divider[0] for the first element. Divider is an extension of the Element class. |

AppTest.error
-------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Sequence of all st.error elements.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/testing/v1/app_test.py#L622 "View st.error source code on GitHub") | |
| --- | --- |
| AppTest.error | |
|  |  |
| --- | --- |
| Returns | |
| (ElementList of Error) | Sequence of all st.error elements. Individual elements can be accessed from an ElementList by index (order on the page). For example, at.error[0] for the first element. Error is an extension of the Element class. |

AppTest.exception
-----------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Sequence of all st.exception elements.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/testing/v1/app_test.py#L636 "View st.exception source code on GitHub") | |
| --- | --- |
| AppTest.exception | |
|  |  |
| --- | --- |
| Returns | |
| (ElementList of Exception) | Sequence of all st.exception elements. Individual elements can be accessed from an ElementList by index (order on the page). For example, at.exception[0] for the first element. Exception is an extension of the Element class. |

AppTest.expander
----------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Sequence of all st.expander elements.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/testing/v1/app_test.py#L650 "View st.expander source code on GitHub") | |
| --- | --- |
| AppTest.expander | |
|  |  |
| --- | --- |
| Returns | |
| (Sequence of Expandable) | Sequence of all st.expander elements. Individual elements can be accessed from a Sequence by index (order on the page). For example, at.expander[0] for the first element. Expandable is an extension of the Block class. |

AppTest.header
--------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Sequence of all st.header elements.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/testing/v1/app_test.py#L664 "View st.header source code on GitHub") | |
| --- | --- |
| AppTest.header | |
|  |  |
| --- | --- |
| Returns | |
| (ElementList of Header) | Sequence of all st.header elements. Individual elements can be accessed from an ElementList by index (order on the page). For example, at.header[0] for the first element. Header is an extension of the Element class. |

AppTest.info
------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Sequence of all st.info elements.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/testing/v1/app_test.py#L678 "View st.info source code on GitHub") | |
| --- | --- |
| AppTest.info | |
|  |  |
| --- | --- |
| Returns | |
| (ElementList of Info) | Sequence of all st.info elements. Individual elements can be accessed from an ElementList by index (order on the page). For example, at.info[0] for the first element. Info is an extension of the Element class. |

AppTest.json
------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Sequence of all st.json elements.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/testing/v1/app_test.py#L692 "View st.json source code on GitHub") | |
| --- | --- |
| AppTest.json | |
|  |  |
| --- | --- |
| Returns | |
| (ElementList of Json) | Sequence of all st.json elements. Individual elements can be accessed from an ElementList by index (order on the page). For example, at.json[0] for the first element. Json is an extension of the Element class. |

AppTest.latex
-------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Sequence of all st.latex elements.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/testing/v1/app_test.py#L706 "View st.latex source code on GitHub") | |
| --- | --- |
| AppTest.latex | |
|  |  |
| --- | --- |
| Returns | |
| (ElementList of Latex) | Sequence of all st.latex elements. Individual elements can be accessed from an ElementList by index (order on the page). For example, at.latex[0] for the first element. Latex is an extension of the Element class. |

AppTest.main
------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Sequence of elements within the main body of the app.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/testing/v1/app_test.py#L424 "View st.main source code on GitHub") | |
| --- | --- |
| AppTest.main | |
|  |  |
| --- | --- |
| Returns | |
| (Block) | A container of elements. Block can be queried for elements in the same manner as AppTest. For example, Block.checkbox will return all st.checkbox within the associated container. |

AppTest.markdown
----------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Sequence of all st.markdown elements.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/testing/v1/app_test.py#L720 "View st.markdown source code on GitHub") | |
| --- | --- |
| AppTest.markdown | |
|  |  |
| --- | --- |
| Returns | |
| (ElementList of Markdown) | Sequence of all st.markdown elements. Individual elements can be accessed from an ElementList by index (order on the page). For example, at.markdown[0] for the first element. Markdown is an extension of the Element class. |

AppTest.metric
--------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Sequence of all st.metric elements.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/testing/v1/app_test.py#L734 "View st.metric source code on GitHub") | |
| --- | --- |
| AppTest.metric | |
|  |  |
| --- | --- |
| Returns | |
| (ElementList of Metric) | Sequence of all st.metric elements. Individual elements can be accessed from an ElementList by index (order on the page). For example, at.metric[0] for the first element. Metric is an extension of the Element class. |

AppTest.multiselect
-------------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Sequence of all st.multiselect widgets.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/testing/v1/app_test.py#L748 "View st.multiselect source code on GitHub") | |
| --- | --- |
| AppTest.multiselect | |
|  |  |
| --- | --- |
| Returns | |
| (WidgetList of Multiselect) | Sequence of all st.multiselect widgets. Individual widgets can be accessed from a WidgetList by index (order on the page) or key. For example, at.multiselect[0] for the first widget or at.multiselect(key="my\_key") for a widget with a given key. |

AppTest.number\_input
---------------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Sequence of all st.number\_input widgets.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/testing/v1/app_test.py#L762 "View st.number_input source code on GitHub") | |
| --- | --- |
| AppTest.number\_input | |
|  |  |
| --- | --- |
| Returns | |
| (WidgetList of NumberInput) | Sequence of all st.number\_input widgets. Individual widgets can be accessed from a WidgetList by index (order on the page) or key. For example, at.number\_input[0] for the first widget or at.number\_input(key="my\_key") for a widget with a given key. |

AppTest.radio
-------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Sequence of all st.radio widgets.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/testing/v1/app_test.py#L776 "View st.radio source code on GitHub") | |
| --- | --- |
| AppTest.radio | |
|  |  |
| --- | --- |
| Returns | |
| (WidgetList of Radio) | Sequence of all st.radio widgets. Individual widgets can be accessed from a WidgetList by index (order on the page) or key. For example, at.radio[0] for the first widget or at.radio(key="my\_key") for a widget with a given key. |

AppTest.select\_slider
----------------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Sequence of all st.select\_slider widgets.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/testing/v1/app_test.py#L790 "View st.select_slider source code on GitHub") | |
| --- | --- |
| AppTest.select\_slider | |
|  |  |
| --- | --- |
| Returns | |
| (WidgetList of SelectSlider) | Sequence of all st.select\_slider widgets. Individual widgets can be accessed from a WidgetList by index (order on the page) or key. For example, at.select\_slider[0] for the first widget or at.select\_slider(key="my\_key") for a widget with a given key. |

AppTest.selectbox
-----------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Sequence of all st.selectbox widgets.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/testing/v1/app_test.py#L804 "View st.selectbox source code on GitHub") | |
| --- | --- |
| AppTest.selectbox | |
|  |  |
| --- | --- |
| Returns | |
| (WidgetList of Selectbox) | Sequence of all st.selectbox widgets. Individual widgets can be accessed from a WidgetList by index (order on the page) or key. For example, at.selectbox[0] for the first widget or at.selectbox(key="my\_key") for a widget with a given key. |

AppTest.sidebar
---------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Sequence of all elements within st.sidebar.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/testing/v1/app_test.py#L437 "View st.sidebar source code on GitHub") | |
| --- | --- |
| AppTest.sidebar | |
|  |  |
| --- | --- |
| Returns | |
| (Block) | A container of elements. Block can be queried for elements in the same manner as AppTest. For example, Block.checkbox will return all st.checkbox within the associated container. |

AppTest.slider
--------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Sequence of all st.slider widgets.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/testing/v1/app_test.py#L818 "View st.slider source code on GitHub") | |
| --- | --- |
| AppTest.slider | |
|  |  |
| --- | --- |
| Returns | |
| (WidgetList of Slider) | Sequence of all st.slider widgets. Individual widgets can be accessed from a WidgetList by index (order on the page) or key. For example, at.slider[0] for the first widget or at.slider(key="my\_key") for a widget with a given key. |

AppTest.subheader
-----------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Sequence of all st.subheader elements.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/testing/v1/app_test.py#L832 "View st.subheader source code on GitHub") | |
| --- | --- |
| AppTest.subheader | |
|  |  |
| --- | --- |
| Returns | |
| (ElementList of Subheader) | Sequence of all st.subheader elements. Individual elements can be accessed from an ElementList by index (order on the page). For example, at.subheader[0] for the first element. Subheader is an extension of the Element class. |

AppTest.success
---------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Sequence of all st.success elements.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/testing/v1/app_test.py#L846 "View st.success source code on GitHub") | |
| --- | --- |
| AppTest.success | |
|  |  |
| --- | --- |
| Returns | |
| (ElementList of Success) | Sequence of all st.success elements. Individual elements can be accessed from an ElementList by index (order on the page). For example, at.success[0] for the first element. Success is an extension of the Element class. |

AppTest.status
--------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Sequence of all st.status elements.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/testing/v1/app_test.py#L860 "View st.status source code on GitHub") | |
| --- | --- |
| AppTest.status | |
|  |  |
| --- | --- |
| Returns | |
| (Sequence of Status) | Sequence of all st.status elements. Individual elements can be accessed from a Sequence by index (order on the page). For example, at.status[0] for the first element. Status is an extension of the Block class. |

AppTest.table
-------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Sequence of all st.table elements.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/testing/v1/app_test.py#L874 "View st.table source code on GitHub") | |
| --- | --- |
| AppTest.table | |
|  |  |
| --- | --- |
| Returns | |
| (ElementList of Table) | Sequence of all st.table elements. Individual elements can be accessed from an ElementList by index (order on the page). For example, at.table[0] for the first element. Table is an extension of the Element class. |

AppTest.tabs
------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Sequence of all tabs within st.tabs elements.

Each tab within a single st.tabs will be returned as a separate Tab
in the Sequence. Additionally, the tab labels are forwarded to each
Tab element as a property. For example, st.tabs("A","B") will
yield two Tab objects, with Tab.label returning "A" and "B",
respectively.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/testing/v1/app_test.py#L888 "View st.tabs source code on GitHub") | |
| --- | --- |
| AppTest.tabs | |
|  |  |
| --- | --- |
| Returns | |
| (Sequence of Tab) | Sequence of all tabs within st.tabs elements. Individual tabs can be accessed from an ElementList by index (order on the page). For example, at.tabs[0] for the first tab. Tab is an extension of the Block class. |

AppTest.text
------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Sequence of all st.text elements.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/testing/v1/app_test.py#L908 "View st.text source code on GitHub") | |
| --- | --- |
| AppTest.text | |
|  |  |
| --- | --- |
| Returns | |
| (ElementList of Text) | Sequence of all st.text elements. Individual elements can be accessed from an ElementList by index (order on the page). For example, at.text[0] for the first element. Text is an extension of the Element class. |

AppTest.text\_area
------------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Sequence of all st.text\_area widgets.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/testing/v1/app_test.py#L922 "View st.text_area source code on GitHub") | |
| --- | --- |
| AppTest.text\_area | |
|  |  |
| --- | --- |
| Returns | |
| (WidgetList of TextArea) | Sequence of all st.text\_area widgets. Individual widgets can be accessed from a WidgetList by index (order on the page) or key. For example, at.text\_area[0] for the first widget or at.text\_area(key="my\_key") for a widget with a given key. |

AppTest.text\_input
-------------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Sequence of all st.text\_input widgets.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/testing/v1/app_test.py#L936 "View st.text_input source code on GitHub") | |
| --- | --- |
| AppTest.text\_input | |
|  |  |
| --- | --- |
| Returns | |
| (WidgetList of TextInput) | Sequence of all st.text\_input widgets. Individual widgets can be accessed from a WidgetList by index (order on the page) or key. For example, at.text\_input[0] for the first widget or at.text\_input(key="my\_key") for a widget with a given key. |

AppTest.time\_input
-------------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Sequence of all st.time\_input widgets.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/testing/v1/app_test.py#L950 "View st.time_input source code on GitHub") | |
| --- | --- |
| AppTest.time\_input | |
|  |  |
| --- | --- |
| Returns | |
| (WidgetList of TimeInput) | Sequence of all st.time\_input widgets. Individual widgets can be accessed from a WidgetList by index (order on the page) or key. For example, at.time\_input[0] for the first widget or at.time\_input(key="my\_key") for a widget with a given key. |

AppTest.title
-------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Sequence of all st.title elements.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/testing/v1/app_test.py#L964 "View st.title source code on GitHub") | |
| --- | --- |
| AppTest.title | |
|  |  |
| --- | --- |
| Returns | |
| (ElementList of Title) | Sequence of all st.title elements. Individual elements can be accessed from an ElementList by index (order on the page). For example, at.title[0] for the first element. Title is an extension of the Element class. |

AppTest.toast
-------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Sequence of all st.toast elements.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/testing/v1/app_test.py#L978 "View st.toast source code on GitHub") | |
| --- | --- |
| AppTest.toast | |
|  |  |
| --- | --- |
| Returns | |
| (ElementList of Toast) | Sequence of all st.toast elements. Individual elements can be accessed from an ElementList by index (order on the page). For example, at.toast[0] for the first element. Toast is an extension of the Element class. |

AppTest.toggle
--------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Sequence of all st.toggle widgets.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/testing/v1/app_test.py#L992 "View st.toggle source code on GitHub") | |
| --- | --- |
| AppTest.toggle | |
|  |  |
| --- | --- |
| Returns | |
| (WidgetList of Toggle) | Sequence of all st.toggle widgets. Individual widgets can be accessed from a WidgetList by index (order on the page) or key. For example, at.toggle[0] for the first widget or at.toggle(key="my\_key") for a widget with a given key. |

AppTest.warning
---------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Sequence of all st.warning elements.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/testing/v1/app_test.py#L1006 "View st.warning source code on GitHub") | |
| --- | --- |
| AppTest.warning | |
|  |  |
| --- | --- |
| Returns | |
| (ElementList of Warning) | Sequence of all st.warning elements. Individual elements can be accessed from an ElementList by index (order on the page). For example, at.warning[0] for the first element. Warning is an extension of the Element class. |

[Previous: App testing](/develop/api-reference/app-testing)[Next: Testing element classes](/develop/api-reference/app-testing/testing-element-classes)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
