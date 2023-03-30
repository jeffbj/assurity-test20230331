import requests
import unittest
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')


class TestQueryInfo(unittest.TestCase):
    def setUp(self):
        self.api_url = "https://api.tmsandbox.co.nz/v1/Categories/6327/Details.json?catalogue=false"

        logging.info("Test cases setUp: get the response of the tested API")
        self.res_json = requests.get(self.api_url).json()

    def test_name(self):
        logging.info("Running Name test...")
        expectedName = "Carbon credits"
        actualName = self.res_json['Name']

        self.assertEqual(actualName, expectedName)
        logging.info("Name test passed")

    def test_canRelist(self):
        logging.info("Running CanRelist  test...")
        canRelist = self.res_json['CanRelist']

        self.assertTrue(canRelist)
        logging.info("CanRelist  test passed")

    def test_promotionsGalleryDescription(self):
        logging.info("Running Promotions Gallery Description test...")
        expectedContent = "Good position in category"
        promotions = self.res_json['Promotions']
        promotionGallery = next((p for p in promotions if p['Name'] == 'Gallery'), None)

        self.assertIsNotNone(promotionGallery)
        actualContent = promotionGallery['Description']
        self.assertIn(expectedContent, actualContent)
        logging.info("Promotions Gallery Description test passed")
