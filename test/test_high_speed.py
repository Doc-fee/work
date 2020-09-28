# -*- coding: utf-8 -*-

def test_high_speed(app):
    app.open_home_page()
    app.click_starting_overlay()
    app.forms.select_extra_forms()
    app.forms.select_high_speed()
    app.filter.open_filter()
    app.filter.filter_for_the_current_year()
    app.filter.click_filter_ok()








