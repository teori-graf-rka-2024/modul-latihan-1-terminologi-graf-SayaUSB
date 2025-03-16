import networkx as nx

def create_graph(edges: list[tuple[int, int]]) -> nx.Graph:
    """Membuat graf tidak berarah dari daftar sisi."""
    G = nx.Graph()
    G.add_edges_from(edges)
    return G

def get_degree(G: nx.Graph, node: int) -> int:
    """Menghitung derajat suatu simpul."""
    return G.degree[node]

def dfs_traversal(G: nx.Graph, start: int) -> list[int]:
    """Traversal DFS mulai dari simpul tertentu."""
    return list(nx.dfs_preorder_nodes(G, source=start))

def bfs_traversal(G: nx.Graph, start: int) -> list[int]:
    """Traversal BFS mulai dari simpul tertentu."""
    edges = nx.bfs_edges(G, start)
    nodes = [start]
    for u, v in edges:
        nodes.append(v)
    return nodes

def find_shortest_path(G: nx.Graph, source: int, target: int) -> None:
    """Mencari jalur terpendek dan memvisualisasikannya"""
    path = nx.shortest_path(G, source=source, target=target)
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, node_size=500, node_color='lightgray')
    nx.draw_networkx_edges(G, pos, width=1, edge_color='gray')
    path_edges = list(zip(path, path[1:]))
    nx.draw_networkx_nodes(G, pos, nodelist=path, node_size=700, node_color='limegreen')
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, width=3, edge_color='red')
    nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif')
    arr = []
    for a, b in path_edges:
        arr.append(a)
        arr.append(b)
    return list(set(arr))
