import os
import json
class HashTable:
  def __init__(self):
    self.size = 0
    self.users=[]
    self.slots = [None] * self.size
    self.data = [None] * self.size

  def LoadUsers(self):
    availableFiles = os.listdir()
    if "users.json" in availableFiles:
      with open("users.json") as file:
        users = json.load(file)
        for key in users:
          self.size=self.size+1
          self.users.append(key)
        return self.size

  def put(self, key, data):
    hashvalue = self.hashfunction(key, len(self.slots))

    if self.slots[hashvalue] == None:
      self.slots[hashvalue] = key
      self.data[hashvalue] = data
    else:
      if self.slots[hashvalue] == key:
        self.data[hashvalue] = data
      else:
        nextslot = self.rehash(hashvalue, len(self.slots))
        while self.slots[nextslot] != None and \
                self.slots[nextslot] != key:
          nextslot = self.rehash(nextslot, len(self.slots))

        if self.slots[nextslot] == None:
          self.slots[nextslot] = key
          self.data[nextslot] = data
        else:
          self.data[nextslot] = data  # replace

  def hashfunction(self, key, size):
    return key % size

  def rehash(self, oldhash, size):
    return (oldhash + 1) % size

  def get(self, key):
    startslot = self.hashfunction(key, len(self.slots))
    data = None
    stop = False
    found = False
    position = startslot
    while self.slots[position] != None\
            and not found and not stop:
      if self.slots[position] == key:
        found = True
        data = self.data[position]
      else:
        position = self.rehash(position, len(self.slots))
        if position == startslot:
          stop = True
    return data

  def __getitem__(self, key):
    return self.get(key)

  def __setitem__(self, key, data):
    self.put(key, data)

def main():
  hashtable=HashTable()
  hashtable.LoadUsers()
  for name in range(hashtable.size):
    key=hashtable.users[name]
    ascii=0
    for c in key:
      ascii = ord(c)+ascii
      hashtable[ascii]=key
  print( hashtable.users)

main()