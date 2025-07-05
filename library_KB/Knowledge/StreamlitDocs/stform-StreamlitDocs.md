st.form - Streamlit Docs

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
* [Execution flow](/develop/api-reference/execution-flow)/
* [st.form](/develop/api-reference/execution-flow/st.form)

*star*

#### Tip

This page only contains information on the `st.forms` API. For a deeper dive into creating and using forms within Streamlit apps, read our guide on [Using forms](/develop/concepts/architecture/forms).

st.form
-------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Create a form that batches elements together with a "Submit" button.

A form is a container that visually groups other elements and
widgets together, and contains a Submit button. When the form's
Submit button is pressed, all widget values inside the form will be
sent to Streamlit in a batch.

To add elements to a form object, you can use with notation
(preferred) or just call methods directly on the form. See
examples below.

Forms have a few constraints:

* Every form must contain a st.form\_submit\_button.
* st.button and st.download\_button cannot be added to a form.
* Forms can appear anywhere in your app (sidebar, columns, etc),
  but they cannot be embedded inside other forms.
* Within a form, the only widget that can have a callback function is
  st.form\_submit\_button.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/elements/form.py#L69 "View st.form source code on GitHub") | |
| --- | --- |
| st.form(key, clear\_on\_submit=False, \*, enter\_to\_submit=True, border=True, width="stretch", height="content") | |
| Parameters | |
| key (str) | A string that identifies the form. Each form must have its own key. (This key is not displayed to the user in the interface.) |
| clear\_on\_submit (bool) | If True, all widgets inside the form will be reset to their default values after the user presses the Submit button. Defaults to False. (Note that Custom Components are unaffected by this flag, and will not be reset to their defaults on form submission.) |
| enter\_to\_submit (bool) | Whether to submit the form when a user presses Enter while interacting with a widget inside the form.  If this is True (default), pressing Enter while interacting with a form widget is equivalent to clicking the first st.form\_submit\_button in the form.  If this is False, the user must click an st.form\_submit\_button to submit the form.  If the first st.form\_submit\_button in the form is disabled, the form will override submission behavior with enter\_to\_submit=False. |
| border (bool) | Whether to show a border around the form. Defaults to True.  Note  Not showing a border can be confusing to viewers since interacting with a widget in the form will do nothing. You should only remove the border if there's another border (e.g. because of an expander) or the form is small (e.g. just a text input and a submit button). |
| width ("stretch", "content", or int) | The width of the form container. This can be one of the following:   * "stretch" (default): The width of the container matches the   width of the parent container. * "content": The width of the container matches the width of its   content, but doesn't exceed the width of the parent container. * An integer specifying the width in pixels: The container has a   fixed width. If the specified width is greater than the width of   the parent container, the width of the container matches the width   of the parent container. |
| height ("content" or int) | The height of the form container. This can be one of the following:   * "content" (default): The height of the container matches the   height of its content. * An integer specifying the height in pixels: The container has a   fixed height. If the content is larger than the specified   height, scrolling is enabled.   Note  Use scrolling containers sparingly. If you use scrolling containers, avoid heights that exceed 500 pixels. Otherwise, the scroll surface of the container might cover the majority of the screen on mobile devices, which makes it hard to scroll the rest of the app. |

#### Examples

Inserting elements using with notation:

```

import streamlit as st

with st.form("my_form"):
    st.write("Inside the form")
    slider_val = st.slider("Form slider")
    checkbox_val = st.checkbox("Form checkbox")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("slider", slider_val, "checkbox", checkbox_val)
st.write("Outside the form")

```

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen *open\_in\_new*](https://doc-form1.streamlit.app//?utm_medium=oembed&)

Inserting elements out of order:

```

import streamlit as st

form = st.form("my_form")
form.slider("Inside the form")
st.slider("Outside the form")

# Now add a submit button to the form:
form.form_submit_button("Submit")

```

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen *open\_in\_new*](https://doc-form2.streamlit.app//?utm_medium=oembed&)

[Previous: st.dialog](/develop/api-reference/execution-flow/st.dialog)[Next: st.form\_submit\_button](/develop/api-reference/execution-flow/st.form_submit_button)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
