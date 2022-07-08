def check_connection(u: int, v: int, length: int):
    if u == v:
        return True, length
    if u in seen:
        return False, -1
    seen.add(u)
    for adj_node in relation.get(u, []):
        res, l = check_connection(adj_node, v, length + 1)
        if res:
            return True, l
    relation[u] = []
    return False, -1


n = int(input())
results = []
for _ in range(n):
    line = [int(num) for num in input().split()]
    n_nodes, n_edges, s, t = line
    relation = {}
    for __ in range(n_edges):
        v, u = [int(num) for num in input().split()]
        relation[v] = relation.get(v, []) + [u]

    seen = set()
    is_connected, length = check_connection(t, s, 0)
    results.append(length)
    print(length)

# for res in results:
#     print(res)
