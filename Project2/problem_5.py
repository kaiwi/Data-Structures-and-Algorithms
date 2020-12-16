# Blockchain

import hashlib
from datetime import datetime
import json


class Block:

    def __init__(self, index, data, previous_hash):
        self.data = data
        self.index = index
        self.previous_hash = str(previous_hash)
        self.timestamp = datetime.utcnow().strftime("%H:%M %#m/%#d/%Y")  # Timestamp generated on Windows.

    def calc_hash(self):
        """
        Generates a hash based on class attributes.
        :return: sha256
        """
        sha = hashlib.sha256()
        sha.update(str(self.__dict__).encode('utf-8'))

        return sha.hexdigest()

    def __repr__(self):
        s = "Timestamp: {}\n".format(self.timestamp)
        s += "Data: \"{}\"\n".format(self.data)
        s += "SHA256 Hash: {}\n".format(self.calc_hash())
        s += "Prev_Hash: {}\n".format(self.previous_hash)
        return s


class Blockchain:

    def __init__(self, initial_size=10):
        self.head = None  # Linked List
        self.bucket_array = [None for _ in range(initial_size)]  # Hash Map
        self.p = 31
        self.num_blocks = 0
        # add rehashing?
        self.load_factor = 0.7

    def set(self, block):
        pass

    def get(self, key):
        pass

    def get_bucket_index(self, key):
        pass

    def get_hash_code(self, key):
        pass

    def _rehash(self):
        pass


if __name__ == "__main__":
    # tests
    test = "Hello world!"
    a = Block(0, test, 0)
    print(a)
    pass
