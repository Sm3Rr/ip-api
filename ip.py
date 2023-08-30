
import requests

url = input("https://example.com : ")
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

for _ in range(5000):
    response = requests.get(url, headers=headers)
    # در اینجا می توانید تنظیمات جانبی دیگر را برای وارد کردن به عنوان پارامتر های دیگر مانند پارامترهای query_string، پارامترهای بدن درخواست یا پارامترهای صحت سنجی اضافه کنید

    # در اینجا می توانید چک کنید که آیا درخواست درست به سرور ارسال شده است

    # در اینجا می توانید با محتوای جواب انجام بدهید

    print(response.status_code)
