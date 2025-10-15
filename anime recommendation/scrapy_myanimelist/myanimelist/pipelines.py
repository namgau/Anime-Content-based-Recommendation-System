# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import os
import numpy as np
from myanimelist.items import AnimeItem, ReviewItem, ProfileItem
# from pymongo import MongoClient

class ProcessPipeline(object):
    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        pass

    def process_item(self, item, spider):
        item_class = item.__class__.__name__

        if item_class == "AnimeItem":
            item = self.process_anime(item)
        elif item_class == "ReviewItem":
            item = self.process_review(item)
        elif item_class == "ProfileItem":
            item = self.process_profile(item)

        return item

    def process_anime(self, item):
        # Xử lý score
        score = item.get('score')
        if not score or score == 'N/A':
            item['score'] = np.nan
        else:
            item['score'] = float(str(score).replace("\n", "").strip())

        # Xử lý ranked
        ranked = item.get('ranked')
        if not ranked or ranked == 'N/A':
            item['ranked'] = np.nan
        else:
            item['ranked'] = int(str(ranked).replace("#", "").strip())

        # Xử lý popularity
        popularity = item.get('popularity')
        if popularity:
            item['popularity'] = int(str(popularity).replace("#", "").strip())
        else:
            item['popularity'] = np.nan

        # Xử lý members
        members = item.get('members')
        if members:
            item['members'] = int(str(members).replace(",", "").strip())
        else:
            item['members'] = np.nan

        # Xử lý episodes
        episodes = item.get('episodes')
        if episodes:
            item['episodes'] = str(episodes).replace(",", "").strip()
        else:
            item['episodes'] = None

        return item

    def process_review(self, item):
        score = item.get('score')
        if score:
            item['score'] = float(str(score).replace("\n", "").strip())
        else:
            item['score'] = np.nan
        return item

    def process_profile(self, item):
        return item


class SaveLocalPipeline(object):
    def open_spider(self, spider):
        os.makedirs('data/', exist_ok=True)

        self.files = {
            'AnimeItem': open('data/animes.json', 'w', encoding='utf-8'),
            'ReviewItem': open('data/reviews.json', 'w', encoding='utf-8'),
            'ProfileItem': open('data/profiles.json', 'w', encoding='utf-8'),
        }

        # Viết mở đầu mảng JSON
        for f in self.files.values():
            f.write('[')
            self.first_item = True

    def close_spider(self, spider):
        # Viết đóng mảng JSON
        for f in self.files.values():
            f.write(']')
            f.close()

    def process_item(self, item, spider):
        item_class = item.__class__.__name__
        self.save(item_class, item)
        return item

    def save(self, item_class, item):
        f = self.files[item_class]
        if f.tell() > 1:  # Nếu không phải phần tử đầu tiên
            f.write(',\n')
        json.dump(dict(item), f, ensure_ascii=False, indent=2)