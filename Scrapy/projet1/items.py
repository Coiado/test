# -*- coding: utf-8 Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Projet1Item(scrapy.Item):
    title = scrapy.Field()
    adresse = scrapy.Field()
    historique = scrapy.Field()
    statut = scrapy.Field()
    technique = scrapy.Field()
    siecle = scrapy.Field()
    elements = scrapy.Field()
    date_protection= scrapy.Field()
