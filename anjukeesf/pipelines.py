# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import pymongo
import redis
from scrapy.exceptions import DropItem
import anjukeesf.settings as settings
from anjukeesf.items import Mongodb_xiaoquItem,Mongodb_fangyuanItem,Mongodb_zuItem,RedisItem,Redis_esfItem,Redis_zuItem

class RedisPipeline(object):
    def __init__(self):
        self.redis_db = redis.Redis(host=settings.REDIS_HOST,port=settings.REDIS_PORT,db=settings.REDIS_DB)
        self.redis_table = settings.MY_REDIS
    def process_item(self, item, spider):
        if isinstance(item, RedisItem):
            if self.redis_db.exists(item['url']):
                raise DropItem('%s is exist!' %(item['url']))
            else:
                self.redis_db.lpush(self.redis_table,item['url'])
        if isinstance(item, Redis_esfItem):
            if self.redis_db.exists(item['esf_url']):
                raise DropItem('%s is exist!' %(item['esf_url']))
            else:
                self.redis_db.lpush(self.redis_table,item['esf_url'])
        if isinstance(item, Redis_zuItem):
            if self.redis_db.exists(item['zu_url']):
                raise DropItem('%s is exist!' %(item['zu_url']))
            else:
                self.redis_db.lpush(self.redis_table,item['zu_url'])
        return item


class MongodbPipeline(object):
    def __init__(self):
        self.conn = pymongo.MongoClient('mongodb://{}:{}'.format(settings.MONGODB_HOST,settings.MONGODB_PORT))
        self.db = self.conn[settings.MONGODB_DB]
        self.dc_xiaoqu = self.db[settings.MONGODB_DC_xiaoqu]
        self.dc_fangyuan = self.db[settings.MONGODB_DC_fangyuan]
        self.dc_zu = self.db[settings.MONGODB_DC_zu]

    def process_item(self, item, spider):
        if isinstance(item,Mongodb_xiaoquItem):
            if self.site_xiaoqu_exist(item):
                self.dc_xiaoqu.insert(dict(item))
            else:
                raise DropItem('%s is exist!' %(item['esf_xiaoqu_url']))
            return item
        if isinstance(item,Mongodb_fangyuanItem):
            if self.site_fangyuan_exist(item):
                self.dc_fangyuan.insert(dict(item))
            else:
                raise DropItem('%s is exist!' %(item['esf_fangyuan_url']))
            return item
        if isinstance(item,Mongodb_zuItem):
            if self.site_zu_exist(item):
                self.dc_zu.insert(dict(item))
            else:
                raise DropItem('%s is exist!' %(item['esf_zu_url']))
            return item

    def site_xiaoqu_exist(self,item):
        if self.dc_xiaoqu.find_one({'esf_xiaoqu_url':item['esf_xiaoqu_url']}):
            return False
        else:
            return True
    def site_fangyuan_exist(self,item):
        if self.dc_fangyuan.find_one({'esf_fangyuan_url':item['esf_fangyuan_url']}):
            return False
        else:
            return True
    def site_zu_exist(self,item):
        if self.dc_zu.find_one({'esf_zu_url':item['esf_zu_url']}):
            return False
        else:
            return True