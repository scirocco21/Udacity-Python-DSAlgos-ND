import sys
import heapq

# def huffman_encoding(data):
#     freq_hash = create_freq_hash(data)

# def huffman_decoding(data,tree):
#     pass

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

# Step 2: Transform the key, value pairs in the frequency hash into a priority queue
def build_min_heap(data):
  heap_array = []
  freq_hash = create_freq_hash(data)
  for key in freq_hash:
    heap_array.append([freq_hash[key],key])
  heapq.heapify(heap_array)
  return heap_array

# Step 3: Test
data = "AAAAAAABBBCCCCCCCDDEEEEEE"

freq_hash = create_freq_hash(data)
priority_queue = build_min_heap(data)

for item in priority_queue:
  print(item)
heapq.heappop(priority_queue)
print("The smallest item is: ",priority_queue[0])

# class HuffmannTree:
#   def mergeNodes(self,nodeA,nodeB, priority_queue):
#     print("merging")
#     node = HuffmannNode()
#     node.freq = nodeA.freq + nodeB.freq
#     priority_queue.insert([None, node.freq])
#     print("ready to return the node ", node.char, node.freq)
#     return node

#   def insert(self,priority_queue):
#     print("Inserting into tree: ")
#     nodeA = priority_queue.getMin()
#     priority_queue.delete_min()
#     nodeB = priority_queue.getMin()
#     priority_queue.delete_min()

#     new_node_A = HuffmannNode(nodeA)
#     new_node_B = HuffmannNode(nodeB)
#     new_node_C = self.mergeNodes(new_node_A, new_node_B, priority_queue)
#     new_node_C.left = new_node_A 
#     new_node_C.right = new_node_B
#     print("nodeA: ", new_node_A.char,new_node_A.freq)
#     print("nodeB:", new_node_B.char, new_node_B.freq)
#     print("nodeC:", new_node_C.freq)
# class HuffmannNode:
#   def __init__(self,node=None):
#     self.right = None
#     self.left = None
#     self.freq = node[1] if node else None
#     self.char = node[0] if node else None

# hufftree = HuffmannTree()

# while len(priority_queue.heap) >= 1:
#   hufftree.insert(priority_queue)