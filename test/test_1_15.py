# -*- coding: utf-8 -*-

#def test_1_12(app):
#    app.open_home_page()
#    app.click_on_clear()
#    app.forms.select_analytical_forms()
#    app.forms.select_1_12()
#    app.filter.open_filter()
#    app.filter.filter_for_the_current_year()
#    app.filter.click_filter_ok()
#    app.details.detail_total()


def test_detail_all(app):
    app.open_home_page()
    app.click_on_clear()
    app.forms.select_analytical_forms()
    app.forms.select_1_15()
    app.filter.open_filter()
    app.filter.filter_for_the_current_year()
    app.filter.click_filter_ok()
    app.details.detail_all()