def define_graph_adjacent_matrix(nodes):
    return [[0 for i in range(nodes)] for j in range(nodes)]


def breadth_search(graph):
    looked_at = [0]
    queue = [0]
    got = []

    while len(queue) != 0:
        item = queue[0]
        for node in range(9):
            if graph[item][node] == 1 and node not in looked_at:
                queue.append(node)
                looked_at.append(node)
                got.append(str(item) + " - " + str(node))
        queue = queue[1:]
    return got


graph = define_graph_adjacent_matrix(9)

graph[0][2] = 1
graph[0][3] = 1
graph[0][1] = 1

graph[1][0] = 1
graph[1][2] = 1
graph[1][4] = 1

graph[2][0] = 1
graph[2][1] = 1
graph[2][6] = 1
graph[2][5] = 1
graph[2][3] = 1

graph[3][0] = 1
graph[3][2] = 1
graph[3][6] = 1

graph[4][1] = 1

graph[5][7] = 1
graph[5][2] = 1

graph[6][2] = 1
graph[6][8] = 1
graph[6][3] = 1

graph[7][5] = 1

graph[8][6] = 1

print(breadth_search(graph))
