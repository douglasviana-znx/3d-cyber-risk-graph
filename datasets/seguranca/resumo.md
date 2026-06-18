# Resumo de Análise — Cyber Graph Risk Mapping

## Grafo

Rede corporativa fictícia com 17 ativos (vértices) e 23 conexões (arestas).
Grafo direcionado e ponderado. Pesos representam dificuldade de comprometimento: 1 = muito exposto, 10 = muito protegido.

## Caminho Mínimo (Dijkstra)

Caminho de menor resistência de Internet até Database:

**Internet → Firewall → Load Balancer → Web Server → App Server → Database**
Custo total: **13**

Caminhos adicionais:
- **Internet → Backup Server** (custo 20): Internet → Firewall → Email Server → Workstation 2 → File Server → Backup Server
- **Internet → Active Directory** (custo 14): Internet → Firewall → Email Server → Workstation 2 → Active Directory
- **Internet → Admin Console** (custo 17): Internet → Firewall → SIEM → Admin Console

## Centralidade (Top 5 por Betweenness)

- **Database** (betweenness: 0.1208)
- **SIEM** (betweenness: 0.1208)
- **Active Directory** (betweenness: 0.0958)
- **Admin Console** (betweenness: 0.0875)
- **App Server** (betweenness: 0.075)

Ativos com maior betweenness centrality são pontos de passagem obrigatória na rede.
Seu comprometimento fragmenta caminhos críticos ou isola segmentos inteiros.

## Corte Mínimo (Internet → Database)

Valor do corte: **2**

Arestas críticas:

- Internet → Firewall (capacidade: 2)

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
