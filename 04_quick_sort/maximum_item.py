def maximum(arr):
  if len(arr) == 1:
    return arr[0]
  
  return max(arr[0], maximum(arr[1:]))


if __name__ == "__main__":
  print('maximum of [1, 2, 3, 4, 5] =', maximum([1, 2, 3, 4, 5]))
  print('maximum of [8, 0, 10, 14, 2] =', maximum([8, 0, 10, 14, 2]))
