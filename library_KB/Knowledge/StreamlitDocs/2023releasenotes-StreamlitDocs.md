﻿2023 release notes - Streamlit Docs

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
* [2023](/develop/quick-reference/release-notes/2023)

2023 release notes
==================

This page contains release notes for Streamlit versions released in 2023. For the latest version of Streamlit, see [Release notes](/develop/quick-reference/release-notes).

**Version 1.29.0**
------------------

*Release date: November 30, 2023*

**Highlights**

* 🔲 [`st.container`](/develop/api-reference/layout/st.container) and [`st.form`](/develop/api-reference/execution-flow/st.form) now have a `border` parameter to show or hide a border.
* 🐍 Streamlit supports Python 3.12!

**Notable Changes**

* ⌛ `st.dataframe`, `st.data_editor`, and `st.table` support `datetime.timedelta` values ([#7689](https://github.com/streamlit/streamlit/pull/7689), [#4489](https://github.com/streamlit/streamlit/issues/4489)).
* 💀 Streamlit apps preload skeleton elements for a smoother appearance when initializing ([#7598](https://github.com/streamlit/streamlit/pull/7598)).
* 🏃 Reduced the overhead of running `AppTest`-simulated apps, especially for fast-running apps ([#7691](https://github.com/streamlit/streamlit/pull/7691)).
* 🛁 String representations of `AppTest` data are improved for a better testing and debugging experience ([#7658](https://github.com/streamlit/streamlit/pull/7658)).
* 🔢 Apps can be configured to identify `Enum` classes as the same if they have matching member names ([#7408](https://github.com/streamlit/streamlit/pull/7408), [#4909](https://github.com/streamlit/streamlit/issues/4909)). Thanks, [Asaurus1](https://github.com/Asaurus1)!
* ❌ The "Made with Streamlit" footer no longer appears at the bottom of apps ([#7583](https://github.com/streamlit/streamlit/pull/7583)).
* 🧹 Unused config options have been deprecated ([#7584](https://github.com/streamlit/streamlit/pull/7584)).
* 🕳️ Query parameters can be empty ([#7601](https://github.com/streamlit/streamlit/pull/7601), [#7416](https://github.com/streamlit/streamlit/issues/7416)).
* 💅 Visual tweaks ([#7592](https://github.com/streamlit/streamlit/pull/7592), [#7630](https://github.com/streamlit/streamlit/pull/7630)).

**Other Changes**

* 🦗 Bug fix: Convert floats to bytes instead of hashing to avoid hashing instability ([#7754](https://github.com/streamlit/streamlit/pull/7754)). Thanks, [BlackHC](https://github.com/BlackHC)!
* 🦎 Bug fix: Corrected broken URLs and typos in error messages ([#7746](https://github.com/streamlit/streamlit/pull/7746), [#7764](https://github.com/streamlit/streamlit/pull/7764), [#7770](https://github.com/streamlit/streamlit/pull/7770)). Thanks, [ObservedObserver](https://github.com/ObservedObserver)!
* 🐌 Bug fix: `st.connection` correctly caches results when using two connections of the same type ([#7730](https://github.com/streamlit/streamlit/pull/7730), [#7709](https://github.com/streamlit/streamlit/issues/7709)).
* 🕸️ Bug fix: Using context managers with multithreading now displays content in the expected order ([#7715](https://github.com/streamlit/streamlit/pull/7715), [#7668](https://github.com/streamlit/streamlit/issues/7668)). Thanks, [eric-skydio](https://github.com/eric-skydio)!
* 🦂 Bug fix: Added https fallback when obtaining the host machine's address ([#7712](https://github.com/streamlit/streamlit/pull/7712), [#7703](https://github.com/streamlit/streamlit/issues/7703)). Thanks, [LarsHill](https://github.com/LarsHill)!
* 🛡️ Bug fix: Added security patch for `pyarrow` vulnerability. Custom components using `pyarrow` table deserialization should require `pyarrow>=14.0.1` ([#7695](https://github.com/streamlit/streamlit/pull/7695), [#7700](https://github.com/streamlit/streamlit/issues/7700)).
* 🦟 Bug fix: Improved typing for `st.connection` ([#7671](https://github.com/streamlit/streamlit/pull/7671)). Thanks, [thezanke](https://github.com/thezanke)!
* 🪰 Bug fix: Retries of `SnowflakeConnection` methods are narrowed to only occur with transient errors to avoid unnecessary repeated errors ([#7645](https://github.com/streamlit/streamlit/pull/7645), [#7637](https://github.com/streamlit/streamlit/issues/7637)).
* 🏗️ Removed the v0 testing framework which was undocumented ([#7657](https://github.com/streamlit/streamlit/pull/7657)).
* 🪳 Bug fix: The navigation expander arrow no longer disappears ([#7634](https://github.com/streamlit/streamlit/pull/7634), [#7547](https://github.com/streamlit/streamlit/issues/7547)).
* ❄️ Improved the error message for `SnowflakeConnection` when a configuration is not found ([#7652](https://github.com/streamlit/streamlit/pull/7652)).
* 🕷️ Bug fix: `st.rerun` no longer causes a `RecursionError` when used with `st.chat_input` ([#7643](https://github.com/streamlit/streamlit/pull/7643), [#7629](https://github.com/streamlit/streamlit/issues/7629)).
* 🐞 Bug fix: `st.file_uploader` no longer causes an extra rerun and therefore doesn't conflict with `st.chat_input` ([#7641](https://github.com/streamlit/streamlit/pull/7641), [#7556](https://github.com/streamlit/streamlit/issues/7556)).
* 🐝 Bug fix: `AppTest` no longer raises an error when encountering `st.container` ([#7644](https://github.com/streamlit/streamlit/pull/7644), [#7636](https://github.com/streamlit/streamlit/issues/7636)).
* 🪲 Bug fix: Graphviz charts scale correctly when exiting fullscreen view ([#7398](https://github.com/streamlit/streamlit/pull/7398), [#7527](https://github.com/streamlit/streamlit/issues/6527)).
* 🎥 Bug fix: "Record a screencast" is hidden when known to be unsupported in a browser ([#7604](https://github.com/streamlit/streamlit/pull/7604)).
* 🐛 Bug fix: Increased the top padding of embedded apps to better display the dataframe toolbar ([#7681](https://github.com/streamlit/streamlit/pull/7681), [#7609](https://github.com/streamlit/streamlit/pull/7609), [#7607](https://github.com/streamlit/streamlit/issues/7607)).
* 🐜 Bug fix: `st.rerun` uses `NoReturn` for improved type checking ([#7422](https://github.com/streamlit/streamlit/pull/7422)) Thanks, [kongzii](https://github.com/kongzii).

**Version 1.28.0**
------------------

*Release date: October 26, 2023*

**Release videos**

* [Introducing `AppTest`](https://www.youtube.com/watch?v=99OEoP5sy0U)

**Highlights**

* 🧪 Introducing a new testing framework for Streamlit apps! Check out our [documentation](/develop/api-reference/app-testing) to learn how to build automated tests for your apps.
* 💻 Announcing the general availability of `st.connection`, a command to conveniently manage connections in Streamlit apps. Check out the [docs](/develop/api-reference/connections/st.connection) to learn more.
* ❄️ `SnowparkConnection` has been upgraded to the new and improved `SnowflakeConnection` — the same, great functionality *plus more*! Check out our [built-in connections](/develop/api-reference/connections#built-in-connections).
* 🛠️ `st.dataframe` and `st.data_editor` have a new toolbar! Users can search and download data in addition to enjoying improved UI for row additions and deletions. See our updated guide on [Dataframes](/develop/concepts/design/dataframes).

**Notable Changes**

* 🌀 When using a spinner with cached functions, the spinner will be overlaid instead of pushing content down ([#7488](https://github.com/streamlit/streamlit/pull/7488)).
* 📅 `st.data_editor` now supports datetime index editing ([#7483](https://github.com/streamlit/streamlit/pull/7483)).
* 🔢 Improved support for `decimal.Decimal` in `st.dataframe` and `st.data_editor` ([#7475](https://github.com/streamlit/streamlit/pull/7475)).
* 🥸 Global kwargs were added for `hashlib` ([#7527](https://github.com/streamlit/streamlit/pull/7527), [#7526](https://github.com/streamlit/streamlit/issues/7526)). Thanks, [DueViktor](https://github.com/DueViktor)!
* 📋 `st.components.v1.iframe` now permits writing to clipboard ([#7487](https://github.com/streamlit/streamlit/pull/7487)). Thanks, [dilipthakkar](https://github.com/dilipthakkar)!
* 📝 `SafeSessionState` disconnect was replaced with script runner yield points for improved efficiency and clarity ([#7373](https://github.com/streamlit/streamlit/pull/7373)).
* 🤖 The Langchain callback handler will show the full input string inside the body of a `st.status` when the input string is too long to show as a label ([#7478](https://github.com/streamlit/streamlit/pull/7478)). Thanks, [pokidyshev](https://github.com/pokidyshev)!
* 📈 `st.graphviz_chart` now supports using different Graphviz layout engines ([#7505](https://github.com/streamlit/streamlit/pull/7505), [#4089](https://github.com/streamlit/streamlit/issues/4089)).
* 🦋 Assorted visual tweaks ([#7486](https://github.com/streamlit/streamlit/pull/7486), [#7592](https://github.com/streamlit/streamlit/pull/7592)).
* 📊 `plotly.js` was upgraded to version 2.26.1 ([#7449](https://github.com/streamlit/streamlit/pull/7449), [#7476](https://github.com/streamlit/streamlit/issues/7476), [#7045](https://github.com/streamlit/streamlit/issues/7045)).
* 💽 Legacy serialization for DataFrames was removed. All DataFrames will be serialized by Apache Arrow ([#7429](https://github.com/streamlit/streamlit/pull/7429)).
* 🖼️ Compatibility for Pillow 10.x was added ([#7442](https://github.com/streamlit/streamlit/pull/7442)).
* 📬 Migrated `_stcore/allowed-message-origins` endpoint to `_stcore/host-config` ([#7342](https://github.com/streamlit/streamlit/pull/7342)).
* 💬 Added `post_parent_message` platform command to send custom messages from a Streamlit app to its parent window ([#7522](https://github.com/streamlit/streamlit/pull/7522)).

**Other Changes**

* ⌨️ Improved string dtype handling for DataFrames ([#7479](https://github.com/streamlit/streamlit/pull/7479)).
* ✒️ `st.write` will avoid using `unsafe_allow_html=True` if possible ([#7432](https://github.com/streamlit/streamlit/pull/7432)).
* 🐛 Bug fix: Implementation of `st.expander` was simplified for improved behavior and consistency ([#7247](https://github.com/streamlit/streamlit/pull/7247), [#2839](https://github.com/streamlit/streamlit/issues/2839), [#4111](https://github.com/streamlit/streamlit/issues/4111), [#4651](https://github.com/streamlit/streamlit/issues/4651), [#5604](https://github.com/streamlit/streamlit/issues/5604)).
* 🪲 Bug fix: Multipage links in the sidebar are now aligned with other sidebar elements ([#7531](https://github.com/streamlit/streamlit/pull/7531)).
* 🐜 Bug fix: `st.chat_input` won't incorrectly prompt for `label` parameter in IDEs ([#7560](https://github.com/streamlit/streamlit/pull/7560)).
* 🐝 Bug fix: Scroll bars correctly overlay `st.dataframe` and `st.data_editor` without adding empty space ([#7090](https://github.com/streamlit/streamlit/pull/7090), [#6888](https://github.com/streamlit/streamlit/issues/6888)).
* 🐞 Bug fix: `st.chat_message` behaves correctly with the removal of AutoSizer ([#7504](https://github.com/streamlit/streamlit/pull/7504), [#7473](https://github.com/streamlit/streamlit/issues/7473)).
* 🕷️ Bug fix: Anchor links are reliably produced for non-English headers ([#7454](https://github.com/streamlit/streamlit/pull/7454), [#5291](https://github.com/streamlit/streamlit/issues/5291)).
* ☃️ Bug fix: `st.connections.SnowparkConnection` more accurately detects when it's running within Streamlit in Snowflake ([#7502](https://github.com/streamlit/streamlit/pull/7502)).
* 🪳 Bug fix: A user-friendly warning is shown when exceeding the size limitations of a pandas `Styler` object ([#7497](https://github.com/streamlit/streamlit/pull/7497), [#5953](https://github.com/streamlit/streamlit/issues/5953)).
* 🪰 Bug fix: `st.data_editor` automatically converts non-string column names to strings ([#7485](https://github.com/streamlit/streamlit/pull/7485), [#6950](https://github.com/streamlit/streamlit/issues/6950)).
* 🦠 Bug fix: `st.data_editor` correctly identifies non-range indices as a required column ([#7481](https://github.com/streamlit/streamlit/pull/7481), [#6995](https://github.com/streamlit/streamlit/issues/6995)).
* 🦟 Bug fix: `st.file_uploader` displays compound file extensions like `csv.gz` correctly ([#7362](https://github.com/streamlit/streamlit/pull/7362)). Thanks, [mo42](https://github.com/mo42)!
* 🦂 Bug fix: Column Configuration no longer uses deprecated type checks ([#7496](https://github.com/streamlit/streamlit/pull/7496), [#7477](https://github.com/streamlit/streamlit/pull/7477), [#7550](https://github.com/streamlit/streamlit/issues/7550)). Thanks, [c-bik](https://github.com/c-bik)!
* 🦗 Bug fix: Additional toolbar items no longer stack vertically ([#7470](https://github.com/streamlit/streamlit/pull/7470), [#7471](https://github.com/streamlit/streamlit/issues/7471)).
* 🕸️ Bug fix: Column Configuration no longer causes a type warning in Mypy ([#7457](https://github.com/streamlit/streamlit/pull/7457)). Thanks, [kopp](https://github.com/kopp)!
* 🐌 Bug fix: Bokeh Sliders no longer cause JavaScript errors ([#7441](https://github.com/streamlit/streamlit/pull/7441), [#7171](https://github.com/streamlit/streamlit/issues/7171)).
* 🦎 Bug fix: Caching now recognizes DataFrames with the same values but different column names as different ([#7331](https://github.com/streamlit/streamlit/pull/7331), [#7086](https://github.com/streamlit/streamlit/issues/7086)).

**Version 1.27.0**
------------------

*Release date: September 21, 2023*

**Highlights**

* ✨ Introducing `st.scatter_chart` — a new, simple chart element to build scatter charts Streamlit-y fast and easy! See our [documentation](/develop/api-reference/charts/st.scatter_chart).
* 🔗 Introducing `st.link_button`! Want to open an external link in a new tab with a bit more pizazz than a plain-text link? Check out our [documentation](/develop/api-reference/widgets/st.link_button) to see how.
* 🏃 Announcing the general availability of [`st.rerun`](/develop/api-reference/execution-flow/st.rerun), a command to interrupt your script and trigger an immediate rerun.

**Notable Changes**

* 👻 You can initialize widgets with an empty state by setting `None` as an initial value for [`st.number_input`](/develop/api-reference/widgets/st.number_input), [`st.selectbox`](/develop/api-reference/widgets/st.selectbox), [`st.date_input`](/develop/api-reference/widgets/st.date_input), [`st.time_input`](/develop/api-reference/widgets/st.time_input), [`st.radio`](/develop/api-reference/widgets/st.radio), [`st.text_input`](/develop/api-reference/widgets/st.text_input), and [`st.text_area`](/develop/api-reference/widgets/st.text_area)!
* 📤 [`st.download_button`](/develop/api-reference/widgets/st.download_button) now uses `target="_self"` instead of opening a new tab ([#7151](https://github.com/streamlit/streamlit/pull/7151), [#7132](https://github.com/streamlit/streamlit/issues/7132)).
* 🧟 Removed unmaintained `pympler` dependency ([#7193](https://github.com/streamlit/streamlit/pull/7193), [#7131](https://github.com/streamlit/streamlit/issues/7131)). Thanks, [rudyardrichter](https://github.com/rudyardrichter)!

**Other Changes**

* 🐛 Bug fix: `st.multiselect` now shows a correct message when no result matches a user's search ([#7205](https://github.com/streamlit/streamlit/pull/7205), [#7116](https://github.com/streamlit/streamlit/issues/7116)).
* 🪲 Bug fix: `st.experimental_user` now defaults to `test@example.com` ([#7219](https://github.com/streamlit/streamlit/pull/7219), [#7215](https://github.com/streamlit/streamlit/issues/7215)).
* 🐜 Bug fix: `st.slider` labels don't overlap when small ranges are selected ([#7221](https://github.com/streamlit/streamlit/pull/7221), [#3385](https://github.com/streamlit/streamlit/issues/3385)).
* 🐝 Bug fix: Type-checking correctly identifies all string types to avoid hashing errors ([#7255](https://github.com/streamlit/streamlit/pull/7255), [#6455](https://github.com/streamlit/streamlit/issues/6455)).
* 🐞 Bug fix: JSON is parsed with JSON5 to avoid errors from null values when using `st.pydeck_chart` ([#7256](https://github.com/streamlit/streamlit/pull/7256), [#5799](https://github.com/streamlit/streamlit/issues/5799)).
* 🕷️ Bug fix: Identical widgets on different pages are correctly interpreted by Streamlit as distinct ([#7264](https://github.com/streamlit/streamlit/pull/7264), [#6146](https://github.com/streamlit/streamlit/issues/6146)).
* 🦋 Bug fix: Visual tweaks to widgets for responsive behavior ([#7145](https://github.com/streamlit/streamlit/pull/7145)).
* 🪳 Bug fix: SVGs are accurately displayed ([#7183](https://github.com/streamlit/streamlit/pull/7183), [#3882](https://github.com/streamlit/streamlit/issues/3882)).
* 🪰 Bug fix: `st.video` correctly updates with changes to `start_time` ([#7257](https://github.com/streamlit/streamlit/pull/7257), [#7126](https://github.com/streamlit/streamlit/issues/7126)).
* 🦠 Bug fix: Additional error handling was added to `st.session_state` ([#7280](https://github.com/streamlit/streamlit/pull/7280), [#7206](https://github.com/streamlit/streamlit/issues/7206)).
* 🦟 Bug fix: `st.map` correctly refreshes with new data ([#7307](https://github.com/streamlit/streamlit/pull/7307), [#7294](https://github.com/streamlit/streamlit/issues/7294)).
* 🦂 Bug fix: The decorative app header line is no longer covered by the sidebar ([#7297](https://github.com/streamlit/streamlit/pull/7297), [#6264](https://github.com/streamlit/streamlit/issues/6264)).
* 🦗 Bug fix: `st.code` no longer triggers a `CachedStFunctionWarning` ([#7306](https://github.com/streamlit/streamlit/pull/7306), [#7055](https://github.com/streamlit/streamlit/issues/7055)).
* 🕸️ Bug fix: `st.download_button` no longer resets with different `data` ([#7316](https://github.com/streamlit/streamlit/pull/7316), [#7308](https://github.com/streamlit/streamlit/issues/7308)).
* 🐌 Bug fix: Widgets consistently recognize user interaction while a page is still running, with or without `fastRerun` enabled ([#7283](https://github.com/streamlit/streamlit/pull/7283), [#6643](https://github.com/streamlit/streamlit/issues/6643)).
* 🦎 Bug fix: `st.tabs` was improved to better handle and render conditionally appearing tabs ([#7287](https://github.com/streamlit/streamlit/pull/7287), [#7310](https://github.com/streamlit/streamlit/pull/7310), [#5454](https://github.com/streamlit/streamlit/issues/5454), [#7040](https://github.com/streamlit/streamlit/issues/7040)).

**Version 1.26.0**
------------------

*Release date: August 24, 2023*

**Highlights**

* 🤖 Introducing `st.status` to display output from long-running processes and external API calls ([#7140](https://github.com/streamlit/streamlit/pull/7140)). Works great with `st.chat_message`! See our [documentation](/develop/api-reference/status/st.status) for how to use this feature.
* 🚥 Introducing [`st.toggle`](/develop/api-reference/widgets/st.toggle) — an alternative to `st.checkbox` when you need an on/off switch.

**Notable Changes**

* 🎨 Simple [chart elements](/develop/api-reference/charts) have a `color` parameter to set the color of your data points or series ([#7022](https://github.com/streamlit/streamlit/pull/7022)).
* 🌈 [Markdown](/develop/api-reference/text/st.markdown) supports rainbow and gray colors ([#7106](https://github.com/streamlit/streamlit/pull/7106), [#7179](https://github.com/streamlit/streamlit/pull/7179)).
* 📏 [`st.header`](/develop/api-reference/text/st.header) and [`st.subheader`](/develop/api-reference/text/st.subheader) have optional, colored dividers ([#7133](https://github.com/streamlit/streamlit/pull/7133)).
* 🚀 Deploying to Community Cloud is even easier—locally running apps have a [deploy button](/develop/concepts/architecture/app-chrome#deploy-this-app) in their toolbars ([#7085](https://github.com/streamlit/streamlit/pull/7085), [#6935](https://github.com/streamlit/streamlit/issues/6935)).
* 🖌️ [`st.download_button`](/develop/api-reference/widgets/st.download_button) has a new parameter `type` for theming ([#7056](https://github.com/streamlit/streamlit/pull/7056), [#7038](https://github.com/streamlit/streamlit/issues/7038)).
* 🤖 [`st.chat_message`](/develop/api-reference/chat/st.chat_message) has ai and human presets for messages ([#7094](https://github.com/streamlit/streamlit/pull/7094)).
* 💅 [`st.radio`](/develop/api-reference/widgets/st.radio) options support markdown and have captions ([#7018](https://github.com/streamlit/streamlit/pull/7018), [#7105](https://github.com/streamlit/streamlit/pull/7105), [#6085](https://github.com/streamlit/streamlit/issues/6085)).
* 🧼 Assorted visual tweaks ([#7050](https://github.com/streamlit/streamlit/pull/7050), [#894](https://github.com/streamlit/streamlit/issues/894)).
* 🛏️ Replaced deprecated `imghdr` dependency with `pillow` ([#7081](https://github.com/streamlit/streamlit/pull/7081), [#7027](https://github.com/streamlit/streamlit/issues/7027)).
* 🔢 [`st.number_input`](/develop/api-reference/widgets/st.number_input)'s step buttons (+/-) are ignored during tabbing navigation ([#7154](https://github.com/streamlit/streamlit/pull/7154)). Thanks [@denck007](https://github.com/denck007)!

**Other Changes**

* 🍞 Bug fix: Toast messages are no longer blocked by `st.chat_input` ([#7204](https://github.com/streamlit/streamlit/pull/7204), [#7115](https://github.com/streamlit/streamlit/issues/7115)).
* 🕸️ Bug fix: Widget IDs are now stable to prevent inconsistent statefulness ([#7003](https://github.com/streamlit/streamlit/pull/7003)).
* 🦟 Bug fix: Browser autofill is correctly recognized within forms now ([#7150](https://github.com/streamlit/streamlit/pull/7150), [#7101](https://github.com/streamlit/streamlit/issues/7101), [#7084](https://github.com/streamlit/streamlit/issues/7084)).
* 🪱 Bug fix: `st.file_uploader` no longer causes session state to reset when a websocket connection is dropped and reconnected ([#7149](https://github.com/streamlit/streamlit/pull/7149), [#7025](https://github.com/streamlit/streamlit/pull/7025)).
* 🏎️ Bug fix: Pydeck JSON data is cached for improved performance ([#7113](https://github.com/streamlit/streamlit/pull/7113), [#5532](https://github.com/streamlit/streamlit/issues/5532)).
* 🦋 Bug fix: `st.chat_input` no longer submits prematurely while typing with an input method editor ([#6993](https://github.com/streamlit/streamlit/pull/6993)).
* 🐞 Bug fix: Label backgrounds for `st.tabs` are now transparent ([#7070](https://github.com/streamlit/streamlit/pull/7070), [#5707](https://github.com/streamlit/streamlit/issues/5707)).
* 🐝 Bug fix: Page width is no longer ignored when using the `help` parameter in `st.button` ([#7033](https://github.com/streamlit/streamlit/pull/7033), [#6161](https://github.com/streamlit/streamlit/issues/6161)).
* 🐜 Bug fix: Tweaked Altair color specification for improved visibility in dark mode ([#7061](https://github.com/streamlit/streamlit/pull/7061), [#3343](https://github.com/streamlit/streamlit/issues/3343)).
* 🪲 Bug fix: `st.chat_message` can correctly use local images as avatars ([#7130](https://github.com/streamlit/streamlit/pull/7130)).
* 🐛 Bug fix: Specified that MD5 is not used for security ([#7122](https://github.com/streamlit/streamlit/pull/7122), [#7120](https://github.com/streamlit/streamlit/issues/7120)).
* 🪄 Bug fix: Async function docstrings are ignored by [Streamlit magic](/develop/api-reference/write-magic/magic) ([#7143](https://github.com/streamlit/streamlit/pull/7143), [#7137](https://github.com/streamlit/streamlit/issues/7137)).

**Version 1.25.0**
------------------

*Release date: July 20, 2023*

**Highlights**

* 🍞 Introducing `st.toast` — a command to briefly show toast messages to users in the bottom-right corner of apps. See [our documentation](/develop/api-reference/status/st.toast) on how to use this feature.

**Notable Changes**

* 🗺️ [`st.map`](/develop/api-reference/charts/st.map) now has parameters for `latitude`, `longitude`, `color`, and `size` to customize data points ([#6896](https://github.com/streamlit/streamlit/pull/6896)).
* 🚩 [`st.multiselect`](/develop/api-reference/widgets/st.multiselect) supports setting placeholders and specifying the maximum number of selections via the `placeholder` and `max_selections` keyword-only arguments, respectively ([#6901](https://github.com/streamlit/streamlit/pull/6901), [#4750](https://github.com/streamlit/streamlit/issues/4750)). Thanks, [@fhiroki](https://github.com/fhiroki)!
* 📅 Customize the date format for `st.date_input` with the `format` parameter ([#6974](https://github.com/streamlit/streamlit/pull/6974), [#5234](https://github.com/streamlit/streamlit/issues/5234)).
* ↩️ [Forms](/develop/api-reference/execution-flow/st.form) can now be submitted with Enter/Return while inside [`st.text_input`](/develop/api-reference/widgets/st.text_input), [`st.number_input`](/develop/api-reference/widgets/st.number_input), or [`st.text_area`](/develop/api-reference/widgets/st.text_area) ([#6911](https://github.com/streamlit/streamlit/pull/6911), [#3790](https://github.com/streamlit/streamlit/issues/3790)).
* 🍢 The app menu icon in the upper-right corner of apps has been changed from "**☰**" to "**⋮**" ([#6947](https://github.com/streamlit/streamlit/pull/6947)).

**Other Changes**

* ⛓️ Minimum required versions increased for multiple Python dependencies, including `numpy>=1.19.3` and `pandas>=1.3.0` ([#6802](https://github.com/streamlit/streamlit/pull/6802)).
* 🛡️ `protobufjs` was bumped from 7.2.1 to 7.2.4 ([#6959](https://github.com/streamlit/streamlit/pull/6959)).
* ✨ Visual design tweaks to Streamlit's input widgets ([#6944](https://github.com/streamlit/streamlit/pull/6944)).
* 🦋 Bug Fix: `st.slider` now accepts general number types like `numpy.int64` instead of just `int` and `float` ([#6816](https://github.com/streamlit/streamlit/pull/6816), [#6815](https://github.com/streamlit/streamlit/issues/6815)). Thanks, [@milliams](https://github.com/milliams)!
* 🐜 Bug Fix: Data labels for `st.slider` and `st.select_slider` no longer overflow when inside `st.expander` ([#6828](https://github.com/streamlit/streamlit/pull/6828), [#6297](https://github.com/streamlit/streamlit/issues/6297)).
* 🐛 Bug Fix: Elements no longer re-render from scratch with each rerun ([#6923](https://github.com/streamlit/streamlit/pull/6923), [#6920](https://github.com/streamlit/streamlit/issues/6920)).
* 🐞 Bug Fix: `st.data_editor` hashes styler objects correctly for stability across reruns ([#6815](https://github.com/streamlit/streamlit/pull/6915), [#6898](https://github.com/streamlit/streamlit/issues/6898)).
* 🐝 Bug Fix: Fixed the padding for embedded apps using `st.chat_input` to prevent messages being cutoff ([#6979](https://github.com/streamlit/streamlit/pull/6979)).

**Version 1.24.0**
------------------

*Release date: June 27, 2023*

**Highlights**

* 💬 Introducing `st.chat_message` and `st.chat_input` — two new [chat elements](/develop/api-reference/chat) that let you build conversational apps. Learn how to use these features in your LLM-powered chat apps in our [tutorial](/develop/tutorials/llms/build-conversational-apps).
* 💾 Streamlit's caching decorators now allow you to customize Streamlit's hashing of input parameters with the keyword-only argument [`hash_funcs`](/develop/concepts/architecture/caching#the-hash_funcs-parameter).

**Notable Changes**

* 🐍 We've deprecated support for Python 3.7 in the core library and Streamlit Community Cloud ([#6868](https://github.com/streamlit/streamlit/pull/6868)).
* 📅 `st.cache_data` and `st.cache_resource` can hash timezone-aware `datetime` objects ([#6812](https://github.com/streamlit/streamlit/pull/6812), [#6690](https://github.com/streamlit/streamlit/issues/6690), [#5110](https://github.com/streamlit/streamlit/issues/5110)).

**Other Changes**

* ✨ Visual design tweaks to Streamlit's input widgets ([#6817](https://github.com/streamlit/streamlit/pull/6817)).
* 🐛 Bug fix: `st.write` pretty-prints dataclasses using `st.help` ([#6750](https://github.com/streamlit/streamlit/pull/6750)).
* 🪲 Bug fix: `st.button`'s height is consistent with that of other widgets ([#6738](https://github.com/streamlit/streamlit/pull/6738)).
* 🐜 Bug fix: Upgraded the `react-range` frontend dependency to fix the memory usage of sliders ([#6764](https://github.com/streamlit/streamlit/pull/6764), [#5436](https://github.com/streamlit/streamlit/issues/5436)). Thanks [@wolfd](https://github.com/wolfd)!
* 🐝 Bug fix: Pydantic validators no longer result in exceptions on app reruns ([#6664](https://github.com/streamlit/streamlit/pull/6664), [#3218](https://github.com/streamlit/streamlit/issues/3218)).
* 🐞 Bug fix: `streamlit config show` honors newlines ([#6758](https://github.com/streamlit/streamlit/pull/6758), [#2868](https://github.com/streamlit/streamlit/issues/2868)).
* 🪰 Bug fix: Fixed a race condition to ensure Streamlit reruns the latest code when the file changes ([#6884](https://github.com/streamlit/streamlit/pull/6884)).
* 🦋 Bug fix: Apps no longer rerun when users click anchor links ([#6834](https://github.com/streamlit/streamlit/pull/6834), [#6500](https://github.com/streamlit/streamlit/issues/6500)).
* 🕸️ Bug fix: Added robust out-of-bounds checks for `min_value` and `max_value` in `st.number_input` ([#6847](https://github.com/streamlit/streamlit/pull/6847), [#6797](https://github.com/streamlit/streamlit/issues/6797)).

**Version 1.23.0**
------------------

*Release date: June 1, 2023*

**Highlights**

* ✂️ Announcing the general availability of [st.data\_editor](/develop/api-reference/data/st.data_editor), a widget that allows you to edit DataFrames and many other data structures in a table-like UI. **Breaking change:** the data editor's representation used in `st.session_state` was altered. Find out more about the new format in [Access edited data](/develop/concepts/design/dataframes#access-edited-data).
* ⚙️ Introducing the [Column configuration API](/develop/api-reference/data/st.column_config) with a suite of methods to configure the display and editing behavior of `st.dataframe` and `st.data_editor` columns (e.g. their title, visibility, type, or format). Keep an eye out for a detailed [blog post](https://blog.streamlit.io/) and in-depth [documentation](/develop/concepts/design/dataframes#configuring-columns) upcoming in the next two weeks.
* 🔌 Learn to use `st.experimental_connection` to create and manage data connections in your apps with the new [Connecting to data](/develop/concepts/connections/connecting-to-data) docs and [video tutorial](https://www.youtube.com/watch?v=xQwDfW7UHMo).

**Notable Changes**

* 📊 Streamlit now supports Protobuf 4 and Altair 5 ([#6215](https://github.com/streamlit/streamlit/issues/6215), [#6618](https://github.com/streamlit/streamlit/pull/6618), [#5626](https://github.com/streamlit/streamlit/issues/5626), [#6622](https://github.com/streamlit/streamlit/pull/6622)).
* ☎️ st.dataframe and st.data\_editor can hide index columns with `hide_index`, specify the display order of columns with `column_order`, and disable editing for individual columns with the `disabled` parameter.
* ⏱️ The `ttl` parameter in [st.cache\_data](/develop/api-reference/caching-and-state/st.cache_data) and [st.cache\_resource](/develop/api-reference/caching-and-state/st.cache_resource) accepts formatted strings, so you can simply say `ttl="30d"`, `ttl="1h30m"` and any other combination of `w`, `d`, `h`, `m`, `s` supported by [Pandas's Timedelta constructor](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.html) ([#6560](https://github.com/streamlit/streamlit/pull/6560)).
* 📂 `st.file_uploader` now interprets the `type` parameter more accurately. For example, "jpg" or ".jpg" now accept both "jpg" and "jpeg" extensions. This functionality has also been extended to "mpeg/mpg", "tiff/tif", "html/htm", and "mpeg4/mp4".
* 🤫 The new `global.disableWidgetStateDuplicationWarning` configuration option allows the silencing of warnings triggered by setting widget default values and keyed session state values concurrently ([#3605](https://github.com/streamlit/streamlit/issues/3605), [#6640](https://github.com/streamlit/streamlit/pull/6640)). Thanks, [@antonAce](https://github.com/antonAce)!

**Other Changes**

* 🏃‍♀️Improved startup time by lazy loading some dependencies ([#6531](https://github.com/streamlit/streamlit/pull/6531)).
* 👋 Removed `st.beta_*` and `st.experimental_show` due to deprecation and low-use ([#6558](https://github.com/streamlit/streamlit/pull/6558))
* 🚀 Further improvements to st.dataframe and st.data\_editor:
  + Improved editing on mobile devices for the data editor ([#6548](https://github.com/streamlit/streamlit/pull/6548)).
  + All editable columns have an icon in their column header and support tooltips ([#6550](https://github.com/streamlit/streamlit/pull/6550), [#6561](https://github.com/streamlit/streamlit/pull/6561)).
  + Enable editing for columns containing datetime, date, or time values ([#6025](https://github.com/streamlit/streamlit/pull/6025)).
  + New input validation options for columns in the data editor, such as `max_chars` and `validate` for text columns, and `min_value`, `max_value` and `step` for number columns ([#6563](https://github.com/streamlit/streamlit/pull/6563)).
  + Improved type parsing capabilities in the data editor ([#6551](https://github.com/streamlit/streamlit/pull/6551)).
  + Unified missing values to `None` in returned data structures ([#6544](https://github.com/streamlit/streamlit/pull/6544)).
  + A warning is shown in cells when integers exceed the maximum safe value of `(2^53) -1` ([#6311](https://github.com/streamlit/streamlit/issues/6311), [#6549](https://github.com/streamlit/streamlit/pull/6549)).
  + Prevented editing the sessions state by showing a warning ([#6634](https://github.com/streamlit/streamlit/pull/6634)).
  + Fixed issues with list columns sometimes breaking the frontend ([#6644](https://github.com/streamlit/streamlit/pull/6644)).
  + Fixed a display issue with index columns using category dtype ([#6680](https://github.com/streamlit/streamlit/issues/6680), [#6598](https://github.com/streamlit/streamlit/pull/6598)).
  + Fixed an issue that prevented a rerun when adding empty rows ([#6598](https://github.com/streamlit/streamlit/pull/6598)).
  + Unified the behavior between `st.data_editor` and `st.dataframe` related to auto-hiding the index column(s) based on the input data ([#6659](https://github.com/streamlit/streamlit/issues/6659), [#6598](https://github.com/streamlit/streamlit/pull/6598))
* 🛡️ Streamlit's [Security Policy](https://github.com/streamlit/streamlit/blob/develop/SECURITY.md) can be found in its GitHub repository ([#6666](https://github.com/streamlit/streamlit/pull/6666)).
* 🤏 Documented the integer size limit for `st.number_input` and `st.slider` ([#6724](https://github.com/streamlit/streamlit/pull/6724)).
* 🐍 The majority of Streamlit's Python dependencies have set a maximum allowable version, with the standard upper limit set to the next major version, but not inclusive of it ([#6691](https://github.com/streamlit/streamlit/pull/6691)).
* 💅 UI design improvements to in-app modals ([#6688](https://github.com/streamlit/streamlit/pull/6688)).
* 🐞 Bug fix: `st.date_input`'s date selector is equally visible in dark mode ([#6072](https://github.com/streamlit/streamlit/issues/6072), [#6630](https://github.com/streamlit/streamlit/pull/6630)).
* 🐜 Bug fix: the sidebar navigation expansion indicator in multipage apps is restored ([#6731](https://github.com/streamlit/streamlit/pull/6731)).
* 🐛 Bug fix: The docstring and exception message for `st.set_page_config` have been updated to clarify that this command can be invoked once for each page within a multipage app, rather than once per entire app ([#6594](https://github.com/streamlit/streamlit/pull/6594)).
* 🐝 Bug fix: `st.json` no longer collapses multiple spaces in both keys and values with single space when rendered ([#6657](https://github.com/streamlit/streamlit/issues/6657), [#6663](https://github.com/streamlit/streamlit/pull/6663)).

**Version 1.22.0**
------------------

*Release date: April 27, 2023*

**Highlights**

* 🔌 Introducing `st.experimental_connection`: Easily connect your app to data sources and APIs using our new connection feature. Find more details in the [API reference](/develop/api-reference/connections), and stay tuned for an upcoming blog post and in-depth documentation! In the meantime, explore our updated [MySQL](/develop/tutorials/databases/mysql) and [Snowflake](/develop/tutorials/databases/snowflake) connection tutorials for examples of this feature.

**Notable Changes**

* 🐼 Streamlit now supports Pandas 2.0 ([#6413](https://github.com/streamlit/streamlit/issues/6413), [#6378](https://github.com/streamlit/streamlit/pull/6378), [#6507](https://github.com/streamlit/streamlit/pull/6507)). Thanks, [connortann](https://github.com/connortann)!
* 🍔 Customize the visibility of items in the toolbar, options menu, and the settings dialog using the `client.toolbarMode` [config option](https://docs.streamlit.io/develop/concepts/configuration#view-all-configuration-options) ([#6174](https://github.com/streamlit/streamlit/pull/6174)).
* 🪵 Streamlit logs now reside in the "streamlit" namespace instead of the root logger, enabling app developers to better manage log handling ([#3978](https://github.com/streamlit/streamlit/issues/3978), [#6377](https://github.com/streamlit/streamlit/pull/6377)).

**Other Changes**

* 🔏 CLI parameters can no longer be used to set sensitive configuration values ([#6376](https://github.com/streamlit/streamlit/pull/6376)).
* 🤖 Improved the debugging experience by reducing log noise ([#6391](https://github.com/streamlit/streamlit/pull/6391)).
* 🐞 Bug fix: `@st.cache_data` decorated functions support UUID objects as parameters ([#6440](https://github.com/streamlit/streamlit/issues/6440), [#6459](https://github.com/streamlit/streamlit/pull/6459)).
* 🐛 Bug fix: Tabbing through buttons and other elements now displays a red border only when focused, not when clicked ([#6373](https://github.com/streamlit/streamlit/pull/6373)).
* 🪲 Bug fix: `st.multiselect`'s clear icon is larger and includes a hover effect ([#6471](https://github.com/streamlit/streamlit/pull/6471)).
* 🐜 Bug fix: Custom theme font settings no longer apply to code blocks ([#6484](https://github.com/streamlit/streamlit/issues/6484), [#6535](https://github.com/streamlit/streamlit/pull/6535)).
* ©️ Bug fix: `st.code`'s copy-to-clipboard button appears when you hover on code blocks ([#6490](https://github.com/streamlit/streamlit/issues/6490), [#6498](https://github.com/streamlit/streamlit/pull/6498)).

**Version 1.21.0**
------------------

*Release date: April 6, 2023*

**Highlights**

* 📏 Introducing `st.divider` — a command that displays a horizontal line in your app. Learn how to use this command in its [API reference](/develop/api-reference/text/st.divider).
* 🔏 Streamlit now supports the use of a global `secrets.toml` file, in addition to a project-level file, to easily store and securely access your secrets. Learn more in [Secrets management](/develop/concepts/connections/secrets-management).
* 🚀 [st.help](/develop/api-reference/utilities/st.help) has been revamped to show more information about object methods, attributes, classes, and more, which is great for debugging ([#5857](https://github.com/streamlit/streamlit/pull/5857), [#6382](https://github.com/streamlit/streamlit/pull/6382))!

**Notable Changes**

* 🪜 [st.time\_input](/develop/api-reference/widgets/st.time_input) supports adding a stepping interval with the keyword-only `step` parameter ([#6071](https://github.com/streamlit/streamlit/pull/6071)).
* ❓ Most [text elements](/develop/api-reference/text) can include tooltips with the `help` parameter ([#6043](https://github.com/streamlit/streamlit/pull/6043)).
* ↔️ [st.pyplot](/develop/api-reference/charts/st.pyplot) has a `use_container_width` parameter to set the chart to the container width (now all [chart elements](/develop/api-reference/charts) support this parameter) ([#6067](https://github.com/streamlit/streamlit/pull/6067)).
* 👩‍💻 [st.code](/develop/api-reference/text/st.code) supports optionally displaying line numbers to the code block's left with the boolean `line_numbers` parameter ([#5756](https://github.com/streamlit/streamlit/issues/5756), [#6042](https://github.com/streamlit/streamlit/pull/6042)).
* ⚓ Anchors in header elements can be turned off by setting `anchor=False` ([#6158](https://github.com/streamlit/streamlit/pull/6158)).

**Other Changes**

* 🐼 [st.table](/develop/api-reference/data/st.table) and [st.dataframe](/develop/api-reference/data/st.dataframe) support `pandas.Period`, and number and boolean types in categorical columns ([#2547](https://github.com/streamlit/streamlit/issues/2547), [#5429](https://github.com/streamlit/streamlit/pull/5429), [#5329](https://github.com/streamlit/streamlit/issues/5392), [#6248](https://github.com/streamlit/streamlit/pull/6248)).
* 🕸️ Added `.webp` to the list of allowed static file extensions ([#6331](https://github.com/streamlit/streamlit/pull/6331))
* 🐞 Bug fix: stop script execution on websocket close to immediately clear session information ([#6166](https://github.com/streamlit/streamlit/issues/6166), [#6204](https://github.com/streamlit/streamlit/pull/6204)).
* 🐜 Bug fixes: updated allowed/disallowed label markdown behavior such that unsupported elements are unwrapped and only their children (text contents) render ([#5872](https://github.com/streamlit/streamlit/issues/5872), [#6036](https://github.com/streamlit/streamlit/issues/6036), [#6054](https://github.com/streamlit/streamlit/issues/6054), [#6163](https://github.com/streamlit/streamlit/pull/6163)).
* 🪲 Bug fixes: don't push browser history states on rerun, use HTTPS to load external resources in `streamlit hello`, and make the browser back button work for multipage apps ([#5292](https://github.com/streamlit/streamlit/issues/5292), [#6266](https://github.com/streamlit/streamlit/pull/6266), [#6232](https://github.com/streamlit/streamlit/pull/6232)). Thanks, [whitphx](https://github.com/whitphx)!
* 🐝 Bug fix: avoid showing emoji on non-UTF-8 terminals. ([#2284](https://github.com/streamlit/streamlit/issues/2284), [#6088](https://github.com/streamlit/streamlit/pull/6088)). Thanks, [kcarnold](https://github.com/kcarnold)!
* 📁 Bug fix: override default use of [File System Access API](https://developer.mozilla.org/en-US/docs/Web/API/File_System_Access_API) for `react-dropzone` so that `st.file_uploader`'s File Selection Dialog only shows file types corresponding to those included in the `type` parameter ([#6176](https://github.com/streamlit/streamlit/issues/6176), [#6315](https://github.com/streamlit/streamlit/pull/6315)).
* 💾 Bug fix: make the `.clear()` method on cache-decorated functions work ([#6310](https://github.com/streamlit/streamlit/issues/6310), [#6321](https://github.com/streamlit/streamlit/pull/6321)).
* 🏃 Bug fix: `st.experimental_get_query_params` doesn't need reruns to work ([#6347](https://github.com/streamlit/streamlit/issues/6347), [#6348](https://github.com/streamlit/streamlit/pull/6348)). Thanks, [PaleNeutron](https://github.com/PaleNeutron)!
* 🐛 Bug fix: `CachedStFunctionWarning` mentions `experimental_allow_widgets` instead of the deprecated `suppress_st_warning` ([#6216](https://github.com/streamlit/streamlit/issues/6216), [#6217](https://github.com/streamlit/streamlit/pull/6217)).

**Version 1.20.0**
------------------

*Release date: March 09, 2023*

**Notable Changes**

* 🔐 Added support for configuring SSL to [serve apps directly over HTTPS](/develop/concepts/configuration/https-support) ([#5969](https://github.com/streamlit/streamlit/pull/5969)).
* 🖼️ Granular control over app embedding behavior with the `/?embed` and `/?embed_options` query parameters. Learn how to use this feature in our [docs](/deploy/streamlit-community-cloud/share-your-app/embed-your-app) ([#6011](https://github.com/streamlit/streamlit/pull/6011), [#6019](https://github.com/streamlit/streamlit/pull/6019)).
* ⚡ Enabled the `runner.fastReruns` [configuration option](/develop/concepts/configuration#view-all-configuration-options) by default to make apps much more responsive to user interaction ([#6200](https://github.com/streamlit/streamlit/pull/6200)).

**Other Changes**

* 🍔 Cleaned up the hamburger menu by removing the least used options ([#6080](https://github.com/streamlit/streamlit/pull/6080)).
* 🖨️ Design changes to ensure apps being printed or saved as a PDF look good ([#6180](https://github.com/streamlit/streamlit/pull/6180)).
* 🐞 Bug fix: improved `dtypes` checking in `st.experimental_data_editor` ([#6185](https://github.com/streamlit/streamlit/issues/6185), [#6188](https://github.com/streamlit/streamlit/pull/6188)).
* 🐛 Bug fix: properly position `st.metric`'s `help` tooltip when not inside columns ([#6168](https://github.com/streamlit/streamlit/pull/6168)).
* 🪲 Bug fix: regression in retrieving messages from the server's `ForwardMsgCache` ([#6210](https://github.com/streamlit/streamlit/pull/6210)).
* 🌀 Bug fix: `st.cache_data` docstring for the `show_spinner` param now lists `str` as a supported type ([#6207](https://github.com/streamlit/streamlit/issues/6207), [#6213](https://github.com/streamlit/streamlit/pull/6213)).
* ⏱️ Made ping and websocket timeouts far more forgiving ([#6212](https://github.com/streamlit/streamlit/pull/6212)).
* 🗺️ `st.map` and `st.pydeck_chart` docs state that Streamlit's Mapbox token will not work indefinitely ([#6143](https://github.com/streamlit/streamlit/pull/6143)).

**Version 1.19.0**
------------------

*Release date: February 23, 2023*

**Highlights**

* ✂️ Introducing `st.experimental_data_editor`, a widget that allows you to edit DataFrames and many other data structures in a table-like UI. Read more in our [documentation](/develop/concepts/design/dataframes) and [blog post](https://blog.streamlit.io/editable-dataframes-are-here/).

**Other Changes**

* ✨ Streamlit's GitHub README got a new look ([#6016](https://github.com/streamlit/streamlit/pull/6016)).
* 🌚 Improved readability of styled dataframe cells in dark mode ([#6060](https://github.com/streamlit/streamlit/issues/6060), [#6098](https://github.com/streamlit/streamlit/pull/6098)).
* 🐛 Bug fix: make apps work again in the latest versions of Safari, and in Chrome with third-party cookies blocked ([#6092](https://github.com/streamlit/streamlit/issues/6092), [#6094](https://github.com/streamlit/streamlit/pull/6094), [#6087](https://github.com/streamlit/streamlit/issues/6087), [#6100](https://github.com/streamlit/streamlit/pull/6100)).
* 🐞 Bug fix: refer to new cache primitives in the "Clear cache" dialog and error messages ([#6082](https://github.com/streamlit/streamlit/pull/6082), [#6128](https://github.com/streamlit/streamlit/pull/6128)).
* 🐝 Bug fix: properly cache class member functions and instance methods ([#6109](https://github.com/streamlit/streamlit/issues/6109), [#6114](https://github.com/streamlit/streamlit/pull/6114)).
* 🐜 Bug fix: regression in `st.metric` tooltip position ([#6093](https://github.com/streamlit/streamlit/issues/6093), [#6129](https://github.com/streamlit/streamlit/pull/6129)).
* 🪲 Bug fix: allow fullscreen button to show for dataframes, charts, etc, in expander ([#6083](https://github.com/streamlit/streamlit/pull/6083), [#6148](https://github.com/streamlit/streamlit/pull/6148)).

**Version 1.18.0**
------------------

*Release date: February 09, 2023*

**Highlights**

* 🎊 Introducing `@st.cache_data` and `@st.cache_resource` — two new caching commands to replace `st.cache`! Check out our [blog post](https://blog.streamlit.io/p/c0a90231-9848-47ec-a40c-ad4a344e4de1/) and [documentation](/develop/concepts/architecture/caching) for more information.

**Notable Changes**

* 🪆 `st.columns` supports up to one level of column nesting (i.e., columns inside columns) in the main area of the app.
* ⏳ `st.progress` supports adding a message to display above the progress bar with the `text` keyword parameter.
* ↔️ `st.button` has an optional `use_container_width` parameter to allow you to stretch buttons across the full container width.
* 🐍 We formally added support for Python 3.11.
* 🖨️ Save your app as a PDF via the "Print" option in your app's hamburger menu.
* 🛎️ Apps can serve small, static media files via the `enableStaticServing` config option. See our [documentation](/develop/concepts/configuration/serving-static-files) on how to use this feature and our demo [app](https://static-file-serving.streamlit.app/) for an example.

**Other Changes**

* 🏁 All Streamlit endpoints (including `/healthz`) have been renamed to have a consistent pattern and avoid any clashes with reserved endpoints of GCP (notably Cloud Run and App Engine) ([#5534](https://github.com/streamlit/streamlit/pull/5534)).
* ⚡ Improved caching performance when multiple sessions access an uncomputed cached value simultaneously ([#6017](https://github.com/streamlit/streamlit/pull/6017)).
* 🚧 Streamlit only displays deprecation warnings in the browser when the `client.showErrorDetails` config option is set to `True`. Deprecation warnings always get logged to the console, regardless of whether they're displayed in-browser ([#5945](https://github.com/streamlit/streamlit/pull/5945)).
* 🏓 Refactored the `st.dataframe` internals to improve dataframe handling and conversion, such as detecting more types, converting key-value dicts to dataframes, and more ([#6026](https://github.com/streamlit/streamlit/pull/6026), [#6023](https://github.com/streamlit/streamlit/pull/6023)).
* 💽 The behavior of widget labels when they are passed unsupported Markdown elements is documented ([#5978](https://github.com/streamlit/streamlit/pull/5978)).
* 📊 Bug fix: Plotly improvements — upgraded multiple frontend dependencies, including Plotly, to the latest version to properly redraw cached charts, make Plotly mapbox animations work, and allow users to update the figure layout when using the Streamlit theme ([#5885](https://github.com/streamlit/streamlit/pull/5885), [#5967](https://github.com/streamlit/streamlit/pull/5967), [#6055](https://github.com/streamlit/streamlit/pull/6055)).
* 📶 Bug fix: allow browser tabs that transiently disconnect (due to a network blip, load balancer timeout, etc.) to avoid losing all of their state ([#5856](https://github.com/streamlit/streamlit/pull/5856)).
* 📱 Bug fix: the keyboard is hidden on mobile when `st.selectbox` and `st.multiselect` have less than 10 options ([#5979](https://github.com/streamlit/streamlit/pull/5979)).
* 🐝 Bug fix: design tweaks to `st.metric`, `st.multiselect`, `st.tabs` , and menu items to prevent label overflow and scrolling issues, especially with small viewport sizes ([#5933](https://github.com/streamlit/streamlit/pull/5933), [#6034](https://github.com/streamlit/streamlit/pull/6034)).
* 🐞 Bug fix: switched to a functioning Twemoji URL from which page favicons are loaded in `st.set_page_config` ([#5943](https://github.com/streamlit/streamlit/pull/5943)).
* ✍️ More type hints ([#5986](https://github.com/streamlit/streamlit/pull/5986)). Thanks, [harahu](https://github.com/harahu)!

**Version 1.17.0**
------------------

*Release date: January 12, 2023*

**Notable Changes**

* 🪄 [`@st.experimental_singleton`](/develop/api-reference/caching-and-state/st.experimental_singleton#validating-the-cache) supports an optional `validate` parameter that accepts a validation function for cached data and is called each time the cached value is accessed.
* 💾  [`@st.experimental_memo`](/develop/api-reference/caching-and-state/st.experimental_memo)'s `persist` parameter can also accept booleans.

**Other Changes**

* 📟 Multipage apps exclude `__init__.py` from the page selector ([#5890](https://github.com/streamlit/streamlit/pull/5890)).
* 📐 The iframes of embedded apps have the ability to dynamically resize their height ([#5894](https://github.com/streamlit/streamlit/pull/5894)).
* 🐞 Bug fix: thumb values of range sliders respect the container width ([#5913](https://github.com/streamlit/streamlit/pull/5913)).
* 🪲 Bug fix: all examples in docstrings of Streamlit commands contain relevant imports to make them reproducible ([#5877](https://github.com/streamlit/streamlit/pull/5877)).

[Previous: 2024](/develop/quick-reference/release-notes/2024)[Next: 2022](/develop/quick-reference/release-notes/2022)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
