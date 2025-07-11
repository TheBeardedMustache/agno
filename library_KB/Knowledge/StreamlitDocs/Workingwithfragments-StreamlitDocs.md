﻿Working with fragments - Streamlit Docs

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

      *remove*

      * [Running your app](/develop/concepts/architecture/run-your-app)
      * [Streamlit's architecture](/develop/concepts/architecture/architecture)
      * [The app chrome](/develop/concepts/architecture/app-chrome)
      * [Caching](/develop/concepts/architecture/caching)
      * [Session State](/develop/concepts/architecture/session-state)
      * [Forms](/develop/concepts/architecture/forms)
      * [Fragments](/develop/concepts/architecture/fragments)
      * [Widget behavior](/develop/concepts/architecture/widget-behavior)
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
* [Architecture and execution](/develop/concepts/architecture)/
* [Fragments](/develop/concepts/architecture/fragments)

Working with fragments
======================

Reruns are a central part of every Streamlit app. When users interact with widgets, your script reruns from top to bottom, and your app's frontend is updated. Streamlit provides several features to help you develop your app within this execution model. Streamlit version 1.37.0 introduced fragments to allow rerunning a portion of your code instead of your full script. As your app grows larger and more complex, these fragment reruns help your app be efficient and performant. Fragments give you finer, easy-to-understand control over your app's execution flow.

Before you read about fragments, we recommend having a basic understanding of [caching](/develop/concepts/architecture/caching), [Session State](/concepts/architecture/session-state), and [forms](/develop/concepts/architecture/forms).

Use cases for fragments
-----------------------

Fragments are versatile and applicable to a wide variety of circumstances. Here are just a few, common scenarios where fragments are useful:

* Your app has multiple visualizations and each one takes time to load, but you have a filter input that only updates one of them.
* You have a dynamic form that doesn't need to update the rest of your app (until the form is complete).
* You want to automatically update a single component or group of components to stream data.

Defining and calling a fragment
-------------------------------

Streamlit provides a decorator ([`st.fragment`](/develop/api-reference/execution-flow/st.fragment)) to turn any function into a fragment function. When you call a fragment function that contains a widget function, a user triggers a *fragment rerun* instead of a full rerun when they interact with that fragment's widget. During a fragment rerun, only your fragment function is re-executed. Anything within the main body of your fragment is updated on the frontend, while the rest of your app remains the same. We'll describe fragments written across multiple containers later on.

Here is a basic example of defining and calling a fragment function. Just like with caching, remember to call your function after defining it.

`import streamlit as st
@st.fragment
def fragment_function():
if st.button("Hi!"):
st.write("Hi back!")
fragment_function()`

If you want the main body of your fragment to appear in the sidebar or another container, call your fragment function inside a context manager.

`with st.sidebar:
fragment_function()`

### Fragment execution flow

Consider the following code with the explanation and diagram below.

`import streamlit as st
st.title("My Awesome App")
@st.fragment()
def toggle_and_text():
cols = st.columns(2)
cols[0].toggle("Toggle")
cols[1].text_area("Enter text")
@st.fragment()
def filter_and_file():
cols = st.columns(2)
cols[0].checkbox("Filter")
cols[1].file_uploader("Upload image")
toggle_and_text()
cols = st.columns(2)
cols[0].selectbox("Select", [1,2,3], None)
cols[1].button("Update")
filter_and_file()`

When a user interacts with an input widget inside a fragment, only the fragment reruns instead of the full script. When a user interacts with an input widget outside a fragment, the full script reruns as usual.

If you run the code above, the full script will run top to bottom on your app's initial load. If you flip the toggle button in your running app, the first fragment (`toggle_and_text()`) will rerun, redrawing the toggle and text area while leaving everything else unchanged. If you click the checkbox, the second fragment (`filter_and_file()`) will rerun and consequently redraw the checkbox and file uploader. Everything else remains unchanged. Finally, if you click the update button, the full script will rerun, and Streamlit will redraw everything.

![Diagram of fragment execution flow](/images/concepts/fragment_diagram.png)

Fragment return values and interacting with the rest of your app
----------------------------------------------------------------

Streamlit ignores fragment return values during fragment reruns, so defining return values for your fragment functions is not recommended. Instead, if your fragment needs to share data with the rest of your app, use Session State. Fragments are just functions in your script, so they can access Session State, imported modules, and other Streamlit elements like containers. If your fragment writes to any container created outside of itself, note the following difference in behavior:

* Elements drawn in the main body of your fragment are cleared and redrawn in place during a fragment rerun. Repeated fragment reruns will not cause additional elements to appear.
* Elements drawn to containers outside the main body of fragment will not be cleared with each fragment rerun. Instead, Streamlit will draw them additively and these elements will accumulate until the next full-script rerun.
* A fragment can't draw widgets in containers outside of the main body of the fragment. Widgets can only go in the main body of a fragment.

To prevent elements from accumulating in outside containers, use [`st.empty`](/develop/api-reference/layout/st.empty) containers. For a related tutorial, see [Create a fragment across multiple containers](/develop/tutorials/execution-flow/create-a-multiple-container-fragment).

If you need to trigger a full-script rerun from inside a fragment, call [`st.rerun`](/develop/api-reference/execution-flow/st.rerun). For a related tutorial, see [Trigger a full-script rerun from inside a fragment](/develop/tutorials/execution-flow/trigger-a-full-script-rerun-from-a-fragment).

Automate fragment reruns
------------------------

`st.fragment` includes a convenient `run_every` parameter that causes the fragment to rerun automatically at the specified time interval. These reruns are in addition to any reruns (fragment or full-script) triggered by your user. The automatic fragment reruns will continue even if your user is not interacting with your app. This is a great way to show a live data stream or status on a running background job, efficiently updating your rendered data and *only* your rendered data.

`@st.fragment(run_every="10s")
def auto_function():
# This will update every 10 seconds!
df = get_latest_updates()
st.line_chart(df)
auto_function()`

For a related tutorial, see [Start and stop a streaming fragment](/develop/tutorials/execution-flow/start-and-stop-fragment-auto-reruns).

Compare fragments to other Streamlit features
---------------------------------------------

### Fragments vs forms

Here is a comparison between fragments and forms:

* **Forms** allow users to interact with widgets without rerunning your app. Streamlit does not send user actions within a form to your app's Python backend until the form is submitted. Widgets within a form can not dynamically update other widgets (in or out of the form) in real-time.
* **Fragments** run independently from the rest of your code. As your users interact with fragment widgets, their actions are immediately processed by your app's Python backend and your fragment code is rerun. Widgets within a fragment can dynamically update other widgets within the same fragment in real-time.

A form batches user input without interaction between any widgets. A fragment immediately processes user input but limits the scope of the rerun.

### Fragments vs callbacks

Here is a comparison between fragments and callbacks:

* **Callbacks** allow you to execute a function at the beginning of a script rerun. A callback is a *single prefix* to your script rerun.
* **Fragments** allow you to rerun a portion of your script. A fragment is a *repeatable postfix* to your script, running each time a user interacts with a fragment widget, or automatically in sequence when `run_every` is set.

When callbacks render elements to your page, they are rendered before the rest of your page elements. When fragments render elements to your page, they are updated with each fragment rerun (unless they are written to containers outside of the fragment, in which case they accumulate there).

### Fragments vs custom components

Here is a comparison between fragments and custom components:

* **Components** are custom frontend code that can interact with the Python code, native elements, and widgets in your Streamlit app. Custom components extend what’s possible with Streamlit. They follow the normal Streamlit execution flow.
* **Fragments** are parts of your app that can rerun independently of the full app. Fragments can be composed of multiple Streamlit elements, widgets, or any Python code.

A fragment can include one or more custom components. A custom component could not easily include a fragment!

### Fragments vs caching

Here is a comparison between fragments and caching:

* **Caching:** allows you to skip over a function and return a previously computed value. When you use caching, you execute everything except the cached function (if you've already run it before).
* **Fragments:** allow you to freeze most of your app and just execute the fragment. When you use fragments, you execute only the fragment (when triggering a fragment rerun).

Caching saves you from unnecessarily running a piece of your app while the rest runs. Fragments save you from running your full app when you only want to run one piece.

Limitations and unsupported behavior
------------------------------------

* Fragments can't detect a change in input values. It is best to use Session State for dynamic input and output for fragment functions.
* Using caching and fragments on the same function is unsupported.
* Fragments can't render widgets in externally-created containers; widgets can only be in the main body of a fragment.

[Previous: Forms](/develop/concepts/architecture/forms)[Next: Widget behavior](/develop/concepts/architecture/widget-behavior)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
