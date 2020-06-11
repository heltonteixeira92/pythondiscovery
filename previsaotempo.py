import requests
from bs4 import BeautifulSoup

search = "Tempo em São Paulo"
url = f"https://www.google.com.br/search?&q={search}"
r = requests.get(url)
s = BeautifulSoup(r.text, "html.parser")
update = s.find("div", class_="vk_bk sol-tmp").text
print(update)