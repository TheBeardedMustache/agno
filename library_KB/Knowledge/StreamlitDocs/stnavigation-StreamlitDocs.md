﻿st.navigation - Streamlit Docs

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

      *remove*

      * [st.navigation](/develop/api-reference/navigation/st.navigation)
      * [st.Page](/develop/api-reference/navigation/st.page)
      * [st.page\_link*link*](/develop/api-reference/widgets/st.page_link)
      * [st.switch\_page](/develop/api-reference/navigation/st.switch_page)
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
* [Navigation and pages](/develop/api-reference/navigation)/
* [st.navigation](/develop/api-reference/navigation/st.navigation)

st.navigation
-------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Configure the available pages in a multipage app.

Call st.navigation in your entrypoint file to define the available
pages for your app. st.navigation returns the current page, which can
be executed using .run() method.

When using st.navigation, your entrypoint file (the file passed to
streamlit run) acts like a router or frame of common elements around
each of your pages. Streamlit executes the entrypoint file with every app
rerun. To execute the current page, you must call the .run() method on
the StreamlitPage object returned by st.navigation.

The set of available pages can be updated with each rerun for dynamic
navigation. By default, st.navigation displays the available pages in
the sidebar if there is more than one page. This behavior can be changed
using the position keyword argument.

As soon as any session of your app executes the st.navigation command,
your app will ignore the pages/ directory (across all sessions).

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/commands/navigation.py#L82 "View st.navigation source code on GitHub") | |
| --- | --- |
| st.navigation(pages, \*, position="sidebar", expanded=False) | |
| Parameters | |
| pages (Sequence[page-like], Mapping[str, Sequence[page-like]]) | The available pages for the app.  To create a navigation menu with no sections or page groupings, pages must be a list of page-like objects. Page-like objects are anything that can be passed to st.Page or a StreamlitPage object returned by st.Page.  To create labeled sections or page groupings within the navigation menu, pages must be a dictionary. Each key is the label of a section and each value is the list of page-like objects for that section. If you use position="top", each grouping will be a collapsible item in the navigation menu.  When you use a string or path as a page-like object, they are internally passed to st.Page and converted to StreamlitPage objects. In this case, the page will have the default title, icon, and path inferred from its path or filename. To customize these attributes for your page, initialize your page with st.Page. |
| position ("sidebar", "top", or "hidden") | The position of the navigation menu. If this is "sidebar" (default), the navigation widget appears at the top of the sidebar. If this is "top", the navigation appears in the top header of the app. If this is "hidden", the navigation widget is not displayed.  If there is only one page in pages, the navigation will be hidden for any value of position. |
| expanded (bool) | Whether the navigation menu should be expanded. If this is False (default), the navigation menu will be collapsed and will include a button to view more options when there are too many pages to display. If this is True, the navigation menu will always be expanded; no button to collapse the menu will be displayed.  If st.navigation changes from expanded=True to expanded=False on a rerun, the menu will stay expanded and a collapse button will be displayed.  The parameter is only used when position="sidebar". |
|  |  |
| --- | --- |
| Returns | |
| (StreamlitPage) | The current page selected by the user. To run the page, you must use the .run() method on it. |

#### Examples

The following examples show different possible entrypoint files, each named
streamlit\_app.py. An entrypoint file is passed to streamlit run. It
manages your app's navigation and serves as a router between pages.

**Example 1: Use a callable or Python file as a page**

You can declare pages from callables or file paths. If you pass callables
or paths to st.navigation as a page-like objects, they are internally
converted to StreamlitPage objects using st.Page. In this case, the
page titles, icons, and paths are inferred from the file or callable names.

page\_1.py (in the same directory as your entrypoint file):

```

import streamlit as st

st.title("Page 1")

```

streamlit\_app.py:

```

import streamlit as st

def page_2():
    st.title("Page 2")

pg = st.navigation(["page_1.py", page_2])
pg.run()

```

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen *open\_in\_new*](https://doc-navigation-example-1.streamlit.app//?utm_medium=oembed&)

**Example 2: Group pages into sections and customize them with ``st.Page``**

You can use a dictionary to create sections within your navigation menu. In
the following example, each page is similar to Page 1 in Example 1, and all
pages are in the same directory. However, you can use Python files from
anywhere in your repository. st.Page is used to give each page a custom
title. For more information, see [st.Page](https://docs.streamlit.io/develop/api-reference/navigation/st.page).

Directory structure:

```

your_repository/
├── create_account.py
├── learn.py
├── manage_account.py
├── streamlit_app.py
└── trial.py

```

streamlit\_app.py:

```

import streamlit as st

pages = {
    "Your account": [
        st.Page("create_account.py", title="Create your account"),
        st.Page("manage_account.py", title="Manage your account"),
    ],
    "Resources": [
        st.Page("learn.py", title="Learn about us"),
        st.Page("trial.py", title="Try it out"),
    ],
}

pg = st.navigation(pages)
pg.run()

```

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen *open\_in\_new*](https://doc-navigation-example-2.streamlit.app//?utm_medium=oembed&)

**Example 3: Use top navigation**

You can use the position parameter to place the navigation at the top
of the app. This is useful for apps with a lot of pages because it allows
you to create collapsible sections for each group of pages. The following
example uses the same directory structure as Example 2 and shows how to
create a top navigation menu.

streamlit\_app.py:

```

import streamlit as st

pages = {
    "Your account": [
        st.Page("create_account.py", title="Create your account"),
        st.Page("manage_account.py", title="Manage your account"),
    ],
    "Resources": [
        st.Page("learn.py", title="Learn about us"),
        st.Page("trial.py", title="Try it out"),
    ],
}

pg = st.navigation(pages, position="top")
pg.run()

```

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen *open\_in\_new*](https://doc-navigation-top.streamlit.app//?utm_medium=oembed&)

**Example 4: Stateful widgets across multiple pages**

Call widget functions in your entrypoint file when you want a widget to be
stateful across pages. Assign keys to your common widgets and access their
values through Session State within your pages.

streamlit\_app.py:

```

import streamlit as st

def page1():
    st.write(st.session_state.foo)

def page2():
    st.write(st.session_state.bar)

# Widgets shared by all the pages
st.sidebar.selectbox("Foo", ["A", "B", "C"], key="foo")
st.sidebar.checkbox("Bar", key="bar")

pg = st.navigation([page1, page2])
pg.run()

```

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen *open\_in\_new*](https://doc-navigation-multipage-widgets.streamlit.app//?utm_medium=oembed&)

[Previous: Navigation and pages](/develop/api-reference/navigation)[Next: st.Page](/develop/api-reference/navigation/st.page)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
