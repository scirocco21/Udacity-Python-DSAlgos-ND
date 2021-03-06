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

