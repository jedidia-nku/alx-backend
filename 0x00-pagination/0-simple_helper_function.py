#!/usr/bin/env python3

"""
Module to provide pagination range.
"""

from typing import Tuple

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Function to return a tuple containing start and end index for pagination.

    Args:
    page (int): The current page number (1-indexed).
    page_size (int): The number of items per page.

    Returns:
    Tuple[int, int]: A tuple containing the start index and end index for the pagination.
    """

    start_index = (page - 1) * page_size

    end_index = page * page_size
    
    return start_index, end_index
   