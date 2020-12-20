# Blockchain

import hashlib
import time
from datetime import datetime


class Block:

    def __init__(self, index, data, previous_hash):
        """
        Constructor for the Block class.
        :param index:           Unique ID of the block
        :param data:            String
        :param previous_hash:   Hash of the previous Blockchain block
        """
        self.index = index
        self.data = data
        self.previous_hash = previous_hash
        self.timestamp = datetime.utcnow().strftime("%H:%M:%S %#m/%#d/%Y")  # Timestamp generated on Windows.
        self.hash = self.calc_hash()
        self.next = None  # to handle collisions

    def calc_hash(self):
        """
        Generates a hash based on class constructor.
        :return: sha256 hash string
        """
        sha = hashlib.sha256()
        sha.update(str(self.__dict__).encode('utf-8'))

        return sha.hexdigest()

    def __repr__(self):
        s = "\n"
        s += "        Index: {}\n".format(self.index)
        s += "    Timestamp: {}\n".format(self.timestamp)
        s += "         Data: \"{}\"\n".format(self.data)
        s += "  SHA256 Hash: {}\n".format(self.hash)
        s += "Previous Hash: {}\n".format(self.previous_hash)
        return s


class Blockchain:

    def __init__(self, initial_size=10):
        """
        Constructor for the Blockchain class.
        :param initial_size: Integer size of Hash Map Bucket array.
        """
        self.head = Block(0, "", 0)  # initialize
        self.tail = self.head  # to assign previous hash to subsequent Blocks

        self.bucket_array = [None for _ in range(initial_size)]  # Hash Map attributes
        self.p = 37
        self.num_entries = 0
        self.load_factor = 0.7

        bucket_index = self.get_bucket_index(self.head.hash)  # put constructor block in Hash Map
        self.bucket_array[bucket_index] = self.head

    def set(self, value):
        """
        Places a new Block in the Blockchain and Hash Map.

        Hash Map collisions are added to bucket linked list.
        :param value: String
        :return: None
        """
        # make a new block
        previous_hash = self.tail.hash
        new_block = Block(self.tail.index + 1, value, previous_hash)
        self.tail = new_block  # update tail

        # check for collisions and  implement separate chaining to handle collisions
        check_bucket_index = self.get_bucket_index(new_block.hash)
        bucket_head = self.bucket_array[check_bucket_index]
        if self.bucket_array[check_bucket_index]:  # index already contains a Block
            new_block.next = bucket_head  # place the current bucket block next in chain

        # add new_block to Hash Map
        self.bucket_array[check_bucket_index] = new_block
        self.num_entries += 1

        # check load factor
        current_load_factor = self.num_entries / len(self.bucket_array)
        if current_load_factor > self.load_factor:
            self.num_entries = 0
            self._rehash()

        return

    def get(self, key):
        """
        Retrieve Block from provided hash. Return -1 if non-existent.
        :param key: Block hash.
        :return: Block
        """
        if key == 0:  # origin block
            return self.head
        bucket_index = self.get_bucket_index(key)
        bucket_head = self.bucket_array[bucket_index]
        while bucket_head is not None:  # check separate chain for key
            if bucket_head.hash == key:
                return bucket_head
            bucket_head = bucket_head.next
        return -1

    def get_bucket_index(self, key):
        """
        Returns the Hash Map bucket index of key.
        :param key: Block hash.
        :return: Integer index of Block hash.
        """
        bucket_index = self.get_hash_code(key)
        return bucket_index

    def get_hash_code(self, key):
        """
        Returns an integer based on key to be used as the Hash Map bucket index.
        :param key: Hash
        :return: Integer derived from key.
        """
        key = str(key)
        num_buckets = len(self.bucket_array)
        current_coefficient = 1
        hash_code = 0
        for character in key:
            hash_code += ord(character) * current_coefficient
            hash_code = hash_code % num_buckets  # compress hash_code
            current_coefficient *= self.p
            current_coefficient = current_coefficient % num_buckets  # compress coefficient

        return hash_code % num_buckets  # one last compression before returning

    def _rehash(self):
        old_num_buckets = len(self.bucket_array)
        old_bucket_array = self.bucket_array
        num_buckets = 2 * old_num_buckets
        self.bucket_array = [None for _ in range(num_buckets)]
        for key, block in enumerate(old_bucket_array):
            if block:
                # cannot create new Block or block hashes will change so only the bucket index needs to be rehashed
                while block is not None:  # traverse Separate Chain to rehash every Block
                    self.num_entries += 1
                    next_link = block.next  # store rest of old chain (if any)
                    block.next = None  # cut old separate chain

                    new_bucket_index = self.get_bucket_index(block.hash)  # generate a new bucket index

                    # collision handling
                    if self.bucket_array[new_bucket_index] is not None:  # bucket is occupied
                        block.next = self.bucket_array[new_bucket_index]  # add occupied bucket to separate chain

                    self.bucket_array[new_bucket_index] = block  # store block in bucket
                    block = next_link  # continue down the block separate chain

    def view_hash_map(self):
        """
        Returns a string representation of the Hash Map.
        :return: String
        """
        output = "\nHash Map:"
        for bucket_index, bucket in enumerate(self.bucket_array):
            if bucket is None:
                output += '\n[{}] '.format(bucket_index)
            else:
                bucket_head = self.bucket_array[bucket_index]
                while bucket_head is not None:  # check Linked List for key# time.sleep(1)
                    output += '\n[{}]'.format(bucket_index)
                    output += ' ({}|{}|{}|{}|{}) '.format(bucket_head.index,
                                                          bucket_head.timestamp,
                                                          bucket_head.data,
                                                          bucket_head.hash,
                                                          bucket_head.previous_hash)
                    bucket_head = bucket_head.next
        return output

    def __repr__(self):
        s = "END OF BLOCK CHAIN\n"
        tail = self.tail
        count = self.tail.index
        while count > 0:
            s += tail.__repr__()
            s += "       |\n"
            s += "       |\n"
            s += "      \|/"
            tail = self.get(tail.previous_hash)
            count -= 1
        s += self.head.__repr__()
        s += "\nBEGINNING OF BLOCK CHAIN\n"
        return s


if __name__ == "__main__":

    #  Functional test
    B = Blockchain()
    for _ in range(5):
        B.set("New block:{}".format(_ + 1))
    print(B.view_hash_map())
    print(B)

    # No Block data test
    C = Blockchain()
    C.set("")
    print(C.view_hash_map())
    print(C)

    # Empty Blockchain test

    D = Blockchain()
    print(D.view_hash_map())
    print(D)

    # Rehash and collision test

    B = Blockchain()
    for _ in range(100):
        B.set("New block:{}".format(_ + 1))
    print(B.view_hash_map())
    print(B)

