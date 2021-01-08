'''
Author: shadow3zz
Date: 2021-01-07 20:19:50
LastEditTime: 2021-01-08 13:38:52
Description: file content
'''
import scrapy
import datetime
import os


class OdenSpider(scrapy.Spider):
    # 定制化设置
    name = 'shipxy'
    allowed_domains = ['www.shipxy.com']
    host = "http://weixin.shipxy.com/"

    headerData = {
        "Origin": "http://weixin.shipxy.com/",
        "Connection": "keep-alive",
        "Referer": "http://weixin.shipxy.com/shipxy/map/",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    }

    # 爬虫运行的起始位置
    # 第一步：爬取CEDA登录页面
    def start_requests(self):
        print("start shipxy clawer")
        # 登录页面
        dataPage = "http://weixin.shipxy.com/Openapi/GetShip"
        loginIndexReq = scrapy.FormRequest(
            url=dataPage,
            headers=self.headerData,
            method="POST",
            
            # post的具体数据
            formdata={
                "mmsi": "413795795"
            },
            callback=self.Parse
        )
        yield loginIndexReq


    # 第三步：解析响应内容
    def Parse(self, response):
        print(response.json())

    # 请求错误处理：可以打印，写文件，或者写到数据库中
    def errorHandle(self, failure):
        print(f"request error: {failure.value.response}")

    # 爬虫运行完毕时的收尾工作，例如：可以打印信息，可以发送邮件
    def closed(self, reason):
        # 爬取结束的时候可以发送邮件
        finishTime = datetime.datetime.now()
        subject = f"clawerName had finished, reason = {reason}, finishedTime = {finishTime}"

    def parse(self, response, **kwargs):
        pass
