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