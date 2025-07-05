Use variable font files to customize your font - Streamlit Docs

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

    *add*
  + [Tutorials](/develop/tutorials)

    *remove*

    - [Authentication and personalization](/develop/tutorials/authentication)

      *add*
    - [Chat and LLM apps](/develop/tutorials/chat-and-llm-apps)

      *add*
    - [Configuration and theming](/develop/tutorials/configuration-and-theming)

      *remove*

      * [Use static font files](/develop/tutorials/configuration-and-theming/static-fonts)
      * [Use variable font files](/develop/tutorials/configuration-and-theming/variable-fonts)
    - [Connect to data sources](/develop/tutorials/databases)

      *add*
    - [Elements](/develop/tutorials/elements)

      *add*
    - [Execution flow](/develop/tutorials/execution-flow)

      *add*
    - [Multipage apps](/develop/tutorials/multipage)

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
* [Tutorials](/develop/tutorials)/
* [Configuration and theming](/develop/tutorials/configuration-and-theming)/
* [Use variable font files](/develop/tutorials/configuration-and-theming/variable-fonts)

Use variable font files to customize your font
==============================================

Streamlit comes with Source Sans as the default font, but you can configure your app to use another font. This tutorial uses variable font files and is a walkthrough of Example 1 from [Customize fonts in your Streamlit app](/develop/concepts/configuration/theming-customize-fonts#example-1-define-an-alternative-font-with-variable-font-files). For an example that uses static font files, see [Use static font files to customize your font](/develop/tutorials/configuration-and-theming/static-fonts).

Prerequisites
-------------

* This tutorial requires the following version of Streamlit:

  `streamlit>=1.45.0`
* You should have a clean working directory called `your-repository`.
* You should have a basic understanding of [static file serving](/develop/concepts/configuration/serving-static-files).
* You should have a basic understanding of working with font files in web development. Otherwise, start by reading [Customize fonts in your Streamlit app](/develop/concepts/configuration/theming-customize-fonts) up to Example 1.

Summary
-------

The following example uses static file serving to host Google's [Noto Sans](https://fonts.google.com/noto/specimen/Noto+Sans) and [Noto Sans Mono](https://fonts.google.com/noto/specimen/Noto+Sans+Mono) fonts and configures the app to use them. Both of these fonts are defined with variable font files that include a parameterized weight. However, because font style is not parameterized, Noto Sans requires two files to define the normal and italic styles separately. Noto Sans Mono does not include a separate file for its italic style. Per [CSS rules](https://developer.mozilla.org/en-US/docs/Web/CSS/font-style#italic), because no italic style is explicitly provided, it will be simulated by skewing the normal-style font.

Here's a look at what you'll build:

Complete config.toml file*expand\_more*

Directory structure:

`your_repository/
├── .streamlit/
│ └── config.toml
├── static/
│ ├── NotoSans-Italic-VariableFont_wdth,wght.ttf
│ ├── NotoSans-VariableFont_wdth,wght.ttf
│ └── NotoSansMono-VariableFont_wdth,wght.ttf
└── streamlit_app.py`

`.streamlit/config.toml`:

`[server]
enableStaticServing = true
[[theme.fontFaces]]
family="noto-sans"
url="app/static/NotoSans-Italic-VariableFont_wdth,wght.ttf"
style="italic"
[[theme.fontFaces]]
family="noto-sans"
url="app/static/NotoSans-VariableFont_wdth,wght.ttf"
style="normal"
[[theme.fontFaces]]
family="noto-mono"
url="app/static/NotoSansMono-VariableFont_wdth,wght.ttf"
[theme]
font="noto-sans"
codeFont="noto-mono"`

`streamlit_app.py`:

`import streamlit as st
st.write("Normal efg")
st.write("_Italic efg_")
st.write("*Bold efg*")
st.write("***Bold-italic efg***")
st.write("`Code efg`")`

Download and save your font files
---------------------------------

1. Go to [Google fonts](https://fonts.google.com/).
2. Search for or follow the link to [Noto Sans](https://fonts.google.com/noto/specimen/Noto+Sans), and select "**Get font**."
3. Search for or follow the link to [Noto Sans Mono](https://fonts.google.com/noto/specimen/Noto+Sans+Mono), and select "**Get font**."
4. To download your font files, in the upper-right corner, select the shopping bag (*shopping\_bag*), and then select "*download* **Download all**."
5. In your downloads directory, unzip the downloaded file.
6. From the unzipped files, copy and save the TTF font files into a `static/` directory in `your_repository/`.

   Copy the following files:

   `Noto_Sans,Noto_Sans_Mono/
   ├── Noto_Sans_Mono/
   │ └── NotoSansMono-VariableFont_wdth,wght.ttf
   └── Noto_Sans/
   ├── NotoSans-Italic-VariableFont_wdth,wght.ttf
   └── NotoSans-VariableFont_wdth,wght.ttf`

   Save those files in your repository:

   `your_repository/
   └── static/
   ├── NotoSans-Italic-VariableFont_wdth,wght.ttf
   ├── NotoSans-VariableFont_wdth,wght.ttf
   └── NotoSansMono-VariableFont_wdth,wght.ttf`

   In this example, the font files are `NotoSans-Italic-VariableFont_wdth,wght.ttf` and `NotoSansMono-VariableFont_wdth,wght.ttf` for Noto Sans italic and normal font, respectively. `NotoSansMono-VariableFont_wdth,wght.ttf` is the file for Noto Sans Mono.

Create your app configuration
-----------------------------

1. In `your_repository/`, create a `.streamlit/config.toml` file:

   `your_repository/
   ├── .streamlit/
   │ └── config.toml
   └── static/
   ├── NotoSans-Italic-VariableFont_wdth,wght.ttf
   ├── NotoSans-VariableFont_wdth,wght.ttf
   └── NotoSansMono-VariableFont_wdth,wght.ttf`
2. To enable static file serving, in `.streamlit/config.toml`, add the following text:

   `[server]
   enableStaticServing = true`

   This makes the files in your `static/` directory publicly available through your app's URL at the relative path `app/static/{filename}`.
3. To define your alternative fonts, in `.streamlit/config.toml`, add the following text:

   `[[theme.fontFaces]]
   family="noto-sans"
   url="app/static/NotoSans-Italic-VariableFont_wdth,wght.ttf"
   style="italic"
   [[theme.fontFaces]]
   family="noto-sans"
   url="app/static/NotoSans-VariableFont_wdth,wght.ttf"
   style="normal"
   [[theme.fontFaces]]
   family="noto-mono"
   url="app/static/NotoSansMono-VariableFont_wdth,wght.ttf"`

   The `[[theme.fontFaces]]` table can be repeated to use multiple files to define a single font or to define multiple fonts. In this example, the definitions make `"noto-sans"` and `"noto-mono"` available to other font configuration options.

   *star*

   #### Tip

   For convenience, avoid spaces in your font family names. When you declare the default font, you can also declare fallback fonts. If you avoid spaces in your font family names, you don't need inner quotes.
4. To set your alternative fonts as the default font for your app, in `.streamlit/config.toml`, add the following text:

   `[theme]
   font="noto-sans"
   codeFont="noto-mono"`

   This sets Noto Sans as the default for all text in your app except inline code and code blocks, which will be Noto Sans Mono instead.

Build the example
-----------------

To verify that your font is loaded correctly, create a simple app.

### Initialize your app

1. In your\_repository, create a file named `streamlit_app.py`.
2. In a terminal, change directories to your\_repository, and start your app:

   `streamlit run app.py`

   Your app will be blank because you still need to add code.
3. In `streamlit_app.py`, write the following:

   `import streamlit as st`
4. Save your `streamlit_app.py` file, and view your running app.
5. In your app, select "**Always rerun**", or press the "**A**" key.

   Your preview will be blank but will automatically update as you save changes to `streamlit_app.py`.
6. Return to your code.

### Display some text in your app

1. Create a `streamlit_app.py` file in your working directory.
2. In `streamlit_app.py`, add the following text:

   `import streamlit as st
   st.write("Normal efg")
   st.write("_Italic efg_")
   st.write("*Bold efg*")
   st.write("***Bold-italic efg***")
   st.write("`Code efg`")`

   The example includes "efg" in each line to better show the typographical differences when you run your app. The italic "f" descends below baseline, but the normal "f" doesn't. The italic "e" has a rounded front, but the normal "e" has a sharp corner.
3. Save your `streamlit_app.py` file, and view your running app.

[Previous: Use static font files](/develop/tutorials/configuration-and-theming/static-fonts)[Next: Connect to data sources](/develop/tutorials/databases)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
