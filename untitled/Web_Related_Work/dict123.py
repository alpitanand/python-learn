import requests
import json
# Disable warnings
requests.packages.urllib3.disable_warnings()
# Variables
apic_em_ip = "https://sandboxapic.cisco.com/api/v1"
def get_token(url):
# Define API Call
    api_call = "/ticket"
# Payload contains authentication information
    payload = {"username": "devnetuser", "password": "Cisco123!"}
# Header information
    headers = {"content-type": "application/json"}
# Combine URL, API call and parameters variables
    url += api_call
    response = requests.post(url, data=json.dumps(payload), headers=headers, verify=False)
    response.raise_for_status()
    response = response.json()
    return response["response"]["serviceTicket"]

def get_devices(token, url):
# Define API Call
    api_call = "/network-device"
# Header information
    headers = {"X-AUTH-TOKEN": token}
# Combine URL, API call and parameters variables
    url += api_call
    response = requests.get(url, headers=headers, verify=False)
    response.raise_for_status()
    return response.text
if __name__ == '__main__':
# Assign obtained authentication token to a variable. Provide APIC-EM's
# URL address
    auth_token = get_token(apic_em_ip)
# Get devices. Provide authentication token and
# APIC-EM's URL address
    devices = get_devices(auth_token, apic_em_ip)
    #print(devices)

    x = json.loads(devices)['response']

    for i in range(len(x)):
        if x[i]['family'] != "Unified AP":
            print('{}---{}'.format(x[i]['hostname'], x[i]['serialNumber']))

