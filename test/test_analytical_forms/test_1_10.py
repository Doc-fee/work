def test_percent(app):
    app.open_home_page()
    app.click_starting_overlay()
    app.forms.select_analytical_forms()
    app.forms.select_1_10()
    app.filter.open_filter()
    app.filter.filter_for_2020()
    app.filter.click_filter_ok()
    app.sum_table.calculate_procent()