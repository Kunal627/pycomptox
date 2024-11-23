from ..core.base_client import BaseAPIClient
from typing import Dict, Any, Union

class BioActivityAssay(BaseAPIClient):

    def __init__(self, api_key: str):
        super().__init__(api_key)

    def get_assay(self, aeid: int = None, **kwargs) -> Dict[str, Any]:

        """
        #### Description:
            Get bioactivity assay data by AEID.
        
        #### Parameters:
            - aeid: int
                - The AEID of the assay. If not provided, all assays will be returned.
            - kwargs: Dict
                - Additional keyword arguments.
            
        #### Returns:
            - Dict[str, Any]
                - The response data
                All assay 
                    [
                        { },
                        ]
                
                by aeid 
                    { },
        
        #### Example:
            ```python
            client = BioActivityAssay(api_key=api_key)
            response = client.get_assay(aeid=1)
            response = client.get_assay()
        """

        if aeid is None:
            resource_id = f"bioactivity/assay/"
        else:
            resource_id = f"bioactivity/assay/search/by-aeid/{aeid}"

        return self.get(resource_id, **kwargs)
    
class BioActivityData(BaseAPIClient):
    
    def __init__(self, api_key: str):
        super().__init__(api_key)

    def get_data(self, search_by: str, search_for: Union[int, str], **kwargs) -> Dict[str, Any]:

        """
        #### Description:
            Get bioactivity data by SPID, M4ID, DTXSID, or AEID.

        #### Arguments:
            - search_by: str
                - The search parameter. Must be one of 'spid', 'm4id', 'dtxsid', 'aeid'.
            - search_for: Union[int, str]
                - The value to search for.
            - kwargs: Dict
                - Additional keyword arguments.
        
        #### Returns:
            - Dict[str, Any]
                [
                    { },
                    ]

        #### Example:
            ```python
            client = BioActivityData(api_key=api_key)
            response = client.get_data(search_by="spid", search_for="spid")
            response = client.get_data(search_by="m4id", search_for=392006)
            response = client.get_data(search_by="dtxsid", search_for="DTXSID0021125")
            response = client.get_data(search_by="aeid", search_for=1386)

        """
    
        search_by = search_by.lower()

        if search_by not in ["spid", "m4id", "dtxsid", "aeid"]:
            raise ValueError("search by must be one of 'spid', 'm4id', 'dtxsid', 'aeid'")
        
        if search_by == "spid":
            if not isinstance(search_for, str):
                raise ValueError("spid must be a string")
            resource_id = f"bioactivity/data/search/by-spid/{search_for}"
        
        elif search_by == "m4id":
            if not isinstance(search_for, int):
                raise ValueError("m4id must be a integer")
            resource_id = f"bioactivity/data/search/by-m4id/{search_for}"

        elif search_by == "dtxsid":
            if not isinstance(search_for, str):
                raise ValueError("dtxsid must be a string")
            resource_id = f"bioactivity/data/search/by-dtxsid/{search_for}"

        elif search_by == "aeid":
            if not isinstance(search_for, int):
                raise ValueError("aeid must be a integer")
            resource_id = f"bioactivity/data/search/by-aeid/{search_for}"

        
        return self.get(resource_id, **kwargs)


    def get_summary_by_aeid(self, aeid: int, **kwargs) -> Dict[str, Any]:

        """
        #### Description:
            Get bioactivity data summary by AEID.
        
        #### Parameters:
            - aeid: int
                - The AEID of the assay.
            - kwargs: Dict
                - Additional keyword arguments.
            
        #### Returns:
            - Dict[str, Any]
                - The response data
                {
                "aeid": 0,
                "activeMc": 0,
                "totalMc": 0,
                "activeSc": 0,
                "totalSc": 0
                }
        
        #### Example:
            ```python
            client = BioActivityData(api_key=api_key)
            response = client.get_summary_by_aeid(aeid=1386)
        """

        resource_id = f"bioactivity/data/summary/search/by-aeid/{aeid}"
        return self.get(resource_id, **kwargs)