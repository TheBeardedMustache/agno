Managing dependencies when deploying your app - Streamlit Docs

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

    *add*
  + [Quick reference](/develop/quick-reference)

    *add*
* [*web\_asset*

  Deploy](/deploy)
  + [Concepts](/deploy/concepts)

    *remove*

    - [Dependencies](/deploy/concepts/dependencies)
    - [Secrets](/deploy/concepts/secrets)
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
* [Deploy](/deploy)/
* [Concepts](/deploy/concepts)/
* [Dependencies](/deploy/concepts/dependencies)

Managing dependencies when deploying your app
=============================================

Before you began developing your app, you set up and configured your development environment by installing Python and Streamlit. When you deploy your app, you need to set up and configure your deployment environment in the same way. When you deploy your app to a cloud service, your app's [Python server](/develop/concepts/architecture/architecture#python-backend-server) will be running on a remote machine. This remote machine will not have access all the files and programs on your personal computer.

All Streamlit apps have at least two dependencies: Python and Streamlit. Your app may have additional dependencies in the form of Python packages or software that must be installed to properly execute your script. If you are using a service like Streamlit Community Cloud which is designed for Streamlit apps, we'll take care of Python and Streamlit for you!

Install Python and other software
---------------------------------

If you are using Streamlit Community Cloud, Python is already installed. You can just pick the version in the deployment dialog. If you need to install Python yourself or you have other non-Python software to install, follow your platform's instructions to install additional software. You will commonly use a package management tool to do this.
For example, Streamlit Community Cloud uses Advanced Package Tool (`apt`) for Debian-based Linux systems. For more information about installing non-Python depencies on Streamlit Community Cloud, see [`apt-get` dependencies](/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies#apt-get-dependencies).

Install Python packages
-----------------------

Once you have Python installed in your deployment environment, you'll need to install all the necessary Python packages, including Streamlit! With each `import` of an installed package, you add a Python dependency to your script. You need to install those dependencies in your deployment environment through a Python package manager.

If you are using Streamlit Community Cloud, you'll have the latest version of Streamlit and all of its dependencies installed by default. So, if you're making a simple app and don't need additional dependencies, you won't have to do anything at all!

### `pip` and `requirements.txt`

Since `pip` comes by default with Python, the most common way to configure your Python environment is with a `requirements.txt` file. Each line of a `requirements.txt` file is a package to `pip install`. You should *not* include [built-in Python libraries](https://docs.python.org/3/py-modindex.html) like `math`, `random`, or `distutils` in your `requirements.txt` file. These are a part of Python and aren't installed separately.

*star*

#### Tip

Since dependencies may rely on a specific version of Python, always be aware of the Python version used in your development environment, and select the same version for your deployment environment.

If you have a script like the following, you would only need to install Streamlit. No extra dependencies would be needed since `pandas` and `numpy` are installed as direct dependencies of `streamlit`. Similarly, `math` and `random` are built into Python.

`import streamlit as st
import pandas as pd
import numpy as np
import math
import random
st.write('Hi!')`

However, it's a best practice accurately record packages you use, so the recommended `requirements.txt` file would be:

`streamlit
pandas
numpy`

If you needed to specify certain versions, another valid example would be:

`streamlit==1.24.1
pandas>2.0
numpy<=1.25.1`

A `requirements.txt` file is commonly saved in the root of your repository or file directory. If you are using Streamlit Community Cloud, see [Add Python dependencies](/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies#add-python-dependencies) for more information. Otherwise, check your platform's documentation.

[Previous: Concepts](/deploy/concepts)[Next: Secrets](/deploy/concepts/secrets)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
