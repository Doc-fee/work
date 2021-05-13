def test_detail_total(app):
   app.open_home_page()
   app.click_starting_overlay()
   app.forms.select_analytical_forms()
   app.forms.select_1_28()
   app.filter.open_filter()
   app.filter.filter_for_the_current_year()
   app.filter.click_filter_ok()
   app.details.detail_total()

def test_detail_all(app):
    app.open_home_page()
    app.click_starting_overlay()
    app.forms.select_analytical_forms()
    app.forms.select_1_28()
    app.filter.open_filter()
    app.filter.filter_for_2019()
    app.filter.click_filter_ok()
    app.details.detail_all()

def test_filter_counter(app):
    app.open_home_page()
    app.click_starting_overlay()
    app.forms.select_analytical_forms()
    app.forms.select_1_28()
    app.counter.counter_coulm3_last_row(app)

def test_calculate_procent(app):  # другой способ, не как у всех.
    app.open_home_page()
    app.click_starting_overlay()
    app.forms.select_analytical_forms()
    app.forms.select_1_28()
    app.filter.open_filter()
    app.filter.filter_for_2020()
    app.filter.click_filter_ok()
    app.sum_table.calculate_procent_w_28()
