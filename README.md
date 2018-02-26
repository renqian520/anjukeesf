# anjukeesf
安居客二手房、租房（Scrapy、Redis）

基于Python+scrapy+redis+mongodb的分布式爬虫实现框架

scrapy runspider anjukeesfredisurl.py  主要功能是抓取种子url，保存到redis

scrapy runspider anjukeesfmongodburl.py  主要是从redis里面读url，解析数据保存到mongodb （拓展到其他机器,修改REDIS_HOST = "主机ip"，都是从redis里面读url,MONGODB_HOST = "存储服务器ip"）

middlewares.ProxyMiddleware  使用阿布云代理服务器轮换请求IP 


                                                 安居客二手房房源信息mongodb图示
![安居客二手房房源信息](https://github.com/renqian520/anjukeesf/blob/master/%E5%AE%89%E5%B1%85%E5%AE%A2%E4%BA%8C%E6%89%8B%E6%88%BF%E6%88%BF%E6%BA%90%E4%BF%A1%E6%81%AF.jpg)


                                                 安居客二手房小区信息mongodb图示
![安居客二手房小区信息](https://github.com/renqian520/anjukeesf/blob/master/%E5%AE%89%E5%B1%85%E5%AE%A2%E4%BA%8C%E6%89%8B%E6%88%BF%E5%B0%8F%E5%8C%BA%E4%BF%A1%E6%81%AF.jpg)



                                                 安居客租房房源信息mongodb图示
![安居客租房房源信息](https://github.com/renqian520/anjukeesf/blob/master/%E5%AE%89%E5%B1%85%E5%AE%A2%E7%A7%9F%E6%88%BF%E6%88%BF%E6%BA%90%E4%BF%A1%E6%81%AF.jpg)
