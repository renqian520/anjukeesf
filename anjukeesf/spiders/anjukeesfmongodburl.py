# -*- coding: utf-8 -*-
from scrapy_redis.spiders import RedisSpider
from anjukeesf.items import Mongodb_xiaoquItem,Mongodb_fangyuanItem,Mongodb_zuItem
import re

class Myspider(RedisSpider):
    name = 'mongodburl'
    custom_settings = {
        'ITEM_PIPELINES':{
            'anjukeesf.pipelines.MongodbPipeline':300,
        }
    }
    redis_key = 'anjuke_esf_spider:start_urls'



    def parse(self, response):
        try:
            item_xiaoqu = Mongodb_xiaoquItem()
            item_fangyuan = Mongodb_fangyuanItem()
            item_zu = Mongodb_zuItem()
            #小区
            if 'community/view/' in response.url:
                item_xiaoqu['esf_xiaoqu_url'] = response.url
                item_xiaoqu['esf_xiaoqu_leimu'] = self.get_esf_xiaoqu_leimu(response)
                item_xiaoqu['esf_xiaoqu_name'] = self.get_esf_xiaoqu_name(response)
                item_xiaoqu['esf_xiaoqu_dizhi'] = self.get_esf_xiaoqu_dizhi(response)
                item_xiaoqu['esf_xiaoqu_junjia'] = self.get_esf_xiaoqu_junjia(response)
                item_xiaoqu['esf_xiaoqu_leixing'] = self.get_esf_xiaoqu_leixing(response)
                item_xiaoqu['esf_xiaoqu_wuyefei'] = self.get_esf_xiaoqu_wuyefei(response)
                item_xiaoqu['esf_xiaoqu_mianji'] = self.get_esf_xiaoqu_mianji(response)
                item_xiaoqu['esf_xiaoqu_hushu'] = self.get_esf_xiaoqu_hushu(response)
                item_xiaoqu['esf_xiaoqu_niandai'] = self.get_esf_xiaoqu_niandai(response)
                item_xiaoqu['esf_xiaoqu_chewei'] = self.get_esf_xiaoqu_chewei(response)
                item_xiaoqu['esf_xiaoqu_rongji'] = self.get_esf_xiaoqu_rongji(response)
                item_xiaoqu['esf_xiaoqu_lvhua'] = self.get_esf_xiaoqu_lvhua(response)
                item_xiaoqu['esf_xiaoqu_kaifashang'] = self.get_esf_xiaoqu_kaifashang(response)
                item_xiaoqu['esf_xiaoqu_wuye'] = self.get_esf_xiaoqu_wuye(response)
                item_xiaoqu['esf_xiaoqu_jwd'] = self.get_esf_xiaoqu_jwd(response)
                yield item_xiaoqu

            #二手房
            if 'prop/view/'in response.url:
                item_fangyuan['esf_fangyuan_url'] = response.url
                item_fangyuan['esf_fangyuan_leimu'] = self.get_esf_fangyuan_leimu(response)
                item_fangyuan['esf_fangyuan_title'] = self.get_esf_fangyuan_title(response)
                item_fangyuan['esf_fangyuan_xiaoqu'] = self.get_esf_fangyuan_xiaoqu(response)
                item_fangyuan['esf_fangyuan_dizhi'] = self.get_esf_fangyuan_dizhi(response)
                item_fangyuan['esf_fangyuan_niandai'] = self.get_esf_fangyuan_niandai(response)
                item_fangyuan['esf_fangyuan_leixing'] = self.get_esf_fangyuan_leixing(response)
                item_fangyuan['esf_fangyuan_fangxing'] = self.get_esf_fangyuan_fangxing(response)
                item_fangyuan['esf_fangyuan_mianji'] = self.get_esf_fangyuan_mianji(response)
                item_fangyuan['esf_fangyuan_chaoxiang'] = self.get_esf_fangyuan_chaoxiang(response)
                item_fangyuan['esf_fangyuan_louceng'] = self.get_esf_fangyuan_louceng(response)
                item_fangyuan['esf_fangyuan_zhuangxiu'] = self.get_esf_fangyuan_zhuangxiu(response)
                item_fangyuan['esf_fangyuan_danjia'] = self.get_esf_fangyuan_danjia(response)
                item_fangyuan['esf_fangyuan_shoufu'] = self.get_esf_fangyuan_shoufu(response)
                item_fangyuan['esf_fangyuan_yuegong'] = self.get_esf_fangyuan_yuegong(response)
                item_fangyuan['esf_fangyuan_shijian'] = self.get_esf_fangyuan_shijian(response)
                item_fangyuan['esf_fangyuan_jjr'] = self.get_esf_fangyuan_jjr(response)
                item_fangyuan['esf_fangyuan_dianhua'] = self.get_esf_fangyuan_dianhua(response)
                yield item_fangyuan

            #租房
            if 'fangyuan/' in response.url or 'rent/' in response.url:
                item_zu['esf_zu_url'] = response.url
                item_zu['esf_zu_leimu'] = self.get_esf_zu_leimu(response)
                item_zu['esf_zu_title'] = self.get_esf_zu_title(response)
                item_zu['esf_zu_zujin'] = self.get_esf_zu_zujin(response)
                item_zu['esf_zu_yafu'] = self.get_esf_zu_yafu(response)
                item_zu['esf_zu_fangxing'] = self.get_esf_zu_fangxing(response)
                item_zu['esf_zu_fangshi'] = self.get_esf_zu_fangshi(response)
                item_zu['esf_zu_xiaoqu'] = self.get_esf_zu_xiaoqu(response)
                item_zu['esf_zu_dizhi'] = self.get_esf_zu_dizhi(response)
                item_zu['esf_zu_zhuangxiu'] = self.get_esf_zu_zhuangxiu(response)
                item_zu['esf_zu_mianji'] = self.get_esf_zu_mianji(response)
                item_zu['esf_zu_chaoxiang'] = self.get_esf_zu_chaoxiang(response)
                item_zu['esf_zu_louceng'] = self.get_esf_zu_louceng(response)
                item_zu['esf_zu_leixing'] = self.get_esf_zu_leixing(response)
                item_zu['esf_zu_pro'] = self.get_esf_zu_pro(response)
                item_zu['esf_zu_content'] = self.get_esf_zu_content(response)
                yield item_zu
        except:
            pass

    #小区
    def get_esf_xiaoqu_leimu(self,response):
        try:
            li = []
            for box in response.xpath('//div[@class="p_1180 p_crumbs"]'):
                lei = box.xpath('.//a/text()').extract()
                for i in lei:
                    mu = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;|&gt;', '', str(i))).strip().replace(' ', '')
                    if len(mu):
                        li.append(mu)
                        leimu = '>'.join(li)
                    else:
                        leimu = 'NULL'
                return leimu
        except:
            return 'NULL'
    def get_esf_xiaoqu_name(self,response):
        try:
            name = re.compile('<h1>(.*?)<span class="', re.S).findall(response.text)
            for i in name:
                if len(i):
                    name = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;', '', str(i))).strip().replace(' ','')
                    name = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;', '', str(name))).strip().replace(' ', '')
                else:
                    name = 'NULL'
                return name
            if len(name) == 0:
                return 'NULL'
        except:
            return 'NULL'
    def get_esf_xiaoqu_dizhi(self,response):
        try:
            dizhi = re.compile('<span class="sub-hd">(.*?)</span>', re.S).findall(response.text)
            for i in dizhi:
                if len(i):
                    dizhi = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;', '', str(i))).strip().replace(' ','')
                    dizhi = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;', '', str(dizhi))).strip().replace(' ', '')
                else:
                    dizhi = 'NULL'
                return dizhi
            if len(dizhi) == 0:
                return 'NULL'
        except:
            return 'NULL'
    def get_esf_xiaoqu_junjia(self,response):
        try:
            junjia = re.compile('"comm_midprice":"(.*?)","area_midprice"', re.S).findall(response.text)
            for i in junjia:
                if len(i):
                    junjia = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;', '', str(i))).strip().replace(' ','')
                    junjia = '均价'+str(re.sub('<.*?>|\\n|{1，7}|&nbsp;', '', str(junjia))).strip().replace(' ', '')+'元/m²'
                else:
                    esf_xiaoqu_junjia = 'NULL'
                return junjia
            if len(junjia) == 0:
                return 'NULL'
        except:
            return 'NULL'
    def get_esf_xiaoqu_leixing(self,response):
        try:
            leixing = re.compile('物业类型：</dt><dd>(.*?)</dd>', re.S).findall(response.text)
            for i in leixing:
                if len(i):
                    leixing = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;', '', str(i))).strip().replace(' ','')
                    leixing = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;', '', str(leixing))).strip().replace(' ', '')
                else:
                    leixing = 'NULL'
                return leixing
            if len(leixing) == 0:
                return 'NULL'
        except:
            return 'NULL'
    def get_esf_xiaoqu_wuyefei(self,response):
        try:
            wuyefei = re.compile('物业费：</dt><dd class="other-dd">(.*?)</dd>', re.S).findall(response.text)
            for i in wuyefei:
                if len(i):
                    wuyefei = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;', '', str(i))).strip().replace(' ','')
                    wuyefei = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;', '', str(wuyefei))).strip().replace(' ', '')
                else:
                    wuyefei = 'NULL'
                return wuyefei
            if len(wuyefei) == 0:
                return 'NULL'
        except:
            return 'NULL'
    def get_esf_xiaoqu_mianji(self, response):
        try:
            mianji = re.compile('总建面积：</dt><dd>(.*?)</dd>', re.S).findall(response.text)
            for i in mianji:
                if len(i):
                    mianji = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;', '', str(i))).strip().replace(' ', '')
                    mianji = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;', '', str(mianji))).strip().replace(' ', '')
                else:
                    mianji = 'NULL'
                return mianji
            if len(mianji) == 0:
                return 'NULL'
        except:
            return 'NULL'
    def get_esf_xiaoqu_hushu(self,response):
        try:
            hushu = re.compile('总户数：</dt><dd class="other-dd">(.*?)</dd>', re.S).findall(response.text)
            for i in hushu:
                if len(i):
                    hushu = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;', '', str(i))).strip().replace(' ','')
                    hushu = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;', '', str(hushu))).strip().replace(' ', '')
                else:
                    hushu = 'NULL'
                return hushu
            if len(hushu) == 0:
                return 'NULL'
        except:
            return 'NULL'
    def get_esf_xiaoqu_niandai(self,response):
        try:
            nianxian = re.compile('建造年代：</dt><dd>(.*?)</dd>', re.S).findall(response.text)
            for i in nianxian:
                if len(i):
                    nianxian = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;', '', str(i))).strip().replace(' ','')
                    nianxian = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;', '', str(nianxian))).strip().replace(' ', '')
                else:
                    nianxian = 'NULL'
                return nianxian
            if len(nianxian) == 0:
                return 'NULL'
        except:
            return 'NULL'
    def get_esf_xiaoqu_chewei(self,response):
        try:
            chewei = re.compile('停车位：</dt><dd class="other-dd">(.*?)</dd>', re.S).findall(response.text)
            for i in chewei:
                if len(i):
                    chewei = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;', '', str(i))).strip().replace(' ','')
                    chewei = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;', '', str(chewei))).strip().replace(' ', '')
                else:
                    chewei = 'NULL'
                return chewei
            if len(chewei) == 0:
                return 'NULL'
        except:
            return 'NULL'
    def get_esf_xiaoqu_rongji(self,response):
        try:
            rongji = re.compile('容&nbsp;&nbsp;积&nbsp;&nbsp;率：</dt><dd>(.*?)</dd>', re.S).findall(response.text)
            for i in rongji:
                if len(i):
                    rongji = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;', '', str(i))).strip().replace(' ','')
                    rongji = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;', '', str(rongji))).strip().replace(' ', '')
                else:
                    rongji = 'NULL'
                return rongji
            if len(rongji) == 0:
                return 'NULL'
        except:
            return 'NULL'
    def get_esf_xiaoqu_lvhua(self,response):
        try:
            lvhua = re.compile('绿化率：</dt><dd class="other-dd">(.*?)</dd>', re.S).findall(response.text)
            for i in lvhua:
                if len(i):
                    lvhua = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;', '', str(i))).strip().replace(' ','')
                    lvhua = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;', '', str(lvhua))).strip().replace(' ', '')
                else:
                    lvhua = 'NULL'
                return lvhua
            if len(lvhua) == 0:
                return 'NULL'
        except:
            return 'NULL'
    def get_esf_xiaoqu_kaifashang(self,response):
        try:
            kaifashang = re.compile('开&nbsp;&nbsp;发&nbsp;&nbsp;商：</dt><dd class="dd-column">(.*?)</dd>', re.S).findall(response.text)
            for i in kaifashang:
                if len(i):
                    kaifashang = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;', '', str(i))).strip().replace(' ','')
                    kaifashang = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;', '', str(kaifashang))).strip().replace(' ', '')
                else:
                    kaifashang = 'NULL'
                return kaifashang
            if len(kaifashang) == 0:
                return 'NULL'
        except:
            return 'NULL'
    def get_esf_xiaoqu_wuye(self,response):
        try:
            wuye = re.compile('物业公司：</dt><dd class="dd-column">(.*?)</dd>', re.S).findall(response.text)
            for i in wuye:
                if len(i):
                    wuye = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;', '', str(i))).strip().replace(' ','')
                    wuye = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;', '', str(wuye))).strip().replace(' ', '')
                else:
                    wuye = 'NULL'
                return wuye
            if len(wuye) == 0:
                return 'NULL'
        except:
            return 'NULL'
    def get_esf_xiaoqu_jwd(self,response):
        try:
            jwd = re.compile('point : {(.*?)},', re.S).findall(response.text)
            for i in jwd:
                if len(i):
                    jwd = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;', '', str(i))).strip().replace(' ','')
                    jwd = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;', '', str(jwd))).strip().replace(' ', '')
                else:
                    jwd = 'NULL'
                return jwd
            if len(jwd) == 0:
                return 'NULL'
        except:
            return 'NULL'

    #房源
    def get_esf_fangyuan_leimu(self,response):
        try:
            li = []
            for box in response.xpath('//div[@class="p_1180 p_crumbs"]'):
                lei = box.xpath('.//a/text()').extract()
                for i in lei:
                    mu = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;|&gt;', '', str(i))).strip().replace(' ', '')
                    if len(mu):
                        li.append(mu)
                        leimu = '>'.join(li)
                    else:
                        leimu = 'NULL'
                return leimu
        except:
            return 'NULL'
    def get_esf_fangyuan_title(self,response):
        try:
            title = re.compile('<h3 class="long-title">(.*?)</h3>', re.S).findall(response.text)
            for i in title:
                if len(i):
                    title = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;', '', str(i))).strip().replace(' ','')
                    title = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;', '', str(title))).strip().replace(' ', '')
                else:
                    title = 'NULL'
                return title
            if len(title) == 0:
                return 'NULL'
        except:
            return 'NULL'
    def get_esf_fangyuan_xiaoqu(self,response):
        try:
            xiaoqu = re.compile('小区：(.*?)</dl>', re.S).findall(response.text)
            for i in xiaoqu:
                if len(i):
                    xiaoqu = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;', '', str(i))).strip().replace(' ','')
                    xiaoqu = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;', '', str(xiaoqu))).strip().replace(' ', '')
                else:
                    xiaoqu = 'NULL'
                return xiaoqu
            if len(xiaoqu) == 0:
                return 'NULL'
        except:
            return 'NULL'
    def get_esf_fangyuan_dizhi(self,response):
        try:
            dizhi = re.compile('位置：(.*?)</dd>', re.S).findall(response.text)
            for i in dizhi:
                if len(i):
                    dizhi = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;|&#xE003;|\t', '', str(i))).strip().replace(' ','')
                    dizhi = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;|&#xE003;|\t', '', str(dizhi))).strip().replace(' ', '')
                else:
                    dizhi = 'NULL'
                return dizhi
            if len(dizhi) == 0:
                return 'NULL'
        except:
            return 'NULL'
    def get_esf_fangyuan_niandai(self,response):
        try:
            niandai = re.compile('年代：</dt><dd>(.*?)</dd>', re.S).findall(response.text)
            for i in niandai:
                if len(i):
                    niandai = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;', '', str(i))).strip().replace(' ','')
                    niandai = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;', '', str(niandai))).strip().replace(' ', '')
                else:
                    niandai = 'NULL'
                return niandai
            if len(niandai) == 0:
                return 'NULL'
        except:
            return 'NULL'
    def get_esf_fangyuan_leixing(self,response):
        try:
            leixing = re.compile('类型：</dt><dd>(.*?)</dd>', re.S).findall(response.text)
            for i in leixing:
                if len(i):
                    leixing = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;', '', str(i))).strip().replace(' ','')
                    leixing = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;', '', str(leixing))).strip().replace(' ', '')
                else:
                    leixing = 'NULL'
                return leixing
            if len(leixing) == 0:
                return 'NULL'
        except:
            return 'NULL'
    def get_esf_fangyuan_fangxing(self,response):
        try:
            fangxing = re.compile('房型：</dt><dd>(.*?)</dd>', re.S).findall(response.text)
            for i in fangxing:
                if len(i):
                    fangxing = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;|\t', '', str(i))).strip().replace(' ','')
                    fangxing = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;|\t', '', str(fangxing))).strip().replace(' ', '')
                else:
                    fangxing = 'NULL'
                return fangxing
            if len(fangxing) == 0:
                return 'NULL'
        except:
            return 'NULL'
    def get_esf_fangyuan_mianji(self, response):
        try:
            mianji = re.compile('面积：</dt><dd>(.*?)</dd>', re.S).findall(response.text)
            for i in mianji:
                if len(i):
                    mianji = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;', '', str(i))).strip().replace(' ', '')
                    mianji = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;', '', str(mianji))).strip().replace(' ', '')
                else:
                    mianji = 'NULL'
                return mianji
            if len(mianji) == 0:
                return 'NULL'
        except:
            return 'NULL'
    def get_esf_fangyuan_chaoxiang(self, response):
        try:
            chaoxiang = re.compile('朝向：</dt><dd>(.*?)</dd>', re.S).findall(response.text)
            for i in chaoxiang:
                if len(i):
                    chaoxiang = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;', '', str(i))).strip().replace(' ', '')
                    chaoxiang = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;', '', str(chaoxiang))).strip().replace(' ', '')
                else:
                    chaoxiang = 'NULL'
                return chaoxiang
            if len(chaoxiang) == 0:
                return 'NULL'
        except:
            return 'NULL'
    def get_esf_fangyuan_louceng(self, response):
        try:
            louceng = re.compile('楼层：</dt><dd>(.*?)</dd>', re.S).findall(response.text)
            for i in louceng:
                if len(i):
                    louceng = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;', '', str(i))).strip().replace(' ', '')
                    louceng = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;', '', str(louceng))).strip().replace(' ', '')
                else:
                    louceng = 'NULL'
                return louceng
            if len(louceng) == 0:
                return 'NULL'
        except:
            return 'NULL'
    def get_esf_fangyuan_zhuangxiu(self, response):
        try:
            zhuangxiu = re.compile('装修程度：</dt><dd>(.*?)</dd>', re.S).findall(response.text)
            for i in zhuangxiu:
                if len(i):
                    zhuangxiu = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;', '', str(i))).strip().replace(' ', '')
                    zhuangxiu = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;', '', str(zhuangxiu))).strip().replace(' ', '')
                else:
                    zhuangxiu = 'NULL'
                return zhuangxiu
            if len(zhuangxiu) == 0:
                return 'NULL'
        except:
            return 'NULL'
    def get_esf_fangyuan_danjia(self, response):
        try:
            danjia = re.compile('房屋单价：</dt><dd>(.*?)</dd>', re.S).findall(response.text)
            for i in danjia:
                if len(i):
                    danjia = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;', '', str(i))).strip().replace(' ', '')
                    danjia = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;', '', str(danjia))).strip().replace(' ', '')
                else:
                    danjia = 'NULL'
                return danjia
            if len(danjia) == 0:
                return 'NULL'
        except:
            return 'NULL'
    def get_esf_fangyuan_shoufu(self, response):
        try:
            shoufu = re.compile('参考首付：</dt><dd>(.*?)</dd>', re.S).findall(response.text)
            for i in shoufu:
                if len(i):
                    shoufu = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;', '', str(i))).strip().replace(' ', '')
                    shoufu = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;', '', str(shoufu))).strip().replace(' ', '')
                else:
                    shoufu = 'NULL'
                return shoufu
            if len(shoufu) == 0:
                return 'NULL'
        except:
            return 'NULL'
    def get_esf_fangyuan_yuegong(self, response):
        try:
            yuegong = re.compile('参考月供：</dt>(.*?)</dd>', re.S).findall(response.text)
            for i in yuegong:
                if len(i):
                    yuegong = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;', '', str(i))).strip().replace(' ', '')
                    yuegong = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;', '', str(yuegong))).strip().replace(' ', '')
                else:
                    yuegong = 'NULL'
                return yuegong
            if len(yuegong) == 0:
                return 'NULL'
        except:
            return 'NULL'
    def get_esf_fangyuan_shijian(self, response):
        try:
            shijian = re.compile('发布时间：(.*?)</span>', re.S).findall(response.text)
            for i in shijian:
                if len(i):
                    shijian = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;', '', str(i))).strip().replace(' ', '')
                    shijian = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;', '', str(shijian))).strip().replace(' ', '')
                else:
                    shijian = 'NULL'
                return shijian
            if len(shijian) == 0:
                return 'NULL'
        except:
            return 'NULL'
    def get_esf_fangyuan_jjr(self, response):
        try:
            jjr = re.compile('class="brokerInfo">(.*?)<span', re.S).findall(response.text)
            for i in jjr:
                if len(i):
                    jjr = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;|&#xE048;', '', str(i))).strip().replace(' ', '')
                    jjr = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;|&#xE048;', '', str(jjr))).strip().replace(' ', '')
                else:
                    jjr = 'NULL'
                return jjr
            if len(jjr) == 0:
                return 'NULL'
        except:
            return 'NULL'
    def get_esf_fangyuan_dianhua(self, response):
        try:
            dianhua = re.compile('<span class="mobile">(.*?)</span>', re.S).findall(response.text)
            for i in dianhua:
                if len(i):
                    dianhua = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;', '', str(i))).strip().replace(' ', '')
                    dianhua = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;', '', str(dianhua))).strip().replace(' ', '')
                else:
                    dianhua = 'NULL'
                return dianhua
            if len(dianhua) == 0:
                return 'NULL'
        except:
            return 'NULL'

    # 租房
    def get_esf_zu_leimu(self,response):
        try:
            li = []
            for box in response.xpath('//div[@class="p_1180 p_crumbs"]'):
                lei = box.xpath('.//a/text()').extract()
                for i in lei:
                    mu = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;|&gt;', '', str(i))).strip().replace(' ', '')
                    if len(mu):
                        li.append(mu)
                        leimu = '>'.join(li)
                    else:
                        leimu = 'NULL'
                return leimu
        except:
            return 'NULL'
    def get_esf_zu_title(self,response):
        try:
            title = re.compile('<h3>(.*?)</h3>', re.S).findall(response.text)
            for i in title:
                if len(i):
                    title = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;', '', str(i))).strip().replace(' ','')
                    title = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;', '', str(title))).strip().replace(' ', '')
                else:
                    title = 'NULL'
                return title
            if len(title) == 0:
                title_a = re.compile('<h3 class="fl">(.*?)</h3>', re.S).findall(response.text)
                for i in title_a:
                    if len(i):
                        title_a = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;', '', str(i))).strip().replace(' ', '')
                        title_a = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;', '', str(title_a))).strip().replace(' ', '')
                    else:
                        title_a = 'NULL'
                    return title_a
                if len(title_a) == 0:
                    return 'NULL'
        except:
            return 'NULL'
    def get_esf_zu_zujin(self, response):
        try:
            zujin = re.compile('租金</dt>(.*?)</dl>', re.S).findall(response.text)
            for i in zujin:
                if len(i):
                    zujin = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;', '', str(i))).strip().replace(' ', '')
                    zujin = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;', '', str(zujin))).strip().replace(' ', '')
                else:
                    zujin = 'NULL'
                return zujin
            if len(zujin) == 0:
                return 'NULL'
        except:
            return 'NULL'
    def get_esf_zu_yafu(self, response):
        try:
            yafu = re.compile('租金押付</dt>(.*?)</dl>', re.S).findall(response.text)
            for i in yafu:
                if len(i):
                    yafu = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;', '', str(i))).strip().replace(' ', '')
                    yafu = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;', '', str(yafu))).strip().replace(' ', '')
                else:
                    yafu = 'NULL'
                return yafu
            if len(yafu) == 0:
                return 'NULL'
        except:
            return 'NULL'
    def get_esf_zu_fangxing(self,response):
        try:
            fangxing = re.compile('房型</dt>(.*?)</dl>', re.S).findall(response.text)
            for i in fangxing:
                if len(i):
                    fangxing = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;', '', str(i))).strip().replace(' ','')
                    fangxing = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;', '', str(fangxing))).strip().replace(' ', '')
                else:
                    fangxing = 'NULL'
                return fangxing
            if len(fangxing) == 0:
                return 'NULL'
        except:
            return 'NULL'
    def get_esf_zu_fangshi(self,response):
        try:
            fangshi = re.compile('租赁方式</dt>(.*?)</dd>', re.S).findall(response.text)
            for i in fangshi:
                if len(i):
                    fangshi = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;', '', str(i))).strip().replace(' ','')
                    fangshi = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;', '', str(fangshi))).strip().replace(' ', '')
                else:
                    fangshi = 'NULL'
                return fangshi
            if len(fangshi) == 0:
                return 'NULL'
        except:
            return 'NULL'
    def get_esf_zu_xiaoqu(self,response):
        try:
            xiaoqu = re.compile('所在小区</dt>(.*?)</dl>', re.S).findall(response.text)
            for i in xiaoqu:
                if len(i):
                    xiaoqu = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;', '', str(i))).strip().replace(' ','')
                    xiaoqu = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;', '', str(xiaoqu))).strip().replace(' ', '')
                else:
                    xiaoqu = 'NULL'
                return xiaoqu
            if len(xiaoqu) == 0:
                return 'NULL'
        except:
            return 'NULL'
    def get_esf_zu_dizhi(self,response):
        try:
            dizhi = re.compile('位置</dt>(.*?)</dl>', re.S).findall(response.text)
            for i in dizhi:
                if len(i):
                    dizhi = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;', '', str(i))).strip().replace(' ','')
                    dizhi = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;', '', str(dizhi))).strip().replace(' ', '')
                else:
                    dizhi = 'NULL'
                return dizhi
            if len(dizhi) == 0:
                return 'NULL'
        except:
            return 'NULL'
    def get_esf_zu_zhuangxiu(self, response):
        try:
            zhuangxiu = re.compile('装修</dt>(.*?)</dd>', re.S).findall(response.text)
            for i in zhuangxiu:
                if len(i):
                    zhuangxiu = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;', '', str(i))).strip().replace(' ', '')
                    zhuangxiu = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;', '', str(zhuangxiu))).strip().replace(' ', '')
                else:
                    zhuangxiu = 'NULL'
                return zhuangxiu
            if len(zhuangxiu) == 0:
                return 'NULL'
        except:
            return 'NULL'
    def get_esf_zu_mianji(self, response):
        try:
            mianji = re.compile('面积</dt>(.*?)</dd>', re.S).findall(response.text)
            for i in mianji:
                if len(i):
                    mianji = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;', '', str(i))).strip().replace(' ', '')
                    mianji = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;', '', str(mianji))).strip().replace(' ', '')
                else:
                    mianji = 'NULL'
                return mianji
            if len(mianji) == 0:
                return 'NULL'
        except:
            return 'NULL'
    def get_esf_zu_chaoxiang(self, response):
        try:
            chaoxiang = re.compile('朝向</dt>(.*?)</dd>', re.S).findall(response.text)
            for i in chaoxiang:
                if len(i):
                    chaoxiang = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;', '', str(i))).strip().replace(' ', '')
                    chaoxiang = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;', '', str(chaoxiang))).strip().replace(' ', '')
                else:
                    chaoxiang = 'NULL'
                return chaoxiang
            if len(chaoxiang) == 0:
                return 'NULL'
        except:
            return 'NULL'
    def get_esf_zu_louceng(self, response):
        try:
            louceng = re.compile('楼层</dt>(.*?)</dd>', re.S).findall(response.text)
            for i in louceng:
                if len(i):
                    louceng = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;', '', str(i))).strip().replace(' ', '')
                    louceng = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;', '', str(louceng))).strip().replace(' ', '')
                else:
                    louceng = 'NULL'
                return louceng
            if len(louceng) == 0:
                return 'NULL'
        except:
            return 'NULL'
    def get_esf_zu_leixing(self,response):
        try:
            leixing = re.compile('类型</dt>(.*?)</dd>', re.S).findall(response.text)
            for i in leixing:
                if len(i):
                    leixing = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;', '', str(i))).strip().replace(' ','')
                    leixing = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;', '', str(leixing))).strip().replace(' ', '')
                else:
                    leixing = 'NULL'
                return leixing
            if len(leixing) == 0:
                return 'NULL'
        except:
            return 'NULL'
    def get_esf_zu_pro(self,response):
        try:
            pro = re.compile('配置：(.*?)</p>', re.S).findall(response.text)
            for i in pro:
                if len(i):
                    pro = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;', '', str(i))).strip().replace(' ','')
                    pro = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;', '', str(pro))).strip().replace(' ', '')
                else:
                    pro = 'NULL'
                return pro
            if len(pro) == 0:
                return 'NULL'
        except:
            return 'NULL'
    def get_esf_zu_content(self,response):
        try:
            content = re.compile('"pro_con wb">(.*?)</div>', re.S).findall(response.text)
            for i in content:
                if len(i):
                    content = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;|\t|\r', '', str(i))).strip().replace(' ','')
                    content = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;|\t|\r', '', str(content))).strip().replace(' ', '')
                else:
                    content = 'NULL'
                return content
            if len(content) == 0:
                return 'NULL'
        except:
            return 'NULL'