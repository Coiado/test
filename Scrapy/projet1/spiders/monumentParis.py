# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scrapy import Spider
from pymongo import MongoClient

from projet1.items import Projet1Item


class MonumentparisSpider(Spider):
    name = 'monumentParis'
    allowed_domains = ['culture.gouv.fr']
    start_urls = ['http://www2.culture.gouv.fr/public/mistral/dapamer_fr?ACTION=RETROUVER_TITLE&LEVEL=1&GRP=0&REQ=((paris)%3aLOCA%2cPLOC)']

    def parse(self, response):
        all_links = [response.urljoin(elt) for elt in response.css("table")[-1].css("a::attr(href)").extract()]
        for link in all_links:
            yield Request(link, callback=self.parse_page)
   
    def parse_page(self, response):
        all_links = [response.urljoin(elt) for elt in response.css("table a::attr(href)").extract()]
        for link in all_links:
            yield Request(link, callback=self.parse_monument)

    def parse_monument(self, response):
        all_tr = response.css("table")[-2].css("tr")
        item = Projet1Item()
        flag = 0
	
        for tr in all_tr:
            title, value = tr.css("td")
            title = title.css("n::text").extract_first()
            value = value.css("n::text").extract_first() or value.css("b::text").extract_first()
            if flag == 0:
                item["title"] = value
                flag = 1
            if title.strip() and value.strip():
                if "Localisation" in title:
                    item["localisation"] = value
                elif "Adresse" in title: 
                    item["adresse"] = value
                elif "Historique" in title: 
                    item["historique"] = value
                elif "Statut propriété" in title: 
                    item["statut"] = value
                elif "Technique décor" in title: 
                    item["technique"] = value
                elif "Siècle" in title: 
                    item["siecle"] = value
                elif "Eléments MH" in title: 
                    item["elements"] = value
                elif "Date protection" in title: 
                    item["date_protection"] = value
    
        print(item)
        yield item
                
