from ..core.base_client import BaseAPIClient
from typing import Dict, Any, List, Union
import json

class FunctionalUse(BaseAPIClient):
    def __init__(self, api_key: str):
        super().__init__(api_key)
    
    def get_functional_use(self, type:str, dtxsid: str, **kwargs) -> Dict[str, Any]:
        """
        #### Description: 
            Get functional use information for a given DTXSID. This function can return either the probability or the functional use information for a given DTXSID.
        
        #### Arguments:
            - type: str: The type of information to return. Must be either 'prob' or 'func'.
            - dtxsid: str: The DTXSID for which to retrieve the functional use information.
            - **kwargs: Dict: Additional arguments to pass to the request.
        
        #### Returns:
            - Dict: The response from the API.
                when type is 'prob':
                [
                    {
                    "harmonizedFunctionalUse": "string",
                    "probability": 0
                    }
                ]

                when type is 'func':
                    {
                    "id": 0,
                    "dtxsid": "AAAAAA",
                    "datatype": "AAAAAA",
                    "docid": 0,
                    "doctitle": "AAAAAA",
                    "docdate": "AAAAAA",
                    "reportedfunction": "AAAAAA",
                    "functioncategory": "AAAAAA"
                    }

        #### Example:
            ```python
            client = FunctionalUse(api_key=api_key)
            response = client.get_functional_use(type="prob", dtxsid="DTXSID7020182")
            print(response)
            ```

        """

        type = type.lower()
        if type not in ["prob", "func"]:
            raise ValueError("Type must be either 'prob' or 'func'.")
        
        if type == "prob":
            resource_id = f"exposure/functional-use/probability/search/by-dtxsid/{dtxsid}"
        elif type == "func":
            resource_id = f"exposure/functional-use/search/by-dtxsid/{dtxsid}"

        return self.get(resource_id, **kwargs)
    
class Product(BaseAPIClient):
    def __init__(self, api_key: str):
        super().__init__(api_key)

    def get_product_data(self, type:str, dtxsid: str = None, **kwargs) -> Dict[str, Any]:
        
        """
        #### Description:
            Get product data information for a given DTXSID. This function can return either the PUC or all product data information for a given DTXSID.
        
        #### Arguments:
            - type: str: The type of information to return. Must be either 'puc' or 'all'.
            - dtxsid: str: The DTXSID for which to retrieve the product data information.
            - **kwargs: Dict: Additional arguments to pass to the request.
        
        #### Returns:
            - Dict: The response from the API.
                when type is 'puc':
                    [
                    {
                    "id": 0,
                    "kindName": "AAAAAA",
                    "genCat": "AAAAAA",
                    "prodfam": "AAAAAA",
                    "prodtype": "AAAAAA",
                    "definition": "string"
                    }
                    ]
                when type is 'all':
                    {
                    "id": 0,
                    "dtxsid": "AAAAAA",
                    "docid": 0,
                    "doctitle": "AAAAAA",
                    "docdate": "AAAAAA",
                    "productname": "AAAAAA",
                    "gencat": "AAAAAA",
                    "prodfam": "AAAAAA",
                    "prodtype": "AAAAAA",
                    "classificationmethod": "AAAAAA",
                    "rawmincomp": "AAAAAA",
                    "rawmaxcomp": "AAAAAA",
                    "rawcentralcomp": "AAAAAA",
                    "unittype": "AAAAAA",
                    "lowerweightfraction": 0,
                    "upperweightfraction": 0,
                    "centralweightfraction": 0,
                    "weightfractiontype": "AAAAAA",
                    "component": "AAAAAA"
                    }

        #### Example:
            ```python
            client = Product(api_key=api_key)
            response = client.get_product_data(type="puc", dtxsid="DTXSID7020182")
            print(response)
            ```
        """
        
        type = type.lower()
        if type not in ["puc", "all"]:
            raise ValueError("Type must be either 'puc' or 'all'.")
        
        if type == "puc":
            resource_id = f"exposure/product-data/puc"
        elif type == "all":
            if dtxsid is None:
                raise ValueError("When type is 'all', dtxsid must be provided.")
            resource_id = f"exposure/product-data/search/by-dtxsid/{dtxsid}"

        return self.get(resource_id, **kwargs)
    
class Httk(BaseAPIClient):
    def __init__(self, api_key: str):
        super().__init__(api_key)

    def get_httk_data(self, dtxsid: str, **kwargs) -> Dict[str, Any]:
            
        """
        #### Description:
            Get httk data information for a given DTXSID.

        #### Arguments:
            - dtxsid: str: The DTXSID for which to retrieve the httk data information.
            - **kwargs: Dict: Additional arguments to pass to the request.
        
        #### Returns:
            {
            "id": 0,
            "dtxsid": "AAAAAA",
            "parameter": "AAAAAA",
            "measuredText": "AAAAAA",
            "measured": 0,
            "predictedText": "AAAAAA",
            "predicted": 0,
            "units": "AAAAAA",
            "model": "AAAAAA",
            "reference": "AAAAAA",
            "percentile": "AAAAA",
            "species": "AAAAAA",
            "dataSourceSpecies": "AAAAAA",
            "dataVersion": "AAAAAA",
            "importDate": "1970-01-01T00:00:00.000Z"
            }

        #### Example:
            ```python
            client = Httk(api_key=api_key)
            response = client.get_httk_data(dtxsid="DTXSID1020560")
            print(response)
            ```
        """
        resource_id = f"exposure/httk/search/by-dtxsid/{dtxsid}"

        return self.get(resource_id, **kwargs)
    
class ListPresence(BaseAPIClient):
    def __init__(self, api_key: str):
        super().__init__(api_key)
    
    def get_list_presence(self, dtxsid: str = None, **kwargs) -> Dict[str, Any]:

        """
        #### Description:
            Get list presence information for a given DTXSID. This function can return either the list presence or the list presence tags for a given DTXSID.
        
        #### Arguments:
            - dtxsid: str: The DTXSID for which to retrieve the list presence information.
                           If no dtxsid is provided, the function will return the list presence tags.
            - **kwargs: Dict: Additional arguments to pass to the request.

        #### Returns:
            - Dict: The response from the API.
                when dtxsid is None:
                    [
                    {
                    "id": 0,
                    "tagName": "AAAAAA",
                    "tagDefinition": "AAAAAA",
                    "kindName": "AAAAAA"
                    }
                    ]
                when dtxsid is not None:
                    {
                    "id": 0,
                    "dtxsid": "string",
                    "docid": 0,
                    "doctitle": "AAAAAA",
                    "docsubtitle": "AAAAAA",
                    "docdate": "AAAAAA",
                    "organization": "AAAAAA",
                    "reportedfunction": "AAAAAA",
                    "functioncategory": "AAAAAA",
                    "component": "AAAAAA",
                    "keywordset": "string"
                    }

        #### Example:
            ```python
            client = ListPresence(api_key=api_key)
            response = client.get_list_presence(dtxsid="DTXSID1020560")
            response = client.get_list_presence()

        """

        if dtxsid is None:
            resource_id = f"exposure/list-presence/tags"

        else:
            resource_id = f"exposure/list-presence/search/by-dtxsid/{dtxsid}"
        
        return self.get(resource_id, **kwargs)
    
class GeneralExposure(BaseAPIClient):
    def __init__(self, api_key: str):
        super().__init__(api_key)
    
    def get_general_exposure(self, dtxsid: str, **kwargs) -> Dict[str, Any]:

        """
        #### Description:
            Get general exposure information for a given DTXSID.

        #### Arguments:
            - dtxsid: str: The DTXSID for which to retrieve the general exposure information.
            - **kwargs: Dict: Additional arguments to pass to the request.

        #### Returns:
            {
            "dtxsid": "AAAAAA",
            "productionVolume": 0,
            "units": "AAAAAA",
            "stockholmConvention": 0,
            "probabilityDietary": 0,
            "probabilityResidential": 0,
            "probabilityPesticde": 0,
            "probabilityIndustrial": 0,
            "dataVersion": "AAAAAA",
            "importDate": "1970-01-01T00:00:00.000Z"
            }

        #### Example:
            ```python
            client = GeneralExposure(api_key=api_key)
            response = client.get_general_exposure(dtxsid="DTXSID1020560")
            print(response)
            ```
        """
        resource_id = f"exposure/seem/general/search/by-dtxsid/{dtxsid}"

        return self.get(resource_id, **kwargs)
    
class DemographicExposure(BaseAPIClient):
    def __init__(self, api_key: str):
        super().__init__(api_key)
    
    def get_demographic_exposure(self, dtxsid: str, **kwargs) -> Dict[str, Any]:
    
        """
        #### Description:
            Get demographic exposure information for a given DTXSID.
        
        #### Arguments:
            - dtxsid: str: The DTXSID for which to retrieve the demographic exposure information.
            - **kwargs: Dict: Additional arguments to pass to the request.
        
        #### Returns:
            [
            {
            "id": 0,
            "dtxsid": "AAAAAA",
            "demographic": "AAAAAA",
            "predictor": "AAAAAA",
            "median": 0,
            "medianText": "AAAAAA",
            "l95": 0,
            "l95Text": "AAAAAA",
            "u95": 0,
            "u95Text": "AAAAAA",
            "units": "AAAAAA",
            "ad": 0,
            "reference": "AAAAAA",
            "dataVersion": "AAAAAA",
            "importDate": "1970-01-01T00:00:00.000Z"
            }
            ]
        
        #### Example:
            ```python
            client = DemographicExposure(api_key=api_key)
            response = client.get_demographic_exposure(dtxsid="DTXSID1020560")
            print(response)
            ```
        """

        resource_id = f"exposure/seem/demographic/search/by-dtxsid/{dtxsid}"

        return self.get(resource_id, **kwargs)




        