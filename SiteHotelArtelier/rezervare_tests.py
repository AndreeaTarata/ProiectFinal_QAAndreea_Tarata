import time
import unittest

from selenium import webdriver
from SiteHotelArtelier import locators


class TestArtelierRezervare(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('https://arteliervamaveche.ro/')
        self.driver.maximize_window()
        time.sleep(3)

# se verifica daca numarul de camere afisate este 4
    def test2_rezerva_room_with_balcony(self):
        self.driver.find_element(*locators.REZERVA_ACUM).click()
        time.sleep(1)
        camere = len(self.driver.find_elements(*locators.IMAGINI))
        assert camere == 4

# se verifica daca textul "Rezervarea mea este afisat"
    def test3_rezervarea_mea_is_dispayed(self):
        self.driver.find_element(*locators.REZERVA_ACUM).click()
        time.sleep(1)
        rezervare = self.driver.find_element(*locators.REZERVAREA_MEA).text
        text_rezervare = 'Rezervarea mea'
        self.assertTrue(rezervare, text_rezervare)

# negativ testing. Se verifica functionalitatea codului promotional cand nu este introdusa nicio valoare
    def test6_cod_promotional_gol(self):
        self.driver.find_element(*locators.REZERVA_ACUM).click()
        time.sleep(1)
        self.driver.find_element(*locators.COD_PROMOTIONAL_BTN).click()
        cod_gol = self.driver.find_element(*locators.COD_PROMO_ERROR).text
        self.assertEqual(cod_gol, 'Codul promotional nu a fost gasit!', 'Campul este obligatoriu')

# se verifica functionalitatea login cand se introduc nr de rezervare si parola false
    def test7_autentificare_falsa(self):
        self.driver.find_element(*locators.REZERVA_ACUM).click()
        time.sleep(1)
        self.driver.find_element(*locators.AUTENTIFICARE).click()
        self.driver.find_element(*locators.NR_REZERVARE).send_keys('1')
        self.driver.find_element(*locators.PAROLA).send_keys('1')
        self.driver.find_element(*locators.IDENTIFICA).click()
        text_eroare_aut = self.driver.find_element(*locators.TEXT_AUTENT).text
        self.assertTrue(text_eroare_aut, 'Rezervarea nu a fost identificata.')

# se verifica ca linkul pe care suntem este acelasi cu cel pe care trebuie sa fim cand accesam "Rezerva acum"
    def test8_check_booking_link(self):
        self.driver.find_element(*locators.REZERVA_ACUM).click()
        time.sleep(3)
        expected_url = "https://artelier.pynbooking.direct/"
        actual_url = self.driver.current_url
        self.assertEqual(expected_url, actual_url, f'Expected URL: {expected_url}, Actual URL: {actual_url}')

# itereaza prin valorile de la limbi pentru a verifica daca sunt toate afisate asa cum este cerut
    def test9_iteratie_selectare_limba(self):
        self.driver.find_element(*locators.REZERVA_ACUM).click()
        time.sleep(3)
        limbi_existente = self.driver.find_elements(*locators.LIMBI_DISPONIBILE)
        for limba in limbi_existente:
            limba.click()
            limba_selectata = self.driver.find_element(*locators.LIMBA_DISPONILE).get_attribute()
            self.assertIn(limba_selectata, ["ro", "en", "fr", "de", "it"])

    def tearDown(self) -> None:
        self.driver.quit()
