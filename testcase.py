from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path='path/to/chromedriver')
driver.get("https://www.google.com")
search_box = driver.find_element("name", "q")
search_box.send_keys("DevOps")
search_box.send_keys(Keys.RETURN)
print(driver.title)
driver.quit()