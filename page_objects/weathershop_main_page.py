"""
This page is for the weathershop home page
URL: https://weathershopper.pythonanywhere.com/

"""


from .Base_Page import Base_Page
import conf.locators_conf as locators
from utils.Wrapit import Wrapit

class WeatherShop_Main_Page(Base_Page):

    #locators
    temperature = locators.temperature
    moisturizer = locators.buy_moisturizers
    sunscreen = locators.buy_sunscreens

    def start(self):
        
        url = '/'
        self.open(url)

    def check_temperature(self):

        value = 19
        
        result_flag = self.check_element_present(self.temperature)
        self.log_result(result_flag,
            positive='Temperature is present',
            negative='Temperature not present',
            level='debug')

        result_element = self.get_element(self.temperature,verbose_flag=True)
        print(result_element)

        result_element_text = self.get_dom_text(result_element)
        print(result_element_text)

        current_temperature = result_element_text.decode('utf-8').replace('°C','').replace('℃','')
        print(current_temperature)

        if int(current_temperature) < value:
            result_flag = self.check_element_present(self.moisturizer)
            self.log_result(result_flag,
                positive='Moisturizer is present',
                negative='Moisturizer is not present',
                level='debug')
            self.click_element(self.moisturizer)
        elif int(current_temperature) > value:
            result_flag = self.check_element_present(self.sunscreen)
            self.log_result(result_flag,
                positive='sunscreen is present',
                negative='sunscreen is not present',
                level='debug')
            self.click_element(self.sunscreen)

        return result_flag
