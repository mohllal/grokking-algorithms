def find_smallest_index(arr):
  smallest = arr[0]
  smallest_index = 0

  for i in range(len(arr)):
    if arr[i] < smallest:
      smallest = arr[i]
      smallest_index = i
  
  return smallest_index

def selection_sort(arr):
  sorted_arr = []
  
  for _ in range(len(arr)):
    smallest_index = find_smallest_index(arr)
    sorted_arr.append(arr.pop(smallest_index))
    
  return sorted_arr


if __name__ == "__main__":
  my_list = [1, 9, 10, 7, 5]

  print('before sort:', my_list)
  print('after sort:', selection_sort(my_list))
