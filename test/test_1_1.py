# -*- coding: utf-8 -*-

# def test_detail_total(app):
#    app.open_home_page()
#    app.click_on_clear()
#    app.forms.select_analytical_forms()
#    app.forms.select_1_1()
#    app.filter.open_filter()
#    app.filter.filter_for_the_current_year()
#    app.filter.click_filter_ok()
#    app.details.detail_total()


# def test_detail_all(app):
#     app.open_home_page()
#     app.click_on_clear()
#     app.forms.select_analytical_forms()
#     app.forms.select_1_1()
#     app.filter.open_filter()
#     app.filter.filter_for_the_current_year()
#     app.filter.click_filter_ok()
#     app.details.detail_all()

def test_filter_counter(app):
    app.open_home_page()
    app.click_on_clear()
    app.forms.select_analytical_forms()
    app.forms.select_1_1()
    app.filter.open_filter()
    app.filter.filter_for_the_current_year()
    app.filter.click_filter_ok()
    app.remember_the_total_number()
    app.filter.open_filter()
    app.filter.remember_the_filter_counter_number()
    app.details.detail_all()
#