# Cuckoo Hash

Cuckoo Hash is a hash table that resolves collisions by using two hash functions and two tables. If a collision occurs, the key is moved to the other table. If the other table is full, the key is moved to the other table and the key that was there is moved to the first table. This process is repeated until there are no collisions.

This project implements two variations of the Cuckoo Hashing algorithm.

## Variations

1. **CuckooHash**: This is the standard implementation of the Cuckoo Hashing algorithm. The implementation can be found in [cuckoo_hash.py](cuckoo_hash.py).
2. **CuckooHash24**: This is a modified version of the Cuckoo Hashing algorithm. This has two tables but each slot in the table can hold upto 4 keys. The implementation can be found in [cuckoo_hash_24.py](cuckoo_hash_24.py).
3. **CuckooHashAssessment**: This is a modified version of the Cuckoo Hashing algorithm. This has only one table but 4 slots per table and uses two hash functions. The implementation can be found in [cuckoo_hash_assess.py](cuckoo_hash_assess.py).

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

This project requires Python 3.11 or higher (although it may work with older versions of Python 3).

### Usage

```python
from cuckoo_hash import CuckooHash


cuckoo_hash = CuckooHash(10)
cuckoo_hash.insert(1)
cuckoo_hash.insert(2)

cuckoo_hash.lookup(1) # True
cuckoo_hash.lookup(2) # True

cuckoo_hash.delete(1)
cuckoo_hash.lookup(1) # False
```
