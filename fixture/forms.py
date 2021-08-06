import time

class FormsHelper:

    def __init__(self, app):
        self.app = app



# Choice section

    def select_extra_forms(self):
        wd = self.app.wd
        wd.find_element_by_xpath("(//div[text()='III. Дополнительная отчетность'])").click()
        wd.implicitly_wait(600)

    def select_operational_reports(self):
        wd = self.app.wd
        wd.find_element_by_xpath("(//div[text()='I. Оперативная отчетность'])").click()
        wd.implicitly_wait(600)

    def select_analytical_forms(self):
        wd = self.app.wd
        wd.find_element_by_xpath("(//div[text()='II. Аналитические отчеты и справки'])").click()
        wd.implicitly_wait(600)

    def select_TN(self):
        wd = self.app.wd
        wd.find_element_by_xpath("(//div[text()='IV. Технологические нарушения'])").click()
        wd.implicitly_wait(600)

# Choice form
    #Analytical forms

    def select_1_1(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='1.1 Отказы ЖАТ всего']").click()
        time.sleep(60)


    def select_1_2(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='1.2 Отказы ЖАТ Ш']").click()
        time.sleep(60)


    def select_1_3(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='1.3 Отказы ЖАТ Ш (ЭЦ)']").click()
        time.sleep(60)


    def select_1_4(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='1.4 Отказы ЖАТ Ш (АБ)']").click()
        time.sleep(60)

    def select_1_5(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='1.5 Продолжительность Ш по системам']").click()
        time.sleep(60)


    def select_1_6(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='1.6 Продолжительность Ш (ЭЦ)']").click()
        time.sleep(60)


    def select_1_7(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='1.7 Продолжительность Ш (АБ)']").click()
        time.sleep(60)


    def select_1_8(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='1.8 Среднее время восст. Ш по системам']").click()
        time.sleep(60)


    def select_1_9(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='1.9 Среднее время восст. Ш (ЭЦ)']").click()
        time.sleep(60)


    def select_1_10(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='1.10 Среднее время восст. Ш (АБ)']").click()
        time.sleep(60)


    def select_1_11(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='1.11 Эксплуатационные последствия']").click()
        time.sleep(60)


    def select_1_12(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='1.12 Закрытия ЖАТ']").click()
        time.sleep(60)


    def select_1_13(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='1.13 Задержки у входных']").click()
        time.sleep(60)


    def select_1_14(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='1.14 Перекрытия']").click()
        time.sleep(60)


    def select_1_15(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='1.15 Пропуск по дополнительным средствам']").click()
        time.sleep(60)


    def select_1_16(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='1.16 Отказы по объектам ЖАТ']").click()
        time.sleep(60)


    def select_1_17(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//li[@title='Факты задержек пассажирских и пригородных поездов']").click()
        time.sleep(60)


    def select_1_18(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='1.18 Факты грузовых']").click()
        time.sleep(60)


    def select_1_19(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='1.19 Факты по элементам ЖАТ']").click()
        time.sleep(60)


    def select_1_20(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='1.20 Отказы с фактами пассажирских']").click()
        time.sleep(60)


    def select_1_21(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='1.21 Отказы с фактами пригородных']").click()
        time.sleep(60)


    def select_1_22(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='1.22 Отказы с фактами грузовых']").click()
        time.sleep(60)


    def select_1_23(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='1.23 Отказы с задержками СП, ВСП']").click()
        time.sleep(60)


    def select_1_24(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//li[@title='Отказы систем ЖАТ 1 и 2 категории по классам железнодорожных линий']").click()
        time.sleep(60)


    def select_1_25(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//li[@title='Отказы систем ЖАТ 3 категории по классам железнодорожных линий']").click()
        time.sleep(60)


    def select_1_27(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//li[@title='Опасные отказы устройств ЖАТ (Ш)']").click()
        time.sleep(60)


    def select_1_28(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//li[@title='Количество отказов по объектам ЖАТ']").click()
        time.sleep(60)


    def select_1_30(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//li[@title='Отказы технических средств']").click()
        time.sleep(60)


    def select_1_31(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//li[@title='Задержки поездов по месту из-за отказов технических средств']").click()
        time.sleep(60)


    def select_1_32(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//li[@title='Потери поездов-часов из-за отказов технических средств']").click()
        time.sleep(60)


    def select_2_1(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='2.1 Отказы по типам устройств']").click()
        time.sleep(120)


    def select_2_2(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='2.2 Отказы по системам']").click()
        time.sleep(120)


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


    def select_2_8(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='2.8 Факты по характеру']").click()
        time.sleep(120)


    def select_2_9(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='2.9 Отказы по элементам и характеру']").click()
        time.sleep(120)


    def select_2_10(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='2.10 Отказы по системе и характеру ']").click()
        time.sleep(60)


    def select_3_1(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='3.1 РЦ по элементам']").click()
        time.sleep(60)


    def select_3_2(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//li[@title='Отказы элементов рельсовой линии']").click()
        time.sleep(60)


    def select_3_3(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//li[@title='Отказы по типам и элементам стрелочных электроприводов']").click()
        time.sleep(60)


    def select_3_4(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='3.4 Стрелочные переводы по элементам']").click()
        time.sleep(60)


    def select_3_5(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='3.5 Сигналы']").click()
        time.sleep(60)


    def select_3_6(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='3.6 Аппаратура']").click()
        time.sleep(60)



    def select_3_7(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='3.7 Монтаж']").click()
        time.sleep(60)


    def select_3_8(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='3.8 Кабельные линии']").click()
        time.sleep(60)


    def select_3_9(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='3.9 Воздушные линии']").click()
        time.sleep(60)


    def select_3_10(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='3.10 Аппараты управления']").click()
        time.sleep(60)


    def select_3_11(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='3.11 Электропитающие установки']").click()
        time.sleep(60)


    def select_3_12(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='3.12 Аккумуляторы']").click()
        time.sleep(60)


    def select_3_13(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='3.13 Элементы защиты']").click()
        time.sleep(60)


    def select_3_14(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='3.14 Микропроцессорные системы']").click()
        time.sleep(60)


    def select_3_15(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='3.15 Микропроцессорные системы ']").click()
        time.sleep(60)


    def select_3_16(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='3.16 ГАЦ']").click()
        time.sleep(60)


    def select_3_17(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='3.17 Основные элементы ГАЦ']").click()
        time.sleep(60)


    def select_3_18(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='3.18 КТСМ']").click()
        time.sleep(60)


    def select_3_19(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='3.19 Отказы УКСПС']").click()
        time.sleep(60)


    def select_3_20(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='3.20 Отказы КГУ']").click()
        time.sleep(60)


    def select_3_21(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='3.21 Срабатывания УКСПС']").click()
        time.sleep(60)


    def select_3_22(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='3.22 Срабатывания КГУ']").click()
        time.sleep(60)


    def select_3_23(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='3.23 Справка УКСПС, КГУ']").click()
        time.sleep(60)



    #Extra forms

    def select_high_speed(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='1 Показатели скоростных направлений']").click()
        time.sleep(6)
        wd.implicitly_wait(600)

    def select_high_speed_trains(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='2 Отказы с задержками скоростных поездов']").click()
        time.sleep(10)
        wd.implicitly_wait(600)

    def select_duration_2_1(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='3 Продолжительность отказов Ш по устройствам ЖАТ']").click()
        time.sleep(15)
        wd.implicitly_wait(600)

    def select_unfilled_waivers(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='5 Незаполненные отказы']").click()
        wd.implicitly_wait(600)

    #Operational reports

    def select_O(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//li[@title='Журнал учета нарушений нормальной работы устройств ЖАТ']").click()
        wd.implicitly_wait(600)

    def select_O1(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='О1. ШУ-78']").click()
        wd.implicitly_wait(600)

    def select_O2(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='О2. Отчет ЦУСИ']").click()
        wd.implicitly_wait(600)

    def select_O3(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='О3. Отчет ЦЧС']").click()
        wd.implicitly_wait(600)

    def select_O4(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='О4. Отчет ЦШ']").click()
        wd.implicitly_wait(600)

    def select_O5(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='О5. Отчет ЦШ (факты)']").click()
        wd.implicitly_wait(600)

    #TN forms
    def select_4(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='4. Сводный отчет о задержках и фактах']").click()
        time.sleep(20)
        wd.implicitly_wait(600)

    def select_5(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='5. Кол-во ТН']").click()
        time.sleep(5)
        wd.implicitly_wait(600)

    def select_6(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='6. Кол-во ТН (вид)']").click()
        time.sleep(5)
        wd.implicitly_wait(600)

    def select_7(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='7. Кол-во ТН (по причине)']").click()
        time.sleep(5)
        wd.implicitly_wait(600)

    def select_8(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='8. Задержки по месту ТН (по виду ТН)']").click()
        time.sleep(5)
        wd.implicitly_wait(600)

    def select_9(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='9. Факты вызванные ТН (по виду ТН)']").click()
        time.sleep(5)
        wd.implicitly_wait(600)

    def select_10(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='10. Факты вызванные ТН (по типам поездов)']").click()
        time.sleep(5)
        wd.implicitly_wait(600)

    def select_11(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='11. Факты (пасс. и приг.) вызванные ТН (по типу и виду)']").click()
        time.sleep(5)
        wd.implicitly_wait(600)

    def select_12(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='12. Факты (груз.) вызванные ТН (по типу и виду)']").click()
        time.sleep(5)
        wd.implicitly_wait(600)

    def select_13(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='13. Факты вызванные ОТС и ТН']").click()
        time.sleep(5)
        wd.implicitly_wait(600)

    def select_14(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='14. Факты вызванные ОТС и ТН (по типу и виду)']").click()
        time.sleep(5)
        wd.implicitly_wait(600)

    def select_15(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='15. Задержки и потери п-ч по месту ТН']").click()
        time.sleep(5)
        wd.implicitly_wait(600)

    def select_16(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='16. Задержки по месту ТН']").click()
        time.sleep(5)
        wd.implicitly_wait(600)

    def select_17(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='17. Потери п-ч по месту ТН']").click()
        time.sleep(5)
        wd.implicitly_wait(600)

    def select_18(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='18. Задержки по месту ТН (по причине)']").click()
        time.sleep(5)
        wd.implicitly_wait(600)

    def select_19(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='19. Факты вызванные ТН (по причине)']").click()
        time.sleep(5)
        wd.implicitly_wait(600)