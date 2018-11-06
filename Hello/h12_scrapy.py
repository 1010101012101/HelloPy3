from scrapy.selector import Selector
from scrapy.http import HtmlResponse
import requests
from urllib.request import urlretrieve



url = 'http://quotes.toscrape.com/page/1/'
#url = 'https://detail.1688.com/offer/578483276614.html?spm=a360q.8274423.1130995625.22.75e74c9af0X7nz'

html = requests.get(url).text

response = HtmlResponse(url='http://example.com', body=html, encoding='utf-8')

select = Selector(response=response)

#o = select.xpath('//title/text()').extract()[0]
o = select.xpath('//body/*/div[@class]')

print(o)

