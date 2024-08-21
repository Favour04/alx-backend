#!/usr/bin/env python3
""" BasicCache module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
          - Assign to the dictionary self.cache_data
          the item value for the key key.
          - If key or item is None, this method should not do anything.
        """
        if key and item:
            self.cache_data.update({key: item})

    def get(self, key):
        """
          - return the value in self.cache_data linked to key.
          - If key is None or if the key doesn’t exist in
          self.cache_data, return None.
        """
        if key and key in self.cache_data:
            return self.cache_data.get(key)
