#!/usr/bin/env python3
"""This is a cache system that uses MRU algorithm"""
from collections import OrderedDict
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """This is a class that stores, gets and evicts a value
    using the MRU cache algorithm"""
    def __init__(self):
        """starts a cache"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """This function adds and evcts a value in a cache"""
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                mru_key, _ = self.cache_data.popitem(False)
                print("DISCARD:", mru_key)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """Gets a value using a key"""
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
