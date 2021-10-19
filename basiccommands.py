from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Chrome

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")

driver.get("http://demo.automationtesting.in/Windows.html")

print(driver.title)
print(driver.current_url)
driver.find_element_by_name()

