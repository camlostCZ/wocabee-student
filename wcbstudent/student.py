"""
Implementation of the Student class
The class provides all necessary functionality to do automated
vocabulary practice.
"""

import os
import random
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import *
from browser import init_browser
from vocabulary import Vocabulary


class Student:
    def __init__(self) -> None:
        self.browser = init_browser(PATH_BROWSER, headless=False)
        self.vocabulary = Vocabulary(PATH_VOCABULARY)


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
            answer = self.vocabulary.translate(question)
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


    def run(self):
        self.do_login()
        time.sleep(2)
        self.do_select_class()
        time.sleep(2)
        self.do_choose_practice()
        time.sleep(2)
        self.do_practice(NUM_ANSWERS)
        time.sleep(2)
        self.do_save_and_exit()
        time.sleep(5)   # Wait to let the user read the results
