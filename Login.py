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
