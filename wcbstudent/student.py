"""
"""

import csv
import os
import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from msedge.selenium_tools import Edge, EdgeOptions

from config import *


class Student:
    def __init__(self) -> None:
        self.browser = Student.init_browser(PATH_BROWSER, headless=False)
        self.voc_e = {}
        self.voc_c = {}


    def do_choose_practice(self):
        xpath = '//span[@class="actionBtn btn btn-primary btn-block"]'
        for each in self.browser.find_elements_by_xpath(xpath):
            each.click()
            break


    def do_login(self):
        username = os.environ[VAR_USER]
        password = os.environ[VAR_PASS]
        self.browser.get(URL_APP)
        time.sleep(5)
        elem_user = self.browser.find_element(By.ID, "login").send_keys(username)
        elem_pass = self.browser.find_element(By.ID, "password").send_keys(password)
        self.browser.find_element(By.ID, "loginForm").submit()


    def do_practice(self, count: int):
        for _ in range(count):
            question = WebDriverWait(self.browser, 20).until(EC.visibility_of_element_located((By.ID, "q_word"))).text
            answer = self.translate(question)
            if answer == "":
                print(f"Not found: {question}")
                break
            else:
                time.sleep(len(answer) * 0.1 + random.randint(10, 30) / 10.0)
                elem_answer = self.browser.find_element(By.ID, "translateWordAnswer")
                elem_answer.send_keys(answer)
                self.browser.find_element(By.ID, "translateWordSubmitBtn").click()


    def do_save_and_exit(self):
        self.browser.find_element(By.ID, "backBtn").click()


    def do_select_class(self):
        xpath = '//button[@class="btn btn-lg btn-wocagrey btn-block"]'
        for each in self.browser.find_elements_by_xpath(xpath):
            each.click()
            break


    @staticmethod
    def init_browser(driver_path: str, headless: bool = True) -> webdriver:
        options = EdgeOptions()
        options.use_chromium = True  # Use the Chromium-based browser, not MSIE
        options.add_argument("user-data-dir=C:\\Temp")
        options.add_argument("profile-directory=Profile 1")
        if headless:
            options.add_argument('headless')
            options.add_argument('disable-gpu')
        return Edge(executable_path=driver_path, options=options)


    def load_vocabulary(self, path: str):
        with open(path, "r", encoding="utf-8", newline='') as f:
            reader = csv.DictReader(f, delimiter=';')
            for row in reader:
                self.voc_e[row["english"]] = row["czech"]
                self.voc_c[row["czech"]] = row["english"]


    def run(self):
        self.load_vocabulary(PATH_VOCABULARY)

        self.do_login()
        time.sleep(2)
        self.do_select_class()
        time.sleep(2)
        self.do_choose_practice()
        time.sleep(2)
        self.do_practice(NUM_ANSWERS)
        time.sleep(2)
        self.do_save_and_exit()
        time.sleep(5)


    def translate(self, question: str) -> str:
        result = self.voc_e.get(question, "")
        if result == "":            
            result = self.voc_c.get(question, "")
        return result 
