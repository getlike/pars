from bs4 import BeautifulSoup
import requests

headers = {
    "accept": "*/*",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}
url = "https://transsibinfo.com/news"
soup = requests.get(url, headers=headers)

src = soup.text
with open('index.html', 'w') as file:
    file.write(src)
