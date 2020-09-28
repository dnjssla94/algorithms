

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

def dfs(graph, start_node):
    visited_queue, need_visit_stack = list(), list()
    need_visit_stack.append(start_node)

    while need_visit_stack:
        node = need_visit_stack.pop()
        if node not in visited_queue:
            visited_queue.append(node)
            need_visit_stack.extend(graph[node])

    return visited_queue

result = dfs(graph, "A")
print(result)