from pycomptox.apis.chem_search import ChemSearch

# Initialize the client
api_key = "5506ebc6-9485-11ef-9c61-325096b39f47"
client = ChemSearch(api_key=api_key)

casnum = "95-16-9"
# Define dynamic URL and query parameters
resource_id = "/{}".format(casnum)  # e.g., an endpoint like "/data/resource"
query_params = {"top": 10}

# Make the GET request
response = client.starts_with(word=casnum, query_params=query_params)

print(response)
respose = client.equal(word=casnum, query_params=query_params)
print(response)

casnum = "95-16"
response = client.contain(word=casnum, query_params=query_params)
print(response)
