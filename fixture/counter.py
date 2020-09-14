import time

class CounterHelper:

    def __init__(self, app):
        self.app = app


    #только для форм, где всего отказов - 3й столбец, последняя строка
    #1.1-1.4, 1.12-1.16, 1.20-1.25, 1.27, 1.28, 2.1-2.7, 2.9, 2.10, 3.4, 3.5, 3.7-3.20
    def counter_coulm3_last_row(self, app):
        wd = self.app.wd
        app.filter.open_filter()
        app.filter.filter_for_1st_quarter()
        time.sleep(5)
        f_number_filter = wd.find_element_by_id("countData").text
        int_f_number_filter = int(f_number_filter)
        app.filter.click_filter_ok()
        row_count = len(wd.find_elements_by_xpath("//div[@id='contentScroll']//tbody[@id='dataBody']/tr"))
        total_number = wd.find_element_by_xpath("//tbody[@id='dataBody']/tr[%s]/td[3]" % row_count).text
        if total_number == '':
            total_number = 0
        int_total_number = int(total_number)
        app.filter.open_filter()
        s_number_filter = wd.find_element_by_id("countData").text
        int_s_number_filter = int(s_number_filter)
        if int_total_number == int_s_number_filter:
            if int_total_number == int_f_number_filter:
                print("Счётчик работает корректно")
            else:
                print("Ошибка в счётчике до кнопки 'ок' " + str(int_total_number) + " - " + str(int_f_number_filter))
        else:
            print("Ошибка в счётчике после кнопки 'ок' " + str(int_total_number) + " - " + str(int_s_number_filter))

    #только для форм, где всего отказов - 9й столбец, первая строка
    # 3.1, 3.2
    def counter_coulm9_first_row(self, app):
        wd = self.app.wd
        app.filter.open_filter()
        app.filter.filter_for_1st_quarter()
        time.sleep(5)
        app.filter.click_filter_ok()
        total_number = wd.find_element_by_xpath("//tbody[@id='dataBody']/tr[1]/td[9]").text
        if total_number == '':
            total_number = 0
        int_total_number = int(total_number)
        app.filter.open_filter()
        number_filter = wd.find_element_by_id("countData").text
        int_number_filter = int(number_filter)
        if int_total_number == int_number_filter:
            print("Счётчик работает корректно")
        else:
            print("Ошибка в счётчике " + str(int_total_number) + " - " + str(int_number_filter))

    #только для форм, где всего отказов - 3й столбец, первая строка
    # 3.3
    def counter_coulm3_first_row(self, app):
        wd = self.app.wd
        app.filter.open_filter()
        app.filter.filter_for_1st_quarter()
        time.sleep(5)
        app.filter.click_filter_ok()
        total_number = wd.find_element_by_xpath("//tbody[@id='dataBody']/tr[1]/td[3]").text
        if total_number == '':
            total_number = 0
        int_total_number = int(total_number)
        app.filter.open_filter()
        number_filter = wd.find_element_by_id("countData").text
        int_number_filter = int(number_filter)
        if int_total_number == int_number_filter:
            print("Счётчик работает корректно")
        else:
            print("Ошибка в счётчике " + str(int_total_number) + " - " + str(int_number_filter))



    # оперативная отчётность + 3.23
    def counter_operational_reports(self, app):
        wd = self.app.wd
        app.filter.open_filter()
        app.filter.filter_for_1st_quarter()
        time.sleep(5)
        f_number_filter = wd.find_element_by_id("countData").text
        int_f_number_filter = int(f_number_filter)
        app.filter.click_filter_ok()
        total_number = len(wd.find_elements_by_xpath("//div[@id='contentScroll']//tbody[@id='dataBody']/tr"))
        if total_number == '':
            total_number = 0
        int_total_number = int(total_number)
        app.filter.open_filter()
        s_number_filter = wd.find_element_by_id("countData").text
        int_s_number_filter = int(s_number_filter)
        if int_total_number == int_s_number_filter:
            if int_total_number == int_f_number_filter:
                print("Счётчик работает корректно")
            else:
                print("Ошибка в счётчике до кнопки 'ок' " + str(int_total_number) + " - " + str(int_f_number_filter))
        else:
            print("Ошибка в счётчике после кнопки 'ок' " + str(int_total_number) + " - " + str(int_s_number_filter))

    #только для форм, где всего отказов - 6й столбец, последняя строка
    #3.21, 3.22
    def counter_coulm6_last_row(self, app):
        wd = self.app.wd
        app.filter.open_filter()
        app.filter.filter_for_1st_quarter()
        time.sleep(5)
        f_number_filter = wd.find_element_by_id("countData").text
        int_f_number_filter = int(f_number_filter)
        app.filter.click_filter_ok()
        row_count = len(wd.find_elements_by_xpath("//div[@id='contentScroll']//tbody[@id='dataBody']/tr"))
        total_number = wd.find_element_by_xpath("//tbody[@id='dataBody']/tr[%s]/td[6]" % row_count).text
        if total_number == '':
            total_number = 0
        int_total_number = int(total_number)
        app.filter.open_filter()
        s_number_filter = wd.find_element_by_id("countData").text
        int_s_number_filter = int(s_number_filter)
        if int_total_number == int_s_number_filter:
            if int_total_number == int_f_number_filter:
                print("Счётчик работает корректно")
            else:
                print("Ошибка в счётчике до кнопки 'ок' " + str(int_total_number) + " - " + str(int_f_number_filter))
        else:
            print("Ошибка в счётчике после кнопки 'ок' " + str(int_total_number) + " - " + str(int_s_number_filter))