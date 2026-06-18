import sys

from src.model import load_graph
from src.analysis import shortest_paths, centrality, top_nodes, min_cut
from src.export import ensure_output_dir, write_graph_json, write_resultados_json, write_resumo_md
from src.visualization_data import build_graph_json


def main() -> None:
    print("Cyber Graph Risk Mapping")
    print("=" * 40)

    print("\n[1/4] Carregando grafo...")
    G = load_graph()
    print(f"      {G.number_of_nodes()} nos, {G.number_of_edges()} arestas")

    print("\n[2/4] Calculando algoritmos...")

    paths = shortest_paths(G)
    primary = paths[0]
    print(f"      Caminho minimo Internet -> Database:")
    print(f"        {' -> '.join(primary['path'])} (custo {primary['cost']})")

    cent = centrality(G)
    top = top_nodes(cent)
    print(f"      Top 5 centralidade (betweenness): {', '.join(t['id'] for t in top)}")

    mc = min_cut(G, "Internet", "Database")
    print(f"      Corte minimo Internet -> Database: valor {mc['value']}, {len(mc['cut_edges'])} aresta(s)")
    for e in mc["cut_edges"]:
        print(f"        {e['source']} -> {e['target']} (capacidade {e['capacity']})")

    analysis = {
        "nos": G.number_of_nodes(),
        "arestas": G.number_of_edges(),
        "caminhos_minimos": paths,
        "centralidade": cent,
        "top_centralidade": top,
        "corte_minimo": mc,
    }

    print("\n[3/4] Gerando arquivos de saida...")
    ensure_output_dir()

    graph_json = build_graph_json(G, analysis)
    write_graph_json(graph_json)

    resultados = {
        "nos": analysis["nos"],
        "arestas": analysis["arestas"],
        "caminhos_minimos": analysis["caminhos_minimos"],
        "top_centralidade": analysis["top_centralidade"],
        "corte_minimo": analysis["corte_minimo"],
    }
    write_resultados_json(resultados)
    write_resumo_md(resultados)

    print("\n[4/4] Concluido.")
    print("\nPara visualizar:")
    print("  python -m http.server 8000")
    print("  Abrir: http://localhost:8000/visualizacao/")


if __name__ == "__main__":
    try:
        main()
    except FileNotFoundError as e:
        print(f"Erro: {e}", file=sys.stderr)
        sys.exit(1)
