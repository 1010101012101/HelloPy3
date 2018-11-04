import scrapy


class QuotesSpider(scrapy.Spider):
    name = "taobao"

    def start_requests(self):
        urls = [
            #'http://quotes.toscrape.com/page/1/',
            #'http://quotes.toscrape.com/page/2/',
            'https://detail.1688.com/offer/578483276614.html?spm=a360q.8274423.1130995625.22.75e74c9af0X7nz',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'taobao.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

        videos = response.xpath('//*[@id="detail-main-video-content"]/div/video')
        print("HHHA:1====>len(videos=", len(videos))
        for video in videos:
            print("HHHA:0.1====>", video)

            #scrapy shell "http://quotes.toscrape.com/page/1/"
            #scrapy shell "https://detail.1688.com/offer/578483276614.html?spm=a360q.8274423.1130995625.22.75e74c9af0X7nz"