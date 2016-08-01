#!/usr/bin/env python
# coding:utf-8


class UrlManager(object):

    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def has_new_url(self):
        return len(self.new_urls) != 0

    def get_new_url(self):
        new_url = self.new_urls.pop()
        print 'new url:'+new_url
        print self.new_urls
        self.old_urls.add(new_url)
        print self.old_urls
        return new_url

    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)
            print 'add new url success!'
            print self.new_urls

    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            print '****'
            print url
            self.add_new_url(url)
            print 'add new urls success!'
            print urls