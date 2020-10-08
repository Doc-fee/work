import time

class AssertFormsHelper:

    def __init__(self, app):
        self.app = app

    def assert_2_1_3_1(self):
        wd = self.app.wd
        value3_1 = wd.find_element_by_xpath("//tbody[@id='dataBody']/tr[1]/td[18]").text
        if value3_1 == '':
            value3_1 = 0
        int_value3_1 = int(value3_1)
        wd.find_element_by_xpath("//span[text()='2.1 Отказы по типам устройств']").click()
        time.sleep(300)
        value2_1 = wd.find_element_by_xpath("//tbody[@id='dataBody']/tr[25]/td[9]").text
        if value2_1 == '':
            value2_1 = 0
        int_value2_1 = int(value2_1)
        assert int_value2_1 == int_value3_1

    def assert_2_1_3_2(self):
        wd = self.app.wd
        value3_2 = wd.find_element_by_xpath("//tbody[@id='dataBody']/tr[1]/td[18]").text
        if value3_2 == '':
            value3_2 = 0
        int_value3_2 = int(value3_2)
        wd.find_element_by_xpath("//span[text()='2.1 Отказы по типам устройств']").click()
        time.sleep(300)
        value2_1 = wd.find_element_by_xpath("//tbody[@id='dataBody']/tr[25]/td[9]").text
        if value2_1 == '':
            value2_1 = 0
        int_value2_1 = int(value2_1)
        assert int_value2_1 == int_value3_2

    def assert_2_1_3_4(self):
        wd = self.app.wd
        value3_4 = wd.find_element_by_xpath("//tbody[@id='dataBody']/tr[25]/td[3]").text
        if value3_4 == '':
            value3_4 = 0
        int_value3_4 = int(value3_4)
        wd.find_element_by_xpath("//span[text()='2.1 Отказы по типам устройств']").click()
        time.sleep(300)
        value2_1 = wd.find_element_by_xpath("//tbody[@id='dataBody']/tr[25]/td[18]").text
        if value2_1 == '':
            value2_1 = 0
        int_value2_1 = int(value2_1)
        assert int_value2_1 == int_value3_4

    def assert_2_1_3_5(self):
        wd = self.app.wd
        value3_5 = wd.find_element_by_xpath("//tbody[@id='dataBody']/tr[11]/td[3]").text
        if value3_5 == '':
            value3_5 = 0
        int_value3_5 = int(value3_5)
        wd.find_element_by_xpath("//span[text()='2.1 Отказы по типам устройств']").click()
        time.sleep(300)
        value2_1 = wd.find_element_by_xpath("//tbody[@id='dataBody']/tr[25]/td[21]").text
        if value2_1 == '':
            value2_1 = 0
        int_value2_1 = int(value2_1)
        assert int_value2_1 == int_value3_5

    def assert_2_1_3_6(self):
        wd = self.app.wd
        # всего реле
        relay = wd.find_element_by_xpath("//tbody[@id ='dataBody']/tr[1]/td[66]").text
        if relay == '':
            relay = 0
        relay_int = int(relay)
        # всего Ячейки кодовой автоблокировки
        Coded_autolock_cell = wd.find_element_by_xpath("//tbody[@id ='dataBody']/tr[12]/td[66]").text
        if Coded_autolock_cell == '':
            Coded_autolock_cell = 0
        Coded_autolock_cell_int = int(Coded_autolock_cell)
        # всего Релейные блоки ЭЦ
        Relay_blocks_EC = wd.find_element_by_xpath("//tbody[@id ='dataBody']/tr[13]/td[66]").text
        if Relay_blocks_EC == '':
            Relay_blocks_EC = 0
        Relay_blocks_EC_int = int(Relay_blocks_EC)
        # всего Трансмиттеры (контактные)
        Transmitters = wd.find_element_by_xpath("//tbody[@id ='dataBody']/tr[14]/td[66]").text
        if Transmitters == '':
            Transmitters = 0
        Transmitters_int = int(Transmitters)
        # всего Путевые защитные фильтры
        track_Protective_Filters = wd.find_element_by_xpath("//tbody[@id ='dataBody']/tr[15]/td[66]").text
        if track_Protective_Filters == '':
            track_Protective_Filters = 0
        track_Protective_Filters_int = int(track_Protective_Filters)
        # всего Трансформаторы
        Transformers = wd.find_element_by_xpath("//tbody[@id ='dataBody']/tr[16]/td[66]").text
        if Transformers == '':
            Transformers = 0
        Transformers_int = int(Transformers)
        # всего Резисторы
        Resistors = wd.find_element_by_xpath("//tbody[@id ='dataBody']/tr[23]/td[66]").text
        if Resistors == '':
            Resistors = 0
        Resistors_int = int(Resistors)
        # всего Выпрямители, выпрямит. блоки
        Rectifiers = wd.find_element_by_xpath("//tbody[@id ='dataBody']/tr[24]/td[66]").text
        if Rectifiers == '':
            Rectifiers = 0
        Rectifiers_int = int(Rectifiers)
        # всего Преобразователи
        Converters = wd.find_element_by_xpath("//tbody[@id ='dataBody']/tr[25]/td[66]").text
        if Converters == '':
            Converters = 0
        Converters_int = int(Converters)
        # всего Бесконтактные п/п приборы
        Noncontact_devices = wd.find_element_by_xpath("//tbody[@id ='dataBody']/tr[26]/td[66]").text
        if Noncontact_devices == '':
            Noncontact_devices = 0
        Noncontact_devices_int = int(Noncontact_devices)
        # всего Аппаратура ЧДК
        ChDK_equipment = wd.find_element_by_xpath("//tbody[@id ='dataBody']/tr[30]/td[66]").text
        if ChDK_equipment == '':
            ChDK_equipment = 0
        ChDK_equipment_int = int(ChDK_equipment)
        # всего Аппаратура АСДК, АПК-ДК
        ASDK_APKDK_equipment = wd.find_element_by_xpath("//tbody[@id ='dataBody']/tr[31]/td[66]").text
        if ASDK_APKDK_equipment == '':
            ASDK_APKDK_equipment = 0
        ASDK_APKDK_equipment_int = int(ASDK_APKDK_equipment)
        # всего Аппаратура ТРЦ
        TRC_equipment = wd.find_element_by_xpath("//tbody[@id ='dataBody']/tr[32]/td[66]").text
        if TRC_equipment == '':
            TRC_equipment = 0
        TRC_equipment_int = int(TRC_equipment)
        # всего остальные
        others = wd.find_element_by_xpath("//tbody[@id ='dataBody']/tr[37]/td[66]").text
        if others == '':
            others = 0
        others_int = int(others)
        int_value3_6 = relay_int+Coded_autolock_cell_int+Relay_blocks_EC_int+Transmitters_int+\
                       track_Protective_Filters_int+Transformers_int+Resistors_int+Rectifiers_int+Converters_int+\
                       Noncontact_devices_int+ChDK_equipment_int+ASDK_APKDK_equipment_int+TRC_equipment_int+others_int
        wd.find_element_by_xpath("//span[text()='2.1 Отказы по типам устройств']").click()
        time.sleep(300)
        value2_1 = wd.find_element_by_xpath("//tbody[@id='dataBody']/tr[25]/td[6]").text
        if value2_1 == '':
            value2_1 = 0
        int_value2_1 = int(value2_1)
        assert int_value2_1 == int_value3_6

    def assert_2_1_3_7(self):
        wd = self.app.wd
        value3_7 = wd.find_element_by_xpath("//tbody[@id='dataBody']/tr[17]/td[3]").text
        if value3_7 == '':
            value3_7 = 0
        int_value3_7 = int(value3_7)
        wd.find_element_by_xpath("//span[text()='2.1 Отказы по типам устройств']").click()
        time.sleep(300)
        value2_1 = wd.find_element_by_xpath("//tbody[@id='dataBody']/tr[25]/td[12]").text
        if value2_1 == '':
            value2_1 = 0
        int_value2_1 = int(value2_1)
        assert int_value2_1 == int_value3_7

    def assert_2_1_3_8(self):
        wd = self.app.wd
        value3_8 = wd.find_element_by_xpath("//tbody[@id='dataBody']/tr[32]/td[3]").text
        if value3_8 == '':
            value3_8 = 0
        int_value3_8 = int(value3_8)
        wd.find_element_by_xpath("//span[text()='2.1 Отказы по типам устройств']").click()
        time.sleep(300)
        value2_1 = wd.find_element_by_xpath("//tbody[@id='dataBody']/tr[25]/td[15]").text
        if value2_1 == '':
            value2_1 = 0
        int_value2_1 = int(value2_1)
        assert int_value2_1 == int_value3_8

    def assert_2_1_3_9(self):
        wd = self.app.wd
        value3_9 = wd.find_element_by_xpath("//tbody[@id='dataBody']/tr[16]/td[3]").text
        int_value3_9 = int(value3_9)
        wd.find_element_by_xpath("//span[text()='2.1 Отказы по типам устройств']").click()
        time.sleep(300)
        value2_1 = wd.find_element_by_xpath("//tbody[@id='dataBody']/tr[25]/td[24]").text
        if value2_1 == '':
            value2_1 = 0
        int_value2_1 = int(value2_1)
        assert int_value2_1 == int_value3_9

    def assert_2_1_3_10(self):
        wd = self.app.wd
        value3_9 = wd.find_element_by_xpath("//tbody[@id='dataBody']/tr[12]/td[3]").text
        int_value3_9 = int(value3_9)
        wd.find_element_by_xpath("//span[text()='2.1 Отказы по типам устройств']").click()
        time.sleep(300)
        value2_1 = wd.find_element_by_xpath("//tbody[@id='dataBody']/tr[25]/td[30]").text
        if value2_1 == '':
            value2_1 = 0
        int_value2_1 = int(value2_1)
        assert int_value2_1 == int_value3_9


    # def assert_2_1_3_11(self):
    #     wd = self.app.wd
    #     value3_11 = wd.find_element_by_xpath("//tbody[@id='dataBody']/tr[10]/td[3]").text
    #     int_value3_11 = int(value3_11)
    #     wd.find_element_by_xpath("//span[text()='2.1 Отказы по типам устройств']").click()
    #     time.sleep(300)
    #     value2_1 = wd.find_element_by_xpath("//tbody[@id='dataBody']/tr[25]/td[15]").text
    #     int_value2_1 = int(value2_1)
    #     assert int_value2_1 == int_value3_11

    def assert_2_1_3_13(self):
        wd = self.app.wd
        value3_13 = wd.find_element_by_xpath("//tbody[@id='dataBody']/tr[9]/td[3]").text
        int_value3_13 = int(value3_13)
        wd.find_element_by_xpath("//span[text()='2.1 Отказы по типам устройств']").click()
        time.sleep(300)
        value2_1 = wd.find_element_by_xpath("//tbody[@id='dataBody']/tr[25]/td[36]").text
        if value2_1 == '':
            value2_1 = 0
        int_value2_1 = int(value2_1)
        assert int_value2_1 == int_value3_13

    def assert_2_1_3_15(self):
        wd = self.app.wd
        value3_15 = wd.find_element_by_xpath("//tbody[@id='dataBody']/tr[25]/td[3]").text
        int_value3_15 = int(value3_15)
        wd.find_element_by_xpath("//span[text()='2.1 Отказы по типам устройств']").click()
        time.sleep(300)
        value2_1 = wd.find_element_by_xpath("//tbody[@id='dataBody']/tr[25]/td[39]").text
        if value2_1 == '':
            value2_1 = 0
        int_value2_1 = int(value2_1)
        assert int_value2_1 == int_value3_15

    def assert_2_1_3_16(self):
        wd = self.app.wd
        value3_16 = wd.find_element_by_xpath("//tbody[@id='dataBody']/tr[25]/td[3]").text
        int_value3_16 = int(value3_16)
        wd.find_element_by_xpath("//span[text()='2.1 Отказы по типам устройств']").click()
        time.sleep(300)
        value2_1 = wd.find_element_by_xpath("//tbody[@id='dataBody']/tr[25]/td[51]").text
        if value2_1 == '':
            value2_1 = 0
        int_value2_1 = int(value2_1)
        assert int_value2_1 == int_value3_16

    def assert_2_1_3_18(self):
        wd = self.app.wd
        #Линии связи
        value1 = wd.find_element_by_xpath("//tbody[@id='dataBody']/tr[25]/td[18]").text
        if value1 == '':
            value1 = 0
        int_value1 = int(value1)
        # Электроснаб
        value2 = wd.find_element_by_xpath("//tbody[@id='dataBody']/tr[25]/td[21]").text
        if value2 == '':
            value2 = 0
        int_value2 = int(value2)
        # Внеш возд
        value3 = wd.find_element_by_xpath("//tbody[@id='dataBody']/tr[25]/td[24]").text
        if value3 == '':
            value3 = 0
        int_value3 = int(value3)
        # Прочие
        value4 = wd.find_element_by_xpath("//tbody[@id='dataBody']/tr[25]/td[27]").text
        if value4 == '':
            value4 = 0
        int_value4 = int(value4)
        # Линии связиНаруш.техн. проз. работ ШН
        value5 = wd.find_element_by_xpath("//tbody[@id='dataBody']/tr[25]/td[30]").text
        if value5 == '':
            value5 = 0
        int_value5 = int(value5)
        # Причина не установлена
        value6 = wd.find_element_by_xpath("//tbody[@id='dataBody']/tr[25]/td[33]").text
        if value6 == '':
            value6 = 0
        int_value6 = int(value6)
        # Неисправность КТСМ
        value7 = wd.find_element_by_xpath("//tbody[@id='dataBody']/tr[25]/td[36]").text
        if value7 == '':
            value7 = 0
        int_value7 = int(value7)
        value3_18 = int_value7 + int_value6 + int_value5 + int_value4 + int_value3 + int_value2 + int_value1
        wd.find_element_by_xpath("//span[text()='2.1 Отказы по типам устройств']").click()
        time.sleep(300)
        value2_1 = wd.find_element_by_xpath("//tbody[@id='dataBody']/tr[25]/td[42]").text
        if value2_1 == '':
            value2_1 = 0
        int_value2_1 = int(value2_1)
        assert int_value2_1 == value3_18

    def assert_2_1_3_19_3_20(self):
        wd = self.app.wd
        value3_18 = wd.find_element_by_xpath("//tbody[@id='dataBody']/tr[25]/td[3]").text
        if value3_18 == '':
            value3_18 = 0
        int_value3_18 = int(value3_18)
        wd.find_element_by_xpath("//span[text()='3.19 Отказы УКСПС']").click()
        time.sleep(15)
        value3_19 = wd.find_element_by_xpath("//tbody[@id='dataBody']/tr[25]/td[3]").text
        if value3_19 == '':
            value3_19 = 0
        int_value3_19 = int(value3_19)
        int_value_uksps_kgu = int_value3_19 + int_value3_18
        wd.find_element_by_xpath("//span[text()='2.1 Отказы по типам устройств']").click()
        time.sleep(300)
        value2_1 = wd.find_element_by_xpath("//tbody[@id='dataBody']/tr[25]/td[9]").text
        if value2_1 == '':
            value2_1 = 0
        int_value2_1 = int(value2_1)
        assert int_value2_1 == int_value_uksps_kgu

     # coding late, else will be confuse
    def assert_2_1_2_2(self):
        wd = self.app.wd

