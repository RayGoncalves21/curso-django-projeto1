from unittest import TestCase

from ut.pagination import make_pagination_range


class PaginationTest(TestCase):
    def test_make_pagination_range_returns_a_pagination_range(self):
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=1,
        )['pagination']

        self.assertEqual([1, 2, 3, 4], pagination)

    def test_first_range_is_static_if_current_page_is_less_than_middle_page(self):  # noqa: E501

        # Currente page = 1 - QTY = 2 - middle page = 2

        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=1,
        )['pagination']

        self.assertEqual([1, 2, 3, 4], pagination)

        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=2,
        )['pagination']

        self.assertEqual([1, 2, 3, 4], pagination)

        # Currente page = 3 - QTY = 2 - middle page = 2
        # here range should chage

        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=3,
        )['pagination']

        self.assertEqual([2, 3, 4, 5], pagination)

        # Currente page = 4 - QTY = 2 - middle page = 2
        # here range should chage

        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=4,
        )['pagination']

        self.assertEqual([3, 4, 5, 6], pagination)

    def test_make_sure_middle_ranges_are_corrects(self):  # noqa: E501

        # Currente page = 10 - QTY = 2 - middle page = 2
        # here range should chage

        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=10,
        )['pagination']

        self.assertEqual([9, 10, 11, 12], pagination)

        # Currente page = 12 - QTY = 2 - middle page = 2
        # here range should chage

        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=12,
        )['pagination']

        self.assertEqual([11, 12, 13, 14], pagination)

    def test_make_pagination_range_is_static_when_last_page_is_next(self):
        # Currente page = 18 - QTY = 2 - middle page = 2
        # here range should chage

        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=19,
        )['pagination']

        self.assertEqual([17, 18, 19, 20], pagination)

        # Currente page = 19 - QTY = 2 - middle page = 2
        # here range should chage

        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=19,
        )['pagination']

        self.assertEqual([17, 18, 19, 20], pagination)

        # Currente page = 20 - QTY = 2 - middle page = 2
        # here range should chage

        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=20,
        )['pagination']

        self.assertEqual([17, 18, 19, 20], pagination)

        # Currente page = 21 - QTY = 2 - middle page = 2
        # here range should chage

        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=21,
        )['pagination']

        self.assertEqual([17, 18, 19, 20], pagination)

    def test_make_pagination_uses_page_1_if_page_query_is_valid(self):
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=1,

        )['pagination']
        self.assertEqual([1, 2, 3, 4], pagination)
