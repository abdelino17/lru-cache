# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest

from lrucache import LRUCache

CACHE_CAPACITY = 3


class TestLRUCache(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.lruCache = LRUCache(CACHE_CAPACITY)

    def test_cache(self):
        self.lruCache.put("1", "1")
        self.lruCache.put("2", "2")
        self.lruCache.put("3", "3")

        self.assertEqual(self.lruCache.get("1"), "1")
        self.assertEqual(self.lruCache.get("3"), "3")

        self.lruCache.put("4", "4")
        self.assertEqual(self.lruCache.get("2"), -1)

        self.lruCache.put("5", "5")
        self.assertEqual(self.lruCache.get("1"), -1)


if __name__ == '__main__':
    unittest.main()
