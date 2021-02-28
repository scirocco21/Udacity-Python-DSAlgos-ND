import hashlib
from datetime import datetime

class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash(self.data)

    def calc_hash(self, data):
        sha = hashlib.sha256()
        hash_str = data.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()
    
    def validate_block(self):
      return self.hash == self.calc_hash(self.data)


class Blockchain:
  
    def __init__(self):
      self.latest_block = None
      self.size = 0

    def append(self, data):
      timestamp = datetime.now()
      if self.latest_block is None:
        self.latest_block = Block(timestamp, data, None)
      else:
        self.latest_block = Block(timestamp, data, self.latest_block.previous_hash)
      self.size += 1

