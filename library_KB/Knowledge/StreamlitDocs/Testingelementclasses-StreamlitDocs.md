Testing element classes - Streamlit Docs

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

      *remove*

      * [st.testing.v1.AppTest](/develop/api-reference/app-testing/st.testing.v1.apptest)
      * [Testing element classes](/develop/api-reference/app-testing/testing-element-classes)
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
* [App testing](/develop/api-reference/app-testing)/
* [Testing element classes](/develop/api-reference/app-testing/testing-element-classes)

Testing element classes
=======================

st.testing.v1.element\_tree.Block
---------------------------------

The `Block` class has the same methods and attributes as `AppTest`. A `Block` instance represents a container of elements just as `AppTest` represents the entire app. For example, `Block.button` will produce a `WidgetList` of `Button` in the same manner as [`AppTest.button`](/develop/api-reference/testing/st.testing.v1.apptest#apptestbutton).

`ChatMessage`, `Column`, and `Tab` all inherit from `Block`. For all container classes, parameters of the original element can be obtained as properties. For example, `ChatMessage.avatar` and `Tab.label`.

st.testing.v1.element\_tree.Element
-----------------------------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Element base class for testing.

This class's methods and attributes are universal for all elements
implemented in testing. For example, Caption, Code, Text, and
Title inherit from Element. All widget classes also
inherit from Element, but have additional methods specific to each
widget type. See the AppTest class for the full list of supported
elements.

For all element classes, parameters of the original element can be obtained
as properties. For example, Button.label, Caption.help, and
Toast.icon.

| Class description[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/testing/v1/element_tree.py#L107 "View st.Element source code on GitHub") | |
| --- | --- |
| st.testing.v1.element\_tree.Element(proto, root) | |
|  |  |
| --- | --- |
| Methods | |
| [run](/develop/api-reference/app-testing/testing-element-classes#elementrun)(\*, timeout=None) | Run the AppTest script which contains the element. |
| Attributes | |
| [value](/develop/api-reference/app-testing/testing-element-classes#elementvalue) | The value or contents of the element. |

st.testing.v1.element\_tree.Button
----------------------------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

A representation of st.button and st.form\_submit\_button.

| Class description[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/testing/v1/element_tree.py#L303 "View st.Button source code on GitHub") | |
| --- | --- |
| st.testing.v1.element\_tree.Button(proto, root) | |
|  |  |
| --- | --- |
| Methods | |
| [click](/develop/api-reference/app-testing/testing-element-classes#buttonclick)() | Set the value of the button to True. |
| [run](/develop/api-reference/app-testing/testing-element-classes#buttonrun)(\*, timeout=None) | Run the AppTest script which contains the element. |
| [set\_value](/develop/api-reference/app-testing/testing-element-classes#buttonset_value)(v) | Set the value of the button. |
| Attributes | |
| [value](/develop/api-reference/app-testing/testing-element-classes#buttonvalue) | The value of the button. (bool) |

st.testing.v1.element\_tree.ChatInput
-------------------------------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

A representation of st.chat\_input.

| Class description[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/testing/v1/element_tree.py#L345 "View st.ChatInput source code on GitHub") | |
| --- | --- |
| st.testing.v1.element\_tree.ChatInput(proto, root) | |
|  |  |
| --- | --- |
| Methods | |
| [run](/develop/api-reference/app-testing/testing-element-classes#chatinputrun)(\*, timeout=None) | Run the AppTest script which contains the element. |
| [set\_value](/develop/api-reference/app-testing/testing-element-classes#chatinputset_value)(v) | Set the value of the widget. |
| Attributes | |
| [value](/develop/api-reference/app-testing/testing-element-classes#chatinputvalue) | The value of the widget. (str) |

st.testing.v1.element\_tree.Checkbox
------------------------------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

A representation of st.checkbox.

| Class description[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/testing/v1/element_tree.py#L380 "View st.Checkbox source code on GitHub") | |
| --- | --- |
| st.testing.v1.element\_tree.Checkbox(proto, root) | |
|  |  |
| --- | --- |
| Methods | |
| [check](/develop/api-reference/app-testing/testing-element-classes#checkboxcheck)() | Set the value of the widget to True. |
| [run](/develop/api-reference/app-testing/testing-element-classes#checkboxrun)(\*, timeout=None) | Run the AppTest script which contains the element. |
| [set\_value](/develop/api-reference/app-testing/testing-element-classes#checkboxset_value)(v) | Set the value of the widget. |
| [uncheck](/develop/api-reference/app-testing/testing-element-classes#checkboxuncheck)() | Set the value of the widget to False. |
| Attributes | |
| [value](/develop/api-reference/app-testing/testing-element-classes#checkboxvalue) | The value of the widget. (bool) |

st.testing.v1.element\_tree.ColorPicker
---------------------------------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

A representation of st.color\_picker.

| Class description[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/testing/v1/element_tree.py#L447 "View st.ColorPicker source code on GitHub") | |
| --- | --- |
| st.testing.v1.element\_tree.ColorPicker(proto, root) | |
|  |  |
| --- | --- |
| Methods | |
| [pick](/develop/api-reference/app-testing/testing-element-classes#colorpickerpick)(v) | Set the value of the widget as a hex string. May omit the "#" prefix. |
| [run](/develop/api-reference/app-testing/testing-element-classes#colorpickerrun)(\*, timeout=None) | Run the AppTest script which contains the element. |
| [set\_value](/develop/api-reference/app-testing/testing-element-classes#colorpickerset_value)(v) | Set the value of the widget as a hex string. |
| Attributes | |
| [value](/develop/api-reference/app-testing/testing-element-classes#colorpickervalue) | The currently selected value as a hex string. (str) |

st.testing.v1.element\_tree.DateInput
-------------------------------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

A representation of st.date\_input.

| Class description[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/testing/v1/element_tree.py#L513 "View st.DateInput source code on GitHub") | |
| --- | --- |
| st.testing.v1.element\_tree.DateInput(proto, root) | |
|  |  |
| --- | --- |
| Methods | |
| [run](/develop/api-reference/app-testing/testing-element-classes#dateinputrun)(\*, timeout=None) | Run the AppTest script which contains the element. |
| [set\_value](/develop/api-reference/app-testing/testing-element-classes#dateinputset_value)(v) | Set the value of the widget. |
| Attributes | |
| [value](/develop/api-reference/app-testing/testing-element-classes#dateinputvalue) | The value of the widget. (date or Tuple of date) |

st.testing.v1.element\_tree.Multiselect
---------------------------------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

A representation of st.multiselect.

| Class description[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/testing/v1/element_tree.py#L775 "View st.Multiselect source code on GitHub") | |
| --- | --- |
| st.testing.v1.element\_tree.Multiselect(proto, root) | |
|  |  |
| --- | --- |
| Methods | |
| [run](/develop/api-reference/app-testing/testing-element-classes#multiselectrun)(\*, timeout=None) | Run the AppTest script which contains the element. |
| [select](/develop/api-reference/app-testing/testing-element-classes#multiselectselect)(v) | Add a selection to the widget. Do nothing if the value is already selected. If testing a multiselect widget with repeated options, use set\_value instead. |
| [set\_value](/develop/api-reference/app-testing/testing-element-classes#multiselectset_value)(v) | Set the value of the multiselect widget. (list) |
| [unselect](/develop/api-reference/app-testing/testing-element-classes#multiselectunselect)(v) | Remove a selection from the widget. Do nothing if the value is not already selected. If a value is selected multiple times, the first instance is removed. |
| Attributes | |
| [format\_func](/develop/api-reference/app-testing/testing-element-classes#multiselectformat_func) | The widget's formatting function for displaying options. (callable) |
| [indices](/develop/api-reference/app-testing/testing-element-classes#multiselectindices) | The indices of the currently selected values from the options. (list) |
| [value](/develop/api-reference/app-testing/testing-element-classes#multiselectvalue) | The currently selected values from the options. (list) |
| [values](/develop/api-reference/app-testing/testing-element-classes#multiselectvalues) | The currently selected values from the options. (list) |

st.testing.v1.element\_tree.NumberInput
---------------------------------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

A representation of st.number\_input.

| Class description[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/testing/v1/element_tree.py#L868 "View st.NumberInput source code on GitHub") | |
| --- | --- |
| st.testing.v1.element\_tree.NumberInput(proto, root) | |
|  |  |
| --- | --- |
| Methods | |
| [decrement](/develop/api-reference/app-testing/testing-element-classes#numberinputdecrement)() | Decrement the st.number\_input widget as if the user clicked "-". |
| [increment](/develop/api-reference/app-testing/testing-element-classes#numberinputincrement)() | Increment the st.number\_input widget as if the user clicked "+". |
| [run](/develop/api-reference/app-testing/testing-element-classes#numberinputrun)(\*, timeout=None) | Run the AppTest script which contains the element. |
| [set\_value](/develop/api-reference/app-testing/testing-element-classes#numberinputset_value)(v) | Set the value of the st.number\_input widget. |
| Attributes | |
| [value](/develop/api-reference/app-testing/testing-element-classes#numberinputvalue) | Get the current value of the st.number\_input widget. |

st.testing.v1.element\_tree.Radio
---------------------------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

A representation of st.radio.

| Class description[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/testing/v1/element_tree.py#L929 "View st.Radio source code on GitHub") | |
| --- | --- |
| st.testing.v1.element\_tree.Radio(proto, root) | |
|  |  |
| --- | --- |
| Methods | |
| [run](/develop/api-reference/app-testing/testing-element-classes#radiorun)(\*, timeout=None) | Run the AppTest script which contains the element. |
| [set\_value](/develop/api-reference/app-testing/testing-element-classes#radioset_value)(v) | Set the selection by value. |
| Attributes | |
| [format\_func](/develop/api-reference/app-testing/testing-element-classes#radioformat_func) | The widget's formatting function for displaying options. (callable) |
| [index](/develop/api-reference/app-testing/testing-element-classes#radioindex) | The index of the current selection. (int) |
| [value](/develop/api-reference/app-testing/testing-element-classes#radiovalue) | The currently selected value from the options. (Any) |

st.testing.v1.element\_tree.SelectSlider
----------------------------------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

A representation of st.select\_slider.

| Class description[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/testing/v1/element_tree.py#L1059 "View st.SelectSlider source code on GitHub") | |
| --- | --- |
| st.testing.v1.element\_tree.SelectSlider(proto, root) | |
|  |  |
| --- | --- |
| Methods | |
| [run](/develop/api-reference/app-testing/testing-element-classes#selectsliderrun)(\*, timeout=None) | Run the AppTest script which contains the element. |
| [set\_range](/develop/api-reference/app-testing/testing-element-classes#selectsliderset_range)(lower, upper) | Set the ranged selection by values. |
| [set\_value](/develop/api-reference/app-testing/testing-element-classes#selectsliderset_value)(v) | Set the (single) selection by value. |
| Attributes | |
| [format\_func](/develop/api-reference/app-testing/testing-element-classes#selectsliderformat_func) | The widget's formatting function for displaying options. (callable) |
| [value](/develop/api-reference/app-testing/testing-element-classes#selectslidervalue) | The currently selected value or range. (Any or Sequence of Any) |

st.testing.v1.element\_tree.Selectbox
-------------------------------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

A representation of st.selectbox.

| Class description[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/testing/v1/element_tree.py#L988 "View st.Selectbox source code on GitHub") | |
| --- | --- |
| st.testing.v1.element\_tree.Selectbox(proto, root) | |
|  |  |
| --- | --- |
| Methods | |
| [run](/develop/api-reference/app-testing/testing-element-classes#selectboxrun)(\*, timeout=None) | Run the AppTest script which contains the element. |
| [select](/develop/api-reference/app-testing/testing-element-classes#selectboxselect)(v) | Set the selection by value. |
| [select\_index](/develop/api-reference/app-testing/testing-element-classes#selectboxselect_index)(index) | Set the selection by index. |
| [set\_value](/develop/api-reference/app-testing/testing-element-classes#selectboxset_value)(v) | Set the selection by value. |
| Attributes | |
| [format\_func](/develop/api-reference/app-testing/testing-element-classes#selectboxformat_func) | The widget's formatting function for displaying options. (callable) |
| [index](/develop/api-reference/app-testing/testing-element-classes#selectboxindex) | The index of the current selection. (int) |
| [value](/develop/api-reference/app-testing/testing-element-classes#selectboxvalue) | The currently selected value from the options. (Any) |

st.testing.v1.element\_tree.Slider
----------------------------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

A representation of st.slider.

| Class description[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/testing/v1/element_tree.py#L1119 "View st.Slider source code on GitHub") | |
| --- | --- |
| st.testing.v1.element\_tree.Slider(proto, root) | |
|  |  |
| --- | --- |
| Methods | |
| [run](/develop/api-reference/app-testing/testing-element-classes#sliderrun)(\*, timeout=None) | Run the AppTest script which contains the element. |
| [set\_range](/develop/api-reference/app-testing/testing-element-classes#sliderset_range)(lower, upper) | Set the ranged value of the slider. |
| [set\_value](/develop/api-reference/app-testing/testing-element-classes#sliderset_value)(v) | Set the (single) value of the slider. |
| Attributes | |
| [value](/develop/api-reference/app-testing/testing-element-classes#slidervalue) | The currently selected value or range. (Any or Sequence of Any) |

st.testing.v1.element\_tree.TextArea
------------------------------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

A representation of st.text\_area.

| Class description[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/testing/v1/element_tree.py#L1205 "View st.TextArea source code on GitHub") | |
| --- | --- |
| st.testing.v1.element\_tree.TextArea(proto, root) | |
|  |  |
| --- | --- |
| Methods | |
| [input](/develop/api-reference/app-testing/testing-element-classes#textareainput)(v) | Set the value of the widget only if the value does not exceed the maximum allowed characters. |
| [run](/develop/api-reference/app-testing/testing-element-classes#textarearun)(\*, timeout=None) | Run the AppTest script which contains the element. |
| [set\_value](/develop/api-reference/app-testing/testing-element-classes#textareaset_value)(v) | Set the value of the widget. |
| Attributes | |
| [value](/develop/api-reference/app-testing/testing-element-classes#textareavalue) | The current value of the widget. (str) |

st.testing.v1.element\_tree.TextInput
-------------------------------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

A representation of st.text\_input.

| Class description[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/testing/v1/element_tree.py#L1257 "View st.TextInput source code on GitHub") | |
| --- | --- |
| st.testing.v1.element\_tree.TextInput(proto, root) | |
|  |  |
| --- | --- |
| Methods | |
| [input](/develop/api-reference/app-testing/testing-element-classes#textinputinput)(v) | Set the value of the widget only if the value does not exceed the maximum allowed characters. |
| [run](/develop/api-reference/app-testing/testing-element-classes#textinputrun)(\*, timeout=None) | Run the AppTest script which contains the element. |
| [set\_value](/develop/api-reference/app-testing/testing-element-classes#textinputset_value)(v) | Set the value of the widget. |
| Attributes | |
| [value](/develop/api-reference/app-testing/testing-element-classes#textinputvalue) | The current value of the widget. (str) |

st.testing.v1.element\_tree.TimeInput
-------------------------------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

A representation of st.time\_input.

| Class description[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/testing/v1/element_tree.py#L1312 "View st.TimeInput source code on GitHub") | |
| --- | --- |
| st.testing.v1.element\_tree.TimeInput(proto, root) | |
|  |  |
| --- | --- |
| Methods | |
| [decrement](/develop/api-reference/app-testing/testing-element-classes#timeinputdecrement)() | Select the previous available time. |
| [increment](/develop/api-reference/app-testing/testing-element-classes#timeinputincrement)() | Select the next available time. |
| [run](/develop/api-reference/app-testing/testing-element-classes#timeinputrun)(\*, timeout=None) | Run the AppTest script which contains the element. |
| [set\_value](/develop/api-reference/app-testing/testing-element-classes#timeinputset_value)(v) | Set the value of the widget. |
| Attributes | |
| [value](/develop/api-reference/app-testing/testing-element-classes#timeinputvalue) | The current value of the widget. (time) |

st.testing.v1.element\_tree.Toggle
----------------------------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

A representation of st.toggle.

| Class description[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/testing/v1/element_tree.py#L1385 "View st.Toggle source code on GitHub") | |
| --- | --- |
| st.testing.v1.element\_tree.Toggle(proto, root) | |
|  |  |
| --- | --- |
| Methods | |
| [run](/develop/api-reference/app-testing/testing-element-classes#togglerun)(\*, timeout=None) | Run the AppTest script which contains the element. |
| [set\_value](/develop/api-reference/app-testing/testing-element-classes#toggleset_value)(v) | Set the value of the widget. |
| Attributes | |
| [value](/develop/api-reference/app-testing/testing-element-classes#togglevalue) | The current value of the widget. (bool) |

[Previous: st.testing.v1.AppTest](/develop/api-reference/app-testing/st.testing.v1.apptest)[Next: Command line](/develop/api-reference/cli)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
