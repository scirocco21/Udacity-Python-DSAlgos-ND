import os
result = []
def find_files(suffix, path):
    for filename in os.listdir(path):
      # use join method to get actual filepath, not just name
      filepath = os.path.join(path,filename)

      if os.path.isfile(filepath) and filename.endswith(suffix):
        result.append(filename)
      elif os.path.isdir(filepath):
      # use recursion here
        find_files(suffix,filepath)
    return result

# TEST
# files = find_files(".c", "/Users/sebastiangertz/Desktop/Current Projects/Udacity-Python-DSAlgos-ND/project_two-show-me-the-data-structures/testdir")
# for item in files:
  # print(item)