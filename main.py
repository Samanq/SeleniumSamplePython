from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

print("-" * 100)

# Setting options.
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
# disable logging
options.add_experimental_option('excludeSwitches', ['enable-logging'])

# Instantiating the driver.
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options)

print("driver created.")

# Getting the website.
driver.get("https://www.w3schools.com/")
print(f"{driver.title} loaded")

# Getting the source code of the page.
page_source  = driver.page_source

sleep(3)

# ------------------------------- Accepting cookies  -------------------------------

accept_cookies_button = driver.find_element(By.ID, "accept-choices")
accept_cookies_button.click()

# ------------------------------- Getting elements  -------------------------------

# Getting an element by Id
main_search_box = driver.find_element(By.ID, "search2")
print("search_box found")

# Getting an element by css Selector
main_search_box = driver.find_element(By.CSS_SELECTOR, "input#search2")
print("search_box found again")

# Getting an element by link text
help_link = driver.find_element(By.LINK_TEXT, "Not Sure Where To Begin?")
print("video link found")

# Getting elements by class name.
all_buttons = driver.find_elements(By.CLASS_NAME, "w3-button")
print(f"{len(all_buttons)} buttons found")

# Getting and elemet by X-Path
about_us = driver.find_element(By.XPATH, '//*[@id="main"]/footer/p')
print(f"about us found {about_us.get_attribute('class')}")

# ------------------------------- Getting attributes  -------------------------------

# Getting href attribute of a link
help_href = help_link.get_attribute("href")
print(help_href)

# Getting onkeydown attribute of an element
search_box_on_key_down = main_search_box.get_attribute("onkeydown")
print(search_box_on_key_down)

# Getting innder html of an element
diploma_area_element = driver.find_element(By.ID, 'getdiploma')
diploma_html = diploma_area_element.get_attribute("innerHTML")
print(f'{diploma_html[0:30]}...')


# ------------------------------- Sending keys  --------------------------------

# Sending text to an element
main_search_box.send_keys("Python")

# Sending enter (return) to an element.
main_search_box.send_keys(Keys.RETURN)

# Sending click
sleep(2)
getting_started_button = driver.find_element(By.LINK_TEXT, "Python Get Started")
getting_started_button.click()



sleep(500)