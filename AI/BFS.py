# BFS algorithm in Python


import collections
graph = {
    '1' : ['2','3','4'],
    '2' : ['5', '6'],
    '3' : ['7'],
    '4' : [],
    '5' : ['7'],
    '6' : [],
    '7' : []
}
def bfs(graph, start, end): 
    visited = [start] 
    queue = [start] 
    print('Thu tu duyet: ')
    m = []
    while queue:
        m = queue.pop(0)
        print(m, end = ' ')
        if m[-1] == end: 
            break
        for i in graph[m]:
            if i not in visited:
                visited.append(i)
                queue.append(i)

bfs(graph,'1','5')

# BFS algorithm
def bfs(graph, root): 

    visited, queue = set(), collections.deque([root])
    visited.add(root)

    while queue:

        # Dequeue a vertex from queue
        vertex = queue.popleft()
        print(str(vertex) + " ", end="")

        # If not visited, mark it as visited, and
        # enqueue it
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


if __name__ == '__main__':
    graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}
    print("Following is Breadth First Traversal: ")
    bfs(graph, 0)
