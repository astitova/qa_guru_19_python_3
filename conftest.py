import pytest
from selene import browser

@pytest.fixture(scope="function")
def size_browser():
    browser.config.window_size = (1920, 1080)

    yield

    browser.quit()

@pytest.fixture(scope="function")
def url(size_browser):
    browser.open('https://duckduckgo.com')





