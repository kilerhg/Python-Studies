import scrapy

# Primeiro Web Scraping com Scrapy
# Site:
# Objetivo: Entrar no site aosfatos e verificar todas as noticias buscando, o titulo, data, citação, verdadeira ou falsa

class AosFatosSpider(scrapy.Spider):
    name = 'aos_fatos'

    start_urls = ['https://aosfatos.org/']

    def parse(self, response):
        links = response.xpath('//nav//ul//li/a[re:test(@href, "checamos")]/@href').getall()
        for link in links:
            yield scrapy.Request(
                response.urljoin(link),
                callback=self.parse_category
            )

    def parse_category(self, response):
        import ipdb; ipdb.set_trace()
        pass
