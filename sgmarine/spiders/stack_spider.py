from scrapy import Spider
from scrapy import Request
from scrapy.selector import Selector
import datetime

class StackSpider(Spider):
    name = "sgmarine"
    allowed_domains = ["www.sgmaritime.com"]
    start_urls = [
        "https://www.sgmaritime.com/company-listings"
    ]

    def parse(self, response):
        companies = Selector(response).xpath('//*[@id="Contentplaceholder1_C025_Col00"]/div[2]/div/div/div[@class="col-md-9 col-xs-8 company-details"]')
        print(len(companies))

        item = {}
        if len(companies) > 0:
            for name in companies:
                if len(name.xpath('h3/a/text()').extract())>0:
                    # get company name & url:
                    comp_name = name.xpath('h3/a/text()').extract()[0]
                    comp_name = " ".join(comp_name.split())
                    item['company name'] = comp_name
                    item['url'] = 'https://www.sgmaritime.com' + name.xpath('h3/a/@href').extract()[0]
                    item['crawled_on'] = datetime.date.today().strftime("%Y-%m-%d")

                    # # get company website & phone:
                    # if len(name.xpath('span[@id="valuewebsite_0"]/a/text()'))>0:
                    #     if len(name.xpath('span[@id="valuephone_0"]/a/text()'))>0:
                    #         comp_web = name.xpath('span[@id="valuewebsite_0"]/a/text()').extract()[0]
                    #         comp_web = " ".join(comp_web.split())
                    #         item['company website'] = comp_web
                    #         comp_phone = name.xpath('span[@id="valuephone_0"]/a/text()').extract()[0]
                    #         comp_phone = " ".join(comp_phone.split())
                    #         item['company phone'] = comp_phone
                    #         yield item
                    #     else:
                    #         comp_web = name.xpath('span[@id="valuewebsite_0"]/a/text()').extract()[0]
                    #         comp_web = " ".join(comp_web.split())
                    #         item['company website'] = comp_web
                    #         yield item
                    # else:
                    #     if len(name.xpath('span[@id="valuephone_0"]/a/text()'))>0:
                    #         comp_phone = name.xpath('span[@id="valuephone_0"]/a/text()').extract()[0]
                    #         comp_phone = " ".join(comp_phone.split())
                    #         item['company phone'] = comp_phone
                    #         yield item
                    #     else:
                            # yield item
                    
                    yield item

                if len(name.xpath('p/a/text()').extract())>0:
                    # get company name & url:
                    comp_name2 = name.xpath('p/a/text()').extract()[0]
                    comp_name2 = " ".join(comp_name2.split())
                    if comp_name2 != "More":
                        item['company name'] = comp_name2
                        item['url'] = 'https://www.sgmaritime.com' + name.xpath('p/a/@href').extract()[0]
                        item['crawled_on'] = datetime.date.today().strftime("%Y-%m-%d")

                        # # get company website & phone:
                        # if len(name.xpath('span[@id="valuewebsite_0"]/a/text()'))>0:
                        #     if len(name.xpath('span[@id="valuephone_0"]/a/text()'))>0:
                        #         comp_web = name.xpath('span[@id="valuewebsite_0"]/a/text()').extract()[0]
                        #         comp_web = " ".join(comp_web.split())
                        #         item['company website'] = comp_web
                        #         comp_phone = name.xpath('span[@id="valuephone_0"]/a/text()').extract()[0]
                        #         comp_phone = " ".join(comp_phone.split())
                        #         item['company phone'] = comp_phone
                        #         yield item
                        #     else:
                        #         comp_web = name.xpath('span[@id="valuewebsite_0"]/a/text()').extract()[0]
                        #         comp_web = " ".join(comp_web.split())
                        #         item['company website'] = comp_web
                        #         yield item
                        # else:
                        #     if len(name.xpath('span[@id="valuephone_0"]/a/text()'))>0:
                        #         comp_phone = name.xpath('span[@id="valuephone_0"]/a/text()').extract()[0]
                        #         comp_phone = " ".join(comp_phone.split())
                        #         item['company phone'] = comp_phone
                        #         yield item
                        #     else:
                                # yield item
                        
                        yield item
                
        # Follow pagination url link
        next_page = Selector(response).xpath('//*[@id="Contentplaceholder1_C025_Col00"]/div[2]/nav[2]/ul/li/a[@aria-label="Next"]/@href').extract()[0]
        if next_page:
            next_page_url = 'https://www.sgmaritime.com' + next_page
            yield Request(url=next_page_url, callback=self.parse)