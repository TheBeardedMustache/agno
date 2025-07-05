Text elements - Streamlit Docs

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
* [Text elements](/develop/api-reference/text)

Text elements
=============

Streamlit apps usually start with a call to `st.title` to set the
app's title. After that, there are 2 heading levels you can use:
`st.header` and `st.subheader`.

Pure text is entered with `st.text`, and Markdown with
`st.markdown`.

We also offer a "swiss-army knife" command called `st.write`, which accepts
multiple arguments, and multiple data types. And as described above, you can
also use [magic commands](/develop/api-reference/write-magic/magic) in place of `st.write`.

Headings and body text
----------------------

[![screenshot](/images/api/markdown.jpg)

#### Markdown

Display string formatted as Markdown.

`st.markdown("Hello **world**!")`](/develop/api-reference/text/st.markdown)[![screenshot](/images/api/title.jpg)

#### Title

Display text in title formatting.

`st.title("The app title")`](/develop/api-reference/text/st.title)[![screenshot](/images/api/header.jpg)

#### Header

Display text in header formatting.

`st.header("This is a header")`](/develop/api-reference/text/st.header)[![screenshot](/images/api/subheader.jpg)

#### Subheader

Display text in subheader formatting.

`st.subheader("This is a subheader")`](/develop/api-reference/text/st.subheader)

Formatted text
--------------

[![screenshot](/images/api/badge.jpg)

#### Badge

Display a small, colored badge.

`st.badge("New")`](/develop/api-reference/text/st.badge)[![screenshot](/images/api/caption.jpg)

#### Caption

Display text in small font.

`st.caption("This is written small caption text")`](/develop/api-reference/text/st.caption)[![screenshot](/images/api/code.jpg)

#### Code block

Display a code block with optional syntax highlighting.

`st.code("a = 1234")`](/develop/api-reference/text/st.code)[![screenshot](/images/api/code.jpg)

#### Echo

Display some code on the app, then execute it. Useful for tutorials.

`with st.echo():
st.write('This code will be printed')`](/develop/api-reference/text/st.echo)[![screenshot](/images/api/text.jpg)

#### Preformatted text

Write fixed-width and preformatted text.

`st.text("Hello world")`](/develop/api-reference/text/st.text)[![screenshot](/images/api/latex.jpg)

#### LaTeX

Display mathematical expressions formatted as LaTeX.

`st.latex("\int a x^2 \,dx")`](/develop/api-reference/text/st.latex)[![screenshot](/images/api/divider.jpg)

#### Divider

Display a horizontal rule.

`st.divider()`](/develop/api-reference/text/st.divider)

Utilities
---------

[#### Get help

Display object’s doc string, nicely formatted.

`st.help(st.write)
st.help(pd.DataFrame)`](/develop/api-reference/text/st.help)[#### Render HTML

Renders HTML strings to your app.

`st.html("<p>Foo bar.</p>")`](/develop/api-reference/text/st.html)

Third-party components

These are featured components created by our lovely community. For more examples and inspiration, check out our [Components Gallery](https://streamlit.io/components) and [Streamlit Extras](https://extras.streamlit.app)!

Previous

[![screenshot](/images/api/components/tags.jpg)

#### Tags

Add tags to your Streamlit apps. Created by [@gagan3012](https://github.com/gagan3012).

`st_tags(label='# Enter Keywords:', text='Press enter to add more', value=['Zero', 'One', 'Two'], suggestions=['five', 'six', 'seven', 'eight', 'nine', 'three', 'eleven', 'ten', 'four'], maxtags = 4, key='1')`](https://github.com/gagan3012/streamlit-tags)

[![screenshot](/images/api/components/nlu.jpg)

#### NLU

Apply text mining on a dataframe. Created by [@JohnSnowLabs](https://github.com/JohnSnowLabs/).

`nlu.load('sentiment').predict('I love NLU! <3')`](https://github.com/JohnSnowLabs/nlu)

[![screenshot](/images/api/components/extras-mentions.jpg)

#### Streamlit Extras

A library with useful Streamlit extras. Created by [@arnaudmiribel](https://github.com/arnaudmiribel/).

`mention(label="An awesome Streamlit App", icon="streamlit", url="https://extras.streamlit.app",)`](https://extras.streamlit.app/)

[![screenshot](/images/api/components/annotated-text.jpg)

#### Annotated text

Display annotated text in Streamlit apps. Created by [@tvst](https://github.com/tvst).

`annotated_text("This ", ("is", "verb"), " some ", ("annotated", "adj"), ("text", "noun"), " for those of ", ("you", "pronoun"), " who ", ("like", "verb"), " this sort of ", ("thing", "noun"), ".")`](https://github.com/tvst/st-annotated-text)

[![screenshot](/images/api/components/drawable-canvas.jpg)

#### Drawable Canvas

Provides a sketching canvas using [Fabric.js](http://fabricjs.com/). Created by [@andfanilo](https://github.com/andfanilo).

`st_canvas(fill_color="rgba(255, 165, 0, 0.3)", stroke_width=stroke_width, stroke_color=stroke_color, background_color=bg_color, background_image=Image.open(bg_image) if bg_image else None, update_streamlit=realtime_update, height=150, drawing_mode=drawing_mode, point_display_radius=point_display_radius if drawing_mode == 'point' else 0, key="canvas",)`](https://github.com/andfanilo/streamlit-drawable-canvas)

[![screenshot](/images/api/components/tags.jpg)

#### Tags

Add tags to your Streamlit apps. Created by [@gagan3012](https://github.com/gagan3012).

`st_tags(label='# Enter Keywords:', text='Press enter to add more', value=['Zero', 'One', 'Two'], suggestions=['five', 'six', 'seven', 'eight', 'nine', 'three', 'eleven', 'ten', 'four'], maxtags = 4, key='1')`](https://github.com/gagan3012/streamlit-tags)

[![screenshot](/images/api/components/nlu.jpg)

#### NLU

Apply text mining on a dataframe. Created by [@JohnSnowLabs](https://github.com/JohnSnowLabs/).

`nlu.load('sentiment').predict('I love NLU! <3')`](https://github.com/JohnSnowLabs/nlu)

[![screenshot](/images/api/components/extras-mentions.jpg)

#### Streamlit Extras

A library with useful Streamlit extras. Created by [@arnaudmiribel](https://github.com/arnaudmiribel/).

`mention(label="An awesome Streamlit App", icon="streamlit", url="https://extras.streamlit.app",)`](https://extras.streamlit.app/)

[![screenshot](/images/api/components/annotated-text.jpg)

#### Annotated text

Display annotated text in Streamlit apps. Created by [@tvst](https://github.com/tvst).

`annotated_text("This ", ("is", "verb"), " some ", ("annotated", "adj"), ("text", "noun"), " for those of ", ("you", "pronoun"), " who ", ("like", "verb"), " this sort of ", ("thing", "noun"), ".")`](https://github.com/tvst/st-annotated-text)

[![screenshot](/images/api/components/drawable-canvas.jpg)

#### Drawable Canvas

Provides a sketching canvas using [Fabric.js](http://fabricjs.com/). Created by [@andfanilo](https://github.com/andfanilo).

`st_canvas(fill_color="rgba(255, 165, 0, 0.3)", stroke_width=stroke_width, stroke_color=stroke_color, background_color=bg_color, background_image=Image.open(bg_image) if bg_image else None, update_streamlit=realtime_update, height=150, drawing_mode=drawing_mode, point_display_radius=point_display_radius if drawing_mode == 'point' else 0, key="canvas",)`](https://github.com/andfanilo/streamlit-drawable-canvas)

[![screenshot](/images/api/components/tags.jpg)

#### Tags

Add tags to your Streamlit apps. Created by [@gagan3012](https://github.com/gagan3012).

`st_tags(label='# Enter Keywords:', text='Press enter to add more', value=['Zero', 'One', 'Two'], suggestions=['five', 'six', 'seven', 'eight', 'nine', 'three', 'eleven', 'ten', 'four'], maxtags = 4, key='1')`](https://github.com/gagan3012/streamlit-tags)

[![screenshot](/images/api/components/nlu.jpg)

#### NLU

Apply text mining on a dataframe. Created by [@JohnSnowLabs](https://github.com/JohnSnowLabs/).

`nlu.load('sentiment').predict('I love NLU! <3')`](https://github.com/JohnSnowLabs/nlu)

[![screenshot](/images/api/components/extras-mentions.jpg)

#### Streamlit Extras

A library with useful Streamlit extras. Created by [@arnaudmiribel](https://github.com/arnaudmiribel/).

`mention(label="An awesome Streamlit App", icon="streamlit", url="https://extras.streamlit.app",)`](https://extras.streamlit.app/)

 Next

[Previous: Write and magic](/develop/api-reference/write-magic)[Next: st.title](/develop/api-reference/text/st.title)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
