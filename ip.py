import requests
import socket

def send_request(url, method="GET"):
    if method == "POST":
        data = {"key": "value"}  # اطلاعات برای بدنه درخواست POST را تهیه کنید
        response = requests.post(url, data=data)
    elif method == "GET":
        response = requests.get(url)
    elif method == "SYN":
        ip = socket.gethostbyname(url)
        print(" WEBSITE IP ADDRESS : ", ip)
        return
    elif method == "UAM":
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}  # یک User-Agent مناسب تهیه کنید
        response = requests.get(url, headers=headers)
    
    print(response.text)  # پاسخ سرور را بررسی کنید

url = input(" Enter The Site Url")
method = input(" Enter Method (POST/GET/SYN/UAM): ")

send_request(url, method)
