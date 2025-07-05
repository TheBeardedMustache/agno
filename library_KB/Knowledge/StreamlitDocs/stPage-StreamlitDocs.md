st.Page - Streamlit Docs

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
* [st.Page](/develop/api-reference/navigation/st.page)

st.Page
-------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Configure a page for st.navigation in a multipage app.

Call st.Page to initialize a StreamlitPage object, and pass it to
st.navigation to declare a page in your app.

When a user navigates to a page, st.navigation returns the selected
StreamlitPage object. Call .run() on the returned StreamlitPage
object to execute the page. You can only run the page returned by
st.navigation, and you can only run it once per app rerun.

A page can be defined by a Python file or Callable.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/navigation/page.py#L29 "View st.Page source code on GitHub") | |
| --- | --- |
| st.Page(page, \*, title=None, icon=None, url\_path=None, default=False) | |
| Parameters | |
| page (str, Path, or callable) | The page source as a Callable or path to a Python file. If the page source is defined by a Python file, the path can be a string or pathlib.Path object. Paths can be absolute or relative to the entrypoint file. If the page source is defined by a Callable, the Callable can't accept arguments. |
| title (str or None) | The title of the page. If this is None (default), the page title (in the browser tab) and label (in the navigation menu) will be inferred from the filename or callable name in page. For more information, see [Overview of multipage apps](https://docs.streamlit.io/st.page.automatic-page-labels). |
| icon (str or None) | An optional emoji or icon to display next to the page title and label. If icon is None (default), no icon is displayed next to the page label in the navigation menu, and a Streamlit icon is displayed next to the title (in the browser tab). If icon is a string, the following options are valid:   * A single-character emoji. For example, you can set icon="🚨"  or icon="🔥". Emoji short codes are not supported. * An icon from the Material Symbols library (rounded style) in the  format ":material/icon\_name:" where "icon\_name" is the name   of the icon in snake case.  For example, icon=":material/thumb\_up:" will display the   Thumb Up icon. Find additional icons in the [Material Symbols](https://fonts.google.com/icons?icon.set=Material+Symbols&icon.style=Rounded)   font library. |
| url\_path (str or None) | The page's URL pathname, which is the path relative to the app's root URL. If this is None (default), the URL pathname will be inferred from the filename or callable name in page. For more information, see [Overview of multipage apps](https://docs.streamlit.io/st.page.automatic-page-urls).  The default page will have a pathname of "", indicating the root URL of the app. If you set default=True, url\_path is ignored. url\_path can't include forward slashes; paths can't include subdirectories. |
| default (bool) | Whether this page is the default page to be shown when the app is loaded. If default is False (default), the page will have a nonempty URL pathname. However, if no default page is passed to st.navigation and this is the first page, this page will become the default page. If default is True, then the page will have an empty pathname and url\_path will be ignored. |
|  |  |
| --- | --- |
| Returns | |
| (StreamlitPage) | The page object associated to the given script. |

#### Example

```

import streamlit as st

def page2():
    st.title("Second page")

pg = st.navigation([
    st.Page("page1.py", title="First page", icon="🔥"),
    st.Page(page2, title="Second page", icon=":material/favorite:"),
])
pg.run()

```

StreamlitPage
-------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

A page within a multipage Streamlit app.

Use st.Page to initialize a StreamlitPage object.

| Class description[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/navigation/page.py#L128 "View st.StreamlitPage source code on GitHub") | |
| --- | --- |
| StreamlitPage(page, \*, title=None, icon=None, url\_path=None, default=False) | |
|  |  |
| --- | --- |
| Methods | |
| [run](/develop/api-reference/navigation/st.page#stpagerun)() | Execute the page. |
| Attributes | |
| icon (str) | The icon of the page.  If no icon was declared in st.Page, this property returns "". |
| title (str) | The title of the page.  Unless declared otherwise in st.Page, the page title is inferred from the filename or callable name. For more information, see [Overview of multipage apps](https://docs.streamlit.io/st.page.automatic-page-labels). |
| url\_path (str) | The page's URL pathname, which is the path relative to the app's root URL.  Unless declared otherwise in st.Page, the URL pathname is inferred from the filename or callable name. For more information, see [Overview of multipage apps](https://docs.streamlit.io/st.page.automatic-page-urls).  The default page will always have a url\_path of "" to indicate the root URL (e.g. homepage). |

StreamlitPage.run
-----------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Execute the page.

When a page is returned by st.navigation, use the .run() method
within your entrypoint file to render the page. You can only call this
method on the page returned by st.navigation. You can only call
this method once per run of your entrypoint file.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/navigation/page.py#L272 "View st.run source code on GitHub") | |
| --- | --- |
| StreamlitPage.run() | |

[Previous: st.navigation](/develop/api-reference/navigation/st.navigation)[Next: st.page\_link](https://docs.streamlit.io/develop/api-reference/widgets/st.page_link)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
