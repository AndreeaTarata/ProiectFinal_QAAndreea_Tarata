import time
import unittest

from selenium import webdriver

from SiteHotelArtelier import locators


class TestArtelierReview(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('https://arteliervamaveche.ro/')
        self.driver.maximize_window()
        time.sleep(3)

# Se verifica daca nota afisata este mai mare decat 9. Daca nu este se trimite un email la toti clientii hotelului

    def test4_nota_minima_review_alert(self):
        self.driver.find_element(*locators.REZERVA_ACUM).click()
        time.sleep(3)
        nota = float(self.driver.find_element(*locators.NOTA_REVIEW).get_attribute('innerText'))
        self.assertGreaterEqual(nota, 9, 'Email clienti pentru oferte speciale daca adauga reviewuri!')

# Daca nota din review este mai mica sau mai mare decat 9 administratorul hotelului este anuntat.

    def test5_nota_minima_review_sub9(self):
        self.driver.find_element(*locators.REZERVA_ACUM).click()
        time.sleep(3)
        nota = float(self.driver.find_element(*locators.NOTA_REVIEW).get_attribute('innerText'))
        if nota > 9:
            print("The review rating is above 9.")
        else:
            print("The review rating is not above 9.")

    def tearDown(self) -> None:
        self.driver.quit()
