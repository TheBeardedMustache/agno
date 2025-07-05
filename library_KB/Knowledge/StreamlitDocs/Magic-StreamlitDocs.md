Magic - Streamlit Docs

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

      *remove*

      * [st.write](/develop/api-reference/write-magic/st.write)
      * [st.write\_stream](/develop/api-reference/write-magic/st.write_stream)
      * [magic](/develop/api-reference/write-magic/magic)
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
* [Write and magic](/develop/api-reference/write-magic)/
* [magic](/develop/api-reference/write-magic/magic)

Magic
-----

Magic commands are a feature in Streamlit that allows you to write almost anything (markdown, data,
charts) without having to type an explicit command at all. Just put the thing you want to show on
its own line of code, and it will appear in your app. Here's an example:

`# Draw a title and some text to the app:
'''
# This is the document title
This is some _markdown_.
'''
import pandas as pd
df = pd.DataFrame({'col1': [1,2,3]})
df # 👈 Draw the dataframe
x = 10
'x', x # 👈 Draw the string 'x' and then the value of x
# Also works with most supported chart types
import matplotlib.pyplot as plt
import numpy as np
arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)
fig # 👈 Draw a Matplotlib chart`

### How Magic works

Any time Streamlit sees either a variable or literal
value on its own line, it automatically writes that to your app using
[`st.write`](/develop/api-reference/write-magic/st.write) (which you'll learn about later).

Also, magic is smart enough to ignore docstrings. That is, it ignores the
strings at the top of files and functions.

If you prefer to call Streamlit commands more explicitly, you can always turn
magic off in your `~/.streamlit/config.toml` with the following setting:

`[runner]
magicEnabled = false`

*priority\_high*

#### Important

Right now, Magic only works in the main Python app file, not in imported files. See GitHub issue #288 for a discussion of the issues.

### Featured video

Learn what the [`st.write`](/develop/api-reference/write-magic/st.write) and [magic](/develop/api-reference/write-magic/magic) commands are and how to use them.

[Previous: st.write\_stream](/develop/api-reference/write-magic/st.write_stream)[Next: Text elements](/develop/api-reference/text)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
