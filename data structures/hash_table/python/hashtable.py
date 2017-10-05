
#!/usr/bin/python

"""
 Hash Table implementation

 Load Factor = num of items / tablesize
"""


class HashTable():

    def __init__(self):
        self.size = 11
        self.buckets = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        hashvalue = self.hashfunction(key, len(self.buckets))

        if self.buckets[hashvalue] == None:
            self.buckets[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.buckets[hashvalue] == key:
                self.data[hashvalue] = data
            else:
                nextbucket = self.rehash(hashvalue, len(self.buckets))
                while self.buckets[nextbucket] is not None and \
                        self.buckets[nextbucket] is not key:
                    nextbucket = self.rehash(nextbucket, len(self.buckets))

                if self.buckets[nextbucket] == None:
                    self.buckets[nextbucket] = key
                    self.data[nextbucket] = data
                else:
                    self.data[nextbucket] = data

    def hashfunction(self, key, size):
        return key % size

    def rehash(self, oldhash, size):
        return (oldhash + 1) % size

    def get(self, key):
        startbucket = self.hashfunction(key, len(self.buckets))
        data = None
        stop = False
        found = False
        position = startbucket
        while self.buckets[position] is not None and \
                not found and not stop:
            if self.buckets[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.buckets))
                if position == startbucket:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)
