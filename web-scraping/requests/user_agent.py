# do webscraping with requests at websites that are user-side rendering
import requests
from requests_html import HTMLSession


url = 'https://www.kabum.com.br/'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

# response = requests.get(url, headers=headers)

with HTMLSession() as session:
    response = session.get(url, headers=headers, timeout=10)
    response.html.render()
    print(response.html.html)