st.context - Streamlit Docs

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

      *remove*

      * SERVER

        ---
      * [st.cache\_data](/develop/api-reference/caching-and-state/st.cache_data)
      * [st.cache\_resource](/develop/api-reference/caching-and-state/st.cache_resource)
      * [st.session\_state](/develop/api-reference/caching-and-state/st.session_state)
      * BROWSER

        ---
      * [st.context](/develop/api-reference/caching-and-state/st.context)
      * [st.query\_params](/develop/api-reference/caching-and-state/st.query_params)
      * [st.experimental\_get\_query\_params*delete*](/develop/api-reference/caching-and-state/st.experimental_get_query_params)
      * [st.experimental\_set\_query\_params*delete*](/develop/api-reference/caching-and-state/st.experimental_set_query_params)
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
* [Caching and state](/develop/api-reference/caching-and-state)/
* [st.context](/develop/api-reference/caching-and-state/st.context)

st.context
----------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

An interface to access user session context.

st.context provides a read-only interface to access headers and cookies
for the current user session.

Each property (st.context.headers and st.context.cookies) returns
a dictionary of named values.

| Class description[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/runtime/context.py#L148 "View st.context source code on GitHub") | |
| --- | --- |
| st.context() | |
|  |  |
| --- | --- |
| Attributes | |
| [cookies](/develop/api-reference/caching-and-state/st.context#contextcookies) | A read-only, dict-like object containing cookies sent in the initial request. |
| [headers](/develop/api-reference/caching-and-state/st.context#contextheaders) | A read-only, dict-like object containing headers sent in the initial request. |
| [ip\_address](/develop/api-reference/caching-and-state/st.context#contextip_address) | The read-only IP address of the user's connection. |
| [is\_embedded](/develop/api-reference/caching-and-state/st.context#contextis_embedded) | Whether the app is embedded. |
| [locale](/develop/api-reference/caching-and-state/st.context#contextlocale) | The read-only locale of the user's browser. |
| [theme](/develop/api-reference/caching-and-state/st.context#contexttheme) | A read-only, dictionary-like object containing theme information. |
| [timezone](/develop/api-reference/caching-and-state/st.context#contexttimezone) | The read-only timezone of the user's browser. |
| [timezone\_offset](/develop/api-reference/caching-and-state/st.context#contexttimezone_offset) | The read-only timezone offset of the user's browser. |
| [url](/develop/api-reference/caching-and-state/st.context#contexturl) | The read-only URL of the app in the user's browser. |

context.cookies
---------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

A read-only, dict-like object containing cookies sent in the initial request.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/runtime/context.py#L205 "View st.cookies source code on GitHub") | |
| --- | --- |
| context.cookies | |

#### Examples

**Example 1: Access all available cookies**

Show a dictionary of cookies:

```

import streamlit as st

st.context.cookies

```

**Example 2: Access a specific cookie**

Show the value of a specific cookie:

```

import streamlit as st

st.context.cookies["_ga"]

```

context.headers
---------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

A read-only, dict-like object containing headers sent in the initial request.

Keys are case-insensitive and may be repeated. When keys are repeated,
dict-like methods will only return the last instance of each key. Use
.get\_all(key="your\_repeated\_key") to see all values if the same
header is set multiple times.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/runtime/context.py#L159 "View st.headers source code on GitHub") | |
| --- | --- |
| context.headers | |

#### Examples

**Example 1: Access all available headers**

Show a dictionary of headers (with only the last instance of any
repeated key):

```

import streamlit as st

st.context.headers

```

**Example 2: Access a specific header**

Show the value of a specific header (or the last instance if it's
repeated):

```

import streamlit as st

st.context.headers["host"]

```

Show of list of all headers for a given key:

```

import streamlit as st

st.context.headers.get_all("pragma")

```

context.ip\_address
-------------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

The read-only IP address of the user's connection.

This should not be used for security measures because it can easily be
spoofed. When a user accesses the app through localhost, the IP
address is None. Otherwise, the IP address is determined from the
[remote\_ip](https://www.tornadoweb.org/en/stable/httputil.html#tornado.httputil.HTTPServerRequest.remote_ip) attribute of the Tornado request object and may be an
IPv4 or IPv6 address.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/runtime/context.py#L386 "View st.ip_address source code on GitHub") | |
| --- | --- |
| context.ip\_address | |

#### Example

Check if the user has an IPv4 or IPv6 address:

```

import streamlit as st

ip = st.context.ip_address
if ip is None:
    st.write("No IP address. This is expected in local development.")
elif ip.contains(":"):
    st.write("You have an IPv6 address.")
elif ip.contains("."):
    st.write("You have an IPv4 address.")
else:
    st.error("This should not happen.")

```

context.is\_embedded
--------------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Whether the app is embedded.

This property returns a boolean value indicating whether the app is
running in an embedded context. This is determined by the presence of
embed=true as a query parameter in the URL. This is the only way to
determine if the app is currently configured for embedding because
embedding settings are not accessible through st.query\_params or
st.context.url.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/runtime/context.py#L424 "View st.is_embedded source code on GitHub") | |
| --- | --- |
| context.is\_embedded | |

#### Example

Conditionally show content when the app is running in an embedded
context:

```

import streamlit as st

if st.context.is_embedded:
    st.write("You are running the app in an embedded context.")

```

context.locale
--------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

The read-only locale of the user's browser.

st.context.locale returns the value of [navigator.language](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/language) from
the user's DOM. This is a string representing the user's preferred
language (e.g. "en-US").

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/runtime/context.py#L327 "View st.locale source code on GitHub") | |
| --- | --- |
| context.locale | |

#### Example

Access the user's locale to display locally:

```

import streamlit as st

if st.context.locale == "fr-FR":
    st.write("Bonjour!")
else:
    st.write("Hello!")

```

context.theme
-------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

A read-only, dictionary-like object containing theme information.

Theme information is restricted to the type of the theme (dark or
light) and is inferred from the background color of the app.

Note

Changes made to the background color through CSS are not included.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/runtime/context.py#L239 "View st.theme source code on GitHub") | |
| --- | --- |
| context.theme | |
| Parameters | |
| type ("light", "dark") | The theme type inferred from the background color of the app. |

#### Example

Access the theme type of the app:

```

import streamlit as st

st.write(f"The current theme type is {st.context.theme.type}.")

```

context.timezone
----------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

The read-only timezone of the user's browser.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/runtime/context.py#L271 "View st.timezone source code on GitHub") | |
| --- | --- |
| context.timezone | |

#### Example

Access the user's timezone, and format a datetime to display locally:

```

import streamlit as st
from datetime import datetime, timezone
import pytz

tz = st.context.timezone
tz_obj = pytz.timezone(tz)

now = datetime.now(timezone.utc)

f"The user's timezone is {tz}."
f"The UTC time is {now}."
f"The user's local time is {now.astimezone(tz_obj)}"

```

context.timezone\_offset
------------------------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

The read-only timezone offset of the user's browser.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/runtime/context.py#L300 "View st.timezone_offset source code on GitHub") | |
| --- | --- |
| context.timezone\_offset | |

#### Example

Access the user's timezone offset, and format a datetime to display locally:

```

import streamlit as st
from datetime import datetime, timezone, timedelta

tzoff = st.context.timezone_offset
tz_obj = timezone(-timedelta(minutes=tzoff))

now = datetime.now(timezone.utc)

f"The user's timezone is {tz}."
f"The UTC time is {now}."
f"The user's local time is {now.astimezone(tz_obj)}"

```

context.url
-----------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

The read-only URL of the app in the user's browser.

st.context.url returns the URL through which the user is accessing
the app. This includes the scheme, domain name, port, and path. If
query parameters or anchors are present in the URL, they are removed
and not included in this value.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/runtime/context.py#L356 "View st.url source code on GitHub") | |
| --- | --- |
| context.url | |

#### Example

Conditionally show content when you access your app through
localhost:

```

import streamlit as st

if st.context.url.startswith("http://localhost"):
    st.write("You are running the app locally.")

```

[Previous: st.session\_state](/develop/api-reference/caching-and-state/st.session_state)[Next: st.query\_params](/develop/api-reference/caching-and-state/st.query_params)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
