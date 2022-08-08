> ## Installing Selenium

Notes:

> 1. Create a virtual enviromet.
> 2. install selenium package.
> 3. install webdriver-manager package.
> 4. import packages like example below.

Commands:

> - pip install selenium
> - pip install webdriver-manager

Examaple:

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Setting options.
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option('excludeSwitches', ['enable-logging'])

# Instantiating the driver.
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options)

# Loading a website
driver.get("https://www.w3schools.com/")
```

---

> ## Getting the source code

Commands:

> - driver.page_source

Examaple:

```python
# Loading a website
driver.get("https://www.w3schools.com/")

# Getting the page source
print(driver.page_source)
```

---

> ## Getting elements

Required packages:

> - from selenium.webdriver.common.by import By

Commands:

> - element = driver.find_element(By.\<type>, "value")
> - all_elements = driver.find_elements(By.\<type>, "value")

Examaple:

```python
from selenium.webdriver.common.by import By

# Getting an element by Id
main_search_box = driver.find_element(By.ID, "search2")

# Getting an element by css Selector
main_search_box = driver.find_element(By.CSS_SELECTOR, "input#search2")

# Getting an element by link text
video_link = driver.find_element(By.LINK_TEXT, "Not Sure Where To Begin?")

# Getting elements by class name.
all_buttons = driver.find_elements(By.CLASS_NAME, "w3-button")
print(f"{len(all_buttons)} buttons found")

# Getting and elemet by X-Path
about_us = driver.find_element(By.XPATH, '//*[@id="main"]/footer/p')
```

---

> ## Getting element's attributes

Commands:

> - value = element.get_attribute("\<value>")

Example:

```python
# Getting href attribute of a link
help_href = element("href")
print(f'href = {help_href}')

# Getting onkeydown attribute of an element
on_key_down_value = element.get_attribute("onkeydown")

# Getting html of and element
html = element.get_attribute("innerHTML")
```

---

> ## Wait for element to load

Example:

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div#toc"))
    )
except:
    print("Could not find the element.")
else:
    print(element.text)

```

---

> ## Back and forward in browser

Example:

```python
driver.back()
driver.forward()
```

---

> ## Sending keys to browser

required packages:

> - from selenium.webdriver.common.keys import Keys

Example:

```python
# Sending text to an element
element.send_keys("Python")

# Sending enter (return) to an element.
element.send_keys(Keys.RETURN)

# Sending click
element = driver.find_element(By.LINK_TEXT, "Python Get Started")
element.click()

```

---
