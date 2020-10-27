def test_filter_counter(app):
    app.open_home_page()
    app.click_starting_overlay()
    app.forms.select_extra_forms()
    app.forms.select_unfilled_waivers()
    app.counter.counter_coulm2_last_row(app)