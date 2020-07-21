import streamlit as st
from streamlit_embedcode import *

"## github_gist test"
github_gist("https://gist.github.com/randyzwitch/934d502e53f2adcb48eea2423fe4a47e")

"## gitlab_snippet test"
gitlab_snippet("https://gitlab.com/snippets/1995463", height=400)

"## pastebin_snippet test"
pastebin_snippet("https://pastebin.com/AWYbziQF", width=600, scrolling=False)

"## codepen_snippet test"
codepen_snippet("https://codepen.io/ste-vg/pen/GRooLza", width=600, scrolling=False)

"## ideone_snippet test"
ideone_snippet("https://ideone.com/vQ54cr")

"## tagmycode_snippet test"
tagmycode_snippet(
    "https://tagmycode.com/snippet/5965/recursive-list-files-in-a-dir#.Xwyc43VKglU"
)
