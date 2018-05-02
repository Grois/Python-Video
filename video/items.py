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
    stars = scrapy.Field()
    # 播放量
    hot = scrapy.Field()
    # 播放地址
    play_url = scrapy.Field()
    # 图片
    img = scrapy.Field()
    # 别名
    alias = scrapy.Field()
    # 导演
    director = scrapy.Field()
    # tag
    tags = scrapy.Field()
    # 简介
    description = scrapy.Field()
    # 播放时间
    play_time = scrapy.Field()

