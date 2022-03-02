import urllib.request
import json
import os
import ssl

def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.

# Request data goes here
data = {
    "Inputs": {
        "data":
        [
            {
                "Hydrogen": 2845,
                "Oxigen": 5860,
                "Nitrogen": 27842,
                "Methane": 7406,
                "CO": 32,
                "CO2": 1344,
                "Ethylene": 16684,
                "Ethane": 5467,
                "Acethylene": 7,
                "DBDS": 19,
                "Power factor": 1,
                "Interfacial V": 45,
                "Dielectric rigidity": 55,
                "Water content": 0
            },
        ]
    },
    "GlobalParameters": 1.0
}

body = str.encode(json.dumps(data))

url = 'http://PLEASE-ENTER-YOUR-OWNED-AML-ACI-ENDPOINT-NAME.southeastasia.azurecontainer.io/score'
api_key = 'PLEASE-ENTER-YOUR-OWN-API-KEY' # Replace this with the API key for the web service
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)

    result = response.read()
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(json.loads(error.read().decode("utf8", 'ignore')))