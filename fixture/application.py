from selenium import webdriver

from fixture.assert_forms import AssertFormsHelper
from fixture.details import DetailsHelper
from fixture.filter import FilterHelper
from fixture.forms import FormsHelper
from fixture.counter import CounterHelper
import time

class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.filter = FilterHelper(self)
        self.forms = FormsHelper(self)
        self.details = DetailsHelper(self)
        self.counter = CounterHelper(self)
        self.assert_forms = AssertFormsHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://onil-iis/onil.web.uo/")

    def click_clear(self):
        wd = self.wd
        wd.find_element_by_xpath("//div[@id='starting-overlay']/div/img").click()
        time.sleep(2)

    def click_starting_overlay(self):
        wd = self.wd
        window = wd.find_elements_by_xpath("//div[@id='starting-overlay']")
        if window:
            self.click_clear()


    def destroy(self):
        self.wd.quit()