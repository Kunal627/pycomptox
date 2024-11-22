from ..core.base_client import BaseAPIClient
from typing import Dict, Any, List
import json

class ChemSearch(BaseAPIClient):
    """
    #### Description: 
         Client for Chemical search. This client provides methods to search chemicals based on various parameters.
    """

    def __init__(self, api_key: str):
        super().__init__(api_key)

    """
    #### GET Methods
    """
    def starts_with(self, word: str, query_params: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        #### Description:
            Fetch chemical which starts with the search word.

        #### path parameter:
            - word: DTXCID, DTXSID , CAS number, Inchl (starting 13 characters), URLencoded chemical name(starting characters).

        #### Query Parameters:
            - top: Int32  -> Number of records to return.

        #### Output Schema:
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
        
        #### Example:
            client = ChemSearch(api_key=api_key)
            response = client.starts_with(word="95-16-9", query_params={"top": 10})
        """
        if query_params is None:
            query_params = {}
        
        resource_id = f"chemical/search/start-with/{word}"
        
        return self.get(f"{resource_id}", params=query_params)

    def equal(self, word: str, query_params: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        #### Description:
             Fetch chemical exact match.

        #### path parameter:        
             word: DTXCID, DTXSID, CAS number, Inchl, or URLencoded chemical name(including synonyms).

        #### Query Parameters:
            - top: Int32  -> Number of records to return.

        #### Output Schema:
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

        #### Example:
            client = ChemSearch(api_key=api_key)
            response = client.equal(word="95-16-9", query_params={"top": 10})
        """
        if query_params is None:
            query_params = {}
        
        resource_id = f"chemical/search/equal/{word}"
        
        return self.get(f"{resource_id}", params=query_params)   
    
    def contain(self, word: str, query_params: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        #### Description:
             Substring of search word.
        
        #### path parameter:
            - word: Exact match of DTXSID, Substring match of DTXCID , Substr CAS number, Substr InChlKey Substr URLencoded chemical name(including synonyms).

        #### Query Parameters:
            - top: Int32  -> Number of records to return.
            - projection: String  -> Default: chemicalsearchall

        #### Output Schema:
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

        #### Example:
            client = ChemSearch(api_key=api_key)
            response = client.contain(word="95-16", query_params={"top": 10})
        """
        if query_params is None:
            query_params = {}
        
        resource_id = f"chemical/search/contain/{word}"
        
        return self.get(f"{resource_id}", params=query_params)  

    def by_mass(self, range: List[float], query_params: Dict[str, Any] = None) -> Dict[str, Any]:
            """
            #### Description:
                Search ms ready chemical using mass range .

            #### path parameter:
                range: It's a range of mass with two values separated by a comma. e.g. 200.9,200.95 (start mass, end mass)

            #### Query Parameters:
                 None

            #### Output Schema:
                [
                    "string"
                ]

            #### Example:
                client = ChemSearch(api_key=api_key)
                response = client.by_mass(range=[200.9, 200.95], query_params={})
            """
            if query_params is None:
                query_params = {}

            resource_id = f"chemical/msready/search/by-mass/{range[0]}/{range[1]}"

            return self.get(f"{resource_id}", params=query_params)  
    
    def by_formula(self, formula: str, query_params: Dict[str, Any] = None) -> Dict[str, Any]:
            """
            #### Description:
                Search ms ready chemicals by formula.

            #### path parameter:
                formula: formula string

            #### Query Parameters:
                - None

            #### Output Schema:
                [
                    "string"
                ]

            #### Example:
                client = ChemSearch(api_key=api_key)
                response = client.by_formula(formula="C16H24N2O5S", query_params
            """
            if query_params is None:
                query_params = {}

            resource_id = f"chemical/msready/search/by-formula/{formula}"

            return self.get(f"{resource_id}", params=query_params)  
    
    def by_dtxcid(self, dtxcid: str, query_params: Dict[str, Any] = None) -> Dict[str, Any]:
            """
            #### Description:
                Search ms ready chemicals by formula.

            #### path parameter:
                dtxcid: DSSTox Compound Identifier

            #### Query Parameters:
                - None

            #### Output Schema:
                [
                    "string"
                ]

            #### Example:
                client = ChemSearch(api_key=api_key)
                response = client.by_dtxcid(dtxcid="DTXCID30182", query_params={})
            """
            if query_params is None:
                query_params = {}

            resource_id = f"chemical/msready/search/by-dtxcid/{dtxcid}"

            return self.get(f"{resource_id}", params=query_params)  
    
    def by_batch(self, data_list: List[str], query_params: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        #### Description:
            note : Search batch of values (values are separated by EOL character and maximum 200 values are allowed).

        #### path parameter:
            - None

        #### Query Parameters:
            - None

        #### Output Schema:
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
        
        #### Example:
            client = ChemSearch(api_key=api_key)
            response = client.by_batch(data_list=["DTXCID30182", "DTXCID30182"], query_params={
        """
        kwargs = {}
        kwargs["data"] = '\n'.join(data_list)

        headers = {}
        headers["Content-Type"] = "text/plain"

        #print(req_body)
        if query_params is None:
            query_params = {}

        resource_id = f"chemical/search/equal/"

        return self.post(resource_id, headers=headers, **kwargs)
    
    def by_mass_batch(self, data_list: List[str], query_params: Dict[str, Any] = None) -> Dict[str, Any]:
        # TO be implemented
        kwargs = {}

        return self.post("resource_id", headers="headers", **kwargs)
    

class ChemFate(BaseAPIClient):

    """
    #### Description: 
         Client for Chemical Fate search. This client provides methods to search chemicals batch of DTXIDS and single DTXID.
    """
     
    def __init__(self, api_key: str):
        super().__init__(api_key)

    def get_dtxids_batch(self, data_list: List[str], query_params: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        ####  Description:
            Fetch fate data for a batch of DTXSIDs . Maximum 1000 DTXSIDs are allowed in a single request.

        #### path parameter:
            - None

        #### Query Parameters:
            - None

        #### request body:
            ["string"]

        #### Output Schema:
        {
            "id": 0,
            "valueType": "string",
            "dtxsid": "string",
            "dtxcid": "string",
            "unit": "string",
            "resultValue": 0,
            "modelSource": "string",
            "endpointName": "string",
            "description": "string",
            "minValue": 0,
            "maxValue": 0
        }

        #### Example:
            client = ChemFate(api_key=api_key)
            response = client.get_dtxids_batch(data_list=["DTXSID7020182"], query_params={})
        """
        kwargs = {}
        kwargs["json"] = data_list

        headers = {}
        headers["Content-Type"] = "application/json"

        #print(req_body)
        if query_params is None:
            query_params = {}

        resource_id = f"chemical/fate/search/by-dtxsid/"

        return self.post(resource_id, headers=headers, **kwargs)
    
    def by_dtxsid(self, dtxsid: str, query_params: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        ####  Description:
                Fetch fate data for a DTXSID.

        #### path parameter:
                dtxsid: DTXSID

        #### Query Parameters:
                - None

        #### Output Schema:
            [
            {
                "id": 0,
                "valueType": "string",
                "dtxsid": "string",
                "dtxcid": "string",
                "unit": "string",
                "resultValue": 0,
                "modelSource": "string",
                "endpointName": "string",
                "description": "string",
                "minValue": 0,
                "maxValue": 0
            }
            ]
        
        #### Example:
            client = ChemFate(api_key=api_key)
            response = client.by_dtxsid(dtxsid="DTXSID7020182")
        """
        if query_params is None:
            query_params = {}
        
        resource_id = f"chemical/fate/search/by-dtxsid/{dtxsid}"
        
        return self.get(f"{resource_id}", params=query_params)
    