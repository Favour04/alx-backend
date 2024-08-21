#!/usr/bin/env python3
""" FIFOCache module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
        Contains the FIFO algorithm for caching
    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
          - Assign to the dictionary self.cache_data
          the item value for the key key.
          - If key or item is None, this method
          should not do anything.
          - If the number of items in self.cache_data
          is higher that BaseCaching.MAX_ITEMS:

            - Discard the first item put in cache (FIFO algorithm)
            - Print DISCARD: with the key discarded and following by a new line
        """
        if key and item:
            if len(self.cache_data) < BaseCaching.MAX_ITEMS:
                self.cache_data.update({key: item})
            if key in self.cache_data.keys():
                self.cache_data.pop(key)
                self.cache_data.update({key: item})
            else:
                keys = list(self.cache_data.keys())
                self.cache_data.pop(keys[0])
                self.cache_data.update({key: item})
                print(f"DISCARD: {keys[0]}")

    def get(self, key):
        """
          - return the value in self.cache_data linked to key.
          - If key is None or if the key doesn’t exist in
          self.cache_data, return None.
        """
        if key and key in self.cache_data:
            return self.cache_data.get(key)
