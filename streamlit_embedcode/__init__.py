import streamlit as st


def _clean_link(link):
    """Strip trailing slash if present on link.

    Parameters
    ----------
    link : str
        URL from code sharing website

    Returns
    -------
    str
        Returns value of `link` without trailing slash.

    Example
    -------
    >>> _clean_link("https://gist.github.com/randyzwitch/be8c5e9fb5b8e7b046afebcac12e5087/")
    'https://gist.github.com/randyzwitch/be8c5e9fb5b8e7b046afebcac12e5087'

    >>> _clean_link("https://gist.github.com/randyzwitch/be8c5e9fb5b8e7b046afebcac12e5087")
    'https://gist.github.com/randyzwitch/be8c5e9fb5b8e7b046afebcac12e5087'
    """

    return link[:-1] if link[-1] == "/" else link


def github_gist(link, height=600, width=950, scrolling=True):
    """Embed a GitHub gist.

    Parameters
    ----------
    link : str
        URL from https://gist.github.com/
    height: int
        Height of the resulting iframe
    width: int
        Width of the resulting iframe
    scrolling: bool
        If content is larger than iframe size, provide scrollbars?
    
    Example
    -------
    >>> github_gist("https://gist.github.com/randyzwitch/be8c5e9fb5b8e7b046afebcac12e5087/")
    """

    gistcreator, gistid = _clean_link(link).split("/")[-2:]
    return st.html(
        f"""<script src="https://gist.github.com/{gistcreator}/{gistid}.js"></script>""",
        height=height,
        width=width,
        scrolling=scrolling,
    )


def gitlab_snippet(link, height=600, width=950, scrolling=True):
    """Embed a Gitlab snippet.

    Parameters
    ----------
    link : str
        URL from https://gitlab.com/explore/snippets
    height: int
        Height of the resulting iframe
    width: int
        Width of the resulting iframe
    scrolling: bool
        If content is larger than iframe size, provide scrollbars?
    
    Example
    -------
    >>> gitlab_snippet("https://gitlab.com/snippets/1990429/", height = 400)
    """

    snippetnumber = _clean_link(link).split("/")[-1]
    return st.html(
        f"""<script src='https://gitlab.com/snippets/{snippetnumber}.js'></script>""",
        height=height,
        width=width,
        scrolling=scrolling,
    )


def pastebin_snippet(link, height=600, width=950, scrolling=True):
    """Embed a Pastebin snippet.

    Parameters
    ----------
    link : str
        URL from https://pastebin.com/
    height: int
        Height of the resulting iframe
    width: int
        Width of the resulting iframe
    scrolling: bool
        If content is larger than iframe size, provide scrollbars?
    
    Example
    -------
    >>> pastebin_snippet("https://pastebin.com/AWYbziQF", width = 600, scrolling = False)
    """

    snippetnumber = _clean_link(link).split("/")[-1]
    return st.html(
        f"""<script src="https://pastebin.com/embed_js/{snippetnumber}"></script>""",
        height=height,
        width=width,
        scrolling=scrolling,
    )


def codepen_snippet(
    link, height=600, width=950, scrolling=True, theme="light", preview=True
):

    user, _, slughash = _clean_link(link).split("/")[-3:]
    return st.html(
        f"""
        <p class="codepen" 
        data-height="{height}" 
        data-theme-id="{theme}" 
        data-default-tab="html,result" 
        data-user="{user}" 
        data-slug-hash="{slughash}" 
        data-preview="{str(preview).lower()}" 
        style="height: {height}px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;"">
    </p><script async src="https://static.codepen.io/assets/embed/ei.js"></script>
    """,
        height=height,
        width=width,
        scrolling=scrolling,
    )


def ideone_snippet(link, height=600, width=950, scrolling=True):

    snippetnumber = _clean_link(link).split("/")[-1]
    return st.html(
        f"""<script src="https://ideone.com/e.js/{snippetnumber}" type="text/javascript" ></script>""",
        height=height,
        width=width,
        scrolling=scrolling,
    )


def tagmycode_snippet(link, height=600, width=950, scrolling=True):

    snippetnumber = _clean_link(link).split("/")[-2]
    return st.html(
        f"""<script src="https://tagmycode.com/embed/js/{snippetnumber}"></script>""",
        height=height,
        width=width,
        scrolling=scrolling,
    )
