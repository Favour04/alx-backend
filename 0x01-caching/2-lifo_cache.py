#!/usr/bin/env python3
""" LIFOCache module
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
        Contains the LIFO algorithm for caching
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

            - Discard the last item put in cache (LIFO algorithm)
            - Print DISCARD: with the key discarded and following by a new line
        """
        if key and item:
            if len(self.cache_data) < BaseCaching.MAX_ITEMS:
                self.cache_data.update({key: item})
            if key in self.cache_data.keys():
                self.cache_data.pop(key)
                self.cache_data.update({key: item})
            else:
                pop_k, pop_v = self.cache_data.popitem()
                self.cache_data.update({key: item})
                print(f"DISCARD: {pop_k}")

    def get(self, key):
        """
          - return the value in self.cache_data linked to key.
          - If key is None or if the key doesn’t exist
          in self.cache_data, return None.
        """
        if key and key in self.cache_data:
            return self.cache_data.get(key)
