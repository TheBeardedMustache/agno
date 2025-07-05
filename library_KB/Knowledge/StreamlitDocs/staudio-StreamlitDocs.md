st.audio - Streamlit Docs

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

      *remove*

      * [st.audio](/develop/api-reference/media/st.audio)
      * [st.image](/develop/api-reference/media/st.image)
      * [st.logo](/develop/api-reference/media/st.logo)
      * [st.video](/develop/api-reference/media/st.video)
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
* [Media elements](/develop/api-reference/media)/
* [st.audio](/develop/api-reference/media/st.audio)

st.audio
--------

Streamlit VersionVersion 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0Version 1.21.0Version 1.20.0

Display an audio player.

| Function signature[[source]](https://github.com/streamlit/streamlit/blob/1.46.0/lib/streamlit/elements/media.py#L74 "View st.audio source code on GitHub") | |
| --- | --- |
| st.audio(data, format="audio/wav", start\_time=0, \*, sample\_rate=None, end\_time=None, loop=False, autoplay=False, width="stretch") | |
| Parameters | |
| data (str, Path, bytes, BytesIO, numpy.ndarray, or file) | The audio to play. This can be one of the following:   * A URL (string) for a hosted audio file. * A path to a local audio file. The path can be a str   or Path object. Paths can be absolute or relative to the   working directory (where you execute streamlit run). * Raw audio data. Raw data formats must include all necessary file   headers to match the file format specified via format.   If data is a NumPy array, it must either be a 1D array of the waveform or a 2D array of shape (C, S) where C is the number of channels and S is the number of samples. See the default channel order at <http://msdn.microsoft.com/en-us/library/windows/hardware/dn653308(v=vs.85).aspx> |
| format (str) | The MIME type for the audio file. This defaults to "audio/wav". For more information about MIME types, see <https://www.iana.org/assignments/media-types/media-types.xhtml>. |
| start\_time (int, float, timedelta, str, or None) | The time from which the element should start playing. This can be one of the following:   * None (default): The element plays from the beginning. * An int or float specifying the time in seconds. float   values are rounded down to whole seconds. * A string specifying the time in a format supported by [Pandas'   Timedelta constructor](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.html),   e.g. "2 minute", "20s", or "1m14s". * A timedelta object from [Python's built-in datetime library](https://docs.python.org/3/library/datetime.html#timedelta-objects),   e.g. timedelta(seconds=70). |
| sample\_rate (int or None) | The sample rate of the audio data in samples per second. This is only required if data is a NumPy array. |
| end\_time (int, float, timedelta, str, or None) | The time at which the element should stop playing. This can be one of the following:   * None (default): The element plays through to the end. * An int or float specifying the time in seconds. float   values are rounded down to whole seconds. * A string specifying the time in a format supported by [Pandas'   Timedelta constructor](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.html),   e.g. "2 minute", "20s", or "1m14s". * A timedelta object from [Python's built-in datetime library](https://docs.python.org/3/library/datetime.html#timedelta-objects),   e.g. timedelta(seconds=70). |
| loop (bool) | Whether the audio should loop playback. |
| autoplay (bool) | Whether the audio file should start playing automatically. This is False by default. Browsers will not autoplay audio files if the user has not interacted with the page by clicking somewhere. |
| width ("stretch" or int) | The width of the audio player element. This can be one of the following:   * "stretch" (default): The width of the element matches the   width of the parent container. * An integer specifying the width in pixels: The element has a   fixed width. If the specified width is greater than the width of   the parent container, the width of the element matches the width   of the parent container. |

#### Examples

To display an audio player for a local file, specify the file's string
path and format.

```

import streamlit as st

st.audio("cat-purr.mp3", format="audio/mpeg", loop=True)

```

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen *open\_in\_new*](https://doc-audio-purr.streamlit.app//?utm_medium=oembed&)

You can also pass bytes or numpy.ndarray objects to st.audio.

```

import streamlit as st
import numpy as np

audio_file = open("myaudio.ogg", "rb")
audio_bytes = audio_file.read()

st.audio(audio_bytes, format="audio/ogg")

sample_rate = 44100  # 44100 samples per second
seconds = 2  # Note duration of 2 seconds
frequency_la = 440  # Our played note will be 440 Hz
# Generate array with seconds*sample_rate steps, ranging between 0 and seconds
t = np.linspace(0, seconds, seconds * sample_rate, False)
# Generate a 440 Hz sine wave
note_la = np.sin(frequency_la * t * 2 * np.pi)

st.audio(note_la, sample_rate=sample_rate)

```

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen *open\_in\_new*](https://doc-audio.streamlit.app//?utm_medium=oembed&)

[Previous: Media elements](/develop/api-reference/media)[Next: st.image](/develop/api-reference/media/st.image)

*forum*

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

© 2025 Snowflake Inc.Cookie policy

*forum* Ask AI
