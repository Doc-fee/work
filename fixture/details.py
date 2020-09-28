import time
import datetime


class DetailsHelper:

    def __init__(self, app):
        self.app = app

    def detail_total(self):
        wd = self.app.wd
        d = datetime.date.today()
        name_form = wd.find_element_by_xpath("//div[@id='breadNavBar']").text
        f_name_form = str(name_form)
        f_d = str(d)
        f = open('C:\\Users\\cherepanova\\Desktop\\Jresults\\detail_total.txt', 'a')
        f.write("\n")
        f.write(f_d)
        f.write("\n")
        f.write("Тестирование детализации Итого ")
        f.write(f_name_form)
        f.write("\n")
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
                                f_index = str(index)
                                f.write(f_index)
                                f.write(' Не загружает детализацию.\n')
                            else:
                                row_count = len(
                                    wd.find_elements_by_xpath("//div[@data-type='detail']//tbody[@id='dataBody']/tr"))
                                list_detail.append(row_count)
                                if value == row_count:
                                    print(str(index) + ' Корректная детализация')
                                    f_index = str(index)
                                    f.write(f_index)
                                    f.write(' Корректная детализация\n')
                                else:
                                    print(str(index) + ' Ошибка детализации' + ' Значение в таблице: ' + str(
                                        value) + ' Значение в детализации: ' + str(row_count))
                                    f_index = str(index)
                                    f_value = str(value)
                                    f_row_count = str(row_count)
                                    f.write(f_index)
                                    f.write(' Ошибка детализации')
                                    f.write(' Значение в таблице: ')
                                    f.write(f_value)
                                    f.write(' Значение в таблице: ')
                                    f.write(f_row_count)
                                    f.write("\n")
                            wd.find_element_by_xpath("//a[@data-view-name='form']").click()
                            time.sleep(2)
                    else:
                        print(str(index) + " Нет данных для проверки")
                        f_index = str(index)
                        f.write(f_index)
                        f.write(' Нет данных для проверки\n')
            index += 1
        f.close()

    def detail_all(self):
        wd = self.app.wd
        d = datetime.date.today()
        name_form = wd.find_element_by_xpath("//div[@id='breadNavBar']").text
        f_name_form = str(name_form)
        f_d = str(d)
        f = open('C:\\Users\\cherepanova\\Desktop\\Jresults\\detail_all.txt', 'a')
        f.write("\n")
        f.write(f_d)
        f.write("\n")
        f.write("Тестирование детализации всех ячеек ")
        f.write(f_name_form)
        f.write("\n")
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
                                    f_indextr=str(indextr)
                                    f_indextd = str(indextd)
                                    f.write('Строка: ')
                                    f.write(f_indextr)
                                    f.write('Столбец: ')
                                    f.write(f_indextd)
                                    f.write(' Не загружает детализацию.\n')
                                else:
                                    row_count = 0
                                    row_count = len(wd.find_elements_by_xpath(
                                        "//div[@data-type='detail']//tbody[@id='dataBody']/tr"))
                                    list_detail.append(row_count)
                                    if value == row_count:
                                        print('Строка: ' + str(indextr) + ' Столбец: ' + str(
                                            indextd) + ' Корректная детализация')
                                        f_indextr = str(indextr)
                                        f_indextd = str(indextd)
                                        f.write('Строка: ')
                                        f.write(f_indextr)
                                        f.write('Столбец: ')
                                        f.write(f_indextd)
                                        f.write(' Корректная детализация\n')
                                    else:
                                        print('Строка: ' + str(indextr) + ' Столбец: ' + str(
                                            indextd) + ' Ошибка детализации' + ' Значение в таблице: ' + str(
                                            value) + ' Значение в детализации: ' + str(row_count))
                                        f_indextr = str(indextr)
                                        f_indextd = str(indextd)
                                        f_value = str(value)
                                        f_row_count = str(row_count)
                                        f.write('Строка: ')
                                        f.write(f_indextr)
                                        f.write('Столбец: ')
                                        f.write(f_indextd)
                                        f.write(' Ошибка детализации')
                                        f.write(' Значение в таблице: ')
                                        f.write(f_value)
                                        f.write(' Значение в таблице: ')
                                        f.write(f_row_count)
                                        f.write("\n")

                                wd.find_element_by_xpath("//a[@data-view-name='form']").click()
                                time.sleep(2)
                        else:
                            print('Строка: ' + str(indextr) + ' Столбец: ' + str(indextd) + " Нет данных для проверки")
                            f_indextr = str(indextr)
                            f_indextd = str(indextd)
                            f.write('Строка: ')
                            f.write(f_indextr)
                            f.write('Столбец: ')
                            f.write(f_indextd)
                            f.write(' Нет данных для проверки\n')
                    else:
                        print('Строка: ' + str(indextr) + ' Столбец: ' + str(indextd) + " Нет данных для проверки")
                        f_indextr = str(indextr)
                        f_indextd = str(indextd)
                        f.write('Строка: ')
                        f.write(f_indextr)
                        f.write('Столбец: ')
                        f.write(f_indextd)
                        f.write(' Нет данных для проверки\n')
                indextd += 1
        f.close()