#!/usr/bin/env python
# coding:utf-8

from baike_spider import url_manager
from baike_spider import html_downloader
from baike_spider import html_parser
from baike_spider import html_outputer

class SpiderMain(object):

    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1
        # 先添加起始url到url管理器
        self.urls.add_new_url(root_url)
        # 循环抓取 如果url管理器中有新的url,循环就继续
        while self.urls.has_new_url():
            try:
                # 得到一个新的url
                new_url = self.urls.get_new_url()
                print '%d : %s' % (count, new_url)
                # 将url放到下载器下载内容
                html_cont = self.downloader.download(new_url)
                # 将下载好的内容中的url 和 其他数据分别解释,保存到new_urls,和new_data
                new_urls, new_data = self.parser.parser(new_url, html_cont)
                print '-----'
                print len(new_urls)
                print '》》》'
                print new_data
                # 将新找到的若干url添加到url管理器,注意这里的函数是add_new_urls,表示添加多条数据
                self.urls.add_new_urls(new_urls)
                # 将找到的内容收集起来
                self.outputer.collect_data(new_data)

                # 爬取100条是停止爬取
                if count == 100:
                    break

                count = count+1
            except Exception, e:
                print e
                print "craw failed!"

        # 最后将所有收集好的数据输出
        self.outputer.output_html()

if __name__ == '__main__':
    root_url = "http://baike.baidu.com/view/21087.htm"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)


