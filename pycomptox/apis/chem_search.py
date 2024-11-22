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

    def get_chemical(self, op :str, word: str, **kwargs) -> Dict[str, Any]:
        """
        #### Description:
            Fetch chemical details based starting characters, exact match or substring of search word.

        #### input parameters:
            - op: Operator to search chemical. Valid values are 'start-with', 'equal', 'contain'
            - word: DTXCID, DTXSID , CAS number, Inchl (starting 13 characters), URLencoded chemical name(starting characters).

        #### Query Parameters:
            - top: Int32  -> Number of records to return.
              this will work only with 'start-with' and 'contain' operator
            - projection: String  -> Default: chemicalsearchall
              this will work only with 'equal' and 'contain' operator

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
            kawrgs = {"params": {"top": 20}}
            response = client.get_chemical(op="contain", word="95-16-9")

            kwargs = {"params": {"top": 20, "projection": "chemicalsearchall"}
            response = client.get_chemical(op="contain", word="95-16-9", **kwargs)

        """
        op = op.lower()
        if op not in ["start-with", "equal", "contain"]:
            raise ValueError("Invalid operator. Valid values are 'start-with', 'equal', 'contain'")
        if op == "start-with":
            resource_id = f"chemical/search/start-with/{word}"
        elif op == "equal":
            resource_id = f"chemical/search/equal/{word}"
        elif op == "contain":
            resource_id = f"chemical/search/contain/{word}"

        return self.get(f"{resource_id}",**kwargs)

    def ms_ready(self, op :str, word :str = None, start :float = None, end :float = None, **kwargs) -> Dict[str, Any]:

        """
        #### Description:
            Search ms ready chemicals based on mass range, formula or DTXCID.

        #### input parameters:
            - op: Operator to search ms ready chemicals. Valid values are 'mass', 'formula', 'dtxcid'
            - word: formula or DTXCID
            - start: start mass value
            - end: end mass value

        #### Output Schema:
            [
                "string"
            ]

        #### Example:
            client = ChemSearch(api_key=api_key)
            response = client.ms_ready(op="mass", start=200.9, end=200.95)
            response = client.ms_ready(op="formula", word="C16H24N2O5S")
            response = client.ms_ready(op="dtxcid", word="DTXCID30182")
        """

        op = op.lower()
        if op not in ["mass", "formula", "dtxcid"]:
            raise ValueError("Invalid operator. Valid values are 'mass', 'formula', 'dtxcid'")
        
        if op == "mass":
            if start is None or end is None:
                raise ValueError("Please provide start and end mass values")
            resource_id = f"chemical/msready/search/by-mass/{start}/{end}"

        elif op == "formula":
            if word is None:
                raise ValueError("Please provide formula")
            resource_id = f"chemical/msready/search/by-formula/{word}"

        elif op == "dtxcid":
            if word is None:
                raise ValueError("Please provide DTXCID")
            resource_id = f"chemical/msready/search/by-dtxcid/{word}"
        
        return self.get(f"{resource_id}", **kwargs)
           
    def by_batch(self, data_list: List[str], **kwargs) -> Dict[str, Any]:
        """
        #### Description:
            note : Search batch of values (values are separated by EOL character and maximum 200 values are allowed).

        #### Input Parameters:
            - data_list: List of DTXCID or DTXSID

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
            response = client.by_batch(data_list=["DTXCID30182", "DTXCID30182"])
        """
        kwargs = {}
        kwargs["data"] = '\n'.join(data_list)

        headers = {}
        headers["Content-Type"] = "text/plain"

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

    def get_dtxids_batch(self, data_list: List[str], **kwargs) -> Dict[str, Any]:
        """
        ####  Description:
            Fetch fate data for a batch of DTXSIDs . Maximum 1000 DTXSIDs are allowed in a single request.

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
    

class ChemList(BaseAPIClient):
    """
    #### Description: 
         Client for Chemical List search. This client provides methods to search chemicals based on various parameters.
    
    """

    def __init__(self, api_key: str):
        super().__init__(api_key)


    def get_list_types(self, **kwargs) -> Dict[str, Any]:
        """
        #### Description:
            Fetch list types.

        #### Output Schema:
            [
                "string"
            ]

            Some of the values : ['federal', 'international', 'other', 'state']

        #### Example:
            client = ChemList(api_key=api_key)
            response = client.get_list_types()
        """
        
        resource_id = f"chemical/list/type"
        
        return self.get(f"{resource_id}", **kwargs)
    
    def get_public_list(self, op : str,  value: str, **kwargs) -> Dict[str, Any]:
        """
        #### Description:
            Fetch public lists, based on the operator and value. The valid values for operator are "name" or "type".

        #### Input parameter:
            - value: List Name or List Type.
              e.g list types : ['federal', 'international', 'other', 'state']

        #### Query Parameters:
            - projection : enum  -> Default: chemicallistall
              Allowed: chemicallistall ┃ chemicallistwithdtxsids ┃ chemicallistname ┃ ccdchemicaldetaillists

        #### Output Schema:
            {
                "shortDescription": "string",
                "id": 0,
                "type": "string",
                "longDescription": "string",
                "visibility": "string",
                "createdAt": "1970-01-01T00:00:00.000Z",
                "chemicalCount": 0,
                "listName": "string",
                "updatedAt": "1970-01-01T00:00:00.000Z",
                "label": "string"
            }
        #### Example:
            client = ChemList(api_key=api_key)
            response = client.get_public_list(op="name", value="40CFR1164")
            kwargs = {"params": {"projection": "chemicallistwithdtxsids"}
            response = client.get_public_list(op="type", value="other", **kwargs)
        """
        if op not in ["name", "type", "dtxsid"]:
            raise ValueError("Invalid operator. Valid values are 'name', 'dtxsid', 'type'")
        
        if op == "name":
            resource_id = f"chemical/list/search/by-name/{value}"
        elif op == "type":
            resource_id = f"chemical/list/search/by-type/{value}"
        elif op == "dtxsid":
            resource_id = f"chemical/list/search/by-dtxsid/{value}"
        
        return self.get(f"{resource_id}", **kwargs)

    def get_chem_by_list(self, op:str, list: str, word:str = None, **kwargs) -> Dict[str, Any]:
        """
        #### Description:
            Fetch chemicals based on list name and search word. This works for strating characters, exact match or substring of search DTXSID.
        
        #### Input Parameters:
            - op: Operator to search chemical. Valid values are 'start-with', 'equal', 'contain'
            - list: List name
            - word: Search word (DTXSID)
              No need to provide the search word for 'listname' operator.

        #### Output Schema:
            [
                "string"
            ]
        
        #### Example:
            client = ChemList(api_key=api_key)
            response = client.get_chem_by_list(op="start-with", list="40CFR1164", word="DTXSID10")
            response = client.get_chem_by_list(op="equal", list="40CFR1164", word="DTXSID101015049")
            response = client.get_chem_by_list(op="contain", list="40CFR1164", word="1015049")
        
        """
        op = op.lower()
        if op not in ["start-with", "equal", "contain", "listname"]:
            raise ValueError("Invalid operator. Valid values are 'start-with', 'equal', 'contain'")
        
        if op == "start-with":
            resource_id = f"chemical/list/chemicals/search/start-with/{list}/{word}"
        elif op == "equal":
            resource_id = f"chemical/list/chemicals/search/equal/{list}/{word}"
        elif op == "contain":
            resource_id = f"chemical/list/chemicals/search/contain/{list}/{word}"
        elif op == "listname":
            resource_id = f"chemical/list/chemicals/search/by-listname/{list}"

        return self.get(resource_id, **kwargs)
    
    def get_all_public_lists(self, **kwargs) -> Dict[str, Any]:
        """
        #### Description:
            Fetch all public lists.

        #### Output Schema:
            [
               {
                 "id" : 819,
                 "type" : "state",
                 "label" : "WATER: Regional Monitoring Program for Water Quality in San Francisco Bay",
                 "visibility" : "PUBLIC",
                 "longDescription" : "The Regional Monitoring Program for Water Quality in San",
                 "chemicalCount" : 1084,
                 "createdAt" : "2019-11-18T09:07:36Z",
                 "updatedAt" : "2019-11-18T09:10:30Z",
                 "listName" : "SFEIWATER",
                 "shortDescription" : "Chemicals monitored in the Regional Monitoring Program for Water Quality in San Francisco Bay (RMP)"
               }
            ]

        #### Example:
            client = ChemList(api_key=api_key)
            response = client.get_all_public_lists()
        """
        resource_id = f"chemical/list/"
        
        return self.get(f"{resource_id}", **kwargs)
    

class ChemDetails(BaseAPIClient):
    """
    #### Description: 
         Client for Chemical Details search. This client provides methods to search chemicals based on dtxsid or dtxcid.
    """
    def __init__(self, api_key: str):
        super().__init__(api_key)

    def get_chemical_details(self, by :str, word: str, **kwargs) -> Dict[str, Any]:
        """
        #### Description:
            Fetch chemical details based on DTXSID or DTXCID.

        #### Input Parameters:
            - by: Operator to search chemical. Valid values are 'dtxsid', 'dtxcid'
            - word: DTXSID or DTXCID

        #### Query Parameters:
            Projection: Default: None
              Allowed: chemicaldetailstandard ┃ chemicalidentifier ┃ chemicalstructure ┃ ntatoolkit ┃ ccdchemicaldetails ┃ chemicaldetailall ┃ compact

        #### Output Schema:
            {
                "id": "string",
                "qcLevelDesc": "string",
                "qcLevel": 0,
                "pubmedCount": 0,
                "sourcesCount": 0,
                "casrn": "string",
                "activeAssays": 0,
                "percentAssays": 0,
                "pubchemCount": 0,
                "dtxsid": "string",
                "molFormula": "string",
                "compoundId": 0,
                "cpdataCount": 0,
                "dtxcid": "string",
                "preferredName": "string",
                "relatedSubstanceCount": 0,
                "wikipediaArticle": "string",
                "relatedStructureCount": 0,
                "descriptorStringTsv": "string",
                "monoisotopicMass": 0,
                "hasStructureImage": 0,
                "genericSubstanceId": 0,
                "toxcastSelect": "string",
                "isotope": 0,
                "pubchemCid": 0,
                "multicomponent": 0,
                "inchiString": "string",
                "inchikey": "string",
                "totalAssays": 0,
                "iupacName": "string",
                "smiles": "string",
                "msReadySmiles": "string",
                "qcNotes": "string",
                "qsarReadySmiles": "string",
                "pprtvLink": "string",
                "irisLink": "string",
                "isMarkush": false
            }
        
        #### Example:
            client = ChemDetails(api_key=api_key)
            response = client.get_chemical_details(by="dtxsid", word="DTXSID1020560")
            response = client.get_chemical_details(by="dtxcid", word="DTXCID505")
        """

        if by not in ["dtxsid", "dtxcid"]:
            raise ValueError("Invalid operator. Valid values are 'dtxsid', 'dtxcid'")
        
        if by == "dtxsid":
            resource_id = f"chemical/detail/search/by-dtxsid/{word}"
        elif by == "dtxcid":
            resource_id = f"chemical/detail/search/by-dtxcid/{word}"
        
        return self.get(f"{resource_id}", **kwargs)

    def get_chemical_details_batch(self, by:str, data_list: List[str], **kwargs) -> Dict[str, Any]:

        """
        #### Description:
            Fetch chemical details based on DTXSID or DTXCID in batch.

        #### Input Parameters:
            - by: Operator to search chemical. Valid values are 'dtxsid', 'dtxcid'
            - data_list: List of DTXSID or DTXCID
        
        #### Query Parameters:
            Projection: Default: None
              Allowed: chemicaldetailstandard ┃ chemicalidentifier ┃ chemicalstructure ┃ ntatoolkit ┃ ccdchemicaldetails ┃ chemicaldetailall ┃ compact

        #### Output Schema:
            [{str, Any}]
        
        #### Example:
            client = ChemDetails(api_key=api_key)
            response = client.get_chemical_details_batch(by="dtxcid", data_list=["DTXCID505", "DTXCID505"])
            response = client.get_chemical_details_batch(by="dtxsid", data_list=["DTXSID1020560", "DTXSID1020560"])
        """
        by = by.lower()
        if by not in ["dtxsid", "dtxcid"]:
            raise ValueError("Invalid operator. Valid values are 'dtxsid', 'dtxcid'")
        
        if by == "dtxsid":
            resource_id = f"chemical/detail/search/by-dtxsid/"
        elif by == "dtxcid":
            resource_id = f"chemical/detail/search/by-dtxcid/"
        
        kwargs = {}
        kwargs["json"] = data_list

        headers = {}
        headers["Content-Type"] = "application/json"

        return self.post(resource_id, headers=headers, **kwargs)
    

class GHSClassExist(BaseAPIClient):
    """
    #### Description:
        This endpoint will return Y if Pubchem has GHS Safety data otherwise it will return N.
    """

    def __init__(self, api_key: str):
        super().__init__(api_key)
    
    def if_class_exist(self, dtx_id:str, **kwargs) -> Dict[str, Any]:
        """
        #### Description:
            This endpoint will return Y if Pubchem has GHS Safety data otherwise it will return N.

        #### Input Parameters:
            - dtx: DTXSID

        #### Output Schema:
            {
            "dtxsid": "string",
            "isSafetyData": false,
            "safetyUrl": "string"
            }
        #### Example:
            client = GHSClassExist(api_key=api_key)
            response = client.if_class_exist(dtx="DTXSID1020560")
        """ 
        resource_id = f"chemical/ghslink/to-dtxsid/{dtx_id}"
        
        return self.get(f"{resource_id}", **kwargs)

    
    def if_class_exist_batch(self, dtx_id_list: List[str], **kwargs) -> Dict[str, Any]:
        """
        #### Description:
            Similar to if_class_exist but for batch of DTXSIDs.
        
        #### Input Parameters:
            - dtx_id_list: List of DTXSIDs
        
        #### Output Schema:
            [
                {
                    "dtxsid": "string",
                    "isSafetyData": false,
                    "safetyUrl": "string"
                }
            ]
        
        #### Example:
            client = GHSClassExist(api_key=api_key)
            response = client.if_class_exist_batch(dtx_id_list=["DTXSID1020560"])
        """
        kwargs = {}
        kwargs["json"] = dtx_id_list

        headers = {}
        headers["Content-Type"] = "application/json"
        resource_id = f"chemical/ghslink/to-dtxsid/" 

        return self.post(resource_id, headers=headers, **kwargs)


class SystemIUPAC(BaseAPIClient):
    """
    #### Description:
        This endpoint returns smile code, InChlKey or InChl for a chemical name.
    """

    def __init__(self, api_key: str):
        super().__init__(api_key)

    def get_iupac(self, chem_name: str, what:str, **kwargs) -> str:
        """
        #### Description:
            This endpoint returns smile code, InChlKey or InChi for a chemical name.

        #### Input Parameters:
            - chem_name: Chemical Name
            - what: Valid values are 'smiles', 'inchikey', 'inchi'

        #### Output Schema:
            "string"

        #### Example:
            client = SystemIUPAC(api_key=api_key)
            response = client.get_iupac(chem_name="acetamide", what="inchikey")
            response = client.get_iupac(chem_name="acetamide", what="inchi")
            response = client.get_iupac(chem_name="acetamide", what="smiles")

        """

        what = what.lower()
        if what not in ["smiles", "inchikey", "inchi"]:
            raise ValueError("Invalid operator. Valid values are 'smiles', 'inchikey', 'inchi'")

        if what == "smiles":
            resource_id = f"chemical/opsin/to-smiles/{chem_name}"
        elif what == "inchikey":
            resource_id = f"chemical/opsin/to-inchikey/{chem_name}"
        elif what == "inchi":
            resource_id = f"chemical/opsin/to-inchi/{chem_name}"
      
        return self.get(resource_id, **kwargs)
    

class ChemProperties(BaseAPIClient):
    """
    #### Description:
        Get Chemical properties.
    """

    def __init__(self, api_key: str):
        super().__init__(api_key)

    def get_properties(self, by: str, params: Dict[str, Any] = None , **kwargs) -> Dict[str, Any]:
        """
        #### Description:
            Get Chemical properties.

        #### Input Parameters:
            - by: Operator to search chemical. Valid values are 'propid', 'dtxsid', 'predicted', 'experimental'
            - params: Dict of parameters based on operator.

        #### Output Schema:
            When by = "dtxsid"

            [
                {
                "name": "string",
                "value": 0,
                "id": 0,
                "source": "string",
                "dtxsid": "string",
                "dtxcid": "string",
                "unit": "string",
                "propertyId": "string",
                "propType": "string",
                "description": "string"
                }
            ]

            when by = "experimental" or "predicted"
            [
                {
                "name": "string",
                "propertyId": "string",
                "propType": "string"
                }
            ]

        #### Example:
            client = ChemProperties(api_key=api_key)
            response = client.get_properties(by="dtxsid", params = {"dtxsid": "DTXSID7020182"})
            response = client.get_properties(by="propid", params={"propertyid": "density", "start": 1.311, "end": 1.313})
            response = client.get_properties(by="experimental")
            response = client.get_properties(by="predicted")
        
        """

        by = by.lower()
        if by not in ["propid", "dtxsid", "predicted", "experimental"]:
            raise ValueError("Invalid operator. Valid values are 'dtxsid', 'dtxcid', 'predicted', 'experimental'")
        
        if by == "propid":
            if not all(key in params for key in ["start", "end", "propertyid"]):
                raise ValueError("Please provide propertyid, start and end values in params")
            resource_id = f"chemical/property/search/by-range/{params['propertyid']}/{params['start']}/{params['end']}"
        
        elif by == "dtxsid":
            if "dtxsid" not in params:
                raise ValueError("Please provide dtxsid in params")
            resource_id = f"chemical/property/search/by-dtxsid/{params['dtxsid']}"

        elif by == "experimental":
            resource_id = f"chemical/property/experimental/name"

        elif by == "predicted":
            resource_id = f"chemical/property/predicted/name"
        
        return self.get(resource_id, **kwargs)

    def get_properties_batch(self, dtxsid_list: List[str], **kwargs) -> Dict[str, Any]:
        
        """
        #### Description:
            Get Chemical properties in batch.

        #### Input Parameters:
            - dtxsid_list: List of DTXSIDs
        
        #### Output Schema:
            [
                {
                "name": "string",
                "value": 0,
                "id": 0,
                "source": "string",
                "dtxsid": "string",
                "dtxcid": "string",
                "unit": "string",
                "propertyId": "string",
                "propType": "string",
                "description": "string"
                }
            ]

        #### Example:
            client = ChemProperties(api_key=api_key)
            response = client.get_properties_batch(dtxsid_list=["DTXSID7020182"])
        """
        kwargs = {}
        kwargs["json"] = dtxsid_list

        headers = {}
        headers["Content-Type"] = "application/json"
        resource_id = f"chemical/property/search/by-dtxsid/" 

        return self.post(resource_id, headers=headers, **kwargs)


class IndigoService(BaseAPIClient):
    """
    #### Description:
    """

    def __init__(self, api_key: str):
        super().__init__(api_key)


class ChemFile(BaseAPIClient):

    def __init__(self, api_key: str):
        super().__init__(api_key)

class Synonyms(BaseAPIClient):

    def __init__(self, api_key: str):
        super().__init__(api_key)