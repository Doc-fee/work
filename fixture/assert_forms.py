import time

class AssertFormsHelper:

    def __init__(self, app):
        self.app = app

    def assert_2_1_3_1(self):
        wd = self.app.wd
        value3_1 = wd.find_element_by_xpath("//tbody[@id='dataBody']/tr[1]/td[18]").text
        int_value3_1 = int(value3_1)
        wd.find_element_by_xpath("//span[text()='2.1 Отказы по типам устройств']").click()
        time.sleep(300)
        value2_1 = wd.find_element_by_xpath("//tbody[@id='dataBody']/tr[25]/td[9]").text
        int_value2_1 = int(value2_1)
        assert int_value2_1 == int_value3_1

    def assert_2_1_3_2(self):
        wd = self.app.wd
        value3_2 = wd.find_element_by_xpath("//tbody[@id='dataBody']/tr[1]/td[18]").text
        int_value3_2 = int(value3_2)
        wd.find_element_by_xpath("//span[text()='2.1 Отказы по типам устройств']").click()
        time.sleep(300)
        value2_1 = wd.find_element_by_xpath("//tbody[@id='dataBody']/tr[25]/td[9]").text
        int_value2_1 = int(value2_1)
        assert int_value2_1 == int_value3_2

    def assert_2_1_3_4(self):
        wd = self.app.wd
        value3_4 = wd.find_element_by_xpath("//tbody[@id='dataBody']/tr[25]/td[3]").text
        int_value3_4 = int(value3_4)
        wd.find_element_by_xpath("//span[text()='2.1 Отказы по типам устройств']").click()
        time.sleep(300)
        value2_1 = wd.find_element_by_xpath("//tbody[@id='dataBody']/tr[25]/td[9]").text
        int_value2_1 = int(value2_1)
        assert int_value2_1 == int_value3_4

    def assert_2_1_3_5(self):
        wd = self.app.wd
        value3_5 = wd.find_element_by_xpath("//tbody[@id='dataBody']/tr[11]/td[3]").text
        int_value3_5 = int(value3_5)
        wd.find_element_by_xpath("//span[text()='2.1 Отказы по типам устройств']").click()
        time.sleep(300)
        value2_1 = wd.find_element_by_xpath("//tbody[@id='dataBody']/tr[25]/td[21]").text
        int_value2_1 = int(value2_1)
        assert int_value2_1 == int_value3_5

    def assert_2_1_3_7(self):
        wd = self.app.wd
        value3_7 = wd.find_element_by_xpath("//tbody[@id='dataBody']/tr[17]/td[3]").text
        int_value3_7 = int(value3_7)
        wd.find_element_by_xpath("//span[text()='2.1 Отказы по типам устройств']").click()
        time.sleep(300)
        value2_1 = wd.find_element_by_xpath("//tbody[@id='dataBody']/tr[25]/td[12]").text
        int_value2_1 = int(value2_1)
        assert int_value2_1 == int_value3_7

    def assert_2_1_3_8(self):
        wd = self.app.wd
        value3_8 = wd.find_element_by_xpath("//tbody[@id='dataBody']/tr[32]/td[3]").text
        int_value3_8 = int(value3_8)
        wd.find_element_by_xpath("//span[text()='2.1 Отказы по типам устройств']").click()
        time.sleep(300)
        value2_1 = wd.find_element_by_xpath("//tbody[@id='dataBody']/tr[25]/td[15]").text
        int_value2_1 = int(value2_1)
        assert int_value2_1 == int_value3_8

    def assert_2_1_3_9(self):
        wd = self.app.wd
        value3_9 = wd.find_element_by_xpath("//tbody[@id='dataBody']/tr[16]/td[3]").text
        int_value3_9 = int(value3_9)
        wd.find_element_by_xpath("//span[text()='2.1 Отказы по типам устройств']").click()
        time.sleep(300)
        value2_1 = wd.find_element_by_xpath("//tbody[@id='dataBody']/tr[25]/td[24]").text
        int_value2_1 = int(value2_1)
        assert int_value2_1 == int_value3_9

    def assert_2_1_3_10(self):
        wd = self.app.wd
        value3_9 = wd.find_element_by_xpath("//tbody[@id='dataBody']/tr[12]/td[3]").text
        int_value3_9 = int(value3_9)
        wd.find_element_by_xpath("//span[text()='2.1 Отказы по типам устройств']").click()
        time.sleep(300)
        value2_1 = wd.find_element_by_xpath("//tbody[@id='dataBody']/tr[25]/td[30]").text
        int_value2_1 = int(value2_1)
        assert int_value2_1 == int_value3_9


    # def assert_2_1_3_11(self):
    #     wd = self.app.wd
    #     value3_11 = wd.find_element_by_xpath("//tbody[@id='dataBody']/tr[10]/td[3]").text
    #     int_value3_11 = int(value3_11)
    #     wd.find_element_by_xpath("//span[text()='2.1 Отказы по типам устройств']").click()
    #     time.sleep(300)
    #     value2_1 = wd.find_element_by_xpath("//tbody[@id='dataBody']/tr[25]/td[15]").text
    #     int_value2_1 = int(value2_1)
    #     assert int_value2_1 == int_value3_11

    def assert_2_1_3_13(self):
        wd = self.app.wd
        value3_13 = wd.find_element_by_xpath("//tbody[@id='dataBody']/tr[9]/td[3]").text
        int_value3_13 = int(value3_13)
        wd.find_element_by_xpath("//span[text()='2.1 Отказы по типам устройств']").click()
        time.sleep(300)
        value2_1 = wd.find_element_by_xpath("//tbody[@id='dataBody']/tr[25]/td[36]").text
        int_value2_1 = int(value2_1)
        assert int_value2_1 == int_value3_13

    def assert_2_1_3_15(self):
        wd = self.app.wd
        value3_15 = wd.find_element_by_xpath("//tbody[@id='dataBody']/tr[25]/td[3]").text
        int_value3_15 = int(value3_15)
        wd.find_element_by_xpath("//span[text()='2.1 Отказы по типам устройств']").click()
        time.sleep(300)
        value2_1 = wd.find_element_by_xpath("//tbody[@id='dataBody']/tr[25]/td[51]").text
        int_value2_1 = int(value2_1)
        assert int_value2_1 == int_value3_15

    def assert_2_1_3_16(self):
        wd = self.app.wd
        value3_16 = wd.find_element_by_xpath("//tbody[@id='dataBody']/tr[25]/td[3]").text
        int_value3_16 = int(value3_16)
        wd.find_element_by_xpath("//span[text()='2.1 Отказы по типам устройств']").click()
        time.sleep(300)
        value2_1 = wd.find_element_by_xpath("//tbody[@id='dataBody']/tr[25]/td[51]").text
        int_value2_1 = int(value2_1)
        assert int_value2_1 == int_value3_16



     # coding late, else will be confuse
    def assert_2_1_2_2(self):
        wd = self.app.wd

