import networkx as nx


ROUTES = [
    ("Internet", "Database"),
    ("Internet", "Backup_Server"),
    ("Internet", "Active_Directory"),
    ("Internet", "Admin_Console"),
]


def shortest_paths(G: nx.DiGraph) -> list[dict]:
    results = []
    for source, target in ROUTES:
        if source not in G or target not in G:
            continue
        try:
            path = nx.dijkstra_path(G, source, target, weight="weight")
            cost = nx.dijkstra_path_length(G, source, target, weight="weight")
            results.append({"source": source, "target": target, "path": path, "cost": cost})
        except nx.NetworkXNoPath:
            pass
    return results


def centrality(G: nx.DiGraph) -> dict:
    degree = nx.degree_centrality(G)
    betweenness = nx.betweenness_centrality(G, weight="weight", normalized=True)
    closeness = nx.closeness_centrality(G)
    return {"degree": degree, "betweenness": betweenness, "closeness": closeness}


def top_nodes(centrality_data: dict, n: int = 5) -> list[dict]:
    ranked = sorted(centrality_data["betweenness"].items(), key=lambda x: x[1], reverse=True)
    return [{"id": node, "betweenness": round(score, 4)} for node, score in ranked[:n]]


def min_cut(G: nx.DiGraph, source: str, target: str) -> dict:
    cut_value, partition = nx.minimum_cut(G, source, target, capacity="capacity")
    reachable, non_reachable = partition

    cut_edges = []
    for u in reachable:
        for v in non_reachable:
            if G.has_edge(u, v):
                cut_edges.append({
                    "source": u,
                    "target": v,
                    "capacity": G[u][v]["capacity"],
                })

    return {
        "value": int(cut_value),
        "cut_edges": cut_edges,
        "partition_reachable": sorted(reachable),
        "partition_non_reachable": sorted(non_reachable),
    }
