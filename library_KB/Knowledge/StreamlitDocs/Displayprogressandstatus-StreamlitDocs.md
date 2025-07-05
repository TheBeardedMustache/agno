Display progress and status - Streamlit Docs

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

      *remove*

      * CALLOUTS

        ---
      * [st.success](/develop/api-reference/status/st.success)
      * [st.info](/develop/api-reference/status/st.info)
      * [st.warning](/develop/api-reference/status/st.warning)
      * [st.error](/develop/api-reference/status/st.error)
      * [st.exception](/develop/api-reference/status/st.exception)
      * OTHER

        ---
      * [st.progress](/develop/api-reference/status/st.progress)
      * [st.spinner](/develop/api-reference/status/st.spinner)
      * [st.status](/develop/api-reference/status/st.status)
      * [st.toast](/develop/api-reference/status/st.toast)
      * [st.balloons](/develop/api-reference/status/st.balloons)
      * [st.snow](/develop/api-reference/status/st.snow)
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
* [Status elements](/develop/api-reference/status)

Display progress and status
===========================

Streamlit provides a few methods that allow you to add animation to your
apps. These animations include progress bars, status messages (like
warnings), and celebratory balloons.

Animated status elements
------------------------

[![screenshot](/images/api/progress.jpg)

#### Progress bar

Display a progress bar.

`for i in range(101):
st.progress(i)
do_something_slow()`](/develop/api-reference/status/st.progress)[![screenshot](/images/api/spinner.jpg)

#### Spinner

Temporarily displays a message while executing a block of code.

`with st.spinner("Please wait..."):
do_something_slow()`](/develop/api-reference/status/st.spinner)[![screenshot](/images/api/status.jpg)

#### Status container

Display output of long-running tasks in a container.

`with st.status('Running'):
do_something_slow()`](/develop/api-reference/status/st.status)[![screenshot](/images/api/toast.jpg)

#### Toast

Briefly displays a toast message in the bottom-right corner.

`st.toast('Butter!', icon='🧈')`](/develop/api-reference/status/st.toast)[![screenshot](/images/api/balloons.jpg)

#### Balloons

Display celebratory balloons!

`st.balloons()`](/develop/api-reference/status/st.balloons)[![screenshot](/images/api/snow.jpg)

#### Snowflakes

Display celebratory snowflakes!

`st.snow()`](/develop/api-reference/status/st.snow)

Simple callout messages
-----------------------

[![screenshot](/images/api/success.jpg)

#### Success box

Display a success message.

`st.success("Match found!")`](/develop/api-reference/status/st.success)[![screenshot](/images/api/info.jpg)

#### Info box

Display an informational message.

`st.info("Dataset is updated every day at midnight.")`](/develop/api-reference/status/st.info)[![screenshot](/images/api/warning.jpg)

#### Warning box

Display warning message.

`st.warning("Unable to fetch image. Skipping...")`](/develop/api-reference/status/st.warning)[![screenshot](/images/api/error.jpg)

#### Error box

Display error message.

`st.error("We encountered an error")`](/develop/api-reference/status/st.error)[![screenshot](/images/api/exception.jpg)

#### Exception output

Display an exception.

`e = RuntimeError("This is an exception of type RuntimeError")
st.exception(e)`](/develop/api-reference/status/st.exception)

Third-party components

These are featured components created by our lovely community. For more examples and inspiration, check out our [Components Gallery](https://streamlit.io/components) and [Streamlit Extras](https://extras.streamlit.app)!

[![screenshot](/images/api/components/stqdm.jpg)

#### Stqdm

The simplest way to handle a progress bar in streamlit app. Created by [@Wirg](https://github.com/Wirg).

`from stqdm import stqdm
for _ in stqdm(range(50)):
sleep(0.5)`](https://github.com/Wirg/stqdm)

[![screenshot](/images/api/components/custom-notification-box.jpg)

#### Custom notification box

A custom notification box with the ability to close it out. Created by [@Socvest](https://github.com/Socvest).

`from streamlit_custom_notification_box import custom_notification_box
styles = {'material-icons':{'color': 'red'}, 'text-icon-link-close-container': {'box-shadow': '#3896de 0px 4px'}, 'notification-text': {'':''}, 'close-button':{'':''}, 'link':{'':''}}
custom_notification_box(icon='info', textDisplay='We are almost done with your registration...', externalLink='more info', url='#', styles=styles, key="foo")`](https://github.com/Socvest/streamlit-custom-notification-box)

[![screenshot](/images/api/components/extras-emojis.jpg)

#### Streamlit Extras

A library with useful Streamlit extras. Created by [@arnaudmiribel](https://github.com/arnaudmiribel/).

`from streamlit_extras.let_it_rain import rain
rain(emoji="🎈", font_size=54,
falling_speed=5, animation_length="infinite",)`](https://extras.streamlit.app/)

[Previous: Chat elements](/develop/api-reference/chat)[Next: st.success](/develop/api-reference/status/st.success)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
