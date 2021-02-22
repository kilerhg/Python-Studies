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
        news = response.css('a.card::attr(href)').getall()
        for new_url in news:
            yield scrapy.Request(
                response.urljoin(new_url),
                callback=self.parse_new
            )

    def parse_new(self, response):
        title = response.css('article h1::text').get()
        date = " ".join(response.css('p.publish_date::text').get().split())
        quotes = response.css('article blockquote p')
        for quote in quotes:
            quote_text = quote.css('::text').get()
            status = quote.xpath(
                './parent::blockquote/preceding-sibling::figure//figcaption/text()').get()
            yield {
                'title': title,
                'date': date,
                'quote_text': quote_text,
                'status': status,
                'url': response.url
            }
