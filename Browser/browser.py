from selenium import webdriver
from selenium.webdriver.common.by import By
import pyperclip
import pyautogui
import time

class browser_class:


    driver = None


    def start_web_browser(self, link):

        if browser_class.driver is None:
            browser_class.driver = webdriver.Edge()
            browser_class.driver.maximize_window()

        browser_class.driver.get(link)


    def wait_for_id(self, id, time_to_wait=0):

        time.sleep(time_to_wait)
        try:
            browser_class.driver.find_element(By.ID, id).click()
        except:
            return -1
        

    def wait_for_class_name(self, class_name, time_to_wait=0):

        time.sleep(time_to_wait)
        try:
            browser_class.driver.find_element(By.CLASS_NAME, class_name).click()
        except:
            return -1
        

    def keyboard(self, keys_to_press, time_to_wait=1):

        # Split the keys based on space
        keys = keys_to_press.split()

        for key in keys:
            pyautogui.press(key)  # Press the key
            time.sleep(time_to_wait)  # Wait for the specified time


    def copy_paste(self, text):

        pyperclip.copy(text)
        pyautogui.hotkey('ctrl', 'v')
        pyperclip.copy('')

        