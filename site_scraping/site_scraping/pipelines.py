# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import re

class Process_VC_Items(object):
    def process_item(self, item, spider):

        for key in item.keys():
            item['vc_url'] = re.match("https?://[www\.]?[a-zA-Z]*\.[a-zA-Z]{3}", item[key]['url']).group(0)
                            
        print type(item)
        return item



from scrapy.http import HtmlResponse
from scrapy import Selector
import connections

class Decide_to_Store_or_Continue(object):
    
    def find_external_urls(page_text, page_xpath):
        self.external_page_links = Selector(text=self.page_body).xpath(page_xpath).re('https?://[www\.]?[a-zA-Z]*\.[a-zA-Z]{3}.*')
        

    def find_internal_urls(page_text, page_xpath):
        self.internal_page_links = Selector(text=self.page_body).xpath('//ul/li/a/@href').re('/.*')
        
    
    def ensure_value_exists(select_query, insert_query):
        cursor = mysql.mysql_query(select_query, fetch=True)
        if not cursor:
            mysql.mysql_query(insert_query)
        else:
            #returns primary key
            return cursor[0][0]

    def ensure_company_exists(url):
        select_query = ("SELECT company_id FROM company_list WHERE url = {}").format(url)
        insert_query = ("INSERT INTO company_list SET url = {}").format(url)
        company_id = ensure_value_exists(select_query, insert_query)
        return company_id


    def ensure_company_rels_exist(first_company, second_company):
        select_query = ("SELECT relationship_id FROM vc_clients WHERE vc_id = {} AND company_id = {}").format(first_company, second_company)
        insert_query = ("INSERT INTO vc_clients SET vc_id = {} AND company_id = {}").format(first_company, second_company)
        relationship_id = ensure_value_exists(select_query, insert_query)
        return relationship_id

    def store_or_continue():
        find_external_urls()
        find_internal_urls()
        if len(self.external_page_links) > len(self.internal_page_links):
            self.store == True
        else: 
            self.store == False
        
        #this should eventually use super() on the functions that use this
        if store:
            return True
        else:
            return False

            

class Retrieve_URLs(Decide_to_Store_or_Continue):
    def process_item(self, item, spider):
        for key in item.keys():
            if key != 'companies_page':
                return item
            else:
                self.key = key

        self.page_body = item[self.key]['body']
        self.current_site_id = ensure_company_exists(item[self.key]['vc_url'])
        store = store_or_continue()
        
        if store:
            for url in self.external_urls:
                external_id = ensure_company_exists(url)
                relationship_id = ensure_company_rels_exist(self.current_site_id, external_id)

        else:
            #run scrape
            print "needed to run a scrape for:"
            print item['url']
            
            


import json


##This is a test class
class JsonWriterPipeline(object):

    def __init__(self):
        self.file = open('items.jl', 'wb')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        
        self.file.write(line)
        
        print item
        return item
