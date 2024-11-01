#!/usr/bin/env python3
"""A caching system using LIFO algorithm"""
from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    """This class uses LIFO algorithm to store and evict data
    in a cache system"""
    def __init__(self):
        """Starts the cache"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """This function adds a value in a dictionary acting as a cache"""
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                last_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", last_key)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """This code gets an item using a key"""
        return self.cache_data.get(key, None)
