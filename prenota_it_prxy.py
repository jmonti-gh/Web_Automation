
# Built-in Libs
import time
from threading import Thread

# 3er Party Libs
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui

prxy = "172.16.1.49"
port = "3128"
prxy_usr = "jorge.monti"
prxy_pwd = "jorgemonti2009"

chrome_options = Options()
#chrome_options.add_argument('--proxy-server={}'.format(hostname + ":" + port))
chrome_options.add_argument(f'--proxy-server={prxy}:{port}')
drv = webdriver.Chrome(options=chrome_options)


def enter_proxy_auth(proxy_username, proxy_password):
    time.sleep(1)
    pyautogui.typewrite(proxy_username)
    pyautogui.press('tab')
    pyautogui.typewrite(proxy_password)
    pyautogui.press('enter')

def open_a_page(drv, url):
    drv.get(url)


Thread(target=open_a_page, args=(drv, "https://prenotami.esteri.it/")).start()
Thread(target=enter_proxy_auth, args=(prxy_usr, prxy_pwd)).start()


drv.implicitly_wait(3)
drv.maximize_window()

email = drv.find_element(By.ID, "login-email")
email.send_keys('ramiroluis2k12@gmail.com')

pwd = drv.find_element(By.ID, "login-password")
pwd.send_keys('Secretariacell1983')

drv.find_element(By.XPATH, value='//button[@data-sitekey="6LdSmG4cAAAAAOarRxGIhehvv4sPgVeF-vRi-Jqb"]').click()

drv.find_element(By.XPATH, value='//span[text()="Prenota"]').click()

drv.find_element(By.XPATH, value='//a[@href="/Services/Booking/791"]').click()