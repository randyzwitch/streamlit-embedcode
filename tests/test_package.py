from streamlit_embedcode import _clean_link
from seleniumbase import BaseCase  # https://seleniumbase.io/


def test_cleanlink_notrailing():
    assert (
        _clean_link(
            "https://gist.github.com/randyzwitch/be8c5e9fb5b8e7b046afebcac12e5087"
        )
        == "https://gist.github.com/randyzwitch/be8c5e9fb5b8e7b046afebcac12e5087"
    )


def test_cleanlink_trailing():
    assert (
        _clean_link(
            "https://gist.github.com/randyzwitch/be8c5e9fb5b8e7b046afebcac12e5087/"
        )
        == "https://gist.github.com/randyzwitch/be8c5e9fb5b8e7b046afebcac12e5087"
    )


class ComponentsTest(BaseCase):
    def test_basic(self):

        # open the app
        self.open("http://localhost:8501")

        # check basic properties of all Streamlit apps
        self.assert_title("app_to_test · Streamlit")
        self.assert_element("div.withScreencast")
        self.assert_element("div.stApp")

        # github_gist
        self.assert_text("github_gist test")
        self.is_element_in_an_iframe("div.gist-file")
        self.is_element_in_an_iframe("div.gist-data")
        self.is_element_in_an_iframe("div.gist-meta")

        # gitlab_snippet
        self.assert_text("gitlab_snippet test")
        self.is_element_in_an_iframe("div.gitlab-embed-snippets")

        # pastebin_snippet
        self.assert_text("pastebin_snippet test")
        self.is_element_in_an_iframe("div.embedPastebin")

        # codepen_snippet
        self.assert_text("codepen_snippet test")
        self.is_element_in_an_iframe("div.cp_embed_wrapper")

        # ideone_snippet
        self.assert_text("ideone_snippet test")
        # TODO

        # tagmycode_snippet
        self.assert_text("tagmycode_snippet test")
        self.is_element_in_an_iframe("div#tmc-embed-snippet")
