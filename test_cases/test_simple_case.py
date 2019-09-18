#!/usr/bin/python

import unittest
from actions.navigations import Navigations
from page_objects.main_page_po import MainPagePO
from factory.setup import Setup

class TestSimpleClass(unittest.TestCase):
    def test_first(self):
        try:
            self.driver = Setup().get_driver()
            navigations = Navigations(self.driver)
            main_page = MainPagePO(self.driver)
            navigations.acessar_tela_inicial()
            self.assertTrue(main_page.get_logo_image().is_displayed(), "Logo não mostrado!")
        except Exception as e:
            print(e)
            self.assertTrue(False, "DAMN HELL!")
        finally:
            self.driver.quit()
