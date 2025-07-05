App dependencies for your Community Cloud app - Streamlit Docs

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

    *add*
  + [Streamlit Community Cloud](/deploy/streamlit-community-cloud)

    *remove*

    - [Get started](/deploy/streamlit-community-cloud/get-started)

      *add*
    - [Deploy your app](/deploy/streamlit-community-cloud/deploy-your-app)

      *remove*

      * [File organization](/deploy/streamlit-community-cloud/deploy-your-app/file-organization)
      * [App dependencies](/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies)
      * [Secrets management](/deploy/streamlit-community-cloud/deploy-your-app/secrets-management)
      * [Deploy!](/deploy/streamlit-community-cloud/deploy-your-app/deploy)
    - [Manage your app](/deploy/streamlit-community-cloud/manage-your-app)

      *add*
    - [Share your app](/deploy/streamlit-community-cloud/share-your-app)

      *add*
    - [Manage your account](/deploy/streamlit-community-cloud/manage-your-account)

      *add*
    - [Status and limitations](/deploy/streamlit-community-cloud/status)
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
* [Streamlit Community Cloud](/deploy/streamlit-community-cloud)/
* [Deploy your app](/deploy/streamlit-community-cloud/deploy-your-app)/
* [App dependencies](/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies)

App dependencies for your Community Cloud app
=============================================

The main reason that apps fail to build properly is because Streamlit Community Cloud can't find your dependencies! There are two kinds of dependencies your app might have: Python dependencies and external dependencies. Python dependencies are other Python packages (just like Streamlit!) that you `import` into your script. External dependencies are less common, but they include any other software your script needs to function properly. Because Community Cloud runs on Linux, these will be Linux dependencies installed with `apt-get` outside the Python environment.

For your dependencies to be installed correctly, make sure you:

1. Add a [requirements file](/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies#add-python-dependencies) for Python dependencies.
2. Optional: To manage any external dependencies, add a `packages.txt` file.

*push\_pin*

#### Note

Python requirements files should be placed either in the root of your repository or in the same
directory as your app's entrypoint file.

Add Python dependencies
-----------------------

With each `import` statement in your script, you are bringing in a Python dependency. You need to tell Community Cloud how to install those dependencies through a Python package manager. We recommend using a `requirements.txt` file, which is based on `pip`.

You should *not* include [built-in Python libraries](https://docs.python.org/3/py-modindex.html) like `math`, `random`, or `distutils` in your `requirements.txt` file. These are a part of Python and aren't installed separately. Also, Community Cloud has `streamlit` installed by default. You don't strictly need to include `streamlit` unless you want to pin or restrict the version. If you deploy an app without a `requirements.txt` file, your app will run in an environment with just `streamlit` (and its dependencies) installed.

*priority\_high*

#### Important

The version of Python you use is important! Built-in libraries change between versions of Python and other libraries may have specific version requirements, too. Whenever Streamlit supports a new version of Python, Community Cloud quickly follows to default to that new version of Python. Always develop your app in the same version of Python you will use to deploy it. For more information about setting the version of Python when you deploy your app, see [Optional: Configure secrets and Python version](/deploy/streamlit-community-cloud/deploy-your-app/deploy#optional-configure-secrets-and-python-version).

If you have a script like the following, no extra dependencies would be needed since `pandas` and `numpy` are installed as direct dependencies of `streamlit`. Similarly, `math` and `random` are built into Python.

`import streamlit as st
import pandas as pd
import numpy as np
import math
import random
st.write("Hi!")`

However, a valid `requirements.txt` file would be:

`streamlit
pandas
numpy`

Alternatively, if you needed to specify certain versions, another valid example would be:

`streamlit==1.24.1
pandas>2.0
numpy<=1.25.1`

In the above example, `streamlit` is pinned to version `1.24.1`, `pandas` must be strictly greater than version 2.0, and `numpy` must be at-or-below version 1.25.1. Each line in your `requirements.txt` file is effectively what you would like to `pip install` into your cloud environment.

*star*

#### Tip

To learn about limitations of Community Cloud's Python environments, see [Community Cloud status and limitations](/deploy/streamlit-community-cloud/status#python-environments).

### Other Python package managers

There are other Python package managers in addition to `pip`. If you want to consider alternatives to using a `requirements.txt` file, Community Cloud will use the first dependency file it finds. Community Cloud will search the directory where your entrypoint file is, then it will search the root of your repository. In each location, dependency files are prioritized in the following order:

| Recognized Filename | Python Package Manager |
| --- | --- |
| `uv.lock` | [uv](https://docs.astral.sh/uv/concepts/projects/sync/) |
| `Pipfile` | [pipenv](https://pipenv-fork.readthedocs.io/en/latest/basics.html) |
| `environment.yml` | [conda](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-file-manually) |
| `requirements.txt` | [pip](https://pip.pypa.io/en/stable/user_guide/#requirements-files)† |
| `pyproject.toml` | [poetry](https://python-poetry.org/docs/basic-usage/) |

† For efficiency, Community Cloud will attempt to process `requirements.txt` with `uv`, but will fall back to `pip` if needed. `uv` is generally faster and more efficient than `pip`.

*priority\_high*

#### Warning

You should only use one dependency file for your app. If you include more than one (e.g. `requirements.txt` and `environment.yaml`), only the first file encountered will be used as described above, with any dependency file in your entrypoint file's directory taking precedence over any dependency file in the root of your repository.

apt-get dependencies
--------------------

For many apps, a `packages.txt` file is not required. However, if your script requires any software to be installed that is not a Python package, you need a `packages.txt` file. Community Cloud is built on Debian Linux. Anything you want to `apt-get install` must go in your `packages.txt` file. To browse available packages that can be installed, see the Debian 11 ("bullseye") [package list](https://packages.debian.org/bullseye/).

If `packages.txt` exists in the root directory of your repository we automatically detect it, parse it, and install the listed packages. You can read more about apt-get in [Linux documentation](https://linux.die.net/man/8/apt-get).

Add **apt-get** dependencies to `packages.txt` — one package name per line. For example, [`mysqlclient`](https://github.com/PyMySQL/mysqlclient) is a Python package which requires additional software be installed to function. A valid `packages.txt` file to enable `mysqlclient` would be:

`build-essential
pkg-config
default-libmysqlclient-dev`

[Previous: File organization](/deploy/streamlit-community-cloud/deploy-your-app/file-organization)[Next: Secrets management](/deploy/streamlit-community-cloud/deploy-your-app/secrets-management)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
