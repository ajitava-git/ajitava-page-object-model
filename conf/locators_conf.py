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
add_least_expensive_almond = "xpath,//*[contains(text(),'Almond')]/..//button[@class='btn btn-primary'][normalize-space()='Add']"
add_least_expensive_aloe = "xpath,//*[contains(text(),'Aloe')]/..//button[@class='btn btn-primary'][normalize-space()='Add']"

#locators for the weather shop sunscreen page

body = "xpath,//body"
add_least_expensive_spf50 = "xpath,//*[contains(text(),'SPF-50')]/..//button[@class='btn btn-primary'][normalize-space()='Add']"
add_least_expensive_spf30 = "xpath,//*[contains(text(),'SPF-30')]/..//button[@class='btn btn-primary'][normalize-space()='Add']"

#locator for add cart

add_cart = "xpath,//button[@class='thin-text nav-link']"

#locators for page headings

sunscreen_title = "xpath,//h2[normalize-space()='Sunscreens']"
moisturizer_title = "xpath,//h2[normalize-space()='Moisturizers']"