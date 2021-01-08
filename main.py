'''
Author: shadow3zz
Date: 2021-01-07 20:32:11
LastEditTime: 2021-01-07 20:48:40
Description: file content
'''
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

if __name__ == '__main__':
    process = CrawlerProcess(get_project_settings())
    process.crawl('shipxy')    #  你需要将此处的spider_name替换为你自己的爬虫名称
    process.start()