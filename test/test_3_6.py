# -*- coding: utf-8 -*-
import time

# def test_detail_all(app):
#     app.open_home_page()
#     app.click_on_clear()
#     app.forms.select_analytical_forms()
#     app.forms.select_3_6()
#     app.filter.open_filter()
#     app.filter.filter_for_2019()
#     app.filter.click_filter_ok()
#     app.details.detail_all()



def test_with_2_1(app):
    app.open_home_page()
    app.click_on_clear()
    app.forms.select_analytical_forms()
    app.forms.select_3_6()
    app.filter.open_filter()
    #    app.filter.filter_for_2019()
    app.filter.filter_for_January_1st()
    app.filter.filter_service_sh()
    app.filter.click_filter_ok()
    time.sleep(60)
    app.assert_forms.assert_2_1_3_6()




