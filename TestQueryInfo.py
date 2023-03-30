import requests
import unittest
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

# Define a test case class
class TestQueryInfo(unittest.TestCase):
    
    # Set up for each test case
    def setUp(self):
        # Define the API URL to be tested
        self.api_url = "https://api.tmsandbox.co.nz/v1/Categories/6327/Details.json?catalogue=false"

        # Get the response from the API
        logging.info("Test cases setUp: get the response of the tested API")
        self.res_json = requests.get(self.api_url).json()

    # Test that the name matches the expected value
    def test_name(self):
        logging.info("Running Name test...")
        expectedName = "Carbon credits"
        actualName = self.res_json['Name']

        # Assert that the actual name matches the expected name
        self.assertEqual(actualName, expectedName)
        logging.info("Name test passed")

    # Test that CanRelist is True
    def test_canRelist(self):
        logging.info("Running CanRelist  test...")
        canRelist = self.res_json['CanRelist']

        # Assert that CanRelist is True
        self.assertTrue(canRelist)
        logging.info("CanRelist  test passed")

    # Test that the description of the Gallery promotion contains the expected content
    def test_promotionsGalleryDescription(self):
        logging.info("Running Promotions Gallery Description test...")
        expectedContent = "Good position in category"
        promotions = self.res_json['Promotions']
        promotionGallery = next((p for p in promotions if p['Name'] == 'Gallery'), None)

        # Assert that the Gallery promotion exists
        self.assertIsNotNone(promotionGallery)
        
        actualContent = promotionGallery['Description']
        # Assert that the description of the Gallery promotion contains the expected content
        self.assertIn(expectedContent, actualContent)
        logging.info("Promotions Gallery Description test passed")
