# -*- coding: utf-8 -*-

# Scrapy settings for job_hunter project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'job_hunter'

SPIDER_MODULES = ['job_hunter.spiders']
NEWSPIDER_MODULE = 'job_hunter.spiders'

ITEM_PIPELINES = {'job_hunter.pipelines.Process_VC_Items' : 2,
                  'job_hunter.pipelines.Retrieve_URLs' : 3}


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'job_hunter (+http://www.yourdomain.com)'
