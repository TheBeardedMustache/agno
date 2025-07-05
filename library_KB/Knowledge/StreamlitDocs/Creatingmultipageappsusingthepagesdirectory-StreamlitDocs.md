Creating multipage apps using the `pages/` directory - Streamlit Docs

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

      *add*
    - [Multipage apps](/develop/concepts/multipage-apps)

      *remove*

      * [Overview](/develop/concepts/multipage-apps/overview)
      * [Page and navigation](/develop/concepts/multipage-apps/page-and-navigation)
      * [Pages directory](/develop/concepts/multipage-apps/pages-directory)
      * [Working with widgets](/develop/concepts/multipage-apps/widgets)
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
* [Multipage apps](/develop/concepts/multipage-apps)/
* [Pages directory](/develop/concepts/multipage-apps/pages-directory)

Creating multipage apps using the `pages/` directory
====================================================

The most customizable method for declaring multipage apps is using [Page and navigation](/develop/concepts/multipage-apps/page-and-navigation). However, Streamlit also provides a frictionless way to create multipage apps where pages are automatically recognized and shown in a navigation widget inside your app's sidebar. This method uses the `pages/` directory.

This page assumes you understand the [Page terminology](/develop/concepts/multipage-apps/overview#page-terminology) presented in the overview.

App structure
-------------

When you use the `pages/` directory, Streamlit identifies pages in your multipage app by directory structure and filenames. Your entrypoint file (the file you pass to `streamlit run`), is your app's homepage. When you have a `pages/` directory next to your entrypoint file, Streamlit will identify each Python file within it as a page. The following example has three pages. `your_homepage.py` is the entrypoint file and homepage.

`your_working_directory/
├── pages/
│ ├── a_page.py
│ └── another_page.py
└── your_homepage.py`

Run your multipage app just like you would for a single-page app. Pass your entrypoint file to `streamlit run`.

`streamlit run your_homepage.py`

Only `.py` files in the `pages/` directory will be identified as pages. Streamlit ignores all other files in the `pages/` directory and its subdirectories. Streamlit also ignores Python files in subdirectories of `pages/`.

*priority\_high*

#### Important

If you call `st.navigation` in your app (in any session), Streamlit will switch to using the newer, Page-and-navigation multipage structure. In this case, the `pages/` directory will be ignored across all sessions. You will not be able to revert back to the `pages/` directory unless you restart you app.

### How pages are sorted in the sidebar

See the overview to understand how Streamlit assigns [Automatic page labels and URLs](/develop/concepts/multipage-apps/overview#automatic-page-labels-and-urls) based on the `number`, `separator`, `identifier`, and `".py"` extension that constitute a filename.

The entrypoint file is always displayed first. The remaining pages are sorted as follows:

* Files that have a `number` appear before files without a `number`.
* Files are sorted based on the `number` (if any), followed by the `label` (if any).
* When files are sorted, Streamlit treats the `number` as an actual number rather than a string. So `03` is the same as `3`.

This table shows examples of filenames and their corresponding labels, sorted by the order in which they appear in the sidebar.

**Examples**:

| **Filename** | **Rendered label** |
| --- | --- |
| `1 - first page.py` | first page |
| `12 monkeys.py` | monkeys |
| `123.py` | 123 |
| `123_hello_dear_world.py` | hello dear world |
| `_12 monkeys.py` | 12 monkeys |

*star*

#### Tip

Emojis can be used to make your page names more fun! For example, a file named `🏠_Home.py` will create a page titled "🏠 Home" in the sidebar. When adding emojis to filenames, it’s best practice to include a numbered prefix to make autocompletion in your terminal easier. Terminal-autocomplete can get confused by unicode (which is how emojis are represented).

Notes and limitations
---------------------

* Pages support run-on-save.

  + When you update a page while your app is running, this causes a rerun for users currently viewing that exact page.
  + When you update a page while your app is running, the app will not automatically rerun for users currently viewing a different page.
* While your app is running, adding or deleting a page updates the sidebar navigation immediately.
* [`st.set_page_config`](/develop/api-reference/configuration/st.set_page_config) works at the page level.

  + When you set `title` or `favicon` using `st.set_page_config`, this applies to the current page only.
  + When you set `layout` using `st.set_page_config`, the setting will remain for the session until changed by another call to `st.set_page_config`. If you use `st.set_page_config` to set `layout`, it's recommended to call it on *all* pages.
* Pages share the same Python modules globally:

  `# page1.py
  import foo
  foo.hello = 123
  # page2.py
  import foo
  st.write(foo.hello) # If page1 already executed, this writes 123`
* Pages share the same [st.session\_state](/develop/concepts/architecture/session-state):

  `# page1.py
  import streamlit as st
  if "shared" not in st.session_state:
  st.session_state["shared"] = True
  # page2.py
  import streamlit as st
  st.write(st.session_state["shared"]) # If page1 already executed, this writes True`

You now have a solid understanding of multipage apps. You've learned how to structure apps, define pages, and navigate between pages in the user interface. It's time to [create your first multipage app](/get-started/tutorials/create-a-multipage-app)! 🥳

[Previous: Page and navigation](/develop/concepts/multipage-apps/page-and-navigation)[Next: Working with widgets](/develop/concepts/multipage-apps/widgets)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
