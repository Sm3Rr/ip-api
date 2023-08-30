
import requests

# URL مورد نظر خود را در اینجا قرار دهید
url = "http://www.example.com"

# User-Agent جعلی که میخواهید برای ریکوئست استفاده شود
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"

# درخواست GET با نشانه User-Agent جعلی ارسال می شود
headers = {
    'User-Agent': user_agent
}
response = requests.get(url, headers=headers)

# بررسی و چاپ کردن وضعیت درخواست
if response.status_code == 200:
    print("درخواست با موفقیت ارسال شد.")
else:
    print("ارسال درخواست ناموفق بود.")
