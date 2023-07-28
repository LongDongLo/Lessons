import random #7

global graph
graph = {"A": {"B": 2, "C": 6, "D": 5},
         "B": {"A": 2, "C": 9, "G": 8},
         "C": {"A": 6, "B": 9, "D": 3, "F": 11},
         "D": {"A": 5, "C": 3, "E": 9, "F": 7},
         "E": {"D": 9, "F": 14, "H": 1},
         "F": {"C": 11, "D": 7, "E": 14, "G": 4, "H": 12},
         "G": {"B": 8, "F": 4, "H": 6,},
         "H": {"E": 1, "F": 12, "G": 6}}

# graph = {'A': {'B':10, 'C':4},
#         'B': {'A':10, 'C':5, 'E':10},
#         'C': {'A':4, 'B':5, 'D':2},
#         'D': {'C':2, 'E':4},
#         'E': {'B':10, 'D':4}}

def overlap(list1, list2):
    overlapList = []
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                overlapList.append(list2[j])
    return overlapList

def fastestPath(graph):
    pathList = []
    for i in range(100):
        minutes = 0

        graphKeys = list(graph.keys())

        inner = graph.get(graphKeys[0])

        removed = graphKeys[0]

        graphKeys.remove(graphKeys[0])
        # print()
        # print("looped")
        # print()
        appendList = []

        while 'E' in graphKeys:

            appendList.append(removed)
            # print()
            # print("appendList is", appendList)
            # print("CURRENT NODE:", removed, inner)
            # print()
            # print("Unvisited are", graphKeys)
            # print("Potential Destinations are", list(inner.keys()))
            viableDestinations = overlap(graphKeys, list(inner.keys()))

            if len(viableDestinations) == 0:
                break
            else:
                currentDest = random.choice(viableDestinations)

            # print("Viable Destinations are", viableDestinations)
            # print("Go to",currentDest)
            # print("spent",graph[removed][currentDest],'minutes')

            minutes += graph[removed][currentDest]

            graphKeys.remove(currentDest)
            removed = currentDest
            inner = graph[currentDest]
        graphKeys = list(graph.keys())
        appendList.append(str(graphKeys[-1]))
        appendList.append(minutes)


        # print("Unvisited are", graphKeys)
        # print("minutes is", minutes)
        if appendList not in pathList:
            pathList.append(appendList)
        # print("pathlist is", pathList)

    minimum = 1000000

    for i in range(len(pathList)):

        if pathList[i][-1] < minimum:
            minimum = pathList[i][-1]
            fastestPath = pathList[i][:-1]
            # print(minimum)

    return fastestPath

def BFS_SP(graph, start, goal):
    explored = []

    # Queue for traversing the
    # graph in the BFS
    queue = [[start]]

    # If the desired node is
    # reached
    if start == goal:
        print("Same Node")
        return

    # Loop to traverse the graph
    # with the help of the queue
    while queue:
        path = queue.pop(0)
        node = path[-1]

        # Condition to check if the
        # current node is not visited
        if node not in explored:
            neighbours = graph[node]

            # Loop to iterate over the
            # neighbours of the node
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

                # Condition to check if the
                # neighbour node is the goal
                if neighbour == goal:
                    print("Shortest path = ", *new_path)
                    return
            explored.append(node)

    # Condition when the nodes
    # are not connected
    print("So sorry, but a connecting"\
"path doesn't exist :(")
    return

# BFS_SP(graph, "A", "H")

print(fastestPath(graph))


