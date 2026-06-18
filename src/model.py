import csv
import pathlib
import networkx as nx

DATA_DIR = pathlib.Path("data")


def load_graph() -> nx.DiGraph:
    G = nx.DiGraph()

    ativos_path = DATA_DIR / "ativos.csv"
    if not ativos_path.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {ativos_path}")

    with open(ativos_path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            G.add_node(
                row["id"],
                label=row["label"],
                tipo=row["tipo"],
                criticidade=row["criticidade"],
                descricao=row["descricao"],
            )

    conexoes_path = DATA_DIR / "conexoes.csv"
    if not conexoes_path.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {conexoes_path}")

    with open(conexoes_path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            peso = int(row["peso"])
            G.add_edge(
                row["source"],
                row["target"],
                weight=peso,
                capacity=peso,
                descricao=row["descricao"],
            )

    return G
