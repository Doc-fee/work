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
#        self.clear_window =
#        self.wait("visible")

    def open_home_page(self):
        wd = self.wd
        wd.get("http://onil-iis/onil.web.uo/")

    def click_on_clear(self):
        wd = self.wd
        wd.find_element_by_xpath("//div[@id='starting-overlay']/div/img").click()
        time.sleep(2)

    def remember_the_total_number(self):
        wd = self.wd
        total_number = wd.find_element_by_xpath("//tbody[@id='dataBody']/tr[-1]/td[3]")
        int_total_number = int(total_number)
        print(int_total_number)


    def destroy(self):
        self.wd.quit()