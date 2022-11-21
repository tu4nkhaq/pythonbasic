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
                visited.insert(0,i)
                queue.insert(0,i)

bfs(graph,'1','5')