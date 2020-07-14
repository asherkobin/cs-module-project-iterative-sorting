# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
  for i in range(len(arr)):
    min_index = i
    for j in range(i + 1, len(arr)):
      if arr[min_index] > arr[j]:
        min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]

  return arr

# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
  did_swap = True
  iterations = 0

  while did_swap:
    did_swap = False
    for i in range(len(arr) - iterations - 1):
      if arr[i] > arr[i + 1]:
        arr[i], arr[i+1] = arr[i+1], arr[i]
        did_swap = True
    iterations += 1

  return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    # Your code here


    return arr
