from collections import defaultdict, deque
from typing import DefaultDict

def mango_seller_recursive(queue, adjacent, vertices, visited):
  if not queue:
    return False
  
  person = queue.popleft()

  if vertices[person]:
    return True
  
  for child in adjacent[person] - visited:
    visited.add(person)
    queue.append(child)

  return mango_seller_recursive(queue, adjacent, vertices, visited)


def mango_seller_iterative(queue, adjacent, vertices, visited):
  while queue:
    person = queue.popleft()

    if vertices[person]:
      return True

    for child in adjacent[person] - visited:
      visited.add(person)
      queue.append(child)

  return False


if __name__ == "__main__":
  vertices = [False, False, True, False, False, True]
  edges = [[0, 1], [0, 2], [1, 2], [1, 3], [2, 4], [1, 4], [2, 3], [3, 5], [4, 5]]
  
  adjacent: DefaultDict[int, set]= defaultdict(lambda: set())
  for edge in edges:
    adjacent[edge[0]].add(edge[1])

  start = 0

  queue = deque([0])
  visited = set()
  
  is_there_mango_seller = mango_seller_recursive(queue, adjacent, vertices, visited)
  print("is there a mango seller tarting from {}: {}".format(start, is_there_mango_seller))