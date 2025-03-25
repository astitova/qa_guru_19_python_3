from selene import browser, be, have

def test_search_success(url, size_browser):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    assert browser.element('[id="react-layout"]').should(have.text('User-oriented Web UI browser tests in Python'))


def test_search_zero_result(url, size_browser):
    browser.element('[name="q"]').should(be.blank).type('ghjjsjslmsmfklefasc').press_enter()
    assert browser.element('html').should(have.text('результаты не найдены'))



