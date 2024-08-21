#!/usr/bin/env python3
"""
    Simple function
"""


def index_range(page, page_size):
    """
        Return page and page size
    """
    return page_size * (page - 1), page * page_size
