import hashlib
from datetime import datetime

def calc_hash(self):
      sha = hashlib.sha256()

      hash_str = "We are going to encode this string of data!".encode('utf-8')

      sha.update(hash_str)

      return sha.hexdigest()

class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()


class Blockchain:
  
    def __init___(self):
      self.latest_block = None
      self.size = 0

    def append(self, data):
      timestamp = datetime.now()
      if self.latest_block is None:
        self.latest_block = Block(timestamp, data, None)
      else:
        self.latest_block = Block(timestamp, data, self.latest_block.previous_hash)
      self.size += 1

