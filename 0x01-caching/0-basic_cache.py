#!/usr/bin/env python3
"""A caching system"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """A class that stores and retrieves data from a dictionary"""
    def put(self, key, item):
        """Adds a value in a dictionary acting as a cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """This gets a value using a key"""
        return self.cache_data.get(key, None)
