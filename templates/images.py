import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.flags

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

data = requests.get('https://ko.wikipedia.org/wiki/홍콩', headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

flag = soup.select_one(
    '#mw-content-text > div.mw-parser-output > table.infobox.geography.vcard > tbody > tr.mergedtoprow > td > table > tbody > tr:nth-child(1) > td:nth-child(1) > a > img')
flag_src = flag.get("src")
print(flag_src)

doc = {
    'src': flag_src
}
db.flags.insert_one(doc)
