
# Built-in Libs
import time

# 3er Party Libs
from selenium import webdriver
from selenium.webdriver.common.by import By


drv = webdriver.Firefox()
drv.implicitly_wait(3)
#drv.get("https://prenotami.esteri.it/Home?ReturnUrl=%2fServices")
drv.get("https://prenotami.esteri.it/")
drv.maximize_window()

email = drv.find_element(By.ID, "login-email")
email.send_keys('ramiroluis2k12@gmail.com')

pwd = drv.find_element(By.ID, "login-password")
pwd.send_keys('Secretariacell1983')

drv.find_element(By.XPATH, value='//button[@data-sitekey="6LdSmG4cAAAAAOarRxGIhehvv4sPgVeF-vRi-Jqb"]').click()

drv.find_element(By.XPATH, value='//span[text()="Prenota"]').click()

drv.find_element(By.XPATH, value='//a[@href="/Services/Booking/791"]').click()