import datetime
from selenium.common.exceptions import NoSuchElementException


class TimeUnit(object):
    pass


class SumTableHelper:

    def __init__(self, app):
        self.app = app

# метод для тестирования строки Итого некотрых форм
# для 1.1-1.4, 1.11-1.25, 1.27, 1.30, 2.*, 3.4, 3.11, 3.12, 3.14-3.22
    def sum_rows(self, i):
        wd = self.app.wd
        d = datetime.datetime.today()
        name_form = wd.find_element_by_xpath("//div[@id='breadNavBar']").text
        f_name_form = str(name_form)
        f_d = str(d)
        f = open('C:\\Users\\cherepanova\\Desktop\\Jresults\\sum_rows.txt', 'a')
        f.write("\n" + f_d + "\n" + "Тестирование сравнения Итого со строками " + f_name_form + "\n")
        sum_rows = []
        total = []
        column_count = len(wd.find_elements_by_xpath("//div[@id='contentScroll']//tbody[@id='dataBody']/tr[1]/td"))
        rows = wd.find_elements_by_xpath("//div[@id='contentScroll']//tbody[@id='dataBody']/tr")
        for i in range(1, column_count):
            sum = 0
            if i != 1 and i % 3 != 1:
                for row in rows:
                    name_str = row.find_element_by_xpath(".//td[1]").text
                    try: # пытаюсь найти ссылки
                        t = row.find_element_by_xpath(".//td[%s]//a" %i)
                        r = t.text
                        if r == '': # в итого, если нет числа, всё равно есть ссылки
                            r = 0
                    except NoSuchElementException: # если не нахожу ссылки, ставит 0
                        r = 0
                    int_r = int(r)
                    sum = sum + int_r
                total.append(int_r)
                #сумма с вычетом Итого
                sum = sum - int_r
                sum_rows.append(sum)
                condition_errow = sum-int_r
                f_numcolumn = str(i)
                f_total = str(int_r)
                f_sum = str(sum)
                if condition_errow !=0:
                    f.write(' Столбец: ' + f_numcolumn + ' Итого: ' + f_total + ' Строки: ' + f_sum + ' - Ошибка!' + "\n")
                else:
                    f.write(' Столбец: ' + f_numcolumn + ' Итого: ' + f_total + ' Строки: ' + f_sum + "\n")
        f.close()
#        assert sum_rows == total

    def sum_columns(self, i):
        wd = self.app.wd
        d = datetime.datetime.today()
        name_form = wd.find_element_by_xpath("//div[@id='breadNavBar']").text
        f_name_form = str(name_form)
        f_d = str(d)
        f = open('C:\\Users\\cherepanova\\Desktop\\Jresults\\sum_columns.txt', 'a')
        f.write("\n" + f_d + "\n" + "Тестирование сравнения Всего со столбцами " + f_name_form + "\n")
        sum_columns = []
        total = []
        rows = wd.find_elements_by_xpath("//div[@id='contentScroll']//tbody[@id='dataBody']/tr")
        for row in rows:
            name_str = row.find_element_by_xpath(".//td[1]").text
            count = 0
            sum_last = 0
            sum_current = 0
            columns = row.find_elements_by_xpath(".//td")
            indexColumn = 1
            for column in columns:
                if indexColumn == 2:
                    nextColumn_l = 5
                    try:
                        count = column.find_element_by_xpath(".//a").text
                        if indexColumn == nextColumn:
                            nextColumn += 3
                            try:
                                a = column.find_element_by_xpath(".//a")
                                sum_last += int(a.text)
                            except NoSuchElementException:
                                sum_last += 0
                    except NoSuchElementException:
                        count = 0
                        sum_last += 0
                elif indexColumn == 3:
                    nextColumn = 6
                    try:
                        count = column.find_element_by_xpath(".//a").text
                        if indexColumn == nextColumn:
                            nextColumn += 3
                            try:
                                a = column.find_element_by_xpath(".//a")
                                sum_current += int(a.text)
                            except NoSuchElementException:
                                sum_current += 0
                    except NoSuchElementException:
                        count = 0
                        sum_current += 0
                indexColumn += 1
            f_sum_l = str(sum_last)
            f_sum_c = str(sum_current)
            f_count = str(count)
            if count == sum:
                f.write(' Строка: ' + name_str + ' Всего: ' + f_count + ' Столбцы: ' + f_sum + "\n")
            else:
                f.write(' Строка: ' + name_str + ' Всего: ' + f_count + ' Стлбцы: ' + f_sum + "\n" + ' - Ошибка!')
        f.close()