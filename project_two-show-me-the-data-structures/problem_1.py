from collections import OrderedDict 

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.queue = OrderedDict()
        self.capacity = capacity
        self.size = 0

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key in self.queue:
          # get is a use operation so the item queried for needs to be moved 'up'
          val = self.queue[key]
          del self.queue[key]
          # adding the key back in moves it up in insertion order
          self.queue[key] = val          
          return val
        return - 1

    def set(self, key, value):
        if key not in self.queue:
          if self.size < self.capacity:
            self.queue[key] = value
            self.size += 1
          else:
            # if the cache is at capacity, remove first item in insertion order
            self.queue.popitem(False)
            # then add new item on top
            self.queue[key] = value

our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
our_cache.get(9)      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

our_cache.get(3)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
