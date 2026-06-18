import networkx as nx

NODE_TYPE_META = {
    "externo":       {"label": "Externo",        "color": "#FF6B35"},
    "perimetro":     {"label": "Perímetro",       "color": "#FFD700"},
    "dmz":           {"label": "DMZ",             "color": "#87CEEB"},
    "interno":       {"label": "Interno",         "color": "#6AB89A"},
    "identidade":    {"label": "Identidade",      "color": "#9A6AB8"},
    "dados":         {"label": "Dados",           "color": "#FF4444"},
    "backup":        {"label": "Backup",          "color": "#C4A96A"},
    "monitoramento": {"label": "Monitoramento",   "color": "#4A90D9"},
    "administracao": {"label": "Administração",   "color": "#E84393"},
}

CRITICAL_CRITICIDADE = {"alta", "critica"}


def build_graph_json(G: nx.DiGraph, analysis: dict) -> dict:
    primary_path = analysis["caminhos_minimos"][0]["path"]
    path_nodes = set(primary_path)
    path_edges = {(primary_path[i], primary_path[i + 1]) for i in range(len(primary_path) - 1)}

    min_cut_edges = {
        (e["source"], e["target"])
        for e in analysis["corte_minimo"]["cut_edges"]
    }

    betweenness = analysis["centralidade"]["betweenness"]

    nodes = []
    for node_id, attrs in G.nodes(data=True):
        nodes.append({
            "id": node_id,
            "label": attrs.get("label", node_id),
            "type": attrs.get("tipo", "interno"),
            "criticidade": attrs.get("criticidade", "media"),
            "description": attrs.get("descricao", ""),
            "centrality": round(betweenness.get(node_id, 0.0), 4),
            "isCriticalAsset": attrs.get("criticidade") in CRITICAL_CRITICIDADE,
            "isOnShortestPath": node_id in path_nodes,
        })

    links = []
    for u, v, attrs in G.edges(data=True):
        links.append({
            "source": u,
            "target": v,
            "weight": attrs.get("weight", 1),
            "description": attrs.get("descricao", ""),
            "isOnShortestPath": (u, v) in path_edges,
            "isMinCutEdge": (u, v) in min_cut_edges,
        })

    return {
        "meta": {
            "name": "seguranca",
            "titulo": "Grafo 3D de Segurança em Redes Corporativas",
            "descricao": "Modelagem de ativos, conexões e caminhos críticos em uma rede corporativa fictícia.",
        },
        "node_types": NODE_TYPE_META,
        "nodes": nodes,
        "links": links,
        "analysis": {
            "shortest_path": primary_path,
            "shortest_path_cost": analysis["caminhos_minimos"][0]["cost"],
            "additional_paths": analysis["caminhos_minimos"][1:],
            "top_centrality": analysis["top_centralidade"],
            "min_cut": analysis["corte_minimo"],
        },
    }
