# Estruturas de Dados 1 - Atividades Práticas

Este repositório contém as implementações e exercícios práticos da disciplina de **Estruturas de Dados**, abordando estruturas lineares, árvores binárias e árvores de busca balanceadas.

## 📚 Sobre o Projeto

Atividade acadêmica que implementa e demonstra o uso de diversas estruturas de dados através de exercícios práticos organizados em três listas de implementação. Cada questão está organizada em arquivos separados com implementações específicas e testes demonstrativos.

### 📋 Listas de Implementação

- **Lista 1**: Estruturas Lineares - Stack (Pilha), Queue (Fila), Deque (Fila Dupla) e Listas Encadeadas
- **Lista 2**: Árvores Binárias - LinkedBinaryTree, ArrayBinaryTree e Algoritmos de Travessia
- **Lista 3**: Árvores de Busca Balanceadas - BST, AVL e Árvores Rubro-Negras
- **Lista 4**: Algoritmos de Ordenação - Insertion, Selection, Bubble, Shell, Merge, Quick, Heap e Counting Sort

## 🚀 Como Executar

### Executar lista completa:

```bash
python main.py    # Executa todos os exercícios da Lista 1
python main2.py   # Executa todos os exercícios da Lista 2
python main3.py   # Executa todos os exercícios da Lista 3
python main4.py   # Executa todos os exercícios da Lista 4
```

### Executar uma questão específica:

```bash
# Lista 1 (Estruturas Lineares)
python -m questions.question1_X  # onde X é o número da questão (2-20)

# Lista 2 (Árvores Binárias)
python -m questions.question2_X  # onde X é o número da questão (4-8)

# Lista 3 (Árvores de Busca)
python -m questions.question3_X  # onde X é o número da questão (4-7)

# Lista 4 (Algoritmos de Ordenação)
python -m questions.question4_X  # onde X é o número da questão
```

## 🏗️ Estruturas de Dados Implementadas

### 📚 Lista 1: Estruturas Lineares

#### **ArrayStack** (`stack.py`)

Implementação de pilha usando array dinâmico.

**Características:**

- **Princípio LIFO** (Last In, First Out)
- **Operações O(1)**: `push()`, `pop()`, `top()`
- **Redimensionamento automático**
- **Métodos disponíveis:**
  - `push(element)` - adiciona elemento no topo
  - `pop()` - remove e retorna elemento do topo
  - `top()` - consulta elemento do topo
  - `is_empty()` - verifica se está vazia
  - `__len__()` - retorna tamanho

#### **ArrayQueue** (`queue.py`)

Implementação de fila usando array circular.

**Características:**

- **Princípio FIFO** (First In, First Out)
- **Array circular** para eficiência de memória
- **Operações O(1)**: `enqueue()`, `dequeue()`, `first()`
- **Redimensionamento automático**
- **Métodos disponíveis:**
  - `enqueue(element)` - adiciona elemento no final
  - `dequeue()` - remove e retorna primeiro elemento
  - `first()` - consulta primeiro elemento
  - `is_empty()` - verifica se está vazia
  - `__len__()` - retorna tamanho

#### **ArrayDeque** (`deque.py`)

Implementação de deque (double-ended queue) usando array circular.

**Características:**

- **Operações bidirecionais** (inserção/remoção em ambas extremidades)
- **Array circular** para máxima eficiência
- **Operações O(1)** em ambas as extremidades
- **Redimensionamento automático**
- **Métodos disponíveis:**
  - `add_first(element)` - adiciona no início
  - `add_last(element)` - adiciona no final
  - `delete_first()` - remove do início
  - `delete_last()` - remove do final
  - `first()` - consulta primeiro elemento
  - `last()` / `back()` - consulta último elemento
  - `is_empty()` - verifica se está vazio
  - `__len__()` - retorna tamanho

#### **Estruturas Encadeadas**

- `linkedStack.py` - Pilha encadeada
- `linkedQueue.py` - Fila encadeada
- `linkedDeque.py` - Deque encadeado
- `circularQueue.py` - Fila circular encadeada
- `doublyLinkedBase.py` - Base para listas duplamente encadeadas

### 📝 Exercícios da Lista 1

**Exercício 2** - Operações básicas com pilha (push, pop, top)  
**Exercício 3** - Função para transferir elementos entre duas pilhas  
**Exercício 4** - Remoção recursiva de todos os elementos de uma pilha  
**Exercício 5** - Inversão de lista usando pilha  
**Exercício 6** - Operações básicas com fila (enqueue, dequeue, first)  
**Exercício 7** - Operações básicas com deque (add_first, add_last, delete_first, delete_last)  
**Exercício 8** - Verificação de balanceamento de parênteses usando pilha  
**Exercício 9** - Conversão de expressões infixas para pós-fixas  
**Exercício 10** - Calculadora de expressões aritméticas  
**Exercício 11** - Verificação de palíndromo usando deque  
**Exercício 13** - Encontrar o penúltimo nó em lista encadeada  
**Exercício 14** - Concatenar duas listas encadeadas  
**Exercício 15** - Contagem recursiva de nós em lista encadeada  
**Exercício 16** - Contagem de nós em lista circular  
**Exercício 17** - Reversão recursiva de lista encadeada  
**Exercício 18** - Separar elementos positivos e negativos em lista  
**Exercício 19** - Remover duplicados em lista duplamente encadeada  
**Exercício 20** - Implementar método reverse para lista duplamente encadeada

### 🌳 Lista 2: Árvores Binárias

#### **LinkedBinaryTree** (`linkedBinaryTree.py`)

Implementação de árvore binária usando nós encadeados.

**Características:**

- **Nós ligados por ponteiros**
- **Operações de inserção**: `_add_root()`, `_add_left()`, `_add_right()`
- **Travessias implementadas**: `preorder()`, `inorder()`, `postorder()`
- **Métodos de manipulação**: `replace()`, `_delete()`, `_attach()`

#### **ArrayBinaryTree** (`arrayBinaryTree.py`)

Implementação de árvore binária usando array (Seção 8.3.2).

**Características:**

- **Representação baseada em array**
- **Fórmulas de índice**: filho esquerdo = `2i+1`, filho direito = `2i+2`
- **Redimensionamento automático**
- **Mesmas operações da LinkedBinaryTree**

#### **BinaryTree** (`binaryTree.py`)

Classe abstrata base para árvores binárias.

**Métodos principais:**

- `left(p)`, `right(p)` - navegação
- `sibling(p)` - retorna irmão do nó
- `children(p)` - itera sobre filhos
- `inorder()` - travessia em ordem

### 📝 Exercícios da Lista 2

**Exercício 4** - Verificar se duas árvores binárias são idênticas (mesma estrutura e conteúdo)  
**Exercício 5** - Validar se uma árvore é uma árvore soma  
**Exercício 6** - Imprimir todos os caminhos da raiz até cada folha  
**Exercício 7** - Encontrar e listar todos os ancestrais de um nó específico  
**Exercício 8** - Converter árvore para árvore soma (substituir valores pela soma das subárvores)

### 🔍 Lista 3: Árvores de Busca Balanceadas

#### **TreeMap** (`treeMap.py`)

Implementação de árvore de busca binária (BST) usando mapeamento de chave-valor.

**Características:**

- **Ordenação por chaves**
- **Busca O(log n) em árvores balanceadas**
- **Operações**: `__getitem__()`, `__setitem__()`, `__delitem__()`
- **Métodos auxiliares**: `find_position()`, `find_min()`, `find_range()`

#### **AVLTreeMap** (`avlTreeMap.py`)

Implementação de árvore AVL (auto-balanceamento).

**Características:**

- **Balanceamento automático** após inserções e remoções
- **Fator de balanceamento** mantido entre -1 e 1
- **Rotações**: simples e duplas para rebalanceamento
- **Altura armazenada** em cada nó para eficiência
- **Garante O(log n)** para todas as operações

#### **RedBlackTreeMap** (`redBlackTreeMap.py`)

Implementação de árvore rubro-negra (Red-Black Tree).

**Características:**

- **Balanceamento por cores** (vermelho/preto)
- **Propriedades mantidas**: raiz preta, filhos de nós vermelhos são pretos
- **Caminho negro uniforme** da raiz até as folhas
- **Recoloração e rotações** para manter propriedades
- **Inserção e remoção O(log n)**

#### **MapBase** e **MutableMapping**

Classes base para implementação de mapas:

- **MapBase**: Classe base com `_Item` para composição chave-valor
- **MutableMapping**: Classe abstrata para mapas mutáveis com métodos concretos (`get()`, `pop()`, `clear()`, `keys()`, `values()`, `items()`)

### 📝 Exercícios da Lista 3

**Exercício 4** - Inserção sequencial em BST: inserir chaves [30, 40, 24, 58, 48, 26, 11, 13] e mostrar árvore após cada inserção  
**Exercício 5** - Inserção em AVL: inserir chave 52 na árvore AVL da Figura 11.14b e mostrar rebalanceamento  
**Exercício 6** - Remoção em AVL: remover chave 62 da árvore AVL da Figura 11.14b e mostrar rebalanceamento  
**Exercício 7** - Inserção em Rubro-Negra: inserir sequência [5, 16, 22, 45, 2, 10, 18, 30, 50, 12, 1] e mostrar cores e estrutura

### 🔢 Lista 4: Algoritmos de Ordenação

#### **Algoritmos Implementados**

**Algoritmos O(n²) - Quadráticos:**

- **Insertion Sort**: Ordenação por inserção, eficiente para listas pequenas ou quase ordenadas
- **Selection Sort**: Ordenação por seleção, sempre faz n² comparações
- **Bubble Sort**: Ordenação por bolha, troca elementos adjacentes

**Algoritmos O(n log n) - Logarítmicos:**

- **Shell Sort**: Versão otimizada do Insertion Sort com gaps
- **Merge Sort**: Ordenação por intercalação, divide e conquista
- **Quick Sort**: Ordenação rápida, usa pivô para particionamento
- **Heap Sort**: Ordenação por heap, usa estrutura de heap binária

**Algoritmos O(n + k) - Lineares:**

- **Counting Sort**: Ordenação por contagem, eficiente para inteiros em range limitado

#### **Características da Implementação**

Todos os algoritmos foram modificados para contar:

- **Comparações**: Número de testes realizados durante a ordenação
- **Trocas**: Número de movimentações de elementos
- **Análise comparativa**: Média de operações em múltiplas listas de teste

### 📝 Exercícios da Lista 4

**Exercício 1** - Implementação de 8 algoritmos de ordenação com contagem de operações:

- Testa cada algoritmo em 10 listas diferentes
- Exibe lista ordenada, comparações e trocas para cada execução
- Apresenta sumário comparativo com médias de operações
- Análise de desempenho entre algoritmos O(n²) e O(n log n)

## 📁 Estrutura do Projeto

```
├── main.py                    # Executor da Lista 1 (Estruturas Lineares)
├── main2.py                   # Executor da Lista 2 (Árvores Binárias)
├── main3.py                   # Executor da Lista 3 (Árvores de Busca)
├── main4.py                   # Executor da Lista 4 (Algoritmos de Ordenação)
├── README.md                  # Este arquivo
│
├── # Lista 1: Estruturas Lineares
├── stack.py                   # Pilha com array
├── queue.py                   # Fila com array circular
├── deque.py                   # Deque com array circular
├── linkedStack.py             # Pilha encadeada
├── linkedQueue.py             # Fila encadeada
├── linkedDeque.py             # Deque encadeado
├── circularQueue.py           # Fila circular encadeada
├── doublyLinkedBase.py        # Base para listas duplamente encadeadas
│
├── # Lista 2: Árvores Binárias
├── Tree.py                    # Classe abstrata base para árvores
├── binaryTree.py              # Classe abstrata para árvores binárias
├── linkedBinaryTree.py        # Árvore binária com nós encadeados
├── arrayBinaryTree.py         # Árvore binária com array
│
├── # Lista 3: Árvores de Busca
├── mapBase.py                 # Classe base para mapas
├── mutableMapping.py          # Classe abstrata para mapas mutáveis
├── treeMap.py                 # Árvore de busca binária (BST)
├── avlTreeMap.py              # Árvore AVL (auto-balanceamento)
├── redBlackTreeMap.py         # Árvore Rubro-Negra
│
└── questions/                 # Pasta com todos os exercícios
    ├── __init__.py
    │
    ├── # Lista 1: Estruturas Lineares (17 exercícios)
    ├── question1_2.py         # Operações de pilha
    ├── question1_3.py         # Função transfer entre pilhas
    ├── question1_4.py         # Remoção recursiva de pilha
    ├── question1_5.py         # Inversão de lista com pilha
    ├── question1_6.py         # Operações de fila
    ├── question1_7.py         # Operações de deque
    ├── question1_8.py         # Verificação de parênteses
    ├── question1_9.py         # Conversão de expressões
    ├── question1_10.py        # Calculadora aritmética
    ├── question1_11.py        # Teste de palíndromo
    ├── question1_13.py        # Penúltimo nó em lista encadeada
    ├── question1_14.py        # Concatenar listas encadeadas
    ├── question1_15.py        # Contagem recursiva de nós
    ├── question1_16.py        # Contagem de nós em lista circular
    ├── question1_17.py        # Reversão recursiva de lista
    ├── question1_18.py        # Separar positivos e negativos
    ├── question1_19.py        # Remover duplicados em lista dupla
    ├── question1_20.py        # Método reverse para lista dupla
    │
    ├── # Lista 2: Árvores Binárias (5 exercícios)
    ├── question2_4.py         # Verificação de árvores idênticas
    ├── question2_5.py         # Verificação de árvore soma
    ├── question2_6.py         # Caminhos da raiz até as folhas
    ├── question2_7.py         # Encontrar ancestrais de um nó
    ├── question2_8.py         # Conversão para árvore soma
    │
    ├── # Lista 3: Árvores de Busca (4 exercícios)
    ├── question3_4.py         # Inserção em BST
    ├── question3_5.py         # Inserção em AVL
    ├── question3_6.py         # Remoção em AVL
    ├── question3_7.py         # Inserção em Rubro-Negra
    │
    └── # Lista 4: Algoritmos de Ordenação (1 exercício)
        └── question4_1.py     # 8 algoritmos com análise de performance
```

## 🎯 Conceitos Demonstrados

### Lista 1: Estruturas Lineares

- **Implementação de TADs** (Tipos Abstratos de Dados)
- **Arrays circulares** e redimensionamento dinâmico
- **Complexidade temporal O(1)** para operações básicas
- **Algoritmos clássicos** usando estruturas lineares
- **Balanceamento de parênteses** com pilhas
- **Inversão de sequências** usando pilhas
- **Transferência entre estruturas**
- **Algoritmos recursivos** para listas encadeadas
- **Listas circularmente encadeadas** e navegação circular
- **Reversão de listas** com algoritmos recursivos otimizados
- **Filtragem e separação** de elementos em listas encadeadas
- **Remoção de duplicados** em listas duplamente encadeadas
- **Modificação de estruturas** com métodos de inversão in-place

### Lista 2: Árvores Binárias

- **Árvores binárias** com representação encadeada e por array
- **Travessias de árvores**: preorder, inorder, postorder
- **Operações fundamentais** em árvores binárias
- **Diferentes representações** da mesma estrutura de dados
- **Relação entre índices** em representação por array
- **Comparação de árvores**: verificação de estruturas idênticas
- **Árvores soma**: validação e conversão de árvores
- **Algoritmos de busca**: caminhos e ancestrais em árvores
- **Manipulação de árvores**: transformação de valores baseada em subárvores
- **Algoritmos recursivos** para processamento de árvores

### Lista 3: Árvores de Busca Balanceadas

- **Árvores de busca binária (BST)**: ordenação e busca eficiente
- **Árvores AVL**: auto-balanceamento com fator de balanceamento
- **Rotações**: simples (LL, RR) e duplas (LR, RL)
- **Árvores Rubro-Negras**: balanceamento por cores
- **Propriedades de balanceamento**: altura, fator e cores
- **Inserção e remoção** com rebalanceamento automático
- **Complexidade logarítmica** garantida em árvores balanceadas
- **Mapeamento chave-valor** em estruturas de árvore
- **Visualização de estruturas**: representação hierárquica e cores
- **Comparação de desempenho** entre diferentes tipos de árvores

### Lista 4: Algoritmos de Ordenação

- **Análise de complexidade**: O(n²), O(n log n) e O(n + k)
- **Algoritmos quadráticos**: Insertion, Selection e Bubble Sort
- **Algoritmos logarítmicos**: Shell, Merge, Quick e Heap Sort
- **Algoritmos lineares**: Counting Sort para ranges limitados
- **Divide and Conquer**: Merge Sort e Quick Sort
- **Estruturas auxiliares**: Heap no Heap Sort
- **Otimizações**: gaps no Shell Sort, pivô no Quick Sort
- **Análise prática**: contagem de comparações e trocas
- **Comparação de performance**: estudo empírico entre algoritmos
- **Estabilidade**: comportamento com elementos iguais

## 🛠️ Requisitos

- **Python 3.6+**
- Nenhuma dependência externa (apenas biblioteca padrão)

---

**Autor:** Eduardo Inácio  
**Matricula:** 1612611  
**Disciplina:** Estruturas de Dados  
**Instituição:** Universidade Estadual do Ceará
