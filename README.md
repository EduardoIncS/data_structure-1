# Estruturas de Dados 1 - Atividades Práticas

Este repositório contém as implementações e exercícios práticos da disciplina de **Estruturas de Dados**, abordando desde estruturas lineares até estruturas hierárquicas.

## 📚 Sobre o Projeto

Atividade acadêmica que implementa e demonstra o uso de diversas estruturas de dados através de exercícios práticos organizados em listas de implementação. Cada questão está organizada em arquivos separados com implementações específicas e testes demonstrativos.

### 📋 Listas de Implementação

- **Lista 1**: Estruturas lineares - Stack (Pilha), Queue (Fila), Deque (Fila Dupla) e estruturas encadeadas
- **Lista 2**: Estruturas hierárquicas - Árvores Binárias e travessias

## 🚀 Como Executar

### Executar todas as questões:

```bash
python main.py
```

### Executar uma questão específica:

```bash
# Lista 1 (Estruturas Lineares)
python -m questions.question1_X  # onde X é o número da questão (2-20)

# Lista 2 (Árvores)
python -m questions.question2_X  # onde X é o número da questão
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

### 🌳 Lista 2: Estruturas Hierárquicas

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

## 📁 Estrutura do Projeto

```
├── main.py                    # Executor principal de todas as questões
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
├── # Lista 2: Árvores
├── Tree.py                    # Classe abstrata base para árvores
├── binaryTree.py              # Classe abstrata para árvores binárias
├── linkedBinaryTree.py        # Árvore binária com nós encadeados
├── arrayBinaryTree.py         # Árvore binária com array
│
└── questions/                 # Pasta com todos os exercícios
    ├── __init__.py
    │
    ├── # Lista 1: Estruturas Lineares
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
    └── # Lista 2: Árvores
        ├── question2_4.py     # Verificação de árvores idênticas
        ├── question2_5.py     # Verificação de árvore soma
        ├── question2_6.py     # Caminhos da raiz até as folhas
        ├── question2_7.py     # Encontrar ancestrais de um nó
        └── question2_8.py     # Conversão para árvore soma
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

### Lista 2: Árvores

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

## 🛠️ Requisitos

- **Python 3.6+**
- Nenhuma dependência externa (apenas biblioteca padrão)

---

**Autor:** Eduardo Inácio  
**Matricula:** 1612611  
**Disciplina:** Estruturas de Dados  
**Instituição:** Universidade Estadual do Ceará
