# -*- coding: utf-8 -*-

def test_filter_counter(app):
    app.open_home_page()
    app.click_starting_overlay()
    app.forms.select_analytical_forms()
    app.forms.select_3_23()
    app.counter.counter_operational_reports(app)