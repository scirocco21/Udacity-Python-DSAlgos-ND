import os

def find_files(suffix, path):
    result = []
    for filename in os.listdir(path):
      # use join method to get actual filepath, not just name
      filepath = os.path.join(path,filename)

      if os.path.isfile(filepath) and filename.endswith(suffix):
        result.append(filename)
      elif os.path.isdir(filepath):
      # use recursion here
        find_files(suffix,filepath)
    return result