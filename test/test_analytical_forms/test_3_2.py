# -*- coding: utf-8 -*-

def test_detail_all(app):
    app.open_home_page()
    app.click_starting_overlay()
    app.forms.select_analytical_forms()
    app.forms.select_3_2()
    app.filter.open_filter()
    app.filter.filter_for_2019()
    app.filter.click_filter_ok()
    app.details.detail_all()

def test_filter_counter(app):
    app.open_home_page()
    app.click_starting_overlay()
    app.forms.select_analytical_forms()
    app.forms.select_3_2()
    app.counter.counter_coulm9_first_row(app)

def test_with_2_1(app):
    app.open_home_page()
    app.click_starting_overlay()
    app.forms.select_analytical_forms()
    app.forms.select_3_2()
    app.filter.open_filter()
    app.filter.filter_for_2019()
    app.filter.filter_service_sh()
    app.filter.click_filter_ok()
    app.assert_forms.assert_2_1_3_2()


