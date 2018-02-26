# -*- coding: utf-8 -*-
import scrapy
from anjukeesf.items import RedisItem,Redis_esfItem,Redis_zuItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spider import CrawlSpider,Rule

class AnjukeesfspiderSpider(scrapy.Spider):
    name = 'anjukeesfspider'
    allowed_domains = ['anjuke.com']
    custom_settings = {
        'ITEM_PIPELINES':{
            'anjukeesf.pipelines.RedisPipeline':300,
        }
    }

    start_urls = ['https://hangzhou.anjuke.com/community/?from=esf_list_navigation']

    # page_links = LinkExtractor(allow=(r'anjuke.com/community/p\d+/'))
    # xiaoqu_links = LinkExtractor(allow=(r'anjuke.com/community/view/\d+/'),deny=(r'jiedu'))
    # esf_links = LinkExtractor(allow=(r'anjuke.com/community/props/sale/\d+/'))
    # esf_page_links = LinkExtractor(allow=(r'anjuke.com/community/props/sale/\d+/p\d+/'))
    # esf_detail_links = LinkExtractor(allow=(r'anjuke.com/prop/view/[a-zA-Z]{1}\d+'))
    # zu_links = LinkExtractor(allow=(r'anjuke.com/community/props/rent/\d+'))
    # zu_page_links = LinkExtractor(allow=(r'anjuke.com/community/props/rent/\d+/p\d+/'))
    # zu_detail_links = LinkExtractor(allow=(r'zu.anjuke.com/fangyuan/\d+'))
    #
    # rules = (
    #     Rule(page_links),
    #     Rule(xiaoqu_links,callback="parse_item",follow=True),
    #     Rule(esf_links,callback="parse_item", follow=True),
    #     Rule(esf_page_links),
    #     Rule(esf_detail_links,callback="parse_item",follow=True),
    #     Rule(zu_links,callback="parse_item",follow=True),
    #     Rule(zu_page_links),
    #     Rule(zu_detail_links,callback="parse_item",follow=True),
    # )

    def parse(self, response):
        try:
            for box in response.xpath('//div[@class="li-info"]/h3'):
                item = RedisItem()
                item['url'] = 'https://hangzhou.anjuke.com' + box.xpath('.//a/@href').extract()[0]
                pid = str(item['url']).replace('https://hangzhou.anjuke.com/community/view/','').replace('/','')
                esf_list = 'https://hangzhou.anjuke.com/community/props/sale/'+ pid
                zu_list = 'https://hangzhou.anjuke.com/community/props/rent/' + pid
                yield scrapy.Request(esf_list,callback=self.parse_esf,dont_filter=True)
                yield scrapy.Request(zu_list, callback=self.parse_zu,dont_filter=True)
                yield item

            for page in response.xpath('//div[@class="multi-page"]'):
                page_links = page.xpath('.//a[@class="aNxt"]/@href').extract()[0]
                yield scrapy.Request(url=page_links,callback=self.parse)
        except:
            pass

    def parse_esf(self, response):
        try:
            for box in response.xpath('//div[@class="details"]/p[@class="title"]'):
                item_esf = Redis_esfItem()
                item_esf['esf_url'] = box.xpath('.//span/@href').extract()[0]
                yield item_esf
            for page in response.xpath('//div[@class="multi-page"]'):
                page_links = page.xpath('.//a[@class="aNxt"]/@href').extract()[0]
                yield scrapy.Request(url=page_links,callback=self.parse_esf)
        except:
            pass
    def parse_zu(self,response):
        try:
            for box in response.xpath('//div[@class="details"]/p[@class="title"]'):
                item_zu = Redis_zuItem()
                item_zu['zu_url'] = box.xpath('.//span/@href').extract()[0]
                yield item_zu

            for page in response.xpath('//div[@class="multi-page"]'):
                page_links = page.xpath('.//a[@class="aNxt"]/@href').extract()[0]
                yield scrapy.Request(url=page_links,callback=self.parse_zu)
        except:
            pass