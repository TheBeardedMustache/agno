Execution flow - Streamlit Docs

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

      *remove*

      * [st.dialog](/develop/api-reference/execution-flow/st.dialog)
      * [st.form](/develop/api-reference/execution-flow/st.form)
      * [st.form\_submit\_button](/develop/api-reference/execution-flow/st.form_submit_button)
      * [st.fragment](/develop/api-reference/execution-flow/st.fragment)
      * [st.rerun](/develop/api-reference/execution-flow/st.rerun)
      * [st.stop](/develop/api-reference/execution-flow/st.stop)
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

      *add*
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
* [Execution flow](/develop/api-reference/execution-flow)

Execution flow
==============

Change execution
----------------

By default, Streamlit apps execute the script entirely, but we allow some functionality to handle control flow in your applications.

[![screenshot](/images/api/dialog.jpg)

#### Modal dialog

Insert a modal dialog that can rerun independently from the rest of the script.

`@st.dialog("Sign up")
def email_form():
name = st.text_input("Name")
email = st.text_input("Email")`](/develop/api-reference/execution-flow/st.dialog)[#### Fragments

Define a fragment to rerun independently from the rest of the script.

`@st.fragment(run_every="10s")
def fragment():
df = get_data()
st.line_chart(df)`](/develop/api-reference/execution-flow/st.fragment)[#### Rerun script

Rerun the script immediately.

`st.rerun()`](/develop/api-reference/execution-flow/st.rerun)[#### Stop execution

Stops execution immediately.

`st.stop()`](/develop/api-reference/execution-flow/st.stop)

Group multiple widgets
----------------------

By default, Streamlit reruns your script everytime a user interacts with your app.
However, sometimes it's a better user experience to wait until a group of related
widgets is filled before actually rerunning the script. That's what `st.form` is for!

[#### Forms

Create a form that batches elements together with a “Submit" button.

`with st.form(key='my_form'):
name = st.text_input("Name")
email = st.text_input("Email")
st.form_submit_button("Sign up")`](/develop/api-reference/execution-flow/st.form)[#### Form submit button

Display a form submit button.

`with st.form(key='my_form'):
name = st.text_input("Name")
email = st.text_input("Email")
st.form_submit_button("Sign up")`](/develop/api-reference/execution-flow/st.form_submit_button)

Third-party components

These are featured components created by our lovely community. For more examples and inspiration, check out our [Components Gallery](https://streamlit.io/components) and [Streamlit Extras](https://extras.streamlit.app)!

[![screenshot](/images/api/components/autorefresh.jpg)

#### Autorefresh

Force a refresh without tying up a script. Created by [@kmcgrady](https://github.com/kmcgrady).

`from streamlit_autorefresh import st_autorefresh
st_autorefresh(interval=2000, limit=100,
key="fizzbuzzcounter")`](https://github.com/kmcgrady/streamlit-autorefresh)

[![screenshot](/images/api/components/pydantic.jpg)

#### Pydantic

Auto-generate Streamlit UI from Pydantic Models and Dataclasses. Created by [@lukasmasuch](https://github.com/lukasmasuch).

`import streamlit_pydantic as sp
sp.pydantic_form(key="my_form",
model=ExampleModel)`](https://github.com/lukasmasuch/streamlit-pydantic)

[![screenshot](/images/api/components/pages.jpg)

#### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by [@blackary](https://github.com/blackary).

`from st_pages import Page, show_pages, add_page_title
show_pages([ Page("streamlit_app.py", "Home", "🏠"),
Page("other_pages/page2.py", "Page 2", ":books:"), ])`](https://github.com/blackary/st_pages)

[Previous: Navigation and pages](/develop/api-reference/navigation)[Next: st.dialog](/develop/api-reference/execution-flow/st.dialog)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
