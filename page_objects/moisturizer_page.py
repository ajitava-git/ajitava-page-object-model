"""
This page is for the weathershop moisturizer page
URL: https://weathershopper.pythonanywhere.com/moisturizer

"""

from .Base_Page import Base_Page
import conf.locators_conf as locators
from utils.Wrapit import Wrapit
import re

class Moisturizer_Page(Base_Page):

    #locators
    least_expensive_almond = locators.add_least_expensive_almond
    least_expensive_aloe = locators.add_least_expensive_aloe
    body = locators.body
    add_cart = locators.add_cart

    def select_moisturizer(self):

        #Getting the body element
        result_element = self.get_element(self.body,verbose_flag=True)
        print(result_element)

        #Fetching the DOM text for the body
        result_element_text = self.get_dom_text(result_element)
        print(result_element_text)

        clean_text = []

        #Getting the text in raw format and stripping to get only moisturizer name and price
        clean_text = result_element_text.decode('utf-8').strip('\n').strip('Cart - Empty').replace('Moisturizers','').replace('Add','').strip('© Qxf2 Services 2018 - 2022').replace('Rs.','').replace('Price:','')
        print(clean_text)

        #Storing the data in list
        temp_list = re.split(r'(\d+)', clean_text)
        print(temp_list)

        #Cleaning up \n from the list
        res_list = [item.replace('\n', '') for item in temp_list]
        print(res_list)

        #Converting to Dictionary to get key,value pair of moisturizer name and price
        res_dct = map(lambda i: (res_list[i], res_list[i+1]), range(len(res_list)-1)[::2])
        moisturizer_dict = dict(res_dct)
        print(moisturizer_dict)

        #Sorting the dictionary
        sort_cream = dict(sorted(moisturizer_dict.items(), key=lambda item: item[1]))  
        print(sort_cream)

        #Iterating the dict to fetch the least expensive mositurizer
        for key in sort_cream:
            if key.__contains__('Aloe' or 'aloe'):
                print(key)
                #click the add button for aloe moisturizer with least value
                self.click_element(self.least_expensive_aloe)
                break 

        for key in sort_cream:
            if key.__contains__('Almond' or 'almond'):
                print(key)
                #click the add button for almond moisturizer with least value
                self.click_element(self.least_expensive_almond)
                #click add to cart
                self.click_element(self.add_cart)
                break
