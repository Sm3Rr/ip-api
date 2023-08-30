
import requests
from fake_useragent import UserAgent

url = input(" Enter Url: ")

user_agent = UserAgent()

for _ in range(5000):
    headers = {
        'User-Agent': user_agent.random
    }
    response = requests.get(url, headers=headers)
    # اینجا می‌توانید کد دلخواه خود را قرار دهید
    
    print(f'Response status code: {response.status_code}')
