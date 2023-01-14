def sum(arr):
  if len(arr) == 1:
    return arr[0]
  
  return arr[0] + sum(arr[1:])


if __name__ == "__main__":
  print('sum of [1, 2, 3, 4, 5] =', sum([1, 2, 3, 4, 5]))
  print('sum of [8, 0, 10, 14, 2] =', sum([8, 0, 10, 14, 2]))
