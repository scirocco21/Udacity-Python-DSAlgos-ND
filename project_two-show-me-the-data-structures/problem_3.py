import sys

def huffman_encoding(data):
    pass

def huffman_decoding(data,tree):
    pass

# Step 1: convert a character into a frequency hash (include empty spaces as characters as well!)

def create_freq_hash(data):
  freq_hash = {}
  for char in data:
    if freq_hash[char]:
      freq_hash[char] +=1
    else:
      freq_hash[char] = 1
  return freq_hash
