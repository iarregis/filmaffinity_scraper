# filmaffinity_scraper

Este repositorio contiene un proyecto para la extracción de información de películas/series del ranking Top FA de Filmaffinity. Con tal de poder realizar este proceso se requiere las instalación de las siguientes librerías:

```
$ pip install pandas
$ pip install scrapy
$ pip install selenium
$ pip install datetime
```

El script deberá ejecutarse por terminal desde el directorio filmaffinity/filmaffinity/spiders de la siguiente manera:

```
$ scrapy runspider scraperTopFa.py
```

Una vez iniciado el funcionamiento de la araña se procederá a la ejecución de sucesiva crearListaUrlFA.py y scraperTopFA.py que generarán un archivo csv en el directorio filmaffinity/'Output Scraper csv', con la información del número de películas/series requerido.
