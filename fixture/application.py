from selenium import webdriver

from fixture.assert_forms import AssertFormsHelper
from fixture.details import DetailsHelper
from fixture.filter import FilterHelper
from fixture.forms import FormsHelper
from fixture.counter import CounterHelper
from fixture.sum_table import SumTableHelper
import time

class Application:

    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.wd.maximize_window()
        self.wd.implicitly_wait(30)
        self.filter = FilterHelper(self)
        self.forms = FormsHelper(self)
        self.details = DetailsHelper(self)
        self.counter = CounterHelper(self)
        self.assert_forms = AssertFormsHelper(self)
        self.sum_table = SumTableHelper(self)
        self.base_url = base_url

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

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