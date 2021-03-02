import hashlib
from datetime import datetime

class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.previous_block = None
      self.hash = self.calc_hash(self.data)

    def calc_hash(self, data):
        sha = hashlib.sha256()
        hash_str = data.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()
    
    # check if data has been tempered with (and so does match the hash value)
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


    def validate_chain(self):
      # empty chain is trivially valid
      if self.size == 0:
        return True
      # chain with single block has no connection to previous blocks
      if self.size == 1:
        return self.latest_block.validate_block()
      # for chains with size > 1, check (1) that blocks have not been tempered with 
      # and (2) that they link correctly to previous blocks in the chain
      current_block = self.latest_block
      previous_block = current_block.previous_block
      while previous_block is not None:
        print(previous_block.hash == current_block.previous_hash)
        if not current_block.validate_block():
          return False
        if not previous_block.hash == current_block.previous_hash:
          return False
        current_block = previous_block
        previous_block = current_block.previous_block
      return True