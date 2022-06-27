import csv
edgeFile = 'edges.csv'


def bfs(start, end):
    # Begin your code (Part 1)
    """
    graph: to create a graph
    parents: to trace the path
    dis: to record the distance from start_node to current_node
    queue: nodes which can be visited
    visited: nodes which have been visited

    1. Use csv.reader to read the csv file and create a graph 
      according to the csv file, then store into graph{}, whose
      format is graph[from_node][to_node] = distance
    2. Search neighbors of start_node and set their parents and distance 
      Then, put nodes into queue
    3. Following FIFO, pop first element of queue. Check whether the node has 
      been visited, then check if the node is end_node. If the node has not
      been visited and is not end_node, add it to visited and search its
      neighbors. Put its neighbors to queue and update their parents and distance
    4. Trace the path according parents
    """
    with open(edgeFile) as edges:
      rows = csv.reader(edges)
      headers = next(rows)

      graph = {}
      parents = dict()
      dis = dict()
      queue = []
      visited = []

      for row in rows:
        if row[0] in graph:
         graph[row[0]][row[1]] = row[2]
        else:
          graph[row[0]] = dict()
          graph[row[0]][row[1]] = row[2]
  
      dis[start] = 0

      for node in graph[start]:
        if not parents.get(node):
          parents[node] = start
        if not dis.get(node):
          dis[node] = graph[start][node]
        queue.append(node)

      while queue:
        node = queue.pop(0)
        if not graph.get(node):
          continue
        else:
          if node not in visited:
            if node == end:
              break
            else:
              visited.append(node)
              for n in graph[node]:
                if not parents.get(n):
                  parents[n] = node
                if not dis.get(n):
                  dis[n] = float(graph[node][n]) + float(dis[node])
                queue.append(n)

      path = []
      key = end

      while parents[key] != start:
        path.append(int(key))
        key = parents[key]
      path.append(int(key))
      path.append(int(start))
      path.reverse()

      return path, dis[end], len(visited)

      
    raise NotImplementedError("To be implemented")
    # End your code (Part 1)


if __name__ == '__main__':
    path, dist, num_visited = bfs(2270143902, 1079387396)
    print(f'The number of path nodes: {len(path)}')
    print(f'Total distance of path: {dist}')
    print(f'The number of visited nodes: {num_visited}')
