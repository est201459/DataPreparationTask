# -*- coding: utf-8 -*-
import scrapy
from myproject.items import articles, article

class ArticleSpider(scrapy.Spider):
    name            = 'article'

    allowed_domains = ['catalog.data.gov']

    start_urls      = ['https://catalog.data.gov/dataset']

    ##ROBOTSTXT_OBEY  = False

    def parse(self, response):

        ##host = self.allowed_domains[0]

        for link in response.css(".dataset-heading > a"):
            link = f"{link.attrib.get('href')}"
            title = link
            yield response.follow(link,callback=self.parse_detail, meta={'link' : link,'title':title})



    def parse_detail(self,response):

        items = articles()
        item = article()

        items["link"] = response.meta["link"]
        item["title"] = response.css(".module-content > h1::text").extract()[0].strip() #response.meta["title"]
        item["paragraph"]=response.css(".notes >p::text").extract()[0].strip()
        #item["paragraph"] = list()


        #for text in response.css(".notes > p::text").extract():

         #   item["paragraph"].append(text)
        items["body"] = item
        return items