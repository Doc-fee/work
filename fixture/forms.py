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
    #Analytical forms

    def select_1_1(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='1.1 Отказы ЖАТ всего']").click()
        time.sleep(15)

    def select_1_2(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='1.2 Отказы ЖАТ Ш']").click()
        time.sleep(15)

    def select_1_3(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='1.3 Отказы ЖАТ Ш (ЭЦ)']").click()
        time.sleep(15)

    def select_1_4(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='1.4 Отказы ЖАТ Ш (АБ)']").click()
        time.sleep(15)

    def select_1_11(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='1.11 Эксплуатационные последствия']").click()
        time.sleep(15)

    def select_1_12(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='1.12 Закрытия ЖАТ']").click()
        time.sleep(15)

    def select_1_13(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='1.13 Задержки у входных']").click()
        time.sleep(15)

    def select_1_14(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='1.14 Перекрытия']").click()
        time.sleep(15)

    def select_1_15(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='1.15 Пропуск по дополнительным средствам']").click()
        time.sleep(15)

    def select_1_16(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='1.16 Отказы по объектам ЖАТ']").click()
        time.sleep(15)

    def select_1_24(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//li[@title='Отказы систем ЖАТ 1 и 2 категории по классам железнодорожных линий']").click()
        time.sleep(15)

    def select_1_25(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//li[@title='Отказы систем ЖАТ 3 категории по классам железнодорожных линий']").click()
        time.sleep(15)

    def select_1_27(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//li[@title='Опасные отказы устройств ЖАТ (Ш)']").click()
        time.sleep(15)

    def select_2_1(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='2.1 Отказы по типам устройств']").click()
        time.sleep(120)

    def select_2_2(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='2.2 Отказы по системам']").click()
        time.sleep(60)

    def select_2_3(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='2.3 Отказы по характеру']").click()
        time.sleep(60)

    def select_2_4(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='2.4 Эксплуатационные']").click()
        time.sleep(60)

    def select_2_5(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='2.5 Производственные']").click()
        time.sleep(60)

    def select_2_6(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='2.6 Деградационные']").click()
        time.sleep(60)

    def select_2_7(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='2.7 Внешние воздействия']").click()
        time.sleep(60)

    def select_2_9(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='2.9 Отказы по элементам и характеру']").click()
        time.sleep(60)

    def select_2_10(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='2.10 Отказы по системе и характеру ']").click()
        time.sleep(60)

    def select_3_1(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='3.1 РЦ по элементам']").click()
        time.sleep(15)

    def select_3_2(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//li[@title='Отказы элементов рельсовой линии']").click()
        time.sleep(15)

    def select_3_3(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//li[@title='Отказы по типам и элементам стрелочных электроприводов']").click()
        time.sleep(15)

    def select_3_4(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='3.4 Стрелочные переводы по элементам']").click()
        time.sleep(15)

    def select_3_5(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='3.5 Сигналы']").click()
        time.sleep(15)

    def select_3_6(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='3.6 Аппаратура']").click()
        time.sleep(30)

    def select_3_7(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='3.7 Монтаж']").click()
        time.sleep(15)

    def select_3_8(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='3.8 Кабельные линии']").click()
        time.sleep(15)

    def select_3_9(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='3.9 Воздушные линии']").click()
        time.sleep(15)

    def select_3_10(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='3.10 Аппараты управления']").click()
        time.sleep(15)

    def select_3_11(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='3.11 Электропитающие установки']").click()
        time.sleep(15)

    def select_3_12(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='3.12 Аккумуляторы']").click()
        time.sleep(15)

    def select_3_13(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='3.13 Элементы защиты']").click()
        time.sleep(15)

    def select_3_14(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='3.14 Микропроцессорные системы']").click()
        time.sleep(15)

    def select_3_15(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='3.15 Микропроцессорные системы ']").click()
        time.sleep(15)

    def select_3_16(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='3.16 ГАЦ']").click()
        time.sleep(15)

    def select_3_17(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='3.17 Основные элементы ГАЦ']").click()
        time.sleep(15)

    def select_3_18(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='3.18 КТСМ']").click()
        time.sleep(15)

    def select_3_19(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='3.19 Отказы УКСПС']").click()
        time.sleep(15)

    def select_3_20(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='3.20 Отказы КГУ']").click()
        time.sleep(15)

    def select_3_21(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='3.21 Срабатывания УКСПС']").click()
        time.sleep(15)

    def select_3_22(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='3.22 Срабатывания КГУ']").click()
        time.sleep(15)

    def select_3_23(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='3.23 Справка УКСПС, КГУ']").click()
        time.sleep(15)

    #Extra forms

    def select_high_speed(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='1 Показатели скоростных направлений']").click()
        time.sleep(15)

    #Operational reports

    def select_O(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//li[@title='Журнал учета нарушений нормальной работы устройств ЖАТ']").click()
        time.sleep(15)

    def select_O1(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='О1. ШУ-78']").click()
        time.sleep(15)

    def select_O2(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='О2. Отчет ЦУСИ']").click()
        time.sleep(15)

    def select_O3(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='О3. Отчет ЦЧС']").click()
        time.sleep(15)

    def select_O4(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='О4. Отчет ЦШ']").click()
        time.sleep(15)

    def select_O5(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='О5. Отчет ЦШ (факты)']").click()
        time.sleep(15)
