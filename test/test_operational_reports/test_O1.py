def test_filter_counter(app):
    app.open_home_page()
    app.click_starting_overlay()
    app.forms.select_operational_reports()
    app.forms.select_O1()
    app.counter.counter_operational_reports(app)