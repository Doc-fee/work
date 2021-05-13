import datetime
from selenium.common.exceptions import NoSuchElementException

# что это??
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
        f = open('C:\\Users\\cherepanova\\Desktop\\Jresults\\sum_rows.txt', 'a')
        f.write("\n" + str(d) + "\n" + "Тестирование сравнения Итого со строками " + str(name_form) + "\n")
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
                        r = row.find_element_by_xpath(".//td[%s]" % i).text
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
                if condition_errow != 0:
                    f.write(' Столбец: ' + str(i) + ' Итого: ' + str(int_r) + ' Строки: ' + str(sum) + ' - Ошибка!' + "\n")
                else:
                    f.write(' Столбец: ' + str(i) + ' Итого: ' + str(int_r) + ' Строки: ' + str(sum) + "\n")
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
                        count_l = column.text
                        if count_l =='':
                            count_l=0
                    except NoSuchElementException:
                        count_l = 0
                        sum_last += 0
                    int_count_l = int(count_l)
                    total.append(int_count_l)
                elif indexColumn == 3:
                    nextColumn_с = 6
                    try:
                        count_c = column.text
                        if count_c =='':
                            count_c=0
                    except NoSuchElementException:
                        count_c = 0
                    sum_current += 0
                    int_count_c = int(count_c)
                    total.append(int_count_c)
                elif indexColumn == nextColumn_l:
                    nextColumn_l += 3
                    try:
                        a = column.text
                        if a =='':
                            a=0
                        sum_last += int(a)
                    except NoSuchElementException:
                        sum_last += 0

                elif indexColumn == nextColumn_с:
                    nextColumn_с += 3
                    try:
                        a = column.text
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
#        assert sum_columns == total


    def calculate_procent(self):
        wd = self.app.wd
        d = datetime.datetime.today()
        name_form = wd.find_element_by_xpath("//div[@id='breadNavBar']").text
        f_name_form = str(name_form)
        f_d = str(d)
        f = open('C:\\Users\\cherepanova\\Desktop\\Jresults\\percent.txt', 'a')
        f.write("\n" + f_d + "\n" + "Тестирование процентов " + f_name_form + "\n")
        list_row_common_table = wd.find_elements_by_xpath("//tbody[@id='dataBody']/tr")
        indextr = 0
        list_procent = []
        list_rr = []
        l = 0 # Сашка Дурашка
        c = 0
        p = 0
        rr = 0
        counter = 0
        nextColumn_l = 0
        nextColumn_c = 0
        for trt in list_row_common_table:
            list_column_common_table = trt.find_elements_by_xpath(".//td")
            indextd = 0
            indextr += 1
            name_str = wd.find_element_by_xpath("//tbody[@id='dataBody']/tr[%s]/td[1]" %indextr).text
            for td in list_column_common_table:
                if indextd != 0:
                    if indextd %3 !=0:
                        if indextd == 1:
                            nextColumn_l = 4
                            try:
                                lf = td.text
                                if lf == '':
                                    lf = 0
                                l = float(lf)
                            except NoSuchElementException:
                                l = 0
                        elif indextd == 2:
                            nextColumn_c = 5
                            try:
                                cf = td.text
                                if cf == '':
                                    cf =0
                                c = float(cf)
                            except NoSuchElementException:
                                c = 0
                        elif indextd == nextColumn_l:
                            nextColumn_l += 3
                            try:
                                lf = td.text
                                if lf == '':
                                    lf = 0
                                l = float(lf)
                            except NoSuchElementException:
                                l = 0
                        elif indextd == nextColumn_c:
                            nextColumn_c += 3
                            try:
                                cf = td.text
                                if cf == '':
                                    cf = 0
                                c = float(cf)
                            except NoSuchElementException:
                                c = 0
                    else:
                        p = float(td.text)
                        list_procent.append(p)
                    counter += 1
                    if counter == 3:
                        counter = 0
                        if l == 0 and c == 0:
                            rr = 0
                        elif l == 0 and c != 0:
                            rr = 100.00
                        else:
                            rr = round((((c - l) / l) * 100), 1)
                        list_rr.append(rr)
                        if rr == p:
                            f.write(
                                'Строка: ' + str(name_str) + '(' + str(indextr) + ')' + ' Столбец: ' + str(indextd) +
                                ' в таблице:' + str(p) + ' результат:'+ str(rr)+ ' Победил Санёк!\n')
                        else: f.write('Строка: ' + str(name_str) +'(' + str(indextr) +')' + ' Столбец: ' + str(indextd)
                                      +' в таблице:' + str(p) + ' результат ММ:'+ str(rr)+
                                      ' Победила форма!\n')
                indextd += 1
        f.close()
        print(list_procent, list_rr)

    def calculate_procent_w_28(self):
        wd = self.app.wd
        d = datetime.datetime.today()
        name_form = wd.find_element_by_xpath("//div[@id='breadNavBar']").text
        f_name_form = str(name_form)
        f_d = str(d)
        f = open('C:\\Users\\cherepanova\\Desktop\\Jresults\\percent.txt', 'a')
        f.write("\n" + f_d + "\n" + "Тестирование процентов " + f_name_form + "\n")
        list_row_common_table = wd.find_elements_by_xpath("//tbody[@id='dataBody']/tr")
        indextr = 0
        list_procent = []
        list_rr = []
        l = 0  # Сашка Дурашка
        c = 0
        p = 0
        rr = 0
        counter = 0
        nextColumn_l = 0
        nextColumn_c = 0
        for trt in list_row_common_table:
            list_column_common_table = trt.find_elements_by_xpath(".//td")
            indextd = 0
            indextr += 1
            name_str = wd.find_element_by_xpath("//tbody[@id='dataBody']/tr[%s]/td[1]" % indextr).text
            for td in list_column_common_table:
                if indextd != 0:
                    if f_name_form != 'Форма 1.28':
                        if indextd % 3 != 0:
                            if indextd == 1:
                                nextColumn_l = 4
                                try:
                                    lf = td.text
                                    if lf == '':
                                        lf = 0
                                    l = float(lf)
                                except NoSuchElementException:
                                    l = 0
                            elif indextd == 2:
                                nextColumn_c = 5
                                try:
                                    cf = td.text
                                    if cf == '':
                                        cf = 0
                                    c = float(cf)
                                except NoSuchElementException:
                                    c = 0
                            if indextd == nextColumn_l:
                                nextColumn_l += 3
                                try:
                                    lf = td.text
                                    if lf == '':
                                        lf = 0
                                    l = float(lf)
                                except NoSuchElementException:
                                    l = 0
                            if indextd == nextColumn_c:
                                nextColumn_c += 3
                                try:
                                    cf = td.text
                                    if cf == '':
                                        cf = 0
                                    c = float(cf)
                                except NoSuchElementException:
                                    c = 0
                        else:
                            p = float(td.text)
                            list_procent.append(p)
                        counter += 1
                        if counter == 3:
                            counter = 0
                            if l == 0 and c == 0:
                                rr = 0
                            elif l == 0 and c != 0:
                                rr = 100.00
                            else:
                                rr = round((((c - l) / l) * 100), 1)
                            list_rr.append(rr)
                            if rr == p:
                                f.write(
                                    'Строка: ' + str(name_str) + '(' + str(indextr) + ')' + ' Столбец: ' + str(
                                        indextd) +
                                    ' в таблице:' + str(p) + ' результат:' + str(rr) + ' Победил Санёк!\n')
                            else:
                                f.write(
                                    'Строка: ' + str(name_str) + '(' + str(indextr) + ')' + ' Столбец: ' + str(indextd)
                                    + ' в таблице:' + str(p) + ' результат ММ:' + str(rr) +
                                    ' Победила форма!\n')
                    else:
                        if indextd == 1:
                            nextColumn_l = 5
                            try:
                                lf = td.text # все объекты
                                if lf == '':
                                    lf = 0
                                l = float(lf)
                            except NoSuchElementException:
                                l = 0
                        elif indextd == 3:
                            nextColumn_c = 7
                            try:
                                cf = td.text # объекты с отказами
                                if cf == '':
                                    cf = 0
                                c = float(cf)
                            except NoSuchElementException:
                                c = 0
                        elif indextd == 4 or indextd ==8 or indextd == 22:
                            p = float(td.text)
                            list_procent.append(p)
                        elif indextd == nextColumn_l:
                            nextColumn_l = 19
                            try:
                                lf = td.text
                                if lf == '':
                                    lf = 0
                                l = float(lf)
                            except NoSuchElementException:
                                l = 0
                        elif indextd == nextColumn_c:
                            nextColumn_c = 21
                            try:
                                cf = td.text
                                if cf == '':
                                    cf = 0
                                c = float(cf)
                            except NoSuchElementException:
                                c = 0
                    counter += 1
                    if counter == 4 or counter == 8 or counter == 22:
                        if l == 0 and c == 0:
                            rr = 0
                        elif l == 0 and c != 0:
                            rr = 100.00
                        else:
                            rr = round(((c / l) * 100), 1)
                        list_rr.append(rr)
                        if rr == p:
                            f.write(
                                'Строка: ' + str(name_str) + '(' + str(indextr) + ')' + ' Столбец: ' + str(
                                    indextd) +
                                ' в таблице:' + str(p) + ' результат:' + str(rr) + ' Победил Санёк!\n')
                        else:
                            f.write(
                                'Строка: ' + str(name_str) + '(' + str(indextr) + ')' + ' Столбец: ' + str(indextd)
                                + ' в таблице:' + str(p) + ' результат ММ:' + str(rr) +
                                ' Победила форма!\n')


                indextd += 1
        f.close()
        print(list_procent, list_rr)
