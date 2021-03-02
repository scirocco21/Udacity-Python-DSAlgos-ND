import os

def find_files(suffix, path):
    result = []
    for filename in os.listdir(path):
      # 
      if os.path.isfile(path) and path.endswith(suffix):
        result.append(path)
      elif os.path.isdir(path):
        # use recursion here

    return result