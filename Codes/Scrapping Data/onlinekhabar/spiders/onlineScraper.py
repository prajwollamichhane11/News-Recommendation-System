# -*- coding: utf-8 -*-
import scrapy

class OnlinescraperSpider(scrapy.Spider):
    name = 'onlineScraper'
    allowed_domains = ['www.onlinekhabar.com/content/news']
    start_urls = ['https://www.onlinekhabar.com/content/news/']

    def __init__(self):
        self.newsCount = 0

    def parse(self, response):
        NewsLinks = response.xpath('//div[@class="item"]/div[@class="item__wrap"]/a/@href').extract()
        NextPage = response.xpath('//a[@class="next page-numbers"]/@href').extract()[0]

        for link in NewsLinks:
            self.newsCount += 1
            yield scrapy.Request(link,self.parse_article, dont_filter=True)
        if self.newsCount < 210:
            yield scrapy.Request(NextPage,dont_filter=True)

    def parse_article(self,response):
        title = response.xpath("//div[@class='nws__title--card']/h2/text()").extract()[0]
        article = response.xpath('//div[@class="col colspan3 main__read--content ok18-single-post-content-wrap"]/p/text()').extract()

        article_final = ''.join(article)
        yield{
            "News Title":title,
            "News Article":article_final
        }
