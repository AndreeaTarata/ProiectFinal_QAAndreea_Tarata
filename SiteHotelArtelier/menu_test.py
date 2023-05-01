import unittest
from selenium import webdriver
from selenium.webdriver import Keys
import time
from SiteHotelArtelier import locators


class TestArtelierMenu(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('https://arteliervamaveche.ro/')
        self.driver.maximize_window()
        time.sleep(2)

    # se verifica toate elementele din meniu. Codul face click pe fiecare in parte si se intoarce inapoi la homepage.

    def test1_menu(self):
        self.driver.find_element(*locators.REZERVA_ACUM).click()
        self.driver.find_element(*locators.HOME_REZERVA).click()
        self.driver.find_element(*locators.MENIU_RESTAURANT).click()
        self.driver.find_element(*locators.LOGO).click()
        self.driver.find_element(*locators.GALERIE_FOTO).click()
        self.driver.find_element(*locators.LOGO).click()
        self.driver.find_element(*locators.DESPRE_NOI).click()
        self.driver.find_element(*locators.LOGO).send_keys(Keys.CONTROL + Keys.HOME)
        self.driver.find_element(*locators.CONTACT).click()
        # time.sleep(3)
        self.driver.find_element(*locators.CONTACT).send_keys(Keys.CONTROL + Keys.HOME)
        expected_url = "https://arteliervamaveche.ro/#contact"
        actual_url = self.driver.current_url
        self.assertTrue(expected_url, actual_url)

    def tearDown(self) -> None:
        self.driver.quit()
