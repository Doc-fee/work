import time

class FilterHelper:

    def __init__(self, app):
        self.app = app

    def click_filter_ok(self):
        wd = self.app.wd
        wd.find_element_by_id("buttonFilterboxOk").click()
        #wd.implicitly_wait(30)
        time.sleep(170)


    def open_filter(self):
        wd = self.app.wd
        wd.find_element_by_xpath(u"//img[@title='Фильтр']").click()

# По времени
    def filter_for_the_current_year(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='Дата начала']").click()
        wd.find_element_by_xpath("//select [@class='ui-datepicker-month']/option[text()='Январь']").click()
        wd.find_element_by_xpath('//a[@class="ui-state-default"][text()="1"]').click()
        wd.find_element_by_xpath("//span[text()='Дата конца']").click()
        wd.find_element_by_xpath("//select [@class='ui-datepicker-month']/option[text()='Декабрь']").click()
        wd.find_element_by_xpath('//a[@class="ui-state-default"][text()="31"]').click()

    def filter_for_2019(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='Дата начала']").click()
        wd.find_element_by_xpath("//select [@class='ui-datepicker-year']/option[text()='2019']").click()
        wd.find_element_by_xpath("//select [@class='ui-datepicker-month']/option[text()='Январь']").click()
        wd.find_element_by_xpath('//a[@class="ui-state-default"][text()="1"]').click()
        wd.find_element_by_xpath("//span[text()='Дата конца']").click()
        wd.find_element_by_xpath("//select [@class='ui-datepicker-year']/option[text()='2019']").click()
        wd.find_element_by_xpath("//select [@class='ui-datepicker-month']/option[text()='Декабрь']").click()
        wd.find_element_by_xpath('//a[@class="ui-state-default"][text()="31"]').click()

    def filter_for_2020(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='Дата начала']").click()
        wd.find_element_by_xpath("//select [@class='ui-datepicker-year']/option[text()='2020']").click()
        wd.find_element_by_xpath("//select [@class='ui-datepicker-month']/option[text()='Январь']").click()
        wd.find_element_by_xpath('//a[@class="ui-state-default"][text()="1"]').click()
        wd.find_element_by_xpath("//span[text()='Дата конца']").click()
        wd.find_element_by_xpath("//select [@class='ui-datepicker-year']/option[text()='2020']").click()
        wd.find_element_by_xpath("//select [@class='ui-datepicker-month']/option[text()='Декабрь']").click()
        wd.find_element_by_xpath('//a[@class="ui-state-default"][text()="31"]').click()

    def filter_for_1st_quarter(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='Дата начала']").click()
        wd.find_element_by_xpath("//select [@class='ui-datepicker-month']/option[text()='Январь']").click()
        wd.find_element_by_xpath('//a[@class="ui-state-default"][text()="1"]').click()
        wd.find_element_by_xpath("//span[text()='Дата конца']").click()
        wd.find_element_by_xpath("//select [@class='ui-datepicker-month']/option[text()='Март']").click()
        wd.find_element_by_xpath('//a[@class="ui-state-default"][text()="31"]').click()

    def filter_for_January(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='Дата начала']").click()
        wd.find_element_by_xpath("//select [@class='ui-datepicker-month']/option[text()='Январь']").click()
        wd.find_element_by_xpath('//a[@class="ui-state-default"][text()="1"]').click()
        wd.find_element_by_xpath("//span[text()='Дата конца']").click()
        wd.find_element_by_xpath("//select [@class='ui-datepicker-month']/option[text()='Январь']").click()
        wd.find_element_by_xpath('//a[@class="ui-state-default"][text()="31"]').click()

    def filter_for_January_1st(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='Дата начала']").click()
        wd.find_element_by_xpath("//select [@class='ui-datepicker-month']/option[text()='Январь']").click()
        wd.find_element_by_xpath('//a[@class="ui-state-default"][text()="1"]').click()
        wd.find_element_by_xpath("//span[text()='Дата конца']").click()
        wd.find_element_by_xpath("//select [@class='ui-datepicker-month']/option[text()='Январь']").click()
        wd.find_element_by_xpath('//a[@class="ui-state-default"][text()="1"]').click()


# По ответственности
    def filter_service_sh(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//table[@id='filterTree']//span[text()='Ответственность']").click()
        wd.find_elements_by_xpath("//table[@id='filterTree']//span[text()='Ответственность']")[1].click()
        wd.find_element_by_xpath("//div[@class='filterbox-content-area-right selectoids']//span[text()='Ш']").click()
