#!/usr/bin/env python3
"""A class that uses FIFO caching algorithm"""
from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """A class that stores and evicts data in a cache using FIFO algorithm"""
    def __init__(self):
        """Starts the cache"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds a value in dictionary acting as a cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(False)
            print("DISCARD:", first_key)

    def get(self, key):
        """This function gets a value using key"""
        return self.cache_data.get(key, None)
