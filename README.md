# Problema das Oito Rainhas com Algoritmos Genéticos

Este projeto apresenta a resolução do problema das oito rainhas utilizando **Algoritmos Genéticos (AGs)** implementados em Python com a biblioteca [PyGAD](https://pygad.readthedocs.io). Trata-se de um problema clássico de **satisfação de restrições** com espaço de busca exponencial, utilizado como benchmark para técnicas de busca e otimização.

## 1. Formulação do Problema

O problema consiste em posicionar oito rainhas em um tabuleiro 8×8 de forma que nenhuma delas ataque outra. A modelagem utilizada define que:
- Cada **gene** representa a **linha** da rainha.
- Cada **índice** do cromossomo representa a **coluna** correspondente.

Exemplo de cromossomo: `[4, 2, 0, 6, 7, 1, 3, 5]`

## 2. Codificação e Escolhas de Projeto

### Representação do Cromossomo

Um vetor de 8 inteiros, onde cada valor indica a linha da rainha na respectiva coluna:
- Vantagem: representação direta e compatível com operadores genéticos.

### Parâmetros do Algoritmo

| Parâmetro               | Valor     | Justificativa                                                                 |
|------------------------|-----------|-------------------------------------------------------------------------------|
| Tamanho da população   | 100       | Compromisso entre diversidade e custo computacional.                          |
| Seleção                | Torneio   | Promove pressão seletiva sem perda drástica de diversidade.                  |
| Crossover              | Ponto único (80%) | Favorece combinação estruturada de indivíduos.                          |
| Mutação                | 10%       | Introduz variabilidade e previne convergência prematura.                      |
| Critério de parada     | Fitness = 28 ou 200 gerações | Garante término com ou sem solução ideal.                      |

### Função de Fitness

O fitness é definido como:

```
fitness = 28 - número de pares de rainhas em conflito
```

A pontuação máxima (28) corresponde a todas as combinações possíveis de 8 rainhas em pares não conflituosos:

```
C(8, 2) = 28
```

Conflitos são contabilizados com base em:
- Mesma linha: `solution[i] == solution[j]`
- Mesma diagonal: `abs(solution[i] - solution[j]) == abs(i - j)`

## 3. Resultados e Visualização

Durante a execução, o algoritmo gera um gráfico com a **evolução do fitness da melhor solução** ao longo das gerações. Esse gráfico é salvo automaticamente como `fitness_plot.png`.

A função `print_board()` imprime a solução final de forma visual com `Q` indicando a posição de cada rainha.

Exemplo de saída esperada:

```
Melhor solução encontrada: [4, 2, 7, 3, 6, 0, 5, 1]
Fitness da melhor solução: 28

Tabuleiro resultante:
. . . . Q . . .
. . Q . . . . .
. . . . . . . Q
. . . Q . . . .
. . . . . . Q .
Q . . . . . . .
. . . . . Q . .
. Q . . . . . .
```

## 4. Dependências

- Python 3.8+
- [PyGAD](https://pypi.org/project/pygad/)
- [matplotlib](https://matplotlib.org/)

Instalação:

```bash
pip install pygad matplotlib
```

## 5. Execução

Para executar o projeto:

```
python main.py
```

O script irá:
- Rodar o AG até encontrar uma solução com fitness 28 ou completar 200 gerações;
- Imprimir a melhor solução e seu fitness;
- Exibir o tabuleiro correspondente;
- Gerar o gráfico `fitness_plot.png`.

## 6. Observações

- Pequenas variações nos parâmetros do AG (mutação, população, seleção) podem influenciar diretamente o número de gerações necessárias para convergência.
- A taxa de crossover de 80% e de mutação de 10% demonstraram resultados consistentes em múltiplas execuções.
