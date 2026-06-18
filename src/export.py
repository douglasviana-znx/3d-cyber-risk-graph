import json
import pathlib

OUTPUT_DIR = pathlib.Path("datasets/seguranca")


def ensure_output_dir() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def write_graph_json(graph_data: dict) -> None:
    path = OUTPUT_DIR / "graph.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(graph_data, f, ensure_ascii=False, indent=2)
    print(f"  graph.json       -> {path}")


def write_resultados_json(resultados: dict) -> None:
    path = OUTPUT_DIR / "resultados.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(resultados, f, ensure_ascii=False, indent=2)
    print(f"  resultados.json  -> {path}")


def write_resumo_md(resultados: dict) -> None:
    path = OUTPUT_DIR / "resumo.md"

    primary = resultados["caminhos_minimos"][0]
    path_str = " → ".join(n.replace("_", " ") for n in primary["path"])

    top_lines = "\n".join(
        f"- **{t['id'].replace('_', ' ')}** (betweenness: {t['betweenness']})"
        for t in resultados["top_centralidade"]
    )

    mc = resultados["corte_minimo"]
    cut_lines = "\n".join(
        f"- {e['source'].replace('_', ' ')} → {e['target'].replace('_', ' ')} (capacidade: {e['capacity']})"
        for e in mc["cut_edges"]
    )

    additional = ""
    for p in resultados["caminhos_minimos"][1:]:
        p_str = " → ".join(n.replace("_", " ") for n in p["path"])
        additional += f"\n- **{p['source'].replace('_',' ')} → {p['target'].replace('_',' ')}** (custo {p['cost']}): {p_str}"

    content = f"""# Resumo de Análise — Cyber Graph Risk Mapping

## Grafo

Rede corporativa fictícia com {resultados['nos']} ativos (vértices) e {resultados['arestas']} conexões (arestas).
Grafo direcionado e ponderado. Pesos representam dificuldade de comprometimento: 1 = muito exposto, 10 = muito protegido.

## Caminho Mínimo (Dijkstra)

Caminho de menor resistência de Internet até Database:

**{path_str}**
Custo total: **{primary['cost']}**

Caminhos adicionais:{additional}

## Centralidade (Top 5 por Betweenness)

{top_lines}

Ativos com maior betweenness centrality são pontos de passagem obrigatória na rede.
Seu comprometimento fragmenta caminhos críticos ou isola segmentos inteiros.

## Corte Mínimo (Internet → Database)

Valor do corte: **{mc['value']}**

Arestas críticas:

{cut_lines}

Essas arestas, se bloqueadas ou reforçadas, isolam completamente o caminho entre Internet e Database.
Representam os pontos de segmentação de maior prioridade estratégica.

## Interpretação

O caminho de menor resistência até o banco de dados passa pela pilha de aplicação
(Internet → Firewall → Load Balancer → Web Server → App Server → Database).
A conexão de menor peso nesse caminho (peso 2) está na entrada do firewall, indicando que
o controle perimetral é o principal ponto de exposição e proteção da rede.

O corte mínimo confirma que o Firewall é o único nó de separação entre a Internet e a rede
interna. Reforçar essa conexão eleva diretamente o custo de qualquer rota de ataque.

## Referências Conceituais

Modelagem inspirada em:
- *GNNs for Modeling Cyber Attack Patterns* — representação de ativos e vulnerabilidades como grafos.
- *STIX-based Network Security Knowledge Graph* — uso de knowledge graphs em segurança da informação.
- *Cyberattack Graph Modeling for Visual Analytics* — visual analytics de caminhos críticos e análise defensiva.

> Dados inteiramente sintéticos. Nenhuma rede real foi modelada ou analisada.
"""
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  resumo.md        -> {path}")
