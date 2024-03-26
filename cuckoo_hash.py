# explanations for member functions are provided in requirements.py
# each file that uses a cuckoo hash should import it from this file.
import random as rand
from typing import List, Optional


class CuckooHash:
    def __init__(self, init_size: int):
        self.__num_rehashes = 0
        self.CYCLE_THRESHOLD = 10

        self.table_size = init_size
        self.tables = [[None] * init_size for _ in range(2)]

    def hash_func(self, key: int, table_id: int) -> int:
        key = int(str(key) + str(self.__num_rehashes) + str(table_id))
        rand.seed(key)
        return rand.randint(0, self.table_size - 1)

    def get_table_contents(self) -> List[List[Optional[int]]]:
        return self.tables

    # you should *NOT* change any of the existing code above this line
    # you may however define additional instance variables inside the __init__ method.

    def insert(self, key: int) -> bool:
        evictions = 0
        table = 0
        while evictions <= self.CYCLE_THRESHOLD:
            index = self.hash_func(key, table)
            if self.tables[table][index] is None:
                self.tables[table][index] = key
                return True
            else:
                key, self.tables[table][index] = self.tables[table][index], key
                table = (table + 1) % len(self.tables)
                evictions += 1
        return False

    def lookup(self, key: int) -> bool:
        return (
            self.tables[0][self.hash_func(key, 0)] == key
            or self.tables[1][self.hash_func(key, 1)] == key
        )

    def delete(self, key: int) -> None:
        if self.tables[0][self.hash_func(key, 0)] == key:
            self.tables[0][self.hash_func(key, 0)] = None
        elif self.tables[1][self.hash_func(key, 1)] == key:
            self.tables[1][self.hash_func(key, 1)] = None

    def rehash(self, new_table_size: int) -> None:
        self.__num_rehashes += 1
        self.table_size = new_table_size  # do not modify this line

        old_tables = self.tables.copy()
        self.tables = [[None] * new_table_size for _ in range(2)]
        for table in old_tables:
            for key in table:
                if key is not None:
                    self.insert(key)

    # feel free to define new methods in addition to the above
    # fill in the definitions of each required member function (above),
    # and for any additional member functions you define
