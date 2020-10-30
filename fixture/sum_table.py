import time

class SumTableHelper:

    def __init__(self, app):
        self.app = app

    def sum_rows(self, i):
        wd = self.app.wd
        coulm_count = len(wd.find_elements_by_xpath("//div[@id='contentScroll']//tbody[@id='dataBody']/tr[1]/td"))
        rows = wd.find_elements_by_xpath("//div[@id='contentScroll']//tbody[@id='dataBody']/tr")
        for i in range(1, coulm_count):
            sum = 0
            if i != 1 and i % 3 != 0:
                for row in rows:
                    r = row.find_element_by_xpath("//td[%s]/a" %i).text
                    if r == '':
                        r = 0
                    int_r = int(r)
                    sum = sum + int_r
