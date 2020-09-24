import time


class DetailsHelper:

    def __init__(self, app):
        self.app = app

    def detail_total(self):
        wd = self.app.wd
        listTd = []
        list_common_table = []
        list_detail = []
        # нашла строку Итого
        tr = wd.find_element_by_xpath("//td[text()='Итого']/..")
        # получила список ячеек строки Итого
        listTd = tr.find_elements_by_xpath(".//td")
        # пробегаюсь по ячейкам
        index = 0
        for td in listTd:
            if index != 0 and index % 3 != 0:
                a = td.find_elements_by_tag_name("a")
                if len(a) > 0:
                    value = a[0].text
                    if value:
                        value = int(value)
                        list_common_table.append(value)
                        if value:
                            a[0].click()
                            time.sleep(20)
                            # считаю количество столбцов в таблице  (если столбце 1 - "Идёт загрузка данных")
                            error_detail = len(
                                wd.find_elements_by_xpath("//div[@data-type='detail']//tbody[@id='dataBody']/tr[1]/td"))
                            if error_detail == 1:
                                print(str(index) + ' Не загружает детализацию.')
                            else:
                                row_count = len(
                                    wd.find_elements_by_xpath("//div[@data-type='detail']//tbody[@id='dataBody']/tr"))
                                list_detail.append(row_count)
                                if value == row_count:
                                    print(str(index) + ' Корректная детализация')
                                else:
                                    print(str(index) + ' Ошибка детализации' + ' Значение в таблице: ' + str(
                                        value) + ' Значение в детализации: ' + str(row_count))
                            wd.find_element_by_xpath("//a[@data-view-name='form']").click()
                            time.sleep(2)
                    else:
                        print(str(index) + " Нет данных для проверки")
            index += 1

    def detail_all(self):
        wd = self.app.wd
        list_common_table = []
        list_detail = []
        list_row_common_table = []
        list_column_common_table = []
        list_row_common_table = wd.find_elements_by_xpath("//tbody[@id='dataBody']/tr")
        indextr = 0
        for trt in list_row_common_table:
            list_column_common_table = trt.find_elements_by_xpath(".//td")
            indextd = 0
            indextr += 1
            for td in list_column_common_table:
                if indextd != 0 and indextd % 3 != 0:
                    a = td.find_elements_by_tag_name("a")
                    if len(a) > 0:
                        value = 0
                        value = a[0].text
                        if value:
                            value = int(value)
                            list_common_table.append(value)
                            if value:
                                a[0].click()
                                time.sleep(20)
                                # считаю количество столбцов в таблице  (если столбце 1 - "Идёт загрузка данных")
                                error_detail = len(wd.find_elements_by_xpath(
                                    "//div[@data-type='detail']//tbody[@id='dataBody']/tr[1]/td"))
                                if error_detail == 1:
                                    print('Строка: ' + str(indextr) + ' Столбец: ' + str(
                                        indextd) + ' Не загружает детализацию.')
                                else:
                                    row_count = 0
                                    row_count = len(wd.find_elements_by_xpath(
                                        "//div[@data-type='detail']//tbody[@id='dataBody']/tr"))
                                    list_detail.append(row_count)
                                    if value == row_count:
                                        print('Строка: ' + str(indextr) + ' Столбец: ' + str(
                                            indextd) + ' Корректная детализация')
                                    else:
                                        print('Строка: ' + str(indextr) + ' Столбец: ' + str(
                                            indextd) + ' Ошибка детализации' + ' Значение в таблице: ' + str(
                                            value) + ' Значение в детализации: ' + str(row_count))
                                wd.find_element_by_xpath("//a[@data-view-name='form']").click()
                                time.sleep(2)
                        else:
                            print('Строка: ' + str(indextr) + ' Столбец: ' + str(indextd) + " Нет данных для проверки")
                    else:
                        print('Строка: '+ str(indextr) + ' Столбец: '+ str(indextd) + " Нет данных для проверки")
                indextd += 1
    def detail_total_for_1_11(self):
        wd = self.app.wd
        listTd = []
        list_common_table = []
        list_detail = []
        # нашла строку Итого
        tr = wd.find_element_by_xpath("//td[text()='Итого']/..")
        # получила список ячеек строки Итого
        listTd = tr.find_elements_by_xpath(".//td")
        # пробегаюсь по ячейкам
        index = 0
        for td in listTd:
            if index != 0 and index % 3 != 0:
                a = td.find_elements_by_tag_name("a")
                if len(a) > 0:
                    value = a[0].text
                    if value:
                        value = int(value)
                        list_common_table.append(value)
                        if value:
                            a[0].click()
                            time.sleep(20)
                            # считаю количество столбцов в таблице  (если столбце 1 - "Идёт загрузка данных")
                            error_detail = len(
                                wd.find_elements_by_xpath("//div[@data-type='detail']//tbody[@id='dataBody']/tr[1]/td"))
                            if error_detail == 1:
                                print(str(index) + ' Не загружает детализацию.')
                            else:
                                row_count = len(
                                    wd.find_elements_by_xpath("//div[@data-type='detail']//tbody[@id='dataBody']/tr"))
                                list_detail.append(row_count)
                                if value == row_count:
                                    print(str(index) + ' Корректная детализация')
                                else:
                                    print(str(index) + ' Ошибка детализации' + ' Значение в таблице: ' + str(
                                        value) + ' Значение в детализации: ' + str(row_count))
                            wd.find_element_by_xpath("//a[@data-view-name='form']").click()
                            time.sleep(2)
                    else:
                        print(str(index) + " Нет данных для проверки")

            index += 1
        assert list_detail == list_common_table
