﻿2019 release notes - Streamlit Docs

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

    *remove*

    - [Cheat sheet](/develop/quick-reference/cheat-sheet)
    - [Release notes](/develop/quick-reference/release-notes)

      *remove*

      * [2025](/develop/quick-reference/release-notes/2025)
      * [2024](/develop/quick-reference/release-notes/2024)
      * [2023](/develop/quick-reference/release-notes/2023)
      * [2022](/develop/quick-reference/release-notes/2022)
      * [2021](/develop/quick-reference/release-notes/2021)
      * [2020](/develop/quick-reference/release-notes/2020)
      * [2019](/develop/quick-reference/release-notes/2019)
    - [Pre-release features](/develop/quick-reference/prerelease)
    - [Roadmap*open\_in\_new*](https://roadmap.streamlit.app)
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
* [Quick reference](/develop/quick-reference)/
* [Release notes](/develop/quick-reference/release-notes)/
* [2019](/develop/quick-reference/release-notes/2019)

2019 release notes
==================

This page contains release notes for Streamlit versions released in 2019. For the latest version of Streamlit, see [Release notes](/develop/quick-reference/release-notes).

Version 0.52.0
--------------

*Release date: December 20, 2019*

**Highlights:**

* 📤 Preview release of the file uploader widget. To try it out just call
  [`st.file_uploader`](https://docs.streamlit.io/en/latest/api.html#streamlit.file_uploader)!

  *Note that as a **preview release** things may change in the near future.
  Looking forward to hearing input from the community before we stabilize the
  API!*
* 👋 Support for [emoji codes](https://www.webfx.com/tools/emoji-cheat-sheet/) in
  `st.write` and `st.markdown`! Try it out with `st.write("Hello :wave:")`.

**Breaking changes:**

* 🧹 `st.pyplot` now clears figures by default, since that's what you want 99% of
  the time. This allows you to create two or more Matplotlib charts without
  having to call
  [`pyplot.clf`](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.clf.html)
  every time. If you want to turn this behavior off, use
  [`st.pyplot(clear_figure=False)`](https://docs.streamlit.io/en/latest/api.html#streamlit.pyplot)
* 📣 `st.cache` no longer checks for input mutations. This is the first change
  of our ongoing effort to simplify the caching system and prepare Streamlit
  for the launch of other caching primitives like Session State!

Version 0.51.0
--------------

*Release date: November 30, 2019*

**Highlights:**

* 🐕 You can now tweak the behavior of the file watcher with the config option `server.fileWatcherType`. Use it to switch between:
  + `auto` (default) : Streamlit will attempt to use the watchdog module, and
    falls back to polling if watchdog is not available.
  + `watchdog` : Force Streamlit to use the watchdog module.
  + `poll` : Force Streamlit to always use polling.
  + `none` : Streamlit will not watch files.

**Notable bug fixes:**

* Fix the "keyPrefix" option in static report sharing [#724](https://github.com/streamlit/streamlit/pull/724)
* Add support for getColorX and getTargetColorX to DeckGL Chart [#718](https://github.com/streamlit/streamlit/pull/718)
* Fixing Tornado on Windows + Python 3.8 [#682](https://github.com/streamlit/streamlit/pull/682)
* Fall back on webbrowser if xdg-open is not installed on Linux [#701](https://github.com/streamlit/streamlit/pull/701)
* Fixing number input spin buttons for Firefox [#683](https://github.com/streamlit/streamlit/pull/683)
* Fixing CTRL+ENTER on Windows [#699](https://github.com/streamlit/streamlit/pull/699)
* Do not automatically create credential file when in headless mode [#467](https://github.com/streamlit/streamlit/pull/467)

Version 0.50.1
--------------

*Release date: November 10, 2019*

**Highlights:**

* 👩‍🎓 SymPy support and ability to draw mathematical expressions using LaTeX! See
  [`st.latex`](/develop/api-reference/text/st.latex),
  [`st.markdown`](/develop/api-reference/text/st.markdown),
  and
  [`st.write`](/develop/api-reference/write-magic/st.write).
* 🌄 You can now set config options using environment variables. For example,
  `export STREAMLIT_SERVER_PORT=9876`.
* 🐱 Ability to call `streamlit run` directly with Github and Gist URLs. No
  need to grab the "raw" URL first!
* 📃 Cleaner exception stack traces. We now remove all Streamlit-specific code
  from stack traces originating from the user's app.

Version 0.49.0
--------------

*Release date: October 23, 2019*

**Highlights:**

* 💯 New input widget for entering numbers with the keyboard: `st.number_input()`
* 📺 Audio/video improvements: ability to load from a URL, to embed YouTube
  videos, and to set the start position.
* 🤝 You can now (once again) share static snapshots of your apps to S3! See
  the S3 section of `streamlit config show` to set it up. Then share from
  top-right menu.
* ⚙️ Use `server.baseUrlPath` config option to set Streamlit's URL to something
  like `http://domain.com/customPath`.

**Notable bug fixes:**

* Fixes numerous Windows bugs, including [Issues
  #339](https://github.com/streamlit/streamlit/issues/399) and
  [#401](https://github.com/streamlit/streamlit/issues/301).

Version 0.48.0
--------------

*Release date: October 12, 2019*

**Highlights:**

* 🔧 Ability to set config options as command line flags or in a local config file.
* ↕️ You can now maximize charts and images!
* ⚡ Streamlit is now much faster when writing data in quick succession to your app.
* ✳️ Ability to blacklist folder globs from "run on save" and `@st.cache` hashing.
* 🎛️ Improved handling of widget state when Python file is modified.
* 🙈 Improved HTML support in `st.write` and `st.markdown`. HTML is still unsafe, though!

**Notable bug fixes:**

* Fixes `@st.cache` bug related to having your Python environment on current
  working directory. [Issue #242](https://github.com/streamlit/streamlit/issues/242)
* Fixes loading of root url `/` on Windows. [Issue #244](https://github.com/streamlit/streamlit/issues/244)

Version 0.47.0
--------------

*Release date: October 1, 2019*

**Highlights:**

* 🌄 New hello.py showing off 4 glorious Streamlit apps. Try it out!
* 🔄 Streamlit now automatically selects an unused port when 8501 is already in use.
* 🎁 Sidebar support is now out of beta! Just start any command with `st.sidebar.` instead of `st.`
* ⚡ Performance improvements: we added a cache to our websocket layer so we no longer re-send data to the browser when it hasn't changed between runs
* 📈 Our "native" charts `st.line_chart`, `st.area_chart` and `st.bar_chart` now use Altair behind the scenes
* 🔫 Improved widgets: custom st.slider labels; default values in multiselect
* 🕵️‍♀️ The filesystem watcher now ignores hidden folders and virtual environments
* 💅 Plus lots of polish around caching and widget state management

**Breaking change:**

* 🛡️ We have temporarily disabled support for sharing static "snapshots" of Streamlit apps. Now that we're no longer in a limited-access beta, we need to make sure sharing is well thought through and abides by laws like the DMCA. But we're working on a solution!

Version 0.46.0
--------------

*Release date: September 19, 2019*

**Highlights:**

* ✨ Magic commands! Use `st.write` without typing `st.write`. See
  <https://docs.streamlit.io/en/latest/api.html#magic-commands>
* 🎛️ New `st.multiselect` widget.
* 🐍 Fixed numerous install issues so now you can use `pip install streamlit`
  even in Conda! We've therefore deactivated our Conda repo.
* 🐞 Multiple bug fixes and additional polish in preparation for our launch!

**Breaking change:**

* 🛡️ HTML tags are now blacklisted in `st.write`/`st.markdown` by default. More
  information and a temporary work-around at:
  <https://github.com/streamlit/streamlit/issues/152>

Version 0.45.0
--------------

*Release date: August 28, 2019*

**Highlights:**

* 😱 Experimental support for *sidebar*! Let us know if you want to be a beta
  tester.
* 🎁 Completely redesigned `st.cache`! Much more performant, has a cleaner API,
  support for caching functions called by `@st.cached` functions,
  user-friendly error messages, and much more!
* 🖼️ Lightning fast `st.image`, ability to choose between JPEG and PNG
  compression, and between RGB and BGR (for OpenCV).
* 💡 Smarter API for `st.slider`, `st.selectbox`, and `st.radio`.
* 🤖 Automatically fixes the Matplotlib backend -- no need to edit .matplotlibrc

Version 0.44.0
--------------

*Release date: July 28, 2019*

**Highlights:**

* ⚡ Lightning-fast reconnect when you do a ctrl-c/rerun on your Streamlit code
* 📣 Useful error messages when the connection fails
* 💎 Fixed multiple bugs and improved polish of our newly-released interactive widgets

Version 0.43.0
--------------

*Release date: July 9, 2019*

**Highlights:**

* ⚡ Support for interactive widgets! 🎈🎉

Version 0.42.0
--------------

*Release date: July 1, 2019*

**Highlights:**

* 💾 Ability to save Vega-Lite and Altair charts to SVG or PNG
* 🐇 We now cache JS files in your browser for faster loading
* ⛔ Improvements to error-handling inside Streamlit apps

Version 0.41.0
--------------

*Release date: June 24, 2019*

**Highlights:**

* 📈 Greatly improved our support for named datasets in Vega-Lite and Altair
* 🙄 Added ability to ignore certain folders when watching for file changes. See the `server.folderWatchBlacklist` config option.
* ☔ More robust against syntax errors on the user's script and imported modules

Version 0.40.0
--------------

*Release date: June 10, 2019*

**Highlights:**

* Streamlit is more than 10x faster. Just save and watch your analyses update instantly.
* We changed how you run Streamlit apps:
  `$ streamlit run your_script.py [script args]`
* Unlike the previous versions of Streamlit, `streamlit run [script] [script args]` creates a server (now you don't need to worry if the proxy is up). To kill the server, all you need to do is hit **Ctrl+c**.

**Why is this so much faster?**

Now, Streamlit keeps a single Python session running until you kill the server. This means that Streamlit can re-run your code without kicking off a new process; imported libraries are cached to memory. An added bonus is that `st.cache` now caches to memory instead of to disk.

**What happens if I run Streamlit the old way?**

If you run `$ python your_script.py` the script will execute from top to bottom, but won't produce a Streamlit app.

**What are the limitations of the new architecture?**

* To switch Streamlit apps, first you have to kill the Streamlit server with **Ctrl-c**. Then, you can use `streamlit run` to generate the next app.
* Streamlit only works when used inside Python files, not interactively from the Python REPL.

**What else do I need to know?**

* The strings we print to the command line when **liveSave** is on have been cleaned up. You may need to adjust any RegEx that depends on those.
* A number of config options have been renamed:

  | Old config | New config |
  | --- | --- |
  | proxy.isRemote | server.headless |
  | proxy.liveSave | server.liveSave |
  | proxy.runOnSave | server.runOnSave |
  | proxy.watchFileSystem | server.runOnSave |
  | proxy.enableCORS | server.enableCORS |
  | proxy.port | server.port |
  | browser.proxyAddress | browser.serverAddress |
  | browser.proxyPort | browser.serverPort |
  | client.waitForProxySecs | *n/a* |
  | client.throttleSecs | *n/a* |
  | client.tryToOutliveProxy | *n/a* |
  | client.proxyAddress | *n/a* |
  | client.proxyPort | *n/a* |
  | proxy.autoCloseDelaySecs | *n/a* |
  | proxy.reportExpirationSecs | *n/a* |

**What if something breaks?**

If the new Streamlit isn't working, please let us know by Slack or email. You can downgrade at any time with these commands:

`pip install --upgrade streamlit==0.37`

`conda install streamlit=0.37`

**What's next?**

Thank you for staying with us on this journey! This version of Streamlit lays the foundation for interactive widgets, a new feature of Streamlit we're really excited to share with you in the next few months.

Version 0.36.0
--------------

*Release date: May 03, 2019*

**Highlights**

* 🚣‍♀️ `st.progress()` now also accepts floats from 0.0–1.0
* 🤯 Improved rendering of long headers in DataFrames
* 🔐 Shared apps now default to HTTPS

Version 0.35.0
--------------

*Release date: April 26, 2019*

**Highlights**

* 📷 Bokeh support! Check out docs for `st.bokeh_chart`
* ⚡️ Improved the size and load time of saved apps
* ⚾️ Implemented better error-catching throughout the codebase

[Previous: 2020](/develop/quick-reference/release-notes/2020)[Next: Pre-release features](/develop/quick-reference/prerelease)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
