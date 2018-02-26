# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class RedisItem(scrapy.Item):
    url = scrapy.Field()

class Redis_esfItem(scrapy.Item):
    esf_url = scrapy.Field()

class Redis_zuItem(scrapy.Item):
    zu_url = scrapy.Field()

#二手房——小区
class Mongodb_xiaoquItem(scrapy.Item):
    esf_xiaoqu_url = scrapy.Field() # https://hangzhou.anjuke.com/community/view/220591
    esf_xiaoqu_leimu = scrapy.Field() # 首页>杭州小区>余杭小区>临平小区>君临天下
    esf_xiaoqu_name = scrapy.Field()  # 君临天下
    esf_xiaoqu_dizhi = scrapy.Field()  # 余杭-临平-东湖南路364号
    esf_xiaoqu_junjia = scrapy.Field()  # 均价23205元/m²
    esf_xiaoqu_leixing = scrapy.Field()  # 物业类型：暂无数据
    esf_xiaoqu_wuyefei = scrapy.Field()  # 物业费：2.60元/平米/月
    esf_xiaoqu_mianji = scrapy.Field()  # 总建面积：暂无数据
    esf_xiaoqu_hushu = scrapy.Field()  # 总户数：暂无数据
    esf_xiaoqu_niandai = scrapy.Field()  # 建造年代：2005年
    esf_xiaoqu_chewei = scrapy.Field()  # 停车位：暂无数据
    esf_xiaoqu_rongji = scrapy.Field()  # 容积率：2.43
    esf_xiaoqu_lvhua = scrapy.Field()  # 绿化率：42%(高)
    esf_xiaoqu_kaifashang = scrapy.Field()  # 开发商：浙江华鼎房地产开发有限公司
    esf_xiaoqu_wuye = scrapy.Field()  # 物业公司：广东中奥物业管理有限公司
    esf_xiaoqu_jwd = scrapy.Field() #小区经纬度 lat : "30.410377",lng : "120.317801"



#二手房——房源
class Mongodb_fangyuanItem(scrapy.Item):
    esf_fangyuan_url = scrapy.Field() # https://hangzhou.anjuke.com/prop/view/A1071975110
    esf_fangyuan_leimu = scrapy.Field()  # 杭州房产网>杭州二手房>上城二手房>南星二手房>绿城春江花月
    esf_fangyuan_title = scrapy.Field()  # 精装三房保养好《南北通透》《小区绿化好》周边配套齐全！
    esf_fangyuan_xiaoqu = scrapy.Field() # 小区：绿城春江花月
    esf_fangyuan_dizhi = scrapy.Field()  # 位置：上城-南星- 钱江路158号
    esf_fangyuan_niandai = scrapy.Field()  # 年代：2005年
    esf_fangyuan_leixing = scrapy.Field()  # 类型：普通住宅
    esf_fangyuan_fangxing = scrapy.Field()  # 房型：3室2厅2卫
    esf_fangyuan_mianji = scrapy.Field()  # 面积：160平方米
    esf_fangyuan_chaoxiang = scrapy.Field()  # 朝向：南
    esf_fangyuan_louceng = scrapy.Field()  # 楼层：低层(共19层)
    esf_fangyuan_zhuangxiu = scrapy.Field()  # 装修程度：精装修
    esf_fangyuan_danjia = scrapy.Field()  # 房屋单价：46662 元/m²
    esf_fangyuan_shoufu = scrapy.Field()  # 参考首付：225.00万
    esf_fangyuan_yuegong = scrapy.Field()  # 参考月供：34358元
    esf_fangyuan_shijian = scrapy.Field() # 发布时间：2017年12月18日
    esf_fangyuan_jjr = scrapy.Field() # 经纪人 黄伟伟
    esf_fangyuan_dianhua = scrapy.Field() # 经纪人电话 156 5712 3213

 #租房
class Mongodb_zuItem(scrapy.Item):
    esf_zu_url = scrapy.Field() # https://hz.zu.anjuke.com/fangyuan/1118629308
    esf_zu_leimu = scrapy.Field()  # 杭州安居客>杭州租房>余杭租房>瓶窑租房>信达柳郡
    esf_zu_title = scrapy.Field() #君临天下 地铁口高档单身公寓 精装拎包入住只要2800
    esf_zu_zujin = scrapy.Field()  # 2800元/月
    esf_zu_yafu = scrapy.Field()  # 租金押付 面议
    esf_zu_fangxing = scrapy.Field()  # 房型 1室1厅1卫
    esf_zu_fangshi = scrapy.Field()  # 租赁方式 整租
    esf_zu_xiaoqu = scrapy.Field()  # 所在小区 君临天下
    esf_zu_dizhi = scrapy.Field()  # 位置 余杭 临平
    esf_zu_zhuangxiu = scrapy.Field()  # 装修 精装修
    esf_zu_mianji = scrapy.Field()  # 面积 55平米
    esf_zu_chaoxiang = scrapy.Field()  # 朝向 南
    esf_zu_louceng = scrapy.Field()  # 楼层 12/32
    esf_zu_leixing = scrapy.Field()  # 类型 公寓
    esf_zu_pro = scrapy.Field()  # 配置： 冰箱 电视 洗衣机 热水器
    esf_zu_content = scrapy.Field()  # 1、装修精美，拎包入住






