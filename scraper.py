import requests
from bs4 import BeautifulSoup

url = 'https://webscraper.io/test-sites/e-commerce/static'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

try:
    # Check the status code of the response
    if r.status_code == 200:
        print('OK, able to connect')
    else:
        raise Exception(f'We were not able to connect; an error occurred: {r.status_code}')
except Exception as e:
    print(e)
