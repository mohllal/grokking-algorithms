from collections import defaultdict
from typing import DefaultDict, Optional

def get_path(parents, target):
  path = []
  current = target
  
  while current is not None:
    path.append(current)
    current = parents[current]
  
  path.reverse()
  return path


def detect_negative_cycle(graph, distances):
  for source, edge in graph.items():
    for destination, weight in edge.items():
      if distances[source] != float("inf") and distances[source] + weight < distances[destination]:
        print("Graph contains negative weight cycle")
        return True
  return False
    


def bellman_ford(n, graph, start):
  distances: DefaultDict[int, int] = defaultdict(lambda: float("inf"), {start: 0})
  parents: DefaultDict[int, Optional[int]] = defaultdict(lambda: None, {start: None})

  for _ in range(n - 1):
    for source, edge in graph.items():
      for destination, weight in edge.items():
        if distances[source] != float("inf") and distances[source] + weight < distances[destination]:
          distances[destination] = distances[source] + weight
          parents[destination] = source

  return distances, parents


if __name__ == "__main__":
  weights = [4, 2, 3, 1, 2, 4, 4, 5, -4, 5]
  edges = [['A', 'B'], ['A', 'C'], ['B', 'C'], ['C', 'B'], ['B', 'D'], ['B', 'E'], ['C', 'D'], ['C', 'E'], ['D', 'E'], ['E', 'D']]
  
  graph: DefaultDict[int, DefaultDict[int, int]] = defaultdict(lambda: {})
  for i in range(len(edges)):
    edge, weight = edges[i], weights[i]
    graph[edge[0]][edge[1]] = weight
  
  distances, parents = bellman_ford(5, graph, 'A')
  has_negative_cycle = detect_negative_cycle(graph, distances)

  print("minimum cost from 'A' to 'E':", distances['E'])
  print('has the graph contains negative cycle?:', has_negative_cycle)
  if not has_negative_cycle:
    print("minimum cost path from 'A' to 'E':", get_path(parents, 'E'))