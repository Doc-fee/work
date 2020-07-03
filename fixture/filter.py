import time

class FilterHelper:

    def __init__(self, app):
        self.app = app

    def click_filter_ok(self):
        wd = self.app.wd
        wd.find_element_by_id("buttonFilterboxOk").click()
        time.sleep(15)

    def filter_for_the_current_year(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='Дата начала']").click()
        wd.find_element_by_xpath("//select [@class='ui-datepicker-month']/option[text()='Январь']").click()
        wd.find_element_by_xpath('//a[@class="ui-state-default"][text()="1"]').click()
        wd.find_element_by_xpath("//span[text()='Дата конца']").click()
        wd.find_element_by_xpath("//select [@class='ui-datepicker-month']/option[text()='Декабрь']").click()
        wd.find_element_by_xpath('//a[@class="ui-state-default"][text()="31"]').click()

    def open_filter(self):
        wd = self.app.wd
        wd.find_element_by_xpath(u"//img[@title='Фильтр']").click()
        time.sleep(2)

    def count_of_failure(self):
        wd = self.app.wd
        count_of_failure = wd.find_element_by_xpath("//div[@class ='filterbox-header-count-data']")
