import unittest
from cuckoo_hash_24 import CuckooHash24


class TestCuckooHash24(unittest.TestCase):
    def setUp(self):
        self.init_size = 3
        self.cuckoo = CuckooHash24(self.init_size)

    def test_insert_empty_bucket(self):
        self.assertIsNone(self.cuckoo.tables[0][0])
        self.assertTrue(self.cuckoo.insert(1))
        self.assertIsNotNone(self.cuckoo.tables[0][self.cuckoo.hash_func(1, 0)])

    def test_cycle_threshold_one(self):
        self.init_size = 10
        self.cuckoo = CuckooHash24(self.init_size)
        threshold = 71
        for i in range(threshold):
            self.assertTrue(self.cuckoo.insert(i))
        self.assertFalse(self.cuckoo.insert(threshold))

    def test_cycle_threshold_two(self):
        self.init_size = 20
        self.cuckoo = CuckooHash24(self.init_size)
        threshold = 142
        for i in range(threshold):
            self.assertTrue(self.cuckoo.insert(i))
        self.assertFalse(self.cuckoo.insert(threshold))

    def test_insert_duplicate(self):
        self.assertTrue(self.cuckoo.insert(1))
        self.assertTrue(self.cuckoo.insert(1))
        self.assertTrue(self.cuckoo.insert(2))
        self.assertTrue(self.cuckoo.insert(2))
        # check whether the duplicate keys are in the same bucket
        self.assertEqual(self.cuckoo.tables[0][self.cuckoo.hash_func(1, 0)],
                         self.cuckoo.tables[0][self.cuckoo.hash_func(2, 0)])


if __name__ == "__main__":
    unittest.main()
