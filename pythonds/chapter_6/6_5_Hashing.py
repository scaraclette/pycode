''' 
    Creating a hash table class
1. Collision resolution uses linear probing with plus 1 rehash function
'''

class HashTable:
    def __init__(self):
        self.size = 11
        # Slots hold key items
        self.slots = [None] * self.size
        # data holds associated data value with slots
        self.data = [None] * self.size

    def put(self, key, data):
        hashValue = self.hashFunction(key, len(self.slots))

        # Puts if empty on slot
        if self.slots[hashValue] == None:
            self.slots[hashValue] = key
            self.data[hashValue] = data
        else:
            if self.slots[hashValue] == key:
                self.data[hashValue] = data # replace data if key is same
            else:
                nextSlot = self.rehash(hashValue, len(self.slots))
                # Find different slot
                while self.slots[nextSlot] != None and self.slots[nextSlot] != key:
                    nextSlot = self.rehash(nextSlot, len(self.slots))

                if self.slots[nextSlot] == None:
                    self.slots[nextSlot] = key
                    self.data[nextSlot] = data
                else:
                    self.data[nextSlot] = data # replace

    def hashFunction(self, key, size):
        return key % size

    def rehash(self, oldhash, size):
        return (oldhash + 1) % size

    def get(self, key):
        startSlot = self.hashFunction(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = startSlot

        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == startSlot:
                    stop = True
        
        return data

    def __getitem__(self, key):
        return self.get(key)
    
    # Overloading method
    def __setitem__(self, key, data):
        self.put(key, data)

    def __str__(self):
        result = "{"
        for i in range(self.size):
            if self.slots[i] != None:
                if i == self.size - 1:
                    result += str(self.slots[i]) + ": " + self.data[i]
                else:    
                    result += str(self.slots[i]) + ": " + self.data[i] + ", "

        return result + "}"

def client():
    H=HashTable()
    H[54]="cat"
    H[26]="dog"
    H[93]="lion"
    H[17]="tiger"
    H[77]="bird"
    H[31]="cow"
    H[44]="goat"
    H[55]="pig"
    H[20]="chicken"
    print(H.slots)
    print(H.data)
    print(H)

client()