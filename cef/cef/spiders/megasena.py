# -*- coding: utf-8 -*-
import scrapy


class MegasenaSpider(scrapy.Spider):
    name = 'megasena'
    allowed_domains = ['loterias.caixa.gov.br/wps/portal/loterias/landing/megasena/']
    start_urls = ['http://loterias.caixa.gov.br/wps/portal/loterias/landing/megasena//']

    def parse(self, response):
        pass
