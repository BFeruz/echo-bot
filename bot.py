import requests
from settings import URL
from time import sleep
from .sends import send_message,send_contact,send_location,send_video

def get_last_update(url: str) -> dict:
    endpoint = '/getUpdates'
    url += endpoint
    
    response = requests.get(url)
    if response.status_code == 200:
        result = response.json()['result']

        if len(result) != 0:
            return result[-1]

        else:
            return 404
    
    return response.status_code

def main(url: str):
    last_update_id = -1
    while True:
        curr_update = get_last_update(url)

        if curr_update['update_id'] != last_update_id:
            user = curr_update['message']['from']
            text = curr_update['message'].get('text')
            contact = curr_update['message'].get('contact')
            video   = curr_update['message'].get('video')
            location = curr_update['message'].get('location')
            if text:
                send_message(url, user['id'], text)
            elif contact:
                send_contact(url, user['id'],contact['phone_number'],contact['first_name'])
            elif video:    
                 send_video(url, user['id'], )
            elif location:
                send_location(url, user['id'], 'send text message')
            
                   
        last_update_id = curr_update['update_id']

        sleep(0.5)


main(URL)