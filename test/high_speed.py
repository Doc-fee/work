# -*- coding: utf-8 -*-
from selenium.common.exceptions import NoSuchElementException
import pytest
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_high_speed(app):
    app.open_home_page()
    app.click_on_clear()
    app.forms.select_extra_forms()
    app.forms.select_high_speed()
    app.filter.open_filter()
    app.filter.filter_for_the_current_year()
    app.filter.click_filter_ok()







