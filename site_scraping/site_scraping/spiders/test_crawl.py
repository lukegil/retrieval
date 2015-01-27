import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from job_hunter.items import VC_Item
import hashlib
import re
#vc crawl-- for a given url, find their About pages, Jobs page, and portfolio/companies page

class VC_Crawl(CrawlSpider):
#      def __init__(vc_list):
#            start_urls = vc_list
      #this should be integrated into the __init__ function, so the crawler can be called on a set of vc names

      start_urls = ['https://www.usv.com/']
      name = "vc_crawler"

      xpath_rule = "//*/a[normalize-space(text())={}]"
      xpath_rules = [xpath_rule.format('"About"'), 
                     xpath_rule.format('"About us"'),
                     xpath_rule.format('"Jobs"'), 
                     xpath_rule.format('"Careers"'),
                     xpath_rule.format('"Companies"'), 
                     xpath_rule.format('"Portfolio"'),
                     xpath_rule.format('"Our Portfolio"'), 
                     xpath_rule.format('"Portfolio Companies"')]
      
      rules = (Rule(SgmlLinkExtractor(restrict_xpaths=xpath_rules), callback='parse_vc'),)

      def parse_vc(self, response):

            vc_item = VC_Item()
            item_dic = {'url' : response.url,
                        'md5' : hashlib.md5(response.body).hexdigest(),
                        'body' : response.body}

            print response.url

            if re.match(".*about.*", response.meta['link_text'], re.I) is not None:
                  vc_item['about_page'] = item_dic
            if re.match(".*(job|career).*", response.meta['link_text'], re.I) is not None:
                  vc_item['jobs_page'] = item_dic
            if re.match(".*(companies|portfolio).*", response.meta['link_text'], re.I) is not None:
                  vc_item['companies_page'] = item_dic
                  
            
            return vc_item

      def parse_start_url(self, response):
            vc_item = VC_Item()
            
       


                  
