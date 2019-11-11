import scrapy
from scrapy.spiders import CrawlSpider
from scrapy.http import Request
from scrapy import Selector
from selenium import webdriver
import time
import pandas as pd

# Introducir un numero que aseguramos que sea entero, no nulo, ni negativo
while True:
    try:
        n = int(input("\nIntroducir número de peliculas a cuya información obtener: "))
        if(n<1):
            print("\n¡¡Valor no válido!!")
        else:
            break
        
    except ValueError:
        print("\n¡¡Valor no válido!!")
                
# Dado que será necesario accionar evento de carga de 30 peliculas n veces, se calcula numero de veces a cargar items
if ((n/30).is_integer() & ((n/30)!=0)):
    # Todos los múltiples de 30 deben ser actualizados una vez menos que lo que tocaría según la floor división
    numPag = (n // 30) - 1
else:
    numPag = (n // 30)


print(f'\n\tNúmero de películas a scrapear: {n}')
print(f'\n\tNúmero de actualizaciones de página a realizar: {numPag}')

# Recordar poner path a la carpeta del proyecto
driver = webdriver.Firefox('/Users/Inigo/Desktop/UOC Q3/Ciclo Vida Datos/PAC/PR 1 - Web Scraping/filmaffinity')
# Web donde se trabaja con selenium y que se procede a cargar
driver.get("https://www.filmaffinity.com/es/topgen.php")
# Delay para que carguen los pop-ups 
time.sleep(3)
# Accionar primer boton de aceptar gestión información
driver.find_element_by_css_selector('button.qc-cmp-button').click()
# Delay para que carguen los pop-ups
time.sleep(3)
# Accionar primer boton de guardar y salir
driver.find_element_by_xpath('//button[@class="qc-cmp-button qc-cmp-save-and-exit"]').click()

if (numPag==0):
	
	sel = Selector(text=driver.page_source)
	driver.quit()

else:
	# Iteración para que se carguen las veces necesarias los items de peliculas en página web, accionando boton evento jquery
	for i in range(numPag):

		min = 30*(i+1)
		max = 30*(i+2)
		
		print(f'\n\t\tActualización {i+1} - Cargando películas en posiciones {min}:{max}')

		time.sleep(5)
		driver.find_element_by_xpath('//div[@id="load-more-bt"]').click()

	# Introducimos un time.sleep para dejar que la página cargue y poder cargar en el selector ultimas 30 películas cargadas
	time.sleep(15)
	sel = Selector(text=driver.page_source)
	driver.quit()

# Con página con contenidos cargados, extraermos la URL de cada película y seleccionamos numero de peliculas 
# cuya información a extraer fijadas de antemano
url=sel.css('div.mc-title>a::attr(href)').extract()[:n]
totURL=len(url)

# Guardado de direcciones url para carga en la araña scraperTopFA.py
print(f'\n\tGuardando {totURL} peliculas en lista_urls.csv\n')
df = pd.DataFrame(data={"urls": url})
df.to_csv("lista_urls.csv", sep=',',index=False)
