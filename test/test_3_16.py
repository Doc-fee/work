# def test_detail_total(app):
#    app.open_home_page()
#    app.click_on_clear()
#    app.forms.select_analytical_forms()
#    app.forms.select_3_16()
#    app.filter.open_filter()
#    app.filter.filter_for_the_current_year()
#    app.filter.click_filter_ok()
#    app.details.detail_total()

# def test_detail_all(app):
#     app.open_home_page()
#     app.click_on_clear()
#     app.forms.select_analytical_forms()
#     app.forms.select_3_16()
#     app.filter.open_filter()
#     app.filter.filter_for_2019()
#     app.filter.click_filter_ok()
#     app.details.detail_all()

# def test_filter_counter(app):
#     app.open_home_page()
#     app.click_on_clear()
#     app.forms.select_analytical_forms()
#     app.forms.select_3_16()
#     app.counter.counter_coulm3_last_row(app)

def test_with_2_1(app):
    app.open_home_page()
    app.click_starting_overlay()
    app.forms.select_analytical_forms()
    app.forms.select_3_16()
    app.filter.open_filter()
    app.filter.filter_for_2019()
    app.filter.filter_service_sh()
    app.filter.click_filter_ok()
    app.assert_forms.assert_2_1_3_16()