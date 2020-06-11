import time

class FormsHelper:

    def __init__(self, app):
        self.app = app

    def select_high_speed(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='Скоростной ход']").click()
        time.sleep(15)

    def select_extra_forms(self):
        wd = self.app.wd
        wd.find_element_by_xpath("(//div[text()='III. Дополнительные формы'])").click()
        time.sleep(3)
