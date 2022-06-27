import csv
from queue import PriorityQueue
edgeFile = 'edges.csv'


def ucs(start, end):
    # Begin your code (Part 3)
    """
    graph: to create a graph
    parents: to trace the path
    frontier: nodes which can be visited. A priority queue ordered by ucs_w
    explored: nodes which have been visited

    1. Use csv.reader to read the csv file and create a graph 
      according to the csv file, then store into graph{}, whose
      format is graph[from_node][to_node] = distance
    2. Pop first element of queue, which has smallest weight. Add the node to explored.
      Search its neighbors and check them whether they have been visited. If not, update
      their weight and parents
    3. Sort frontier to ensure the first element has the smallest weight
    4. Trace the path according parents
    """
    with open(edgeFile) as edges:
      rows = csv.reader(edges)
      headers = next(rows)

      graph = {}
      parents = dict()
      frontier = []
      explored = []

      for row in rows:
        if row[0] in graph:
         graph[row[0]][row[1]] = row[2]
        else:
          graph[row[0]] = dict()
          graph[row[0]][row[1]] = row[2]

      frontier.append([0, start])

      while frontier:

        tmp = frontier.pop(0)
        ucs_w = tmp[0]
        current_node = tmp[1]

        if not graph.get(current_node):
          continue
        else:
          explored.append(current_node)

          if current_node == end:
            dis = float(ucs_w)
            break

          for node in graph[current_node]:
            if node not in explored:
              new_weight = ucs_w + float(graph[current_node][node])
              frontier.append([new_weight, node])
              parents[node] = current_node
          frontier = sorted(frontier)
          
      path = []
      key = end

      while parents[key] != start:
        path.append(int(key))
        key = parents[key]
        
      path.append(int(key))
      path.append(int(start))
      path.reverse()

      return path, dis, len(explored)
        
    raise NotImplementedError("To be implemented")
    # End your code (Part 3)


if __name__ == '__main__':
    path, dist, num_visited = ucs(2270143902, 1079387396)
    print(f'The number of path nodes: {len(path)}')
    print(f'Total distance of path: {dist}')
    print(f'The number of visited nodes: {num_visited}')
