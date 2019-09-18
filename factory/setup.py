#!/usr/bin/python

from selenium import webdriver

class Setup:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def get_driver(self):
        if self.driver is None:
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(15)
            return self.driver
        else:
            self.driver.implicitly_wait(15)
            return self.driver

    def teardown(self):
        self.driver.quit()
