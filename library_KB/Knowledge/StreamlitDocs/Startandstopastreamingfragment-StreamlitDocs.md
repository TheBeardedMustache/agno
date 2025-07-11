﻿Start and stop a streaming fragment - Streamlit Docs

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

    *add*
  + [Tutorials](/develop/tutorials)

    *remove*

    - [Authentication and personalization](/develop/tutorials/authentication)

      *add*
    - [Chat and LLM apps](/develop/tutorials/chat-and-llm-apps)

      *add*
    - [Configuration and theming](/develop/tutorials/configuration-and-theming)

      *add*
    - [Connect to data sources](/develop/tutorials/databases)

      *add*
    - [Elements](/develop/tutorials/elements)

      *add*
    - [Execution flow](/develop/tutorials/execution-flow)

      *remove*

      * FRAGMENTS

        ---
      * [Rerun your app from a fragment](/develop/tutorials/execution-flow/trigger-a-full-script-rerun-from-a-fragment)
      * [Create a multiple-container fragment](/develop/tutorials/execution-flow/create-a-multiple-container-fragment)
      * [Start and stop a streaming fragment](/develop/tutorials/execution-flow/start-and-stop-fragment-auto-reruns)
    - [Multipage apps](/develop/tutorials/multipage)

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
* [Tutorials](/develop/tutorials)/
* [Execution flow](/develop/tutorials/execution-flow)/
* [Start and stop a streaming fragment](/develop/tutorials/execution-flow/start-and-stop-fragment-auto-reruns)

Start and stop a streaming fragment
===================================

Streamlit lets you turn functions into [fragments](/develop/concepts/architecture/fragments), which can rerun independently from the full script. Additionally, you can tell Streamlit to rerun a fragment at a set time interval. This is great for streaming data or monitoring processes. You may want the user to start and stop this live streaming. To do this, programmatically set the `run_every` parameter for your fragment.

Applied concepts
----------------

* Use a fragment to stream live data.
* Start and stop a fragment from automatically rerunning.

Prerequisites
-------------

* This tutorial requires the following version of Streamlit:

  `streamlit>=1.37.0`
* You should have a clean working directory called `your-repository`.
* You should have a basic understanding of fragments.

Summary
-------

In this example, you'll build an app that streams two data series in a line chart. Your app will gather recent data on the first load of a session and statically display the line chart. Two buttons in the sidebar will allow users to start and stop data streaming to update the chart in real time. You'll use a fragment to manage the frequency and scope of the live updates.

Here's a look at what you'll build:

Complete code*expand\_more*

`import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
def get_recent_data(last_timestamp):
"""Generate and return data from last timestamp to now, at most 60 seconds."""
now = datetime.now()
if now - last_timestamp > timedelta(seconds=60):
last_timestamp = now - timedelta(seconds=60)
sample_time = timedelta(seconds=0.5) # time between data points
next_timestamp = last_timestamp + sample_time
timestamps = np.arange(next_timestamp, now, sample_time)
sample_values = np.random.randn(len(timestamps), 2)
data = pd.DataFrame(sample_values, index=timestamps, columns=["A", "B"])
return data
if "data" not in st.session_state:
st.session_state.data = get_recent_data(datetime.now() - timedelta(seconds=60))
if "stream" not in st.session_state:
st.session_state.stream = False
def toggle_streaming():
st.session_state.stream = not st.session_state.stream
st.title("Data feed")
st.sidebar.slider(
"Check for updates every: (seconds)", 0.5, 5.0, value=1.0, key="run_every"
)
st.sidebar.button(
"Start streaming", disabled=st.session_state.stream, on_click=toggle_streaming
)
st.sidebar.button(
"Stop streaming", disabled=not st.session_state.stream, on_click=toggle_streaming
)
if st.session_state.stream is True:
run_every = st.session_state.run_every
else:
run_every = None
@st.fragment(run_every=run_every)
def show_latest_data():
last_timestamp = st.session_state.data.index[-1]
st.session_state.data = pd.concat(
[st.session_state.data, get_recent_data(last_timestamp)]
)
st.session_state.data = st.session_state.data[-100:]
st.line_chart(st.session_state.data)
show_latest_data()`

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen *open\_in\_new*](https://doc-tutorial-fragment-streaming.streamlit.app/?utm_medium=oembed)

Build the example
-----------------

### Initialize your app

1. In `your_repository`, create a file named `app.py`.
2. In a terminal, change directories to `your_repository`, and start your app:

   `streamlit run app.py`

   Your app will be blank because you still need to add code.
3. In `app.py`, write the following:

   `import streamlit as st
   import pandas as pd
   import numpy as np
   from datetime import datetime, timedelta`

   You'll be using these libraries as follows:

   * You'll work with two data series in a `pandas.DataFrame`.
   * You'll generate random data with `numpy`.
   * The data will have `datetime.datetime` index values.
4. Save your `app.py` file, and view your running app.
5. In your app, select "**Always rerun**", or press the "**A**" key.

   Your preview will be blank but will automatically update as you save changes to `app.py`.
6. Return to your code.

### Build a function to generate random, recent data

To begin with, you'll define a function to randomly generate some data for two time series, which you'll call "A" and "B." It's okay to skip this section if you just want to copy the function.

Complete function to randomly generate sales data*expand\_more*

`def get_recent_data(last_timestamp):
"""Generate and return data from last timestamp to now, at most 60 seconds."""
now = datetime.now()
if now - last_timestamp > timedelta(seconds=60):
last_timestamp = now - timedelta(seconds=60)
sample_time = timedelta(seconds=0.5) # time between data points
next_timestamp = last_timestamp + sample_time
timestamps = np.arange(next_timestamp, now, sample_time)
sample_values = np.random.randn(len(timestamps), 2)
data = pd.DataFrame(sample_values, index=timestamps, columns=["A", "B"])
return data`

1. Start your function definition.

   `def get_recent_data(last_timestamp):
   """Generate and return data from last timestamp to now, at most 60 seconds."""`

   You'll pass the timestamp of your most recent datapoint to your data-generating function. Your function will use this to only return new data.
2. Get the current time and adjust the last timestamp if it is over 60 seconds ago.

   `now = datetime.now()
   if now - last_timestamp > timedelta(seconds=60):
   last_timestamp = now - timedelta(seconds=60)`

   By updating the last timestamp, you'll ensure the function never returns more than 60 seconds of data.
3. Declare a new variable, `sample_time`, to define the time between datapoints. Calculate the timestamp of the first, new datapoint.

   `sample_time = timedelta(seconds=0.5) # time between data points
   next_timestamp = last_timestamp + sample_time`
4. Create a `datetime.datetime` index and generate two data series of the same length.

   `timestamps = np.arange(next_timestamp, now, sample_time)
   sample_values = np.random.randn(len(timestamps), 2)`
5. Combine the data series with the index into a `pandas.DataFrame` and return the data.

   `data = pd.DataFrame(sample_values, index=timestamps, columns=["A", "B"])
   return data`
6. Optional: Test out your function by calling it and displaying the data.

   `data = get_recent_data(datetime.now() - timedelta(seconds=60))
   data`

   Save your `app.py` file to see the preview. Delete these two lines when finished.

### Initialize Session State values for your app

Since you will dynamically change the `run_every` parameter of `@st.fragment()`, you'll need to initialize the associated variables and Session State values before defining your fragment function. Your fragment function will also read and update values in Session State, so you can define those now to make the fragment function easier to understand.

1. Initialize your data for the first app load in a session.

   `if "data" not in st.session_state:
   st.session_state.data = get_recent_data(datetime.now() - timedelta(seconds=60))`

   Your app will display this initial data in a static line chart before a user starts streaming data.
2. Initialize `"stream"` in Session State to turn streaming on and off. Set the default to off (`False`).

   `if "stream" not in st.session_state:
   st.session_state.stream = False`
3. Create a callback function to toggle `"stream"` between `True` and `False`.

   `def toggle_streaming():
   st.session_state.stream = not st.session_state.stream`
4. Add a title to your app.

   `st.title("Data feed")`
5. Add a slider to the sidebar to set how frequently to check for data while streaming.

   `st.sidebar.slider(
   "Check for updates every: (seconds)", 0.5, 5.0, value=1.0, key="run_every"
   )`
6. Add buttons to the sidebar to turn streaming on and off.

   `st.sidebar.button(
   "Start streaming", disabled=st.session_state.stream, on_click=toggle_streaming
   )
   st.sidebar.button(
   "Stop streaming", disabled=not st.session_state.stream, on_click=toggle_streaming
   )`

   Both functions use the same callback to toggle `"stream"` in Session State. Use the current value `"stream"` to disable one of the buttons. This ensures the buttons are always consistent with the current state; "**Start streaming**" is only clickable when streaming is off, and "**Stop streaming**" is only clickable when streaming is on. The buttons also provide status to the user by highlighting which action is available to them.
7. Create and set a new variable, `run_every`, that will determine whether or not the fragment function will rerun automatically (and how fast).

   `if st.session_state.stream is True:
   run_every = st.session_state.run_every
   else:
   run_every = None`

### Build a fragment function to stream data

To allow the user to turn data streaming on and off, you must set the `run_every` parameter in the `@st.fragment()` decorator.

Complete function to show and stream data*expand\_more*

`@st.fragment(run_every=run_every)
def show_latest_data():
last_timestamp = st.session_state.data.index[-1]
st.session_state.data = pd.concat(
[st.session_state.data, get_recent_data(last_timestamp)]
)
st.session_state.data = st.session_state.data[-100:]
st.line_chart(st.session_state.data)`

1. Use an [`@st.fragment`](/develop/api-reference/execution-flow/st.fragment) decorator and start your function definition.

   `@st.fragment(run_every=run_every)
   def show_latest_data():`

   Use the `run_every` variable declared above to set the parameter of the same name.
2. Retrieve the timestamp of the last datapoint in Session State.

   `last_timestamp = st.session_state.data.index[-1]`
3. Update the data in Session State and trim to keep only the last 100 timestamps.

   `st.session_state.data = pd.concat(
   [st.session_state.data, get_recent_data(last_timestamp)]
   )
   st.session_state.data = st.session_state.data[-100:]`
4. Show the data in a line chart.

   `st.line_chart(st.session_state.data)`

   Your fragment-function definition is complete.

### Call and test out your fragment function

1. Call your function at the bottom of your code.

   `show_latest_data()`
2. Test out your app by clicking "**Start streaming**." Try adjusting the frequency of updates.

Next steps
----------

Try adjusting the frequency of data generation or how much data is kept in Session State. Within `get_recent_data` try setting `sample_time` with a widget.

Try using [st.plotly\_chart](/develop/api-reference/charts/st.plotly_chart) or [st.altair\_chart](/develop/api-reference/charts/st.altair_chart) to add labels to your chart.

[Previous: Create a multiple-container fragment](/develop/tutorials/execution-flow/create-a-multiple-container-fragment)[Next: Multipage apps](/develop/tutorials/multipage)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
