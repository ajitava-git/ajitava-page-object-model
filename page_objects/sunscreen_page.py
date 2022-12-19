"""
This page is for the weathershop sunscreen page
URL: https://weathershopper.pythonanywhere.com/sunscreen

"""

from .Base_Page import Base_Page
import conf.locators_conf as locators
from utils.Wrapit import Wrapit
import re
import json

class Sunscreen_Page(Base_Page):

    #locators
    least_expensive_spf50 = locators.add_least_expensive_spf50
    least_expensive_spf30 = locators.add_least_expensive_spf30
    body = locators.body
    add_cart = locators.add_cart

    def select_sunscreen(self):

        #Getting the body element
        result_element = self.get_element(self.body,verbose_flag=True)
        print(result_element)

        #Fetching the DOM text for the body
        result_element_text = self.get_dom_text(result_element)
        print(result_element_text)

        clean_text = []

        #Getting the text in raw format and stripping to get only sunscreen name and price
        clean_text = result_element_text.decode('utf-8').strip('\n').strip('Cart - Empty').replace('Sunscreens','').replace('Add','').strip('© Qxf2 Services 2018 - 2022').replace('Rs.','').replace('Price:','')
        print(clean_text)

        #Getting the SPF-30 and SPF-50 with price as all digits in a list
        temp = re.findall(r'\d+', clean_text)
        res_list = list(map(int, temp))
        print(res_list)

        #Converting to Dictionary to get key,value pair of sunscreen name and price
        res_dct = map(lambda i: (res_list[i], res_list[i+1]), range(len(res_list)-1)[::2])
        sunscreen_dict = dict(res_dct)
        print(sunscreen_dict)

        #Sorting the dictionary
        sort_cream = dict(sorted(sunscreen_dict.items(), key=lambda item: item[1]))
        print(sort_cream)

        #Iterating the dict to fetch the least expensive sunscreen
        for key in sort_cream:
            if key == 30:
                #click the add button for least expensive sunscreen with spf30
                self.click_element(self.least_expensive_spf30)
                break 

        for key in sort_cream:
            if key == 50:
                #click the add button for least expensive sunscreen with spf50
                self.click_element(self.least_expensive_spf50)
                #click add cart
                self.click_element(self.add_cart)
                break        

       

        