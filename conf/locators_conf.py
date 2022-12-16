#Common locator file for all locators
#Locators are ordered alphabetically

############################################
#Selectors we can use
#ID
#NAME
#css selector
#CLASS_NAME
#LINK_TEXT
#PARTIAL_LINK_TEXT
#XPATH
###########################################

#locators for the weather shop home page

temperature = "xpath,//span[@id='temperature']"
buy_moisturizers = "xpath,//button[contains(text(),'Buy moisturizers')]"
buy_sunscreens = "xpath,//button[contains(text(),'Buy sunscreens')]"

#locators for the weather shop moisturizer page

body = "xpath,//body"
add_least_expensive_almond = "xpath,//p[normalize-space()='Boris Almond and Honey']/..//button[@class='btn btn-primary'][normalize-space()='Add']"
add_least_expensive_aloe = "xpath,//body/div[@class='container']/div[2]/div[3]/button[1]"

#locator for add cart

add_cart = "xpath,//button[@class='thin-text nav-link']"