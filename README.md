# Cyber Graph Risk Mapping

**Aluno:** Douglas Viana Fernandes

**Professor/Orientador:** Luiz Henrique da costa Silva

**Instituição:** PUC Minas - /2026

## Sobre o projeto

Este projeto modela uma rede corporativa fictícia como um grafo direcionado e ponderado, com o objetivo de identificar caminhos críticos, ativos prioritários e pontos estratégicos de proteção em segurança da informação.

Os vértices representam ativos da infraestrutura, como firewall, VPN, servidores, estações de trabalho, banco de dados, Active Directory, backup e SIEM. As arestas representam conexões ou dependências entre esses ativos. Os pesos indicam o custo, nível de proteção ou dificuldade de avanço em cada conexão.

A rede utilizada é sintética e foi criada apenas para fins acadêmicos. Ela não representa uma empresa real e não contém dados sensíveis.

## Origem da visualização 3D, no contexto do semestre atual do aluno

A ideia de utilizar uma visualização 3D como apoio à interpretação do grafo foi inspirada em uma modelagem apresentada por **[@arthurcuri](https://github.com/arthurcuri)** em um seminário da disciplina **Medição e Experimentação de Software**, no **1º semestre de 2026**, durante o **6º período**. Na proposta original, a visualização 3D era utilizada para relacionar artigos acadêmicos a uma ementa de disciplina. Neste projeto, essa ideia foi adaptada para outro contexto: a representação de ativos, conexões e caminhos críticos em uma rede corporativa fictícia.

## Base conceitual

A modelagem foi definida a partir de três artigos de referência enviados para o trabalho:

* **Graph Neural Networks (GNNs) for Modeling Cyber Attack Patterns and Predicting System Vulnerabilities in Critical Infrastructure**
* **STIX-based Network Security Knowledge Graph Ontology Modeling Method**
* **Cyberattack Graph Modeling for Visual Analytics**

Esses trabalhos sustentam a ideia de representar ativos, eventos, relações e caminhos de ataque por meio de estruturas de grafos, além de reforçarem o uso de visualização para análise de segurança.

## Modelagem

O grafo é composto por:

* **Vértices:** ativos da rede corporativa.
* **Arestas:** conexões permitidas ou relações de dependência.
* **Pesos:** nível de exposição, custo de avanço ou dificuldade de comprometimento.
* **Direção:** sentido do fluxo ou da dependência entre os ativos.

Neste projeto, pesos menores indicam caminhos de menor resistência. Portanto, o menor caminho até um ativo crítico pode ser interpretado como uma rota de maior risco.

## Algoritmos utilizados

O projeto aplica os seguintes conceitos de Teoria dos Grafos:

* **Caminho mínimo:** identifica a rota de menor custo entre a Internet e ativos críticos, como o banco de dados.
* **Centralidade:** aponta ativos estruturalmente relevantes na rede.
* **Corte mínimo:** indica conexões estratégicas que podem ser bloqueadas, segmentadas ou reforçadas para dificultar o acesso a ativos sensíveis.

## Saídas geradas

O projeto gera três arquivos principais:

```text
datasets/seguranca/graph.json
datasets/seguranca/resultados.json
datasets/seguranca/resumo.md
```

O arquivo `graph.json` alimenta a visualização 3D.
O arquivo `resultados.json` armazena os resultados dos algoritmos.
O arquivo `resumo.md` sintetiza a interpretação da análise.

## Objetivo acadêmico

O objetivo do projeto é demonstrar como grafos podem ser usados para representar redes corporativas e apoiar análises defensivas em segurança da informação.

A proposta não realiza simulação real de ataque. Trata-se de uma abstração baseada em grafos para estudar caminhos críticos, ativos centrais e pontos de proteção em uma rede corporativa.
