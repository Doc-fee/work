def test_filter_counter(app):
    app.open_home_page()
    app.click_starting_overlay()
    app.forms.select_extra_forms()
    app.forms.select_high_speed_trains()
    app.counter.counter_coulm3_first_row(app)