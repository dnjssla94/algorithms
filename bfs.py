

graph = dict()

graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

def bfs(graph, startNode):
    visited_queue = list()
    need_visit_queue = list()

    need_visit_queue.append(startNode)

    while need_visit_queue:
        node = need_visit_queue.pop(0) # 0번 인덱스 값을 사용한다.
        if node not in visited_queue:
            visited_queue.append(node)
            need_visit_queue.extend(graph[node])
    
    return visited_queue

result = bfs(graph, 'A')
print(result)