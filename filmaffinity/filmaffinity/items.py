# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


#class FilmaffinityItem(scrapy.Item):
#    ID = scrapy.Field()
#    name = scrapy.Field()
#    director = scrapy.Field()
#    year = scrapy.Field()
#    country = scrapy.Field()
#    rating = scrapy.Field()
#    numVal = scrapy.Field()
#    url = scrapy.Field()
    
class Filmaffinity_Detail_Item(scrapy.Item):
    titulo = scrapy.Field()
    genero = scrapy.Field()
    anyo = scrapy.Field()
    duracion = scrapy.Field()
    pais = scrapy.Field()
    direccion = scrapy.Field()
    guion = scrapy.Field()
    musica = scrapy.Field()
    fotografia = scrapy.Field()
    reparto = scrapy.Field()
    productor = scrapy.Field()
    puntuacion = scrapy.Field()
    numVal = scrapy.Field()
