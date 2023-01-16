from collections import defaultdict, deque
from typing import DefaultDict

def minimum_steps_recursive(queue, adjacent, vertices, target, visited):
  if not queue:
    return -1
  
  node, step = queue.popleft()
  if vertices[node] == target[0]:
    return step

  visited.add(node)
  for child in adjacent[node] - visited:
      queue.append((child, step + 1))

  return minimum_steps_recursive(queue, adjacent, vertices, target, visited)


def minimum_steps_iterative(queue, adjacent, vertices, target, visited):
  while queue:
    node, step = queue.popleft()
    if vertices[node] == target[0]:
      return step
  
    visited.add(node)
    for child in adjacent[node] - visited:
        queue.append((child, step + 1))

  return -1


if __name__ == "__main__":
  vertices = ['Twin Peaks', 'Queensland', 'Berry Head', 'Bigfoot', 'Golden Gate Bridge', 'Bowlegs']
  edges = [[0, 1], [0, 2], [1, 2], [1, 3], [2, 4], [1, 4], [2, 3], [3, 5], [4, 5]]
  
  adjacent: DefaultDict[int, set]= defaultdict(lambda: set())
  for edge in edges:
    adjacent[edge[0]].add(edge[1])
    
  target = ('Bowlegs', 5)
  start = ('Twin Peaks', 0)

  queue = deque([(start[1], 0)])
  visited = set()
  
  minimum = minimum_steps_recursive(queue, adjacent, vertices, target, visited)
  print("minimum steps for {} starting from {}: {}".format(target, start, minimum))
