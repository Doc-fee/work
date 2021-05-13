def test_filter_counter(app):
    app.open_home_page()
    app.click_starting_overlay()
    app.forms.select_extra_forms()
    app.forms.select_duration_2_1()
    app.counter.counter_coulm3_last_row(app)

def test_percent(app):
    app.open_home_page()
    app.click_starting_overlay()
    app.forms.select_extra_forms()
    app.forms.select_duration_2_1()
    app.filter.open_filter()
    app.filter.filter_for_1st_quarter()
    app.filter.click_filter_ok()
    app.sum_table.calculate_procent()