import requests
import json


# Set the request parameters
url = 'https://mtechn.zendesk.com/api/v2/tickets/recent'
user = 'alexandr.p@rockalab.com'
pwd = 'qaz1qaz1'

# Do the HTTP get request
response = requests.get(url, auth=(user, pwd))

# Check for HTTP codes other than 200
if response.status_code != 200:
    print('Status:', response.status_code, 'Problem with the request. Exiting.')
    exit()

# Decode the JSON response into a dictionary and use the data
data = response.json()
dt = json.dumps(data)
print (dt)
