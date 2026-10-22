from collections import deque


def flat_path(status):
    path = []
    while True:
        path.append(status[0])
        status = status[1]
        if status is None:
            break
    return path[::-1]


def breadth_first_search(start_node, edges, is_solved):
    todo = deque([(start_node, None)])
    checked = set([start_node])

    while todo:
        status = todo.popleft()
        node = status[0]
        if is_solved(node):
            return flat_path(status)

        for next_node in edges[node]:
            if next_node not in checked:
                todo.append((next_node, status))
                checked.add(next_node)
