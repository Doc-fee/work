import time

class FormsHelper:

    def __init__(self, app):
        self.app = app

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


    def select_high_speed(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='Скоростной ход']").click()
        time.sleep(15)

    def select_1_11(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='1.11 Эксплуатационные последствия']").click()
        time.sleep(15)
