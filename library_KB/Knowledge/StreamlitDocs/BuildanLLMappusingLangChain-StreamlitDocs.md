Build an LLM app using LangChain - Streamlit Docs

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

      *remove*

      * [Build a basic LLM chat app](/develop/tutorials/chat-and-llm-apps/build-conversational-apps)
      * [Build an LLM app using LangChain](/develop/tutorials/chat-and-llm-apps/llm-quickstart)
      * [Get chat response feedback](/develop/tutorials/chat-and-llm-apps/chat-response-feedback)
      * [Validate and edit chat responses](/develop/tutorials/chat-and-llm-apps/validate-and-edit-chat-responses)
    - [Configuration and theming](/develop/tutorials/configuration-and-theming)

      *add*
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
* [Chat and LLM apps](/develop/tutorials/chat-and-llm-apps)/
* [Build an LLM app using LangChain](/develop/tutorials/chat-and-llm-apps/llm-quickstart)

Build an LLM app using LangChain
================================

OpenAI, LangChain, and Streamlit in 18 lines of code
----------------------------------------------------

In this tutorial, you will build a Streamlit LLM app that can generate text from a user-provided prompt. This Python app will use the LangChain framework and Streamlit. Optionally, you can deploy your app to [Streamlit Community Cloud](https://streamlit.io/cloud) when you're done.

*This tutorial is adapted from a blog post by Chanin Nantesanamat: [LangChain tutorial #1: Build an LLM-powered app in 18 lines of code](https://blog.streamlit.io/langchain-tutorial-1-build-an-llm-powered-app-in-18-lines-of-code/).*

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen *open\_in\_new*](https://doc-tutorial-llm-18-lines-of-code.streamlit.app/?utm_medium=oembed)

Objectives
----------

1. Get an OpenAI key from the end user.
2. Validate the user's OpenAI key.
3. Get a text prompt from the user.
4. Authenticate OpenAI with the user's key.
5. Send the user's prompt to OpenAI's API.
6. Get a response and display it.

Bonus: Deploy the app on Streamlit Community Cloud!

Prerequisites
-------------

* Python 3.9+
* Streamlit
* LangChain
* [OpenAI API key](https://platform.openai.com/account/api-keys?ref=blog.streamlit.io)

Setup coding environment
------------------------

In your IDE (integrated coding environment), open the terminal and install the following two Python libraries:

`pip install streamlit langchain-openai`

Create a `requirements.txt` file located in the root of your working directory and save these dependencies. This is necessary for deploying the app to the Streamlit Community Cloud later.

`streamlit
openai
langchain`

Building the app
----------------

The app is only 18 lines of code:

`import streamlit as st
from langchain_openai.chat_models import ChatOpenAI
st.title("🦜🔗 Quickstart App")
openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")
def generate_response(input_text):
model = ChatOpenAI(temperature=0.7, api_key=openai_api_key)
st.info(model.invoke(input_text))
with st.form("my_form"):
text = st.text_area(
"Enter text:",
"What are the three key pieces of advice for learning how to code?",
)
submitted = st.form_submit_button("Submit")
if not openai_api_key.startswith("sk-"):
st.warning("Please enter your OpenAI API key!", icon="⚠")
if submitted and openai_api_key.startswith("sk-"):
generate_response(text)`

To start, create a new Python file and save it as `streamlit_app.py` in the root of your working directory.

1. Import the necessary Python libraries.

   `import streamlit as st
   from langchain_openai.chat_models import ChatOpenAI`
2. Create the app's title using `st.title`.

   `st.title("🦜🔗 Quickstart App")`
3. Add a text input box for the user to enter their OpenAI API key.

   `openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")`
4. Define a function to authenticate to OpenAI API with the user's key, send a prompt, and get an AI-generated response. This function accepts the user's prompt as an argument and displays the AI-generated response in a blue box using `st.info`.

   `def generate_response(input_text):
   model = ChatOpenAI(temperature=0.7, api_key=openai_api_key)
   st.info(model.invoke(input_text))`
5. Finally, use `st.form()` to create a text box (`st.text_area()`) for user input. When the user clicks `Submit`, the `generate-response()` function is called with the user's input as an argument.

   `with st.form("my_form"):
   text = st.text_area(
   "Enter text:",
   "What are the three key pieces of advice for learning how to code?",
   )
   submitted = st.form_submit_button("Submit")
   if not openai_api_key.startswith("sk-"):
   st.warning("Please enter your OpenAI API key!", icon="⚠")
   if submitted and openai_api_key.startswith("sk-"):
   generate_response(text)`
6. Remember to save your file!
7. Return to your computer's terminal to run the app.

   `streamlit run streamlit_app.py`

Deploying the app
-----------------

To deploy the app to the Streamlit Cloud, follow these steps:

1. Create a GitHub repository for the app. Your repository should contain two files:

   `your-repository/
   ├── streamlit_app.py
   └── requirements.txt`
2. Go to [Streamlit Community Cloud](http://share.streamlit.io), click the `New app` button from your workspace, then specify the repository, branch, and main file path. Optionally, you can customize your app's URL by choosing a custom subdomain.
3. Click the `Deploy!` button.

Your app will now be deployed to Streamlit Community Cloud and can be accessed from around the world! 🌎

Conclusion
----------

Congratulations on building an LLM-powered Streamlit app in 18 lines of code! 🥳 You can use this app to generate text from any prompt that you provide. The app is limited by the capabilities of the OpenAI LLM, but it can still be used to generate some creative and interesting text.

We hope you found this tutorial helpful! Check out [more examples](https://streamlit.io/generative-ai) to see the power of Streamlit and LLM. 💖

Happy Streamlit-ing! 🎈

[Previous: Build a basic LLM chat app](/develop/tutorials/chat-and-llm-apps/build-conversational-apps)[Next: Get chat response feedback](/develop/tutorials/chat-and-llm-apps/chat-response-feedback)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
