from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.chrome.options import Options

import pyautogui

PATH = "C:\chromedriver.exe"


option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 2
})

driver = webdriver.Chrome(chrome_options=option, executable_path=PATH)
driver.get('http://facebook.com/messages/t/2232825190101619')

elem = driver.find_element_by_name('email')  # Find the search box
elem.send_keys('likweitan@hotmail.com')

elem = driver.find_element_by_name('pass')  # Find the search box
elem.send_keys('yj321998' + Keys.RETURN)

driver.implicitly_wait(10)

element = driver.find_element_by_xpath(
    ".//*[contains(text(), 'Customise chat')]")
driver.execute_script("arguments[0].click();", element)

driver.implicitly_wait(10)

# element = driver.find_element_by_xpath(
#    ".//*[contains(text(), 'Change Photo')]")
try:
    element = driver.find_element_by_xpath(
        "//*[@id='mount_0_0']/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[2]/div/div[1]/div/div/div[2]/div/div[3]/div/div[1]/div[2]/div/div/div/div/span/span")
    webdriver.ActionChains(driver).move_to_element(
        element).click(element).perform()
finally:
    pyautogui.PAUSE = 2.5
    pyautogui.press('esc')
    pyautogui.hotkey('ctrl', 'l')
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.write('D:/Pictures/108APPLE/', interval=0.1)
    pyautogui.press('enter')
    pyautogui.PAUSE = 1
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.write('IMG_8386.JPG', interval=0.1)
    pyautogui.press('enter')
# driver.implicitly_wait(10)
# element.send_keys("D:/Pictures/108APPLE/IMG_8386.JPG")
# a = driver.execute_script(
#    "arguments[0].send_keys = 'D:/Pictures/108APPLE/IMG_8386.JPG'", element)
# webdriver.ActionChains(driver).move_to_element(
#    element).click(element).perform()
# print(a)
