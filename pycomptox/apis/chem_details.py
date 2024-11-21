from ..core.base_client import BaseAPIClient
from typing import Dict, Any

class ChemDetails(BaseAPIClient):
    """
    Client for API1.
    """
    def get_resource(self, resource_id: str, query_params: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Fetch a specific resource.
        """
        if query_params is None:
            query_params = {}
        
#        if "top" in query_params:
#            query_params["top"] = int(query_params["top"])

        return self.get(f"{resource_id}", params=query_params)
