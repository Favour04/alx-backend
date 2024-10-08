#!/usr/bin/env python3
"""
pagination
"""

import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Init function
        """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
            returns page
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page > 0
        start, end = self.index_range(page, page_size)
        return self.dataset()[start: end]

    def index_range(self, page, page_size) -> (int, int):
        """
            returns the vailable index range
        """
        return page_size * (page - 1), page_size * page
