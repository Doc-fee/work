import time

class FormsHelper:

    def __init__(self, app):
        self.app = app

# Choice section

    def select_extra_forms(self):
        wd = self.app.wd
        wd.find_element_by_xpath("(//div[text()='III. Дополнительные формы'])").click()
        time.sleep(3)

    def select_operational_reports(self):
        wd = self.app.wd
        wd.find_element_by_xpath("(//div[text()='I. Оперативная отчетность'])").click()
        time.sleep(3)

    def select_analytical_forms(self):
        wd = self.app.wd
        wd.find_element_by_xpath("(//div[text()='II. Аналитические отчеты и справки'])").click()
        time.sleep(3)

    def select_TN(self):
        wd = self.app.wd
        wd.find_element_by_xpath("(//div[text()='IV. Технологические нарушения'])").click()
        time.sleep(3)
# Choice form
    def select_high_speed(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='Скоростной ход']").click()
        time.sleep(15)

    def select_1_11(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='1.11 Эксплуатационные последствия']").click()
        time.sleep(15)

    def select_1_1(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='1.1 Отказы ЖАТ всего']").click()
        time.sleep(15)

    def select_2_1(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='2.1 Отказы по типам устройств']").click()
        time.sleep(15)

    def select_2_2(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='2.2 Отказы по системам']").click()
        time.sleep(15)
