from selenium import webdriver
from fixture.details import DetailsHelper
from fixture.filter import FilterHelper
from fixture.forms import FormsHelper
import time

class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.filter = FilterHelper(self)
        self.forms = FormsHelper(self)
        self.details = DetailsHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://onil-iis/onil.web.uo/")

    def click_on_clear(self):
        wd = self.wd
        time.sleep(2)
        wd.find_element_by_xpath("//div[@id='starting-overlay']/div/img").click()
        time.sleep(2)

    def destroy(self):
        self.wd.quit()