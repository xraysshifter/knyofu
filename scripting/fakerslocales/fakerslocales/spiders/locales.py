import scrapy


class LocalesSpider(scrapy.Spider):
    name = "locales"
    allowed_domains = ["fakerjs.dev"]
    start_urls = ["https://fakerjs.dev/guide/localization.html"]

    def parse(self, response):
        locales = response.css('.vp-doc._guide_localization td code').getall()
        with open('allfakerslocales.txt', 'w') as file:
            for locale in locales :
                temp = locale.split('<code>')
                clean_locale = [ele.split('</code>') for ele in temp]
                file.write(f"{clean_locale[1][0]}\n")
