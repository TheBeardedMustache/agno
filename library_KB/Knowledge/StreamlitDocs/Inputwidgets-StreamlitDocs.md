Input widgets - Streamlit Docs

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

      *remove*

      * BUTTONS

        ---
      * [st.button](/develop/api-reference/widgets/st.button)
      * [st.download\_button](/develop/api-reference/widgets/st.download_button)
      * [st.form\_submit\_button*link*](/develop/api-reference/execution-flow/st.form_submit_button)
      * [st.link\_button](/develop/api-reference/widgets/st.link_button)
      * [st.page\_link](/develop/api-reference/widgets/st.page_link)
      * SELECTIONS

        ---
      * [st.checkbox](/develop/api-reference/widgets/st.checkbox)
      * [st.color\_picker](/develop/api-reference/widgets/st.color_picker)
      * [st.feedback](/develop/api-reference/widgets/st.feedback)
      * [st.multiselect](/develop/api-reference/widgets/st.multiselect)
      * [st.pills](/develop/api-reference/widgets/st.pills)
      * [st.radio](/develop/api-reference/widgets/st.radio)
      * [st.segmented\_control](/develop/api-reference/widgets/st.segmented_control)
      * [st.selectbox](/develop/api-reference/widgets/st.selectbox)
      * [st.select\_slider](/develop/api-reference/widgets/st.select_slider)
      * [st.toggle](/develop/api-reference/widgets/st.toggle)
      * NUMERIC

        ---
      * [st.number\_input](/develop/api-reference/widgets/st.number_input)
      * [st.slider](/develop/api-reference/widgets/st.slider)
      * DATE AND TIME

        ---
      * [st.date\_input](/develop/api-reference/widgets/st.date_input)
      * [st.time\_input](/develop/api-reference/widgets/st.time_input)
      * TEXT

        ---
      * [st.chat\_input*link*](/develop/api-reference/chat/st.chat_input)
      * [st.text\_area](/develop/api-reference/widgets/st.text_area)
      * [st.text\_input](/develop/api-reference/widgets/st.text_input)
      * MEDIA AND FILES

        ---
      * [st.audio\_input](/develop/api-reference/widgets/st.audio_input)
      * [st.camera\_input](/develop/api-reference/widgets/st.camera_input)
      * [st.data\_editor*link*](/develop/api-reference/data/st.data_editor)
      * [st.file\_uploader](/develop/api-reference/widgets/st.file_uploader)
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
* [Input widgets](/develop/api-reference/widgets)

Input widgets
=============

With widgets, Streamlit allows you to bake interactivity directly into your apps with buttons, sliders, text inputs, and more.

Button elements
---------------

[![screenshot](/images/api/button.svg)

#### Button

Display a button widget.

`clicked = st.button("Click me")`](/develop/api-reference/widgets/st.button)[![screenshot](/images/api/download_button.svg)

#### Download button

Display a download button widget.

`st.download_button("Download file", file)`](/develop/api-reference/widgets/st.download_button)[![screenshot](/images/api/form_submit_button.svg)

#### Form button

Display a form submit button. For use with `st.form`.

`st.form_submit_button("Sign up")`](/develop/api-reference/execution-flow/st.form_submit_button)[![screenshot](/images/api/link_button.svg)

#### Link button

Display a link button.

`st.link_button("Go to gallery", url)`](/develop/api-reference/widgets/st.link_button)[![screenshot](/images/api/page_link.jpg)

#### Page link

Display a link to another page in a multipage app.

`st.page_link("app.py", label="Home", icon="🏠")
st.page_link("pages/profile.py", label="My profile")`](/develop/api-reference/widgets/st.page_link)

Selection elements
------------------

[![screenshot](/images/api/checkbox.jpg)

#### Checkbox

Display a checkbox widget.

`selected = st.checkbox("I agree")`](/develop/api-reference/widgets/st.checkbox)[![screenshot](/images/api/color_picker.jpg)

#### Color picker

Display a color picker widget.

`color = st.color_picker("Pick a color")`](/develop/api-reference/widgets/st.color_picker)[![screenshot](/images/api/feedback.jpg)

#### Feedback

Display a rating or sentiment button group.

`st.feedback("stars")`](/develop/api-reference/widgets/st.feedback)[![screenshot](/images/api/multiselect.jpg)

#### Multiselect

Display a multiselect widget. The multiselect widget starts as empty.

`choices = st.multiselect("Buy", ["milk", "apples", "potatoes"])`](/develop/api-reference/widgets/st.multiselect)[![screenshot](/images/api/pills.jpg)

#### Pills

Display a pill-button selection widget.

`st.pills("Tags", ["Sports", "AI", "Politics"])`](/develop/api-reference/widgets/st.pills)[![screenshot](/images/api/radio.jpg)

#### Radio

Display a radio button widget.

`choice = st.radio("Pick one", ["cats", "dogs"])`](/develop/api-reference/widgets/st.radio)[![screenshot](/images/api/segmented_control.jpg)

#### Segmented control

Display a segmented-button selection widget.

`st.segmented_control("Filter", ["Open", "Closed", "All"])`](/develop/api-reference/widgets/st.segmented_control)[![screenshot](/images/api/select_slider.jpg)

#### Select slider

Display a slider widget to select items from a list.

`size = st.select_slider("Pick a size", ["S", "M", "L"])`](/develop/api-reference/widgets/st.select_slider)[![screenshot](/images/api/selectbox.jpg)

#### Selectbox

Display a select widget.

`choice = st.selectbox("Pick one", ["cats", "dogs"])`](/develop/api-reference/widgets/st.selectbox)[![screenshot](/images/api/toggle.jpg)

#### Toggle

Display a toggle widget.

`activated = st.toggle("Activate")`](/develop/api-reference/widgets/st.toggle)

Numeric input elements
----------------------

[![screenshot](/images/api/number_input.jpg)

#### Number input

Display a numeric input widget.

`choice = st.number_input("Pick a number", 0, 10)`](/develop/api-reference/widgets/st.number_input)[![screenshot](/images/api/slider.jpg)

#### Slider

Display a slider widget.

`number = st.slider("Pick a number", 0, 100)`](/develop/api-reference/widgets/st.slider)

Date and time input elements
----------------------------

[![screenshot](/images/api/date_input.jpg)

#### Date input

Display a date input widget.

`date = st.date_input("Your birthday")`](/develop/api-reference/widgets/st.date_input)[![screenshot](/images/api/time_input.jpg)

#### Time input

Display a time input widget.

`time = st.time_input("Meeting time")`](/develop/api-reference/widgets/st.time_input)

Text input elements
-------------------

[![screenshot](/images/api/text_input.jpg)

#### Text input

Display a single-line text input widget.

`name = st.text_input("First name")`](/develop/api-reference/widgets/st.text_input)[![screenshot](/images/api/text_area.jpg)

#### Text area

Display a multi-line text input widget.

`text = st.text_area("Text to translate")`](/develop/api-reference/widgets/st.text_area)[![screenshot](/images/api/chat_input.jpg)

#### Chat input

Display a chat input widget.

`prompt = st.chat_input("Say something")
if prompt:
st.write(f"The user has sent: {prompt}")`](/develop/api-reference/chat/st.chat_input)

Other input elements
--------------------

[![screenshot](/images/api/audio_input.jpg)

#### Audio input

Display a widget that allows users to record with their microphone.

`speech = st.audio_input("Record a voice message")`](/develop/api-reference/widgets/st.audio_input)[![screenshot](/images/api/data_editor.jpg)

#### Data editor

Display a data editor widget.

`edited = st.data_editor(df, num_rows="dynamic")`](/develop/api-reference/data/st.data_editor)[![screenshot](/images/api/file_uploader.jpg)

#### File uploader

Display a file uploader widget.

`data = st.file_uploader("Upload a CSV")`](/develop/api-reference/widgets/st.file_uploader)[![screenshot](/images/api/camera_input.jpg)

#### Camera input

Display a widget that allows users to upload images directly from a camera.

`image = st.camera_input("Take a picture")`](/develop/api-reference/widgets/st.camera_input)

Third-party components

These are featured components created by our lovely community. For more examples and inspiration, check out our [Components Gallery](https://streamlit.io/components) and [Streamlit Extras](https://extras.streamlit.app)!

Previous

[![screenshot](/images/api/components/chat.jpg)

#### Streamlit Chat

Streamlit Component for a Chatbot UI. Created by [@AI-Yash](https://github.com/AI-Yash).

`from streamlit_chat import message
message("My message")
message("Hello bot!", is_user=True) # align's the message to the right`](https://github.com/AI-Yash/st-chat)

[![screenshot](/images/api/components/option-menu.jpg)

#### Streamlit Option Menu

Select a single item from a list of options in a menu. Created by [@victoryhb](https://github.com/victoryhb).

`from streamlit_option_menu import option_menu
option_menu("Main Menu", ["Home", 'Settings'],
icons=['house', 'gear'], menu_icon="cast", default_index=1)`](https://github.com/victoryhb/streamlit-option-menu)

[![screenshot](/images/api/components/extras-toggle.jpg)

#### Streamlit Extras

A library with useful Streamlit extras. Created by [@arnaudmiribel](https://github.com/arnaudmiribel/).

`from streamlit_extras.stoggle import stoggle
stoggle(
"Click me!", """🥷 Surprise! Here's some additional content""",)`](https://extras.streamlit.app/)

[![screenshot](/images/api/components/elements.jpg)

#### Streamlit Elements

Create a draggable and resizable dashboard in Streamlit. Created by [@okls](https://github.com/okls).

`from streamlit_elements import elements, mui, html
with elements("new_element"):
mui.Typography("Hello world")`](https://github.com/okld/streamlit-elements)

[![screenshot](/images/api/components/tags.jpg)

#### Tags

Add tags to your Streamlit apps. Created by [@gagan3012](https://github.com/gagan3012).

`from streamlit_tags import st_tags
st_tags(label='# Enter Keywords:', text='Press enter to add more', value=['Zero', 'One', 'Two'],
suggestions=['five', 'six', 'seven', 'eight', 'nine', 'three', 'eleven', 'ten', 'four'], maxtags = 4, key='1')`](https://github.com/gagan3012/streamlit-tags)

[![screenshot](/images/api/components/stqdm.jpg)

#### Stqdm

The simplest way to handle a progress bar in streamlit app. Created by [@Wirg](https://github.com/Wirg).

`from stqdm import stqdm
for _ in stqdm(range(50)):
sleep(0.5)`](https://github.com/Wirg/stqdm)

[![screenshot](/images/api/components/timeline.jpg)

#### Timeline

Display a Timeline in Streamlit apps using [TimelineJS](https://timeline.knightlab.com/). Created by [@innerdoc](https://github.com/innerdoc).

`from streamlit_timeline import timeline
with open('example.json', "r") as f:
timeline(f.read(), height=800)`](https://github.com/innerdoc/streamlit-timeline)

[![screenshot](/images/api/components/camera-live.jpg)

#### Camera input live

Alternative for st.camera\_input which returns the webcam images live. Created by [@blackary](https://github.com/blackary).

`from camera_input_live import camera_input_live
image = camera_input_live()
st.image(value)`](https://github.com/blackary/streamlit-camera-input-live)

[![screenshot](/images/api/components/ace.jpg)

#### Streamlit Ace

Ace editor component for Streamlit. Created by [@okld](https://github.com/okld).

`from streamlit_ace import st_ace
content = st_ace()
content`](https://github.com/okld/streamlit-ace)

[![screenshot](/images/api/components/chat.jpg)

#### Streamlit Chat

Streamlit Component for a Chatbot UI. Created by [@AI-Yash](https://github.com/AI-Yash).

`from streamlit_chat import message
message("My message")
message("Hello bot!", is_user=True) # align's the message to the right`](https://github.com/AI-Yash/st-chat)

[![screenshot](/images/api/components/option-menu.jpg)

#### Streamlit Option Menu

Select a single item from a list of options in a menu. Created by [@victoryhb](https://github.com/victoryhb).

`from streamlit_option_menu import option_menu
option_menu("Main Menu", ["Home", 'Settings'],
icons=['house', 'gear'], menu_icon="cast", default_index=1)`](https://github.com/victoryhb/streamlit-option-menu)

[![screenshot](/images/api/components/extras-toggle.jpg)

#### Streamlit Extras

A library with useful Streamlit extras. Created by [@arnaudmiribel](https://github.com/arnaudmiribel/).

`from streamlit_extras.stoggle import stoggle
stoggle(
"Click me!", """🥷 Surprise! Here's some additional content""",)`](https://extras.streamlit.app/)

[![screenshot](/images/api/components/elements.jpg)

#### Streamlit Elements

Create a draggable and resizable dashboard in Streamlit. Created by [@okls](https://github.com/okls).

`from streamlit_elements import elements, mui, html
with elements("new_element"):
mui.Typography("Hello world")`](https://github.com/okld/streamlit-elements)

[![screenshot](/images/api/components/tags.jpg)

#### Tags

Add tags to your Streamlit apps. Created by [@gagan3012](https://github.com/gagan3012).

`from streamlit_tags import st_tags
st_tags(label='# Enter Keywords:', text='Press enter to add more', value=['Zero', 'One', 'Two'],
suggestions=['five', 'six', 'seven', 'eight', 'nine', 'three', 'eleven', 'ten', 'four'], maxtags = 4, key='1')`](https://github.com/gagan3012/streamlit-tags)

[![screenshot](/images/api/components/stqdm.jpg)

#### Stqdm

The simplest way to handle a progress bar in streamlit app. Created by [@Wirg](https://github.com/Wirg).

`from stqdm import stqdm
for _ in stqdm(range(50)):
sleep(0.5)`](https://github.com/Wirg/stqdm)

[![screenshot](/images/api/components/timeline.jpg)

#### Timeline

Display a Timeline in Streamlit apps using [TimelineJS](https://timeline.knightlab.com/). Created by [@innerdoc](https://github.com/innerdoc).

`from streamlit_timeline import timeline
with open('example.json', "r") as f:
timeline(f.read(), height=800)`](https://github.com/innerdoc/streamlit-timeline)

[![screenshot](/images/api/components/camera-live.jpg)

#### Camera input live

Alternative for st.camera\_input which returns the webcam images live. Created by [@blackary](https://github.com/blackary).

`from camera_input_live import camera_input_live
image = camera_input_live()
st.image(value)`](https://github.com/blackary/streamlit-camera-input-live)

[![screenshot](/images/api/components/ace.jpg)

#### Streamlit Ace

Ace editor component for Streamlit. Created by [@okld](https://github.com/okld).

`from streamlit_ace import st_ace
content = st_ace()
content`](https://github.com/okld/streamlit-ace)

[![screenshot](/images/api/components/chat.jpg)

#### Streamlit Chat

Streamlit Component for a Chatbot UI. Created by [@AI-Yash](https://github.com/AI-Yash).

`from streamlit_chat import message
message("My message")
message("Hello bot!", is_user=True) # align's the message to the right`](https://github.com/AI-Yash/st-chat)

[![screenshot](/images/api/components/option-menu.jpg)

#### Streamlit Option Menu

Select a single item from a list of options in a menu. Created by [@victoryhb](https://github.com/victoryhb).

`from streamlit_option_menu import option_menu
option_menu("Main Menu", ["Home", 'Settings'],
icons=['house', 'gear'], menu_icon="cast", default_index=1)`](https://github.com/victoryhb/streamlit-option-menu)

[![screenshot](/images/api/components/extras-toggle.jpg)

#### Streamlit Extras

A library with useful Streamlit extras. Created by [@arnaudmiribel](https://github.com/arnaudmiribel/).

`from streamlit_extras.stoggle import stoggle
stoggle(
"Click me!", """🥷 Surprise! Here's some additional content""",)`](https://extras.streamlit.app/)

 Next

[Previous: Chart elements](/develop/api-reference/charts)[Next: st.button](/develop/api-reference/widgets/st.button)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
