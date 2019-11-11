import scrapy
import pandas as pd
from filmaffinity.items import Filmaffinity_Detail_Item
from datetime import datetime

df=pd.read_csv('/Users/Inigo/Desktop/UOC Q3/Ciclo Vida Datos/PAC/PR 1 - Web Scraping/filmaffinity/filmaffinity/spiders/lista_urls.csv',
				sep=',')
# Convertir urls en lista
urls=list(df['urls'])

# Generación nombre archivo csv de salida
now = datetime.now()
fecha = now.strftime("%d-%m-%Y")
nombreArchivo=str(len(urls))+"_TopFilmaffinity_"+fecha
pathFolder = "/Users/Inigo/Desktop/UOC Q3/Ciclo Vida Datos/PAC/PR 1 - Web Scraping/filmaffinity/Output Scraper csv/"
pathCsv = pathFolder+nombreArchivo+".csv"

class FilmDetailSpider(scrapy.Spider):
	
	# Nombre araña
	name = "film_detail_spider"

	# Settings para guardado de archivo csv
	custom_settings = {
        'FEED_FORMAT': 'csv',
        'FEED_URI': pathCsv,
        'FEED_EXPORT_FIELDS':['titulo','genero','anyo','duracion','pais','direccion','guion','musica','fotografia','reparto','productor','puntuacion','numVal']
    	}

	def start_requests(self):
		
		start_urls = ['https://www.filmaffinity.com/es/topgen.php']
		for url in urls:
			yield scrapy.Request(url=url,callback=self.parse) 

	def parse(self,response):

		item = Filmaffinity_Detail_Item()
#
		item['titulo'] = response.xpath('//dl[@class="movie-info"]/dd/text()').extract()[0].strip()
		item['genero'] = response.xpath('//dt[text()="Género"]/following-sibling::dd[1]/span[@itemprop="genre"]/a//text()').extract()[0].strip()
		item['anyo'] = response.xpath('//dt[text()="Año"]/following-sibling::dd[1]/text()').extract()[0].strip()
		item['duracion'] = response.xpath('//dt[text()="Duración"]/following-sibling::dd[1]/text()').extract()[0].strip()
		item['pais'] = response.xpath('//dt[text()="País"]/following-sibling::dd[1]/text()').extract()[0].strip()
		item['direccion'] = response.xpath('//dd[@class="directors"]/span/a/@title').extract()[0].strip()
		item['guion'] = response.xpath('//dt[text()="Guion"]/following-sibling::dd[1]/div[@class="credits"]/span[@class="nb"]/span/text()').extract()
		item['musica'] = response.xpath('//dt[text()="Música"]/following-sibling::dd[1]/div[@class="credits"]/span[@class="nb"]/span/text()').extract()
		item['fotografia'] = response.xpath('//dt[text()="Fotografía"]/following-sibling::dd[1]/div[@class="credits"]/span[@class="nb"]/span/text()').extract()
		item['reparto'] = response.xpath('//dt[text()="Reparto"]/following-sibling::dd[1]//span[@itemprop="name"]/text()').extract()
		item['productor'] = response.xpath('//dt[text()="Productora"]/following-sibling::dd[1]/div[@class="credits"]/span[@class="nb"]/span/text()').extract()
		item['puntuacion'] = response.css('div#movie-rat-avg ::attr(content)').extract()[0]
		item['numVal'] = response.css('div#movie-count-rat > span ::attr(content)').extract()[0]

		yield item
		
