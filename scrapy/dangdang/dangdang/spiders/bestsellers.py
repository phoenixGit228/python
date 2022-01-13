import scrapy, bs4
from ..items import DangdangItem

class DangDangSpider(scrapy.Spider):
    name = 'dangdang'
    allowed_domains = ['bang.dangdang.com']
    start_urls = []
    for x in range(1,4):
        url = f'http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-year-2018-0-1-{x}'
        start_urls.append(url)
    
    def parse(self, response):
        bs = bs4.BeautifulSoup(response.text, 'html.parser')
        info = bs.find(class_='bang_list_box').find_all('li')
        for x in info:
            item = DangdangItem()
            item['title'] = x.find(class_='name').find('a')['title']
            item['publisher'] = x.find(class_='publisher_info').find('a')['title']
            item['price'] = x.find('span',class_='price_n').text
            print(item)
            yield item
