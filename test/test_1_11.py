# -*- coding: utf-8 -*-

def test_1_11(app):
    app.open_home_page()
    app.click_on_clear()
    app.forms.select_analytical_forms()
    app.forms.select_1_11()
    app.filter.open_filter()
    app.filter.filter_for_the_current_year()
    app.filter.click_filter_ok()