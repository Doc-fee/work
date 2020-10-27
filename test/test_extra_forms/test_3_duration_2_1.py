def test_filter_counter(app):
    app.open_home_page()
    app.click_starting_overlay()
    app.forms.select_extra_forms()
    app.forms.select_duration_2_1()
    app.counter.counter_coulm3_last_row(app)