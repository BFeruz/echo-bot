import requests


def send_message(url:str,chat_id: int, text, parse_mode=False):
    endpoint = '/sendMessage'
    url += endpoint

    payload = {
        'chat_id': chat_id,
        'text': text,
    }
    requests.get(url, params=payload)

def send_contact(url: str, chat_id: int, phone_number: str, first_name: str, last_name: str=None):
    endpoint = '/sendContact'
    url += endpoint

    payload = {
        'chat_id': chat_id,
        'phone_number': phone_number,
        'first_name': first_name,
    }
    if last_name:
        payload['last_name'] = last_name

    r = requests.post(url, params=payload)

def send_video(url:str,chat_id: int, video:str, parse_mode=False):
    endpoint = '/sendVideo'
    url+=endpoint

    payload = {
        'chat_id': chat_id,
        'video': video
    }

    r = requests.post(url, params=payload)

def send_location(url:str,chat_id: int,latitude:float,longitude:float, parse_mode=False):
    endpoint = '/sendLocation'
    url+=endpoint

    payload = {
        'chat_id': chat_id,
        'latitude': latitude,
        'longitude':longitude
    }

    r = requests.post(url, params=payload)

def send_photo(url:str,chat_id: int, photo:str, parse_mode=False):
    endpoint = '/sendPhoto'
    url+=endpoint

    payload = {
        'chat_id': chat_id,
        'photo': photo
    }

    r = requests.post(url, params=payload)

def send_voice(url:str,chat_id: int, voice:str, parse_mode=False):
    endpoint = '/sendVoice'
    url+=endpoint

    payload = {
        'chat_id': chat_id,
        'voice': voice
    }

    r = requests.post(url, params=payload)

def send_audio(url:str,chat_id: int, audio:str, parse_mode=False):
    endpoint = '/sendAudio'
    url+=endpoint

    payload = {
        'chat_id': chat_id,
        'audio': audio
    }

    r = requests.post(url, params=payload)

def send_document(url:str,chat_id: int, document:str, parse_mode=False):
    endpoint = '/sendDocument'
    url+=endpoint

    payload = {
        'chat_id': chat_id,
        'document': document
    }

    r = requests.post(url, params=payload)

def send_animation(url:str,chat_id: int, animation:str, parse_mode=False):
    endpoint = '/sendAnimation'
    url+=endpoint

    payload = {
        'chat_id': chat_id,
        'animation': animation
    }

    r = requests.post(url, params=payload)

def send_dice(url:str,chat_id: int,parse_mode=False):
    endpoint = '/sendDice'
    url+=endpoint

    payload = {
        'chat_id': chat_id
    }

    r = requests.post(url, params=payload)