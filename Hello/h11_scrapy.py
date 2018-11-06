from scrapy.selector import Selector
from scrapy.http import HtmlResponse


body = '<html><body><span>good</span></body></html>'
p = Selector(text=body).xpath('//span/text()').extract()

print(p)

response = HtmlResponse(url='http://example.com', body=body, encoding='utf-8')
print(Selector(response=response).xpath('//span/text()').extract())
