
def test_detail_total(app):
    app.open_home_page()
    app.click_starting_overlay()
    app.forms.select_analytical_forms()
    app.forms.select_2_9()
    app.filter.open_filter()
    app.filter.filter_for_the_current_year()
    app.filter.click_filter_ok()
    app.details.detail_total()

def test_detail_all(app):
    app.open_home_page()
    app.click_starting_overlay()
    app.forms.select_analytical_forms()
    app.forms.select_2_9()
    app.filter.open_filter()
    app.filter.filter_for_the_current_year()
    app.filter.click_filter_ok()
    app.details.detail_all()

def test_filter_counter(app):
    app.open_home_page()
    app.click_starting_overlay()
    app.forms.select_analytical_forms()
    app.forms.select_2_9()
    app.counter.counter_coulm3_last_row(app)

def test_sum_str(app):
    app.open_home_page()
    app.click_starting_overlay()
    app.forms.select_analytical_forms()
    app.forms.select_2_9()
    app.filter.open_filter()
    app.filter.filter_for_1st_quarter()
    app.filter.click_filter_ok()
    app.sum_table.sum_rows(app)

def test_sum_columns(app):
    app.open_home_page()
    app.click_starting_overlay()
    app.forms.select_analytical_forms()
    app.forms.select_2_9()
    app.filter.open_filter()
    app.filter.filter_for_1st_quarter()
    app.filter.click_filter_ok()
    app.sum_table.sum_columns(app)

def test_percent(app):
    app.open_home_page()
    app.click_starting_overlay()
    app.forms.select_analytical_forms()
    app.forms.select_2_9()
    app.filter.open_filter()
    app.filter.filter_for_1st_quarter()
    app.filter.click_filter_ok()
    app.sum_table.calculate_procent()
