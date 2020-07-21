import selenium
from streamlit_embedcode import _clean_link


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


# set up Selenium
# https://www.lambdatest.com/blog/test-automation-using-pytest-and-selenium-webdriver/
import pytest
import subprocess
from selenium import webdriver
from chromedriver_py import binary_path
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

# Fixture for Chrome
@pytest.fixture(scope="class")
def chrome_driver_init(request):
    chrome_driver = webdriver.Chrome(executable_path=binary_path)
    request.cls.driver = chrome_driver
    yield
    chrome_driver.close()


@pytest.mark.usefixtures("chrome_driver_init")
class BasicTest:
    pass


class Test_URL(BasicTest):
    def test_open_url(self):
        self.driver.get("https://www.lambdatest.com/")
        print(self.driver.title)

