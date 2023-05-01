import unittest

import HtmlTestRunner

from SiteHotelArtelier.menu_test import TestArtelierMenu
from SiteHotelArtelier.review_tests import TestArtelierReview
from SiteHotelArtelier.rezervare_tests import TestArtelierRezervare


class MyTestSuites(unittest.TestCase):

# se ruleaza testele si se vor crea rapoarte
    def test_suite(self):
        smoketest = unittest.TestSuite()
        smoketest.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(TestArtelierMenu),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestArtelierRezervare),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestArtelierReview),

        ])
        runner = HtmlTestRunner.HTMLTestRunner(
            report_title='Report1', report_name='smoke Test', combine_reports=True
        )
        runner.run(smoketest)
