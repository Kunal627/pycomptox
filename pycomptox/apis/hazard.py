from ..core.base_client import BaseAPIClient
from typing import Dict, Any, List, Union
import json

class Hazard(BaseAPIClient):
   
    def __init__(self, api_key: str):
      super().__init__(api_key)

    def get_hazard(self, type: str, dtxsid:str, **kwargs) -> Dict[str, Any]:
        """
        #### Description:
            Fetch hazard information for a specific chemical.

        #### Arguments:
            - type: str
                - The type of hazard to fetch. Must be one of 'human', 'eco', or 'all'.
            - dtxsid: str
                - The DTXSID of the chemical to fetch hazard information for.
            - kwargs: Dict
                - Additional arguments to pass to the request.
        
        #### Returns:
            - Dict: The JSON response from the API.
                {
                    "id": 0,
                    "source": "string",
                    "year": "string",
                    "studyDurationValue": 0,
                    "studyDurationClass": "string",
                    "toxvalNumericQualifier": "string",
                    "studyDurationUnits": "string",
                    "riskAssessmentClass": "string",
                    "dtxsid": "string",
                    "exposureRoute": "string",
                    "toxvalNumeric": 0,
                    "subsource": "string",
                    "toxvalType": "string",
                    "toxvalSubtype": "string",
                    "toxvalUnits": "string",
                    "studyType": "string",
                    "sourceUrl": "string",
                    "subsourceUrl": "string",
                    "priorityId": 0,
                    "criticalEffect": "string",
                    "generation": "string",
                    "exposureMethod": "string",
                    "detailText": "string",
                    "population": "string",
                    "strain": "string",
                    "media": "string",
                    "sex": "string",
                    "exposureForm": "string",
                    "lifestage": "string",
                    "supercategory": "string",
                    "speciesCommon": "string",
                    "humanEcoNt": "string"
                }
            
        #### Example:
            ```python
            client = Hazard(api_key=api_key)
            response = client.get_hazard(type="eco", dtxsid="DTXSID1020560")
            print(response)
            ```
        """

        type  = type.lower()
        if type not in ["human", "eco", "all"]:
            raise ValueError("Invalid hazard type. Must be one of 'human', 'eco', or 'all'.")
        
        if type == "all":
            resource_id = f"hazard/search/by-dtxsid/{dtxsid}"
        elif type == "human":
            resource_id = f"hazard/human/search/by-dtxsid/{dtxsid}"
        elif type == "eco":
            resource_id = f"hazard/eco/search/by-dtxsid/{dtxsid}"

        return self.get(resource_id, **kwargs)

    def get_hazard_batch(self, type: str, dtxsid_list: List[str], **kwargs) -> Dict[str, Any]:

        """
        #### Description:
            Similar to get_hazard, but fetches hazard information for multiple chemicals at once. 200 chemicals at a time.
        """

        type  = type.lower()
        if type not in ["human", "eco", "all"]:
            raise ValueError("Invalid hazard type. Must be one of 'human', 'eco', or 'all'.")

        if type == "all":
            resource_id = "hazard/search/by-dtxsid/"
        elif type == "human":
            resource_id = "hazard/human/search/by-dtxsid/"
        elif type == "eco":
            resource_id = "hazard/eco/search/by-dtxsid/"

        kwargs = {}
        kwargs["json"] = dtxsid_list

        headers = {}
        headers["Content-Type"] = "application/json"

        return self.post(resource_id, **kwargs)
    
class SkinEye(BaseAPIClient):

    def __init__(self, api_key: str):
        super().__init__(api_key)

    def get_by_dtxsid(self, dtxsid: Union[str, List[str]],  **kwargs) -> Dict[str, Any]:
        """
        #### Description:
            Fetch skin and eye irritation information for a specific chemical.

        #### Arguments:
            - dtxsid: Union[str, List[str]]
                - The DTXSID of the chemical to fetch skin and eye irritation information for.
            - kwargs: Dict
                - Additional arguments to pass to the request.
        
        #### Returns:
            {
                "id": 0,
                "source": "string",
                "year": 0,
                "endpoint": "string",
                "dtxsid": "string",
                "studyType": "string",
                "strain": "string",
                "resultText": "string",
                "reliability": "string",
                "guideline": "string",
                "score": "string",
                "species": "string",
                "classification": "string"
            }

            in case of batch request:

            [
                 "string"
            ]

        #### Example:
            ```python
            client = SkinEye(api_key=api_key)
            response = client.get_by_dtxsid(dtxsid="DTXSID1020560")
            response = client.get_by_dtxsid(dtxsid=["DTXSID1020560", "DTXSID1020560"])
            ```
        """
        if isinstance(dtxsid, list):
            kwargs = {}
            kwargs["json"] = dtxsid
            headers = {}
            headers["Content-Type"] = "application/json"
            resource_id = "hazard/skin-eye/search/by-dtxsid/"
            return self.post(resource_id, **kwargs)
        
        elif isinstance(dtxsid, str):
            resource_id = f"hazard/skin-eye/search/by-dtxsid/{dtxsid}"
            return self.get(resource_id, **kwargs)
        
class Cancer(BaseAPIClient):

    def __init__(self, api_key: str):
        super().__init__(api_key)

    def get_by_dtxsid(self, dtxsid: Union[str, List[str]],  **kwargs) -> Dict[str, Any]:

        """
        #### Description:
            Fetch cancer information for a specific chemical.

        #### Arguments:
            - dtxsid: Union[str, List[str]]
                - The DTXSID of the chemical to fetch cancer information for.
            - kwargs: Dict
                - Additional arguments to pass to the request.
        
        #### Returns:
            {
                "id": 0,
                "source": "string",
                "url": "string",
                "cancerCall": "string",
                "dtxsid": "string",
                "exposureRoute": "string"
            }

            in case of batch request:

            [
                 "string"
            ]

        #### Example:
            ```python
            client = Cancer(api_key=api_key)
            response = client.get_by_dtxsid(dtxsid="DTXSID1020560")
            response = client.get_by_dtxsid(dtxsid=["DTXSID1020560", "DTXSID1020560"])
            ```
        """
        if isinstance(dtxsid, list):
            kwargs = {}
            kwargs["json"] = dtxsid
            headers = {}
            headers["Content-Type"] = "application/json"
            resource_id = "hazard/cancer-summary/search/by-dtxsid/"
            return self.post(resource_id, **kwargs)
        
        elif isinstance(dtxsid, str):
            resource_id = f"hazard/cancer-summary/search/by-dtxsid/{dtxsid}"
            return self.get(resource_id, **kwargs)
        
class Genotox(BaseAPIClient):

    def __init__(self, api_key: str):
        super().__init__(api_key)
    
    def get_summary_data(self, dtxsid:Union[str, List[str]], **kwargs) -> Dict[str, Any]:
        """
        #### Description:
            Fetch genotoxicity summary data for a specific chemical.

        #### Arguments:
            - dtxid: Union[str, List[str]]
                - The dtxsid of the chemical to fetch genotoxicity summary data for.
            - kwargs: Dict
                - Additional arguments to pass to the request.
        
        #### Returns:
            {
            "id": 0,
            "source": "string",
            "year": 0,
            "dtxsid": "string",
            "strain": "string",
            "species": "string",
            "metabolicActivation": "string",
            "assayCategory": "string",
            "assayResult": "string",
            "assayType": "string"
            }

            in case of batch request:

            [
                 "string"
            ]

        #### Example:
            ```python
            client = Genotox(api_key=api_key)
            response = client.get_summary_data(dtxsid="DTXSID1020560")
            response = client.get_summary_data(dtxsid=["DTXSID1020560", "DTXSID1020560"])
            ```
        """
        if isinstance(dtxsid, list):
            kwargs = {}
            kwargs["json"] = dtxsid
            headers = {}
            headers["Content-Type"] = "application/json"
            resource_id = "hazard/genetox/summary/search/by-dtxsid/"
            return self.post(resource_id, **kwargs)
        
        elif isinstance(dtxsid, str):
            resource_id = f"hazard/genetox/summary/search/by-dtxsid/{dtxsid}"
            return self.get(resource_id, **kwargs)
        
    def get_detail_data(self, dtxsid:Union[str, List[str]], **kwargs) -> Dict[str, Any]:
        """
        #### Description:
            Fetch genotoxicity detail data for a specific chemical.

        #### Arguments:
            - dtxid: Union[str, List[str]]
                - The dtxsid of the chemical to fetch genotoxicity detail data for.
            - kwargs: Dict
                - Additional arguments to pass to the request.
        
        #### Returns:
            {
            "id": 0,
            "source": "string",
            "year": 0,
            "dtxsid": "string",
            "strain": "string",
            "species": "string",
            "metabolicActivation": "string",
            "assayCategory": "string",
            "assayResult": "string",
            "assayType": "string",
            "url": "string"
            }

            in case of batch request:

            [
                 "string"
            ]

        #### Example:
            ```python
            client = Genotox(api_key=api_key)
            response = client.get_detail_data(dtxsid="DTXSID1020560")
            response = client.get_detail_data(dtxsid=["DTXSID1020560", "DTXSID1020560"])
            ```
        """
        if isinstance(dtxsid, list):
            kwargs = {}
            kwargs["json"] = dtxsid
            headers = {}
            headers["Content-Type"] = "application/json"
            resource_id = "hazard/genetox/details/search/by-dtxsid/"
            return self.post(resource_id, **kwargs)
        
        elif isinstance(dtxsid, str):
            resource_id = f"hazard/genetox/details/search/by-dtxsid/{dtxsid}"
            return self.get(resource_id, **kwargs)