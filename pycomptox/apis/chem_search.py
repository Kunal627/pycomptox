from ..core.base_client import BaseAPIClient
from typing import Dict, Any

class ChemSearch(BaseAPIClient):
    """
    Client for API1.
    """
    def __init__(self, api_key: str):
        super().__init__(api_key)
        
    def starts_with(self, word: str, query_params: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Description:
        Fetch chemical which starts with.

        word: DTXCID, DTXSID , CAS number, Inchl (starting 13 characters), URLencoded chemical name(starting characters).

        Query Parameters:
        - top: Int32  -> Number of records to return.

        Output Schema:
        {
          "casrn": "string",
          "dtxsid": "string",
          "dtxcid": "string",
          "preferredName": "string",
          "hasStructureImage": 0,
          "smiles": "string",
          "isMarkush": false,
          "searchName": "string",
          "searchValue": "string",
          "rank": 0
        }
        """
        if query_params is None:
            query_params = {}
        
        resource_id = f"chemical/search/start-with/{word}"
        
        return self.get(f"{resource_id}", params=query_params)

    def equal(self, word: str, query_params: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Description:
        Fetch chemical exact match.

        path parameter:        
        word: DTXCID, DTXSID, CAS number, Inchl, or URLencoded chemical name(including synonyms).

        Query Parameters:
        - top: Int32  -> Number of records to return.

        Output Schema:
        {
          "casrn": "string",
          "dtxsid": "string",
          "dtxcid": "string",
          "preferredName": "string",
          "hasStructureImage": 0,
          "smiles": "string",
          "isMarkush": false,
          "searchName": "string",
          "searchValue": "string",
          "rank": 0
        }
        """
        if query_params is None:
            query_params = {}
        
        resource_id = f"chemical/search/equal/{word}"
        
        return self.get(f"{resource_id}", params=query_params)   
    
    def contain(self, word: str, query_params: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Description:
        Substring of search word.
        
        path parameter:
        word: Exact match of DTXSID, Substring match of DTXCID , Substr CAS number, Substr InChlKey Substr URLencoded chemical name(including synonyms).

        Query Parameters:
        - top: Int32  -> Number of records to return.
        - projection: String  -> Default: chemicalsearchall

        Output Schema:
        {
          "casrn": "string",
          "dtxsid": "string",
          "dtxcid": "string",
          "preferredName": "string",
          "hasStructureImage": 0,
          "smiles": "string",
          "isMarkush": false,
          "searchName": "string",
          "searchValue": "string",
          "rank": 0
        }
        """
        if query_params is None:
            query_params = {}
        
        resource_id = f"chemical/search/contain/{word}"
        
        return self.get(f"{resource_id}", params=query_params)  