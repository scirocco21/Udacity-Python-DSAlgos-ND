import sys

def huffman_encoding(data):
    freq_hash = create_freq_hash(data)

def huffman_decoding(data,tree):
    pass

# Step 1: convert a character into a frequency hash (include empty spaces as characters as well!)

def create_freq_hash(data):
  freq_hash = {}
  for char in data:
    if char in freq_hash:
      freq_hash[char] +=1
    else:
      freq_hash[char] = 1
  return freq_hash

# Test step 1: 
# 
# hash = create_freq_hash("Aabbcccccc")

# for key in hash:
#   print(key, hash[key])


# Step 2: convert the frequency hash into a priority queue represented by min heap

class MinHeap:
  def __init__(self):
    # set up heap as list of nodes
    self.heap = []

  # helper methods to get index positions of parent/child nodes in the heap list
  def getParentIndex(self, self_position):
    return int((self_position - 1) / 2)
  
  def getLeftChildIndex(self, self_position):
    return 2 * self_position + 1

  def getRightChildIndex(self, self_position):
    return 2 * self_position + 2

  # helper methods to determine if a given node has a Parent/left or right child
  def hasParent(self,self_position):
    return self.getParentIndex(self_position) < len(self.heap)

  def hasLeftChild(self, self_position):
    return self.getLeftChildIndex(self_position) < len(self.heap)
  
  def hasRightChild(self,self_position):
    return self.getRightChildIndex(self_position) < len(self.heap)
  
  def getMin(self):
    return self.heap[0]
  