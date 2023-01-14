def quicksort(arr):
  if len(arr) < 2:
    return arr
  
  pivot  = arr[0]
  
  left = [i for i in arr[1:] if i <= pivot]
  right = [i for i in arr[1:] if i > pivot]

  return quicksort(left) + [pivot] + quicksort(right)


if __name__ == "__main__":
  print('quicksort of [4, 10, 2, 3, 11] =', quicksort([4, 10, 2, 3, 11]))
  print('quicksort of [7, 2, 10, 14, 8, 0] =', quicksort([7, 2, 10, 14, 8, 0]))
