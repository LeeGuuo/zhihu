# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class ZhihuuserItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = Field()
    name = Field()
    avatar_url = Field()
    answer_count = Field()
    follower_count = Field()
    type = Field()
    url_token = Field()
    gender = Field()
    allow_message = Field()
    user_type = Field()
    headline = Field()
