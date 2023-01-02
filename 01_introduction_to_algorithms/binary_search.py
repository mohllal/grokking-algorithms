def binary_search_iterative(list, item):
  low = 0
  high = len(list) - 1
  
  while low <= high:
    mid = (low + high) // 2

    if list[mid] < item:
      low = mid + 1
    elif list[mid] > item:
      high = mid - 1
    else:
      return mid

  return None

def binary_search_recursive(list, item, low, high):
  if low > high:
    return None

  mid = (low + high) // 2

  if list[mid] < item:
    return binary_search_recursive(list, item, mid + 1, high)
  elif list[mid] > item:
    return binary_search_recursive(list, item, low, mid - 1)
  else:
    return mid

if __name__ == "__main__":
  my_list = [1, 3, 5, 7, 9]
  n = len(my_list) - 1

  print('iterative binary search')
  print(binary_search_iterative(my_list, 3)) # => 1
  print(binary_search_iterative(my_list, 10)) # => None

  print('recursive binary search')
  print(binary_search_recursive(my_list, 9, 0, n)) # => 1
  print(binary_search_recursive(my_list, 20, 0, n)) # => None