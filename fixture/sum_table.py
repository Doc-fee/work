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
                int_r = 0
                for row in rows:
                    name_str = row.find_element_by_xpath(".//td[1]").text
                    # пытаюсь найти ссылки
                    try:
                        t = row.find_element_by_xpath(".//td[%s]//a" % i)
                        r = t.text
                        # в итого, если нет числа, всё равно есть ссылки
                        if r == '':
                            r = 0
                    # если не нахожу ссылки, ставит 0
                    except NoSuchElementException:
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
                if condition_errow != 0:
                    f.write(' Столбец: ' + f_numcolumn + ' Итого: ' + f_total + ' Строки: ' + f_sum + ' - Ошибка!' + "\n")
                else:
                    f.write(' Столбец: ' + f_numcolumn + ' Итого: ' + f_total + ' Строки: ' + f_sum + "\n")
        f.close()
#        assert sum_rows == total

    # метод для тестирования столбца Всего некотрых форм
    # для 1.1-1.4, 1.12-1.16, 1.27, 2.1-2.3, 2.9-2.10 3.4-3.5, 3.7-3.10, 3.12-3.16, 3.18-3.20
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
            count_l = 0
            count_c = 0
            sum_last = 0
            sum_current = 0
            columns = row.find_elements_by_xpath(".//td")
            indexColumn = 1
            nextColumn_l = 0
            nextColumn_с = 0
            for column in columns:
                if indexColumn == 2:
                    nextColumn_l = 5
                    try:
                        count_l = column.find_element_by_xpath(".//a").text

                    except NoSuchElementException:
                        count_l = 0
                        sum_last += 0
                    int_count_l = int(count_l)
                    total.append(int_count_l)
                elif indexColumn == 3:
                    nextColumn_с = 6
                    try:
                        count_c = column.find_element_by_xpath(".//a").text
                    except NoSuchElementException:
                        count_c = 0
                    sum_current += 0
                    int_count_c = int(count_c)
                    total.append(int_count_c)
                if indexColumn == nextColumn_l:
                    nextColumn_l += 3
                    try:
                        a = column.find_element_by_xpath(".//a").text
                        if a =='':
                            a=0
                        sum_last += int(a)
                    except NoSuchElementException:
                        sum_last += 0

                if indexColumn == nextColumn_с:
                    nextColumn_с += 3
                    try:
                        a = column.find_element_by_xpath(".//a").text
                        if a == '':
                            a=0
                        sum_current += int(a)
                    except NoSuchElementException:
                        sum_current += 0
                indexColumn += 1
            sum_columns.append(sum_last)
            sum_columns.append(sum_current)
            int_sum_current = int(sum_current)
            int_sum_last = int(sum_last)
            f_sum_l = str(sum_last)
            f_sum_c = str(sum_current)
            f_count_l = str(count_l)
            f_count_c = str(count_c)

            if int_count_l == int_sum_last:
                 f.write('Прошлый год Строка: ' + name_str + ' Всего: ' + f_count_l + ' Столбцы: ' + f_sum_l + "\n")
            else:
                 f.write('Прошлый год Строка: ' + name_str + ' Всего: ' + f_count_l + ' Стлбцы: ' + f_sum_l + ' - Ошибка!' + "\n")
            if int_count_c == int_sum_current:
                 f.write('Текущий год Строка: ' + name_str + ' Всего: ' + f_count_c + ' Столбцы: ' + f_sum_c + "\n")
            else:
                 f.write('Текущий год Строка: ' + name_str + ' Всего: ' + f_count_c + ' Стлбцы: ' + f_sum_c +  ' - Ошибка!' + "\n")

        f.close()
        assert sum_columns == total