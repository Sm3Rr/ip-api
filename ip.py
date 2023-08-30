

import requests
import random

def send_requests(url, num_requests):
    for _ in range(num_requests):
        headers = {'User-Agent': generate_user_agent()}
        requests.get(url, headers=headers)

def generate_user_agent():
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.3',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.3',
    ]
    return random.choice(user_agents)

URL = input(" Enter Url: ")
NUM_REQUESTS = int(input(" Enter Req's Amount: "))

send_requests(URL, NUM_REQUESTS)
