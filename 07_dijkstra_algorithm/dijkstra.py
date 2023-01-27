from collections import defaultdict
from typing import DefaultDict, Optional
import heapq

def get_path(parents, target):
  path = []
  current = target
  
  while current is not None:
    path.append(current)
    current = parents[current]
  
  path.reverse()
  return path


def to_be_visited(distances, processed):
  lowest_distance = float("inf")
  lowest_distance_node = None
  
  for node, distance in distances.items():
    if distance < lowest_distance and node not in processed:
      lowest_distance = distance
      lowest_distance_node = node
      
  return lowest_distance_node


def dijkstra(graph, start):
  distances: DefaultDict[int, int] = defaultdict(lambda: float("inf"), {start: 0})
  parents: DefaultDict[int, Optional[int]] = defaultdict(lambda: None, {start: None})
  processed = set([])

  current = to_be_visited(distances, processed)
  while current is not None:
    distance = distances[current]

    for neighbor, weight in graph[current].items():
      neighbor_distance = distance + weight
      
      if neighbor_distance < distances[neighbor]:
        distances[neighbor] = neighbor_distance
        parents[neighbor] = current
    
    processed.add(current)
    current = to_be_visited(distances, processed)
    
  return distances, parents


def dijkstra_with_min_heap(graph, start):
  distances: DefaultDict[int, int] = defaultdict(lambda: float("inf"), {start: 0})
  parents: DefaultDict[int, Optional[int]] = defaultdict(lambda: None, {start: None})
  processed = set([])
  min_heap = [(0, start)]
  
  while min_heap:      
      current_distance, current = heapq.heappop(min_heap)
      
      if current in processed:
        continue
  
      processed.add(current)    
      for neighbor, weight in graph[current].items():
          if neighbor in processed:
            continue

          neighbor_distance = current_distance + weight
          if neighbor_distance  < distances[neighbor]:
              distances[neighbor] = neighbor_distance
              parents[neighbor] = current
              heapq.heappush(min_heap, (neighbor_distance, neighbor))
  
  return distances, parents


if __name__ == "__main__":
  weights = [5, 2, 4, 2, 8, 7, 6, 3, 1]
  edges = [['A', 'B'], ['A', 'C'], ['B', 'D'], ['B', 'G'], ['C', 'B'], ['C', 'G'], ['D', 'G'], ['D', 'F'], ['G', 'F']]
  
  graph: DefaultDict[int, DefaultDict[int, int]] = defaultdict(lambda: {})
  for i in range(len(edges)):
    edge, weight = edges[i], weights[i]
    graph[edge[0]][edge[1]] = weight
  
  distances, parents = dijkstra_with_min_heap(graph, 'A')
  print("minimum distance from 'A' to 'F':", distances['F'])
  print("minimum distance path from 'A' to 'F':", get_path(parents, 'F'))