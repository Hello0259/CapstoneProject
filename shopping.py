import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
s = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("http://automationpractice.com/index.php?controller=authentication&back=my-account")
driver.find_element(By.ID, 'email').send_keys("erborleo@gmail.com")
driver.find_element(By.ID, 'passwd').send_keys("12345")
driver.find_element(By.XPATH, '//*[@id="SubmitLogin"]/span').click()
driver.find_element(By.XPATH, '//*[@id="header_logo"]/a/img').click()
driver.find_element(By.XPATH, '//*[@id="add_to_cart"]/button').click()
time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="layer_cart"]/div[1]/div[2]/div[4]/a/span').click()
time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="center_column"]/p[2]/a[1]/span').click()
time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="center_column"]/form/p/button/span').click()
driver.find_element(By.XPATH, '<input type="checkbox" name="cgv" id="cgv" value="1">').click()
driver.find_element(By.XPATH, '//*[@id="form"]/p/button/span').click()
time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="HOOK_PAYMENT"]/div[1]/div/p/a').click()
driver.find_element(By.XPATH, '//*[@id="cart_navigation"]/button/span').click()
