from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service= Service(
    ChromeDriverManager()
    .install()))

driver.get("https://orteil.dashnet.org/cookieclicker/")
driver.implicitly_wait(4)

cookies_accept_button = driver.find_element(By.LINK_TEXT, "Got it!")
cookies_accept_button.click()
sleep(4)

english_language_button = driver.find_element(By.ID, "langSelect-EN")
english_language_button.click()
sleep(4)

cookie_button = driver.find_element(By.ID, "bigCookie")

cookie_button.click()




for i in range(30000):
    cookie_button.click()
    product_cursor = driver.find_element(By.ID, "product0")
    product_grandma = driver.find_element(By.ID, "product1")
    product_unicorn = driver.find_element(By.ID, "product2")
    
    if i % 12000 == 0:
        pass
        # product_unicorn.click()


    
    


print("Hello")
sleep(30)