# -*- coding: utf-8 -*-

def test_detail_all(app):
    app.open_home_page()
    app.click_on_clear()
    app.forms.select_analytical_forms()
    app.forms.select_3_3()
    app.filter.open_filter()
    app.filter.filter_for_2019()
    app.filter.click_filter_ok()
    app.details.detail_all()
