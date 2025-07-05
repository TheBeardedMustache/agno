st.chat\_input - Streamlit Docs

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

      *remove*

      * [st.chat\_input](/develop/api-reference/chat/st.chat_input)
      * [st.chat\_message](/develop/api-reference/chat/st.chat_message)
      * [st.status*link*](/develop/api-reference/status/st.status)
      * [st.write\_stream*link*](/develop/api-reference/write-magic/st.write_stream)
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
* [Chat elements](/develop/api-reference/chat)/
* [st.chat\_input](/develop/api-reference/chat/st.chat_input)

*star*

#### Tip

Read the [Build a basic LLM chat app](/develop/tutorials/llms/build-conversational-apps) tutorial to learn how to use `st.chat_message` and `st.chat_input` to build chat-based apps.

st.chat\_input
--------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Display a chat input widget.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/elements/widgets/chat.py#L402 "View st.chat_input source code on GitHub") | |
| --- | --- |
| st.chat\_input(placeholder="Your message", \*, key=None, max\_chars=None, accept\_file=False, file\_type=None, disabled=False, on\_submit=None, args=None, kwargs=None, width="stretch") | |
| Parameters | |
| placeholder (str) | A placeholder text shown when the chat input is empty. This defaults to "Your message". For accessibility reasons, you should not use an empty string. |
| key (str or int) | An optional string or integer to use as the unique key for the widget. If this is omitted, a key will be generated for the widget based on its content. No two widgets may have the same key. |
| max\_chars (int or None) | The maximum number of characters that can be entered. If this is None (default), there will be no maximum. |
| accept\_file (bool or str) | Whether the chat input should accept files. This can be one of the following values:   * False (default): No files are accepted and the user can only   submit a message. * True: The user can add a single file to their submission. * "multiple": The user can add multiple files to their   submission.   When the widget is configured to accept files, the accepted file types can be configured with the file\_type parameter.  By default, uploaded files are limited to 200 MB each. You can configure this using the server.maxUploadSize config option. For more information on how to set config options, see [config.toml](https://docs.streamlit.io/develop/api-reference/configuration/config.toml). |
| file\_type (str, Sequence[str], or None) | The allowed file extension(s) for uploaded files. This can be one of the following types:   * None (default): All file extensions are allowed. * A string: A single file extension is allowed. For example, to   only accept CSV files, use "csv". * A sequence of strings: Multiple file extensions are allowed. For   example, to only accept JPG/JPEG and PNG files, use   ["jpg", "jpeg", "png"]. |
| disabled (bool) | Whether the chat input should be disabled. This defaults to False. |
| on\_submit (callable) | An optional callback invoked when the chat input's value is submitted. |
| args (tuple) | An optional tuple of args to pass to the callback. |
| kwargs (dict) | An optional dict of kwargs to pass to the callback. |
| width ("stretch" or int) | The width of the chat input widget. This can be one of the following:   * "stretch" (default): The width of the widget matches the   width of the parent container. * An integer specifying the width in pixels: The widget has a   fixed width. If the specified width is greater than the width of   the parent container, the width of the widget matches the width   of the parent container. |
|  |  |
| --- | --- |
| Returns | |
| (None, str, or dict-like) | The user's submission. This is one of the following types:   * None: If the user didn't submit a message or file in the last   rerun, the widget returns None. * A string: When the widget is not configured to accept files and   the user submitted a message in the last rerun, the widget   returns the user's message as a string. * A dict-like object: When the widget is configured to accept files   and the user submitted a message and/or file(s) in the last   rerun, the widget returns a dict-like object with two attributes,   text and files.   When the widget is configured to accept files and the user submits something in the last rerun, you can access the user's submission with key or attribute notation from the dict-like object. This is shown in Example 3 below.  The text attribute holds a string, which is the user's message. This is an empty string if the user only submitted one or more files.  The files attribute holds a list of UploadedFile objects. The list is empty if the user only submitted a message. Unlike st.file\_uploader, this attribute always returns a list, even when the widget is configured to accept only one file at a time.  The UploadedFile class is a subclass of BytesIO, and therefore is "file-like". This means you can pass an instance of it anywhere a file is expected. |

#### Examples

**Example 1: Pin the chat input widget to the bottom of your app**

When st.chat\_input is used in the main body of an app, it will be
pinned to the bottom of the page.

```

import streamlit as st

prompt = st.chat_input("Say something")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")

```

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen *open\_in\_new*](https://doc-chat-input.streamlit.app//?utm_medium=oembed&)

**Example 2: Use the chat input widget inline**

The chat input can also be used inline by nesting it inside any layout
container (container, columns, tabs, sidebar, etc) or fragment. Create
chat interfaces embedded next to other content, or have multiple
chatbots!

```

import streamlit as st

with st.sidebar:
    messages = st.container(height=300)
    if prompt := st.chat_input("Say something"):
        messages.chat_message("user").write(prompt)
        messages.chat_message("assistant").write(f"Echo: {prompt}")

```

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen *open\_in\_new*](https://doc-chat-input-inline.streamlit.app//?utm_medium=oembed&)

**Example 3: Let users upload files**

When you configure your chat input widget to allow file attachments, it
will return a dict-like object when the user sends a submission. You
can access the user's message through the text attribute of this
dictionary. You can access a list of the user's submitted file(s)
through the files attribute. Similar to st.session\_state, you
can use key or attribute notation.

```

import streamlit as st

prompt = st.chat_input(
    "Say something and/or attach an image",
    accept_file=True,
    file_type=["jpg", "jpeg", "png"],
)
if prompt and prompt.text:
    st.markdown(prompt.text)
if prompt and prompt["files"]:
    st.image(prompt["files"][0])

```

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen *open\_in\_new*](https://doc-chat-input-file-uploader.streamlit.app//?utm_medium=oembed&)

For an overview of the `st.chat_input` and `st.chat_message` API, check out this video tutorial by Chanin Nantasenamat ([@dataprofessor](https://www.youtube.com/dataprofessor)), a Senior Developer Advocate at Streamlit.

[Previous: Chat elements](/develop/api-reference/chat)[Next: st.chat\_message](/develop/api-reference/chat/st.chat_message)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
