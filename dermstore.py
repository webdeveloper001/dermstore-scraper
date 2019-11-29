import csv     
import requests
import json
from bs4 import BeautifulSoup 
import io
import sys
reload(sys)
sys.setdefaultencoding('utf8')
# Get ratings and reviews
codelist = []
session = requests.Session()

session.headers.update({
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
    'X-Distil-Ajax': 'dtyqytwbbuedtbrzwctsetyxbrvacc',
    'X-NewRelic-ID': 'VgcAUFRbABABXFFSBwQHUFU=',
    'X-Requested-With': 'XMLHttpRequest',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Sec-Fetch-Mode': 'cors',
    'cookie': 'osid=sdntgck7qdqeeff7rj5g7f42a6; _evga_f572=4811cce19ea3a74f.; promopop_seen=true; epop_seen=true; D_IID=80C3F85C-C90F-31DF-8830-AF181B9C7A2E; D_UID=F5D108B5-C188-384D-924B-4273F3BA3AD8; D_ZID=2F0C2602-8349-3331-84BD-146715B0D245; D_ZUID=F8B55B02-32B1-3BED-8A41-1AD872F32D52; D_HID=A452330B-70C5-3A5B-92EE-EEE358CDC22E; D_SID=104.200.132.235:ByJrbdmhbR3nEINTPi7syHCR0vbHQVdwUbP/OMC85tc; _gcl_au=1.1.559027162.1568486240; cto_lwid=ad065196-d6ba-4e72-906a-0edfae1d26c3; _ga=GA1.2.2131458904.1568486243; _ivu=AD4FE09C-AB7A-4B28-89B0-AE7EF2019C79; _fbp=fb.1.1568486250009.1295249037; src=walkin; SERVER-PERSIST=371202220.4135.0000; _gid=GA1.2.152582100.1568650908; fs_uid=rs.fullstory.com`H7VJX`6336540464939008:4639555074686976/1600022244; pvhc=1; pvh=20567; PHPSESSID=t76lo137fn6c3sohdsmfkbath7; scroll=0; mp_dermstore_mixpanel=%7B%22distinct_id%22%3A%20%2216d3110b91652c-01f1f1741163fb-5373e62-1fa400-16d3110b917cb5%22%2C%22bc_persist_updated%22%3A%201568486242584%7D; st_ChatWidgetStatus=2|1|'
})
csv.register_dialect('myDialect1',
	  quoting=csv.QUOTE_ALL,
	  skipinitialspace=True)
h_list = open('hcpcs.csv', 'a')
h_reader = csv.reader(h_list, delimiter=',')

f = open('sample1.csv', 'a')
writer = csv.writer(f, dialect='myDialect1')
writer.writerow(['Brand', 'Title', 'Price','Rating', 'link'])
for page in range(0, 19):
    url = 'https://www.dermstore.com/ajax/list_filtered.php?lkey=400073&filtered=true&ipp=128&page={}&price=&filter%5B%5D=500014&filter%5B%5D=500014&sort='
    r = session.get(url.format(page))
    resp = json.loads(r.text)

    soup = BeautifulSoup(resp['products'], features="html.parser")
    products = soup.findAll('div', class_='prod-widget-responsive')

    for product in products:
        writer.writerow([
            product.find('p', class_='item-brand').find('a').text.encode("utf-8"),
            product.find('p', class_='item-name').text.encode("utf-8"),
            product.find('a', class_='item-price').text.strip().encode("utf-8"),
            product.find('span', class_='starsBoxSm').findAll('meta')[1].attrs['content'].encode("utf-8"),
            product.find('p', class_='item-brand').find('a').attrs['href'].encode("utf-8")
        ])
        print(product.find('p', class_='item-brand').find('a').text.encode("utf-8"))
        print(product.find('p', class_='item-name').text.encode("utf-8"))
        print(product.find('a', class_='item-price').text.strip().encode("utf-8"))
        print(product.find('span', class_='starsBoxSm').findAll('meta')[1].attrs['content'].encode("utf-8"))
    
