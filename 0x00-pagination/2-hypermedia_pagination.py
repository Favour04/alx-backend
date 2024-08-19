import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
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
        assert isinstance(page, int) and  page > 0
        assert isinstance(page_size, int) and page > 0
        start, end = self.index_range(page, page_size)
        return self.dataset()[start: end]

    def index_range(self, page, page_size) -> (int, int):
        return page_size * (page - 1), page_size * page

    def get_hyper(self, page: int = 1, page_size: int = 10):
        assert isinstance(page, int) and  page > 0
        assert isinstance(page_size, int) and page > 0
        total_page, rem = self.total_pages(page_size)
        start, end = self.index_range(page, page_size)
        page_size = self.page_size(page_size, page) 
        prev_page = page - 1
        next_page = page + 1
        if prev_page == 0:
            prev_page = None
        if total_page < next_page:
            next_page = None

    def total_pages(self, page_size):
        tln = len(self.dataset())
        if tln % page_size != 0:
            return int(tln / page_size) + 1, tln % page_size
        else:
             return int(tln / page_size), 0

    def page_size(self, page_size, page_no):
        tlp, rem = self.total_pages(page_size)
        if page_no == tlp and rem > 0:
            return rem
        else:
            return page_size
            

