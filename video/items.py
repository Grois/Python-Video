# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class VideoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 名字
    name = scrapy.Field()
    # 一句话描述
    short_desc = scrapy.Field()
    # 评分
    score = scrapy.Field()
    # 主演
    starts = scrapy.Field()
    # 播放量
    hot = scrapy.Field()
    # 播放地址
    play_url = scrapy.Field()

    # pass
