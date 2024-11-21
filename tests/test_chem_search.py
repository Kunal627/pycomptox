import unittest
from unittest.mock import patch, MagicMock
from pycomptox.apis.chem_search import ChemSearch

class TestChemSearch(unittest.TestCase):
    def setUp(self):
        # Test setup: create instances of clients
        self.api_key = "test-api-key"
        self.client = ChemSearch(api_key=self.api_key)

    @patch("requests.request")
    def test_starts_with(self, mock_request):
        # Mock response for GET request
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"id": "123", "name": "Density", "value": 2.5}
        mock_request.return_value = mock_response

        # Call the get_property method
        property_id = "123"
        response = self.client.starts_with(word=property_id)
        print(response)

        # Assert the correct URL and method were used
        mock_request.assert_called_once_with(
            "GET",
            "https://api-ccte.epa.gov/chemical/search/start-with/123",
            headers={"x-api-key": self.api_key, "Content-Type": 'application/json'},
            json=None,
            data=None,
            params={}
        )
        # Assert the response is as expected
        self.assertEqual(response, {"id": "123", "name": "Density", "value": 2.5})