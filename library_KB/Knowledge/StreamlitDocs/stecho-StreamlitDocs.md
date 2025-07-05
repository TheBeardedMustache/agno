st.echo - Streamlit Docs

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

      *remove*

      * HEADINGS AND BODY

        ---
      * [st.title](/develop/api-reference/text/st.title)
      * [st.header](/develop/api-reference/text/st.header)
      * [st.subheader](/develop/api-reference/text/st.subheader)
      * [st.markdown](/develop/api-reference/text/st.markdown)
      * FORMATTED TEXT

        ---
      * [st.badge](/develop/api-reference/text/st.badge)
      * [st.caption](/develop/api-reference/text/st.caption)
      * [st.code](/develop/api-reference/text/st.code)
      * [st.divider](/develop/api-reference/text/st.divider)
      * [st.echo](/develop/api-reference/text/st.echo)
      * [st.latex](/develop/api-reference/text/st.latex)
      * [st.text](/develop/api-reference/text/st.text)
      * UTILITIES

        ---
      * [st.help](/develop/api-reference/text/st.help)
      * [st.html](/develop/api-reference/text/st.html)
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
* [Text elements](/develop/api-reference/text)/
* [st.echo](/develop/api-reference/text/st.echo)

st.echo
-------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Use in a with block to draw some code on the app, then execute it.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/commands/echo.py#L33 "View st.echo source code on GitHub") | |
| --- | --- |
| st.echo(code\_location="above") | |
| Parameters | |
| code\_location ("above" or "below") | Whether to show the echoed code before or after the results of the executed code block. |

#### Example

```

import streamlit as st

with st.echo():
    st.write('This code will be printed')

```

### Display code

Sometimes you want your Streamlit app to contain *both* your usual
Streamlit graphic elements *and* the code that generated those elements.
That's where `st.echo()` comes in.

Ok so let's say you have the following file, and you want to make its
app a little bit more self-explanatory by making that middle section
visible in the Streamlit app:

`import streamlit as st
def get_user_name():
return 'John'
# ------------------------------------------------
# Want people to see this part of the code...
def get_punctuation():
return '!!!'
greeting = "Hi there, "
user_name = get_user_name()
punctuation = get_punctuation()
st.write(greeting, user_name, punctuation)
# ...up to here
# ------------------------------------------------
foo = 'bar'
st.write('Done!')`

The file above creates a Streamlit app containing the words "Hi there,
`John`", and then "Done!".

Now let's use `st.echo()` to make that middle section of the code visible
in the app:

`import streamlit as st
def get_user_name():
return 'John'
with st.echo():
# Everything inside this block will be both printed to the screen
# and executed.
def get_punctuation():
return '!!!'
greeting = "Hi there, "
value = get_user_name()
punctuation = get_punctuation()
st.write(greeting, value, punctuation)
# And now we're back to _not_ printing to the screen
foo = 'bar'
st.write('Done!')`

It's *that* simple!

*push\_pin*

#### Note

You can have multiple `st.echo()` blocks in the same file.
Use it as often as you wish!

[Previous: st.divider](/develop/api-reference/text/st.divider)[Next: st.latex](/develop/api-reference/text/st.latex)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
