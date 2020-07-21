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


class MyTestClass(BaseCase):
    def test_basic(self):

        self.open("http://localhost:8501")
        self.assert_title("app_to_test · Streamlit")
        # self.type('input[name="q"]', "xkcd book\n")
        # self.assert_text("xkcd: volume 0", "h3")
        # self.open("https://xkcd.com/353/")

        # self.assert_element('img[alt="Python"]')
        # self.click('a[rel="license"]')
        # self.assert_text("free to copy and reuse")
        # self.go_back()
        # self.click_link_text("About")
        # self.assert_exact_text("xkcd.com", "h2")
