Layouts and Containers - Streamlit Docs

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

      *remove*

      * [st.columns](/develop/api-reference/layout/st.columns)
      * [st.container](/develop/api-reference/layout/st.container)
      * [st.dialog*link*](/develop/api-reference/execution-flow/st.dialog)
      * [st.empty](/develop/api-reference/layout/st.empty)
      * [st.expander](/develop/api-reference/layout/st.expander)
      * [st.form*link*](/develop/api-reference/execution-flow/st.form)
      * [st.popover](/develop/api-reference/layout/st.popover)
      * [st.sidebar](/develop/api-reference/layout/st.sidebar)
      * [st.tabs](/develop/api-reference/layout/st.tabs)
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
* [Layouts and containers](/develop/api-reference/layout)

Layouts and Containers
======================

Complex layouts
---------------

Streamlit provides several options for controlling how different elements are laid out on the screen.

[![screenshot](/images/api/columns.jpg)

#### Columns

Insert containers laid out as side-by-side columns.

`col1, col2 = st.columns(2)
col1.write("this is column 1")
col2.write("this is column 2")`](/develop/api-reference/layout/st.columns)[![screenshot](/images/api/container.jpg)

#### Container

Insert a multi-element container.

`c = st.container()
st.write("This will show last")
c.write("This will show first")
c.write("This will show second")`](/develop/api-reference/layout/st.container)[![screenshot](/images/api/dialog.jpg)

#### Modal dialog

Insert a modal dialog that can rerun independently from the rest of the script.

`@st.dialog("Sign up")
def email_form():
name = st.text_input("Name")
email = st.text_input("Email")`](/develop/api-reference/execution-flow/st.dialog)[![screenshot](/images/api/empty.jpg)

#### Empty

Insert a single-element container.

`c = st.empty()
st.write("This will show last")
c.write("This will be replaced")
c.write("This will show first")`](/develop/api-reference/layout/st.empty)[![screenshot](/images/api/expander.jpg)

#### Expander

Insert a multi-element container that can be expanded/collapsed.

`with st.expander("Open to see more"):
st.write("This is more content")`](/develop/api-reference/layout/st.expander)[![screenshot](/images/api/popover.svg)

#### Popover

Insert a multi-element popover container that can be opened/closed.

`with st.popover("Settings"):
st.checkbox("Show completed")`](/develop/api-reference/layout/st.popover)[![screenshot](/images/api/sidebar.jpg)

#### Sidebar

Display items in a sidebar.

`st.sidebar.write("This lives in the sidebar")
st.sidebar.button("Click me!")`](/develop/api-reference/layout/st.sidebar)[![screenshot](/images/api/tabs.jpg)

#### Tabs

Insert containers separated into tabs.

`tab1, tab2 = st.tabs(["Tab 1", "Tab2"])
tab1.write("this is tab 1")
tab2.write("this is tab 2")`](/develop/api-reference/layout/st.tabs)

Third-party components

These are featured components created by our lovely community. For more examples and inspiration, check out our [Components Gallery](https://streamlit.io/components) and [Streamlit Extras](https://extras.streamlit.app)!

[![screenshot](/images/api/components/elements.jpg)

#### Streamlit Elements

Create a draggable and resizable dashboard in Streamlit. Created by [@okls](https://github.com/okls).

`from streamlit_elements import elements, mui, html
with elements("new_element"):
mui.Typography("Hello world")`](https://github.com/okld/streamlit-elements)

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

[Previous: Media elements](/develop/api-reference/media)[Next: st.columns](/develop/api-reference/layout/st.columns)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
