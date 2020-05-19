def linear_search(arr, target):
    for idx in range(len(arr)):
      if arr[idx] == target:
        return idx
    
    return -1 # not found

# Write an iterative implementation of Binary Search
def binary_search(arr, target):
  first = 0
  last = len(arr) - 1
  middle = (first + last) // 2

  while first <= last:
    if arr[middle] < target:
      first = middle + 1
    elif arr[middle] == target:
      return middle
    else:
      last = middle - 1

    middle = (first + last) // 2

  return -1 # not found