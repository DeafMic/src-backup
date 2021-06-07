import requests
import time
headers = {
    'Authorization': 'Bearer 948b6cd86bb29150b3e375f2a03386fc69778ff8',
}

try:
    while True:
        response = requests.get('https://api.nrfcloud.com/v1/messages', headers=headers)
        time.sleep(1)
        print(response.json()['items'][0]['message']['data'])
except KeyboardInterrupt:
    print('interrupted!')





