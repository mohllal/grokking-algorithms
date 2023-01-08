def search_boxes(current):
  result = False
  
  if type(current) not in (tuple, list):
    return True

  if not len(current):
    return False

  for item in current:
    result = result or search_boxes(item)
  
  return result

  
if __name__ == "__main__":
  print('key is there:', search_boxes([[], [], [[]], [[]], [], [[['key']]]]))
  print('key is not there:', search_boxes([[], [[[[]]]], [[[]]], [[]], [], [[]]]))