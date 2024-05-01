#!/usr/bin/env python3
""" File 1 simple pagination
    """
import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple of start and end indices for the given page and page size.

    Args:
        page: An integer representing the page number.
        page_size: An integer representing the size of each page.

    Returns:
        A tuple of two integers representing the start and end indices.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Load the dataset from the CSV file if not already loaded.

        Returns:
            A list of lists representing the dataset.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieve a specific page of data from the dataset.

        Args:
            page: An integer representing the page number (default is 1).
            page_size: An integer representing the size of
            each page (default is 10).

        Returns:
            A list of lists representing the data for the specified page.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start, end = index_range(page, page_size)
        return self.dataset()[start:end]
