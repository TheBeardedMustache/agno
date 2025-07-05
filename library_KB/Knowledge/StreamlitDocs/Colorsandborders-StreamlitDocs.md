﻿Colors and borders - Streamlit Docs

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

      *add*
    - [App design](/develop/concepts/design)

      *add*
    - ADDITIONAL

      ---
    - [Connections, secrets, and authentication](/develop/concepts/connections)

      *add*
    - [Custom components](/develop/concepts/custom-components)

      *add*
    - [Configuration and theming](/develop/concepts/configuration)

      *remove*

      * [Configuration options](/develop/concepts/configuration/options)
      * [HTTPS support](/develop/concepts/configuration/https-support)
      * [Serving static files](/develop/concepts/configuration/serving-static-files)
      * THEMING

        ---
      * [Customize your theme](/develop/concepts/configuration/theming)
      * [Customize colors and borders](/develop/concepts/configuration/theming-customize-colors-and-borders)
      * [Customize fonts](/develop/concepts/configuration/theming-customize-fonts)
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
* [Configuration and theming](/develop/concepts/configuration)/
* [Customize colors and borders](/develop/concepts/configuration/theming-customize-colors-and-borders)

Customize colors and borders in your Streamlit app
==================================================

Color values
------------

For all configuration options that accept a color, you can specify the value with one of the following strings:

* A CSS [`<named-color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/named-color) like `"darkBlue"` or `"maroon"`.
* A HEX string like `"#483d8b"` or `"#6A5ACD"`.
* An RGB string like `"rgb(106, 90, 205)"` or `"RGB(70, 130, 180)"`.
* An HSL string like `"hsl(248, 53%, 58%)"` or `"HSL(147, 50%, 47%)"`.

*star*

#### Tip

Although you can specify an alpha value for your colors, this isn't recommended. Streamlit adjusts the alpha value of colors to ensure contextually appropriate shading between background and foreground.

Default Streamlit colors
------------------------

Streamlit comes with two preconfigured themes: light and dark. If you don't specify any theme configuration options, Streamlit will attempt to use the preconfigured theme that best matches each user's browser settings.

Color and border configuration options
--------------------------------------

Most theme configuration options can be set for your whole app, but you can override some with a different value for the sidebar. For example, your app's primary color (`primaryColor`) is used to highlight interactive elements and show focus. If you set `theme.primaryColor`, this will change the primary color for your whole app. However, if you set `theme.sidebar.primaryColor`, this will override `theme.primaryColor` in the sidebar, allowing you to use two different primary colors.

The following two configuration options can only be applied to the whole app:

* `theme.base` sets the default colors for your app's theme to match one of Streamlit's two default themes (`"light"` or `"dark"`). If any theme configuation option is used and `theme.base` is not set, then Streamlit will use `"light"`.
* `theme.showSidebarBorder` sets the visibility of the border between the sidebar and the main body of your app.

The following configuration options can be set separately for the sidebar by using the `[theme.sidebar]` table instead of the `[theme]` table in `config.toml`:

* `theme.primaryColor`
* `theme.backgroundColor`
* `theme.secondaryBackgroundColor`
* `theme.textColor`
* `theme.linkColor`
* `theme.codeBackgroundColor`
* `theme.baseRadius`
* `theme.buttonRadius`
* `theme.borderColor`
* `theme.dataframeBorderColor`
* `theme.showWidgetBorder`

For brevity, on the rest of this page, theming configuration options will not include the `theme.` or `theme.sidebar.` prefix.

### `primaryColor`

`primaryColor` defines the accent color most often used throughout your Streamlit
app. The following features and effects use your primary color:

* Button hover effects
* Elements in focus
* Selected elements

*star*

#### Tip

When your primary color is used as a background, Streamlit changes the text color to white. For example, this happens for `type="primary"` buttons and for selected items in `st.multiselect`.

For legibility, always choose a primary color that is dark enough to contrast well with white text.

#### Example 1: Primary color

The following configuration example has a `"forestGreen"` primary color. In the sidebar, the configuration overrides the primary color to `"darkGoldenrod"`. If you click inside a widget to give it focus, Streamlit displays a primary-color border around the widget. Additionally, if you hover over the secondary and tertiary buttons, the hover color matches the primary color.

`[theme]
base="dark"
primaryColor="forestGreen"
[theme.sidebar]
primaryColor="darkGoldrod"`

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen *open\_in\_new*](https://doc-theming-color-primarycolor.streamlit.app/?utm_medium=oembed)

### `backgroundColor`, `secondaryBackgroundColor`, and `codeBackgroundColor`

`backgroundColor` defines the background color of your app.

`secondaryBackgroundColor` is used for contrast in the following places:

* The background of input or selection regions for widgets
* Headers within elements like `st.dataframe` and `st.help`
* Code blocks and inline code (if `codeBackgroundColor` is not set)

`codeBackgroundColor` sets the background for code blocks and line code. If `codeBackgroundColor` is not set, Streamlit uses `secondaryBackgroundColor` instead.

*push\_pin*

#### Note

If you do not define background colors for the sidebar, Streamlit will swap `backgroundColor` and `secondaryBackgroundColor` in the sidebar:

* If `theme.sidebar.backgroundColor` is not defined, Streamlit uses `theme.secondaryBackgroundColor`.
* If `theme.sidebar.secondaryBackgroundColor` is not defined, Streamlit uses `theme.backgroundColor`.

#### Example 2: Background colors

The following configuration example has a `"white"` background, with a lavender-tinted `"ghostWhite"` sidebar background. The secondary color for the whole app is `"lavender"` and the code background color is `"powderBlue"`. The code background color is configured once in `[theme]` and inherited in the sidebar. However, because Streamlit swaps background colors when the sidebar inherits them, the secondary background color is set in both `[theme]` and `[theme.sidebar]`. To see the secondary color used for a hover effect, hover over a dataframe cell or open the multiselect drop-down menu.

`[theme]
base="light"
backgroundColor="white"
secondaryBackgroundColor="lavender"
codeBackgroundColor="powderBlue"
[theme.sidebar]
backgroundColor="ghostWhite"
secondaryBackgroundColor="lavender"`

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen *open\_in\_new*](https://doc-theming-color-backgroundcolor.streamlit.app/?utm_medium=oembed)

### `textColor` and `linkColor`

You can configure the color of body text and links.

`textColor` sets the default text color for all text in the app except language-highlighting in code blocks, inline code, and links. `linkColor` sets the default font color for all Markdown links in the app.

The following elements are impacted by `textColor`:

* Markdown text, except links
* Text in code blocks that's not colored otherwise from language highlighting
* App-chrome and sidebar menu icons
* Widget labels, icons, option text, and placeholder text
* Dataframe and table text
* Non-Markdown links, like `st.page_link`, `st.link_button`, and the navigation menu

As noted previously, Streamlit changes the text color to white when text is displayed against your primary color.

#### Example 3: Text colors

The following configuration example has `"darkGoldenrod"` text and `"darkOrchid"` links on a `"dark"` base. Buttons (including `st.link_button`) use the `"darkGoldenrod"` text color. In the multiselect widget, the placeholder text, drop-down menu, and tooltip all have `"darkGoldenrod"` text. If you hover over the sidebar, the scrollbar and collapse icon (*chevron\_left*) are `"darkGoldenrod"`.

`[theme]
base="dark"
textColor="darkGoldenrod"
linkColor="darkOrchid"`

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen *open\_in\_new*](https://doc-theming-color-textcolor.streamlit.app/?utm_medium=oembed)

### `baseRadius` and `buttonRadius`

`baseRadius` defines the radius of borders and backgrounds for the following elements:

* Buttons and input areas on widgets
* Selected items, including items in `st.multiselect` and the navigation menu
* Code blocks and inline code
* Dataframes (exterior)
* Badges and Markdown-text backgrounds
* Containers with borders, including expanders, forms, dialogs, popovers, and toasts
* Tooltips, including tooltips within charts
* Status and exception message blocks
* Images, including `st.graphviz` and `st.pyplot`, which display as static images

`buttonRadius` overrides `baseRadius` for buttons and `st.segmented_control`.

A few elements are notably not fully affected by `baseRadius`. Interactive charts and videos, which have a more complex underlying HTML, will always have square corners. This includes `st.video`, `st.map`, and `st.pydeck_chart`. Conversely, `st.chat_input` and `st.audio_input` will always be fully rounded. Sub-elements like tooltips are still affected by `baseRadius`.

#### Example 4: Border radius

In the following configuration example, the main body of the app uses a `"full"` (1rem) base radius, and the sidebar uses `"none"` (0rem). To better highlight this difference, the example includes contrasting primary and background colors.

`[theme]
base="light"
primaryColor="slateBlue"
backgroundColor="mintCream"
secondaryBackgroundColor="darkSeaGreen"
baseRadius="full"
[theme.sidebar]
backgroundColor="aliceBlue"
secondaryBackgroundColor="skyBlue"
baseRadius="none"`

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen *open\_in\_new*](https://doc-theming-color-baseradius.streamlit.app/?utm_medium=oembed)

### `borderColor`, `dataframeBorderColor`, and `showWidgetBorder`

Streamlit does not display borders for unfocused widgets by default (except for buttons). When a user focuses on a widget, Streamlit displays a border around the input area in your `primaryColor`. When the user removes focus, Streamlit hides the border.

If you set `showWidgetBorder=true`, Streamlit will display widget borders when the widget is not in focus. For those widgets, the border color is set by `borderColor`. If `borderColor` is not set, Streamlit infers a color by adding transparency to your `textColor`.

The following elements have borders that you can modify:

* Containers with borders, including expanders, forms, dialogs, popovers, and toasts
* The sidebar, including the right edge and the boundary below the navigation menu
* Dataframes and tables
* `st.tabs` (bottom border)
* Buttons, including `st.button`, `st.pills`, and `st.segmented_control`
* Borders on input regions

`dataframeBorderColor` overrides `borderColor` for dataframes and tables.

#### Example 5: Border color and visibility

The following configuration example uses a `"mediumSlateBlue"` border color throughout the app. In the sidebar, widget borders are shown. In the main body of the app, widget borders are not shown, and there is no border around the multiselect, text, or chat input regions except when they are in focus. However, many other elements, like buttons and dataframes, have always-visible borders.

`[theme]
base="dark"
borderColor="mediumSlateBlue"
showWidgetBorder=false
[theme.sidebar]
showWidgetBorder=true`

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen *open\_in\_new*](https://doc-theming-color-bordercolor.streamlit.app/?utm_medium=oembed)

[Previous: Customize your theme](/develop/concepts/configuration/theming)[Next: Customize fonts](/develop/concepts/configuration/theming-customize-fonts)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
