from ..utils.exceptions import APIRequestError
import requests
from typing import Dict, Any
from .config import Config

conf = Config(api_key="my_api_key", base_url="https://api-ccte.epa.gov")

class BaseAPIClient:
    """
    Base client for interacting with HTTP APIs.
    """
    def __init__(self, api_key: str):
        self.base_url = conf.base_url
        self.api_key = api_key

    def _request(self, method: str, url: str, headers: Dict[str, str] = None, **kwargs) -> Dict[str, Any]:
        """
        Helper function to send an HTTP request.

        :param method: The HTTP method (e.g., 'GET', 'POST', 'PUT', etc.)
        :param url: The full URL to make the request to (relative to base_url)
        :param headers: Additional headers to send with the request
        :param kwargs: Additional arguments like params, data, or json.
        :return: The response as a dictionary.
        """
        

        if headers is None:
            headers = {}
        headers["x-api-key"] = self.api_key

        # Determine the request body
        body = kwargs.get("body", None)
        if body is not None:
            if isinstance(body, dict):
                headers["Content-Type"] = "application/json"
                json_body = body
                data=None
            else:
                json_body = None
                data = body
        else:
            json_body = None
            data = None

        headers["Content-Type"] = "application/json"

        try:
            response = requests.request(method, url, headers=headers, json=json_body, data=data, **kwargs)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise APIRequestError(f"Error during {method} request to {url}: {str(e)}")

    def get(self, endpoint: str, headers: Dict[str, str] = None, params: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Make a GET request to the given endpoint with optional query parameters.

        :param endpoint: The endpoint (e.g., '/data/resource')
        :param headers: Optional headers for the request
        :param params: Optional query parameters for the GET request
        :param kwargs: Additional arguments to pass to the request
        :return: The JSON response from the API.
        """
        url = f"{self.base_url}/{endpoint.strip('/')}"
        return self._request("GET", url, headers=headers, params=params)

    def post(self, endpoint: str, headers: Dict[str, str] = None, data: Dict[str, Any] = None) -> Dict[str, Any]:
        return self._request("POST", endpoint, headers=headers, json=data)

    def put(self, endpoint: str, headers: Dict[str, str] = None, data: Dict[str, Any] = None) -> Dict[str, Any]:
        return self._request("PUT", endpoint, headers=headers, json=data)
