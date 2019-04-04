# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import datetime


class SgmaritimeCrawlerSpider(CrawlSpider):
    name = 'sgmaritime_crawler'
    allowed_domains = ['www.sgmaritime.com']
    start_urls = ['https://www.sgmaritime.com/company-listings?page=1']

    rules = (
        Rule(LinkExtractor(allow=r'company-listings\?page=[1-331]'), callback='parse_item', follow=True),
    )

    # 3306/10 = 331

    def parse_item(self, response):
        # For first page to 15th:
        companies = response.xpath('//*[@id="Contentplaceholder1_C025_Col00"]/div[2]/div/div/div[2]/h3')
        print(len(companies))

        # From page 16th to the last:
        list_comp_name = response.xpath('//*[@id="Contentplaceholder1_C025_Col00"]/div[2]/div/div/div[@class="col-md-9 col-xs-8 company-details"]/p/a')
        print(len(list_comp_name))

        item = {}
        if len(companies) > 0:
            for name in companies:
                comp_name = name.xpath('a/text()').extract()[0]
                comp_name = " ".join(comp_name.split())
                item['company name'] = comp_name
                item['url'] = 'https://www.sgmaritime.com' + name.xpath('a/@href').extract()[0]
                item['crawled_on'] = datetime.date.today().strftime("%Y-%m-%d")
                yield item

        if len(list_comp_name) > 0:
            for name2 in list_comp_name:
                comp_name2 = name2.xpath('text()').extract()[0]
                comp_name2 = " ".join(comp_name2.split())
                if comp_name2 != "More":
                    item['company name'] = comp_name2
                    item['url'] = 'https://www.sgmaritime.com' + name2.xpath('@href').extract()[0]
                    item['crawled_on'] = datetime.date.today().strftime("%Y-%m-%d")
                    yield item