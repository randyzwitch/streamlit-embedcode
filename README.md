# streamlit-embedcode

![Python package](https://github.com/randyzwitch/streamlit-embedcode/workflows/Python%20package/badge.svg)

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/randyzwitch/streamlit-embedcode/examples/streamlit_app.py)

streamlit-embedcode is the easiest way to embed code snippets into your Streamlit app! This [static component](https://docs.streamlit.io/en/stable/develop_streamlit_components.html#create-a-static-component) supports the following code sharing services:

- [GitHub gist](https://gist.github.com/)
- [GitLab snippets](https://gitlab.com/explore/snippets)
- [Pastebin](https://pastebin.com/)
- [CodePen](https://codepen.io/)
- [Ideone](https://ideone.com/)
- [TagMyCode](https://tagmycode.com/)

## Installation

streamlit-embedcode is distributed via [PyPI](https://pypi.org/project/streamlit-embedcode/):

```python
pip install streamlit-embedcode
```

## Examples

Using streamlit-embedcode is as simple as importing the code service you want to use:

```python
import streamlit as st
from streamlit_embedcode import github_gist

github_gist("https://gist.github.com/randyzwitch/be8c5e9fb5b8e7b046afebcac12e5087/")
```

Optionally, you can provide arguments for `height`, `width` and `scrolling` to control the behavior of the iframe the content is displayed in.

![github_streamlit_embed](https://github.com/randyzwitch/streamlit-embedcode/blob/master/_static/gh_gist_example.png)
