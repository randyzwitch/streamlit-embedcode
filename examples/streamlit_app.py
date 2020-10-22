import streamlit as st
from streamlit_embedcode import *

st.beta_set_page_config(page_title="streamlit-embedcode documentation",)

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

    "---"
    "### Example:"
    with st.echo():

        import streamlit as st
        from streamlit_embedcode import github_gist

        t = st.text_input(
            "Enter GitHub gist URL:",
            "https://gist.github.com/randyzwitch/934d502e53f2adcb48eea2423fe4a47e",
        )

        w = st.slider("width", 300, 800, 710)
        github_gist(t, width=w)

elif choice == "gitlab_snippet()":
    """## gitlab_snippet()"""

    gitlab_snippet

    "---"
    "### Example:"
    with st.echo():

        import streamlit as st
        from streamlit_embedcode import gitlab_snippet

        t = st.text_input(
            "Enter GitLab snippet URL:", "https://gitlab.com/snippets/1995463",
        )

        w = st.slider("width", 300, 800, 710)
        gitlab_snippet(t, width=w)

elif choice == "pastebin_snippet()":
    """## pastebin_snippet()"""

    pastebin_snippet

    "---"
    "### Example:"
    with st.echo():

        import streamlit as st
        from streamlit_embedcode import pastebin_snippet

        t = st.text_input(
            "Enter Pastebin snippet URL:", "https://pastebin.com/i1YQv94Q",
        )

        w = st.slider("width", 300, 800, 710)
        pastebin_snippet(t, width=w)

elif choice == "codepen_snippet()":
    """## codepen_snippet()"""

    codepen_snippet

    "---"
    "### Example:"
    with st.echo():

        import streamlit as st
        from streamlit_embedcode import codepen_snippet

        t = st.text_input(
            "Enter CodePen snippet URL:", "https://codepen.io/ste-vg/pen/GRooLza",
        )

        w = st.slider("width", 300, 800, 750, key="1")
        h = st.slider("height", 500, 800, 600, key="2")
        codepen_snippet(t, width=w, height=h)

elif choice == "ideone_snippet()":
    """## ideone_snippet()"""

    ideone_snippet

    "---"
    "### Example:"
    with st.echo():

        import streamlit as st
        from streamlit_embedcode import ideone_snippet

        t = st.text_input("Enter Ideone snippet URL:", "https://ideone.com/vQ54cr",)

        w = st.slider("width", 300, 800, 710, key="1")
        ideone_snippet(t, width=w)

elif choice == "tagmycode_snippet()":
    """## tagmycode_snippet()"""

    tagmycode_snippet

    "---"
    "### Example:"
    with st.echo():

        import streamlit as st
        from streamlit_embedcode import tagmycode_snippet

        t = st.text_input(
            "Enter Ideone snippet URL:",
            "https://tagmycode.com/snippet/5965/recursive-list-files-in-a-dir#.Xwyc43VKglU",
        )

        w = st.slider("width", 300, 800, 710, key="1")
        tagmycode_snippet(t, width=w)
