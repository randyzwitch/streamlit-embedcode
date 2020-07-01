import streamlit as st
from streamlit_embedcode import *

# CSS
st.markdown(
    """
<style>

.reportview-container .markdown-text-container {
    font-family: monospace;
}
.sidebar .sidebar-content {
    background-image: linear-gradient(#2e7bcf,#2e7bcf);
    color: white;
}

.Widget>label {
    color: white;
    font-family: monospace;
}

[class^="st-b"]  {
    color: white;
    font-family: monospace;
}

.st-bb {
    background-color: transparent;
}

.st-at {
    background-color: #0c0080;
}

footer {
    font-family: monospace;
}

.reportview-container .main footer, .reportview-container .main footer a {
    color: #0c0080;
}

header .decoration {
    background-image: none;
}

:root {
    --breakpoint-xs: 1200px;
    --breakpoint-sm: 1200px;
    --breakpoint-md: 1200px;
    --breakpoint-lg: 1200px;
    --breakpoint-xl: 1200px;
}

</style>
""",
    unsafe_allow_html=True,
)

# st-ak st-ai st-al st-am st-an st-ao st-ap st-aq st-ar st-as
choice = st.sidebar.radio(
    "Please choose a function to see its documentation",
    (
        "Home",
        "github_gist()",
        "gitlab_snippet()",
        "pastebin_snippet()",
        "codepen_snippet()",
        "ideone_snippet()",
        "tagmycode_snippet()",
    ),
)

if choice == "Home":
    """
    # streamlit-embedcode

    [streamlit-embedcode](https://github.com/randyzwitch/streamlit-embedcode) is the easiest way to embed code snippets into your Streamlit app! This component supports the following code sharing services:

    - [GitHub gist](https://gist.github.com/)
    - [GitLab snippets](https://gitlab.com/explore/snippets)
    - [Pastebin](https://pastebin.com/)
    - [CodePen](https://codepen.io/)
    - [Ideone](https://ideone.com/)
    - [TagMyCode](https://tagmycode.com/)

    ---

    ## Installation

    streamlit-embedcode is distributed via PyPI:

    ```python
    pip install streamlit-embedcode
    ```
    ---

    ## Examples
    To see examples for each function, please select using the radio button in the sidebar.
    """

elif choice == "github_gist()":
    """## github_gist()"""

    github_gist

elif choice == "gitlab_snippet()":
    """## gitlab_snippet()"""

    gitlab_snippet

elif choice == "pastebin_snippet()":
    """## pastebin_snippet()"""

    pastebin_snippet

elif choice == "codepen_snippet()":
    """## codepen_snippet()"""

    codepen_snippet

elif choice == "ideone_snippet()":
    """## ideone_snippet()"""

    ideone_snippet

elif choice == "tagmycode_snippet()":
    """## tagmycode_snippet()"""

    tagmycode_snippet
