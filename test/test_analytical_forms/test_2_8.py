def test_sum_str(app):
    app.open_home_page()
    app.click_starting_overlay()
    app.forms.select_analytical_forms()
    app.forms.select_2_8()
    app.filter.open_filter()
    app.filter.filter_for_1st_quarter()
    app.filter.click_filter_ok()
    app.sum_table.sum_rows(app)
