import csv
edgeFile = 'edges.csv'
heuristicFile = 'heuristic.csv'


def astar(start, end):
    # Begin your code (Part 4)
    """
    graph: to create a graph
    parents: to trace the path
    frontier: nodes which can be visited. A priority queue ordered by h_n
    explored: nodes which have been visited
    h1_weight; the heuristic function which is from National Yang Ming Chiao 
          University to Big City Shopping Mall
    h2_weight: the heuristic function which is from Hsinchu Zoo to COSTCO Hsinchu Store
    h3_weight: the heuristic function which is from National Experimental High School At 
          Hsinchu Science Park to Nanliao Fighing Port
    h_n: to store current heuristic function
    g_n: to store the distance from start_node to current_node

    1. Use csv.reader to read edges.csv and create a graph 
      according to the csv file, then store the data into graph{},
      whose format is graph[from_node][to_node] = distance
    2. Use csv.reader to read heuristic.csv and create dictionaries. Store the data into 
      respective dictionary, whose format is hx_weight[node] = distance from node to end_node.
    3. If clause determines which heuristic function is going to use
    4. Pop first element of queue, which has smallest weight. Add the node to explored.
      Search its neighbors and check them whether they have been visited. If not, update
      their weight and parents
    3. Sort frontier to ensure the first element has the smallest weight
    4. Trace the path according parents
    """
    with open(edgeFile) as edges:
      rows = csv.reader(edges)
      headers = next(rows)

      graph = {}
      h1_weight = {}
      h2_weight = {}
      h3_weight = {}
      h_n = {}

      for row in rows:
        if row[0] in graph:
         graph[row[0]][row[1]] = row[2]
        else:
          graph[row[0]] = dict()
          graph[row[0]][row[1]] = row[2]

      with open(heuristicFile) as hFile:
        r = csv.reader(hFile)
        headers = next(r)

        for rr in r:
          h1_weight[rr[0]] = rr[1]
          h2_weight[rr[0]] = rr[2]
          h3_weight[rr[0]] = rr[3]

        if end == '1079387396':
          h_n = h1_weight
        elif end == '1737223506':
          h_n = h2_weight
        elif end == '8513026827':
          h_n = h3_weight

        parents = {}
        g_n = {}
        frontier = []
        explored = []

        g_n[start] = 0
        frontier.append([g_n[start] + float(h_n[start]), start])

        while frontier:
          tmp = frontier.pop(0)
          weight = tmp[0]
          current_node = tmp[1]

          if not graph.get(current_node):
            continue
          else:
            explored.append(current_node)

            if current_node == end:
              break

            for node in graph[current_node]:
              g_n[node] = float(g_n[current_node]) + float(graph[current_node][node])
              f_n = g_n[node] + float(h_n[node])
              if node not in explored:
                frontier.append([f_n, node])
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

        return path, float(g_n[end]), len(explored)
        
    #raise NotImplementedError("To be implemented")
    # End your code (Part 4)


if __name__ == '__main__':
    path, dist, num_visited = astar(2270143902, 1079387396)
    print(f'The number of path nodes: {len(path)}')
    print(f'Total distance of path: {dist}')
    print(f'The number of visited nodes: {num_visited}')
