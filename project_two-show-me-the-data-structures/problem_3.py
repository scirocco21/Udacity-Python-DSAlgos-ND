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

# Step 2: define Priority Queue class using min heap
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
  
  # fix the order of nodes to maintain heap property when deleting or inserting a node
  def reorderHeap(self, self_position):
    # "bubble up" as long as there is a leaf node and nodes are out of order
    while self.hasParent(self_position) and self.heap[self_position][1] < self.heap[self.getParentIndex(self_position)][1]:
      # if two nodes violate min heap property, perform swap
      self.heap[self_position], self.heap[self.getParentIndex(self_position)] = self.heap[self.getParentIndex(self_position)],self.heap[self_position]
      # move up one level
      self_position = self.getParentIndex(self_position)

  def insert(self,item):
    # append item to the end of the list
    self.heap.append(item)
    # rerrange the heap from bottom up after insertion
    self.reorderHeap(len(self.heap) - 1)

  def delete_min(self):
    if len(self.heap) == 0:
      return "Heap is empty"
    root = self.getMin()
    # swap root with last item in the heap
    self.heap[0] = self.heap[len(self.heap) - 1]
    self.heap.pop()
    return root

# Step 3: Transform the key, value pairs in the frequency hash into a priority queue
priority_queue = MinHeap()
data = "Hello World"
freq_hash = create_freq_hash(data)

for key,value in freq_hash.items():
  priority_queue.insert([key,value])

# TEST
# priority_queue.delete_min()

# for item in priority_queue.heap:
#   print(item)


class HuffmannTree:
  def mergeNodes(self,nodeA,nodeB, priority_queue):
    node = HuffmannNode()
    node.freq = nodeA.freq + nodeB.freq
    priority_queue.insert([None, node.freq])
    return HuffmannNode(node)

  def insert(self,priority_queue):
    nodeA = priority_queue.getMin()
    priority_queue.delete_min()
    nodeB = priority_queue.getMin()
    priority_queue.delete_min()

    new_node_A = HuffmannNode(nodeA)
    new_node_B = HuffmannNode(nodeB)
    new_node_C = self.mergeNodes(new_node_A, new_node_B, priority_queue)
    new_node_C.left = new_node_A 
    new_node_C.right = new_node_B

class HuffmannNode:
  def __init__(self,node=None):
    self.right = None
    self.left = None
    self.freq = node.freq if node.char else None
    self.char = node.char if node.char else None
