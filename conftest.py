from fixture.application import Application
import pytest

@pytest.fixture(scope='session')
def app(request):
    browser = request.config.getoption('--browser')
    base_url = request.config.getoption('--baseUrl')
    fixture = Application(browser=browser, base_url=base_url)
    request.addfinalizer(fixture.destroy)
    return fixture

def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='firefox')
    parser.addoption('--baseUrl', action='store', default='http://onil-iis/onil.web.uo/')

# @pytest.fixture(scope='session')
# def app(request):
#     fixture = Application()
#     request.addfinalizer(fixture.destroy)
#     return fixture