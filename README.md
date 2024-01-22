# Cuckoo Hash

This is a simple implementation of a Cuckoo Hash in Python.

## Usage

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

## Tests

```bash
python3 project1_tests.py
```
