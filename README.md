# Estruturas de Dados 1 - Atividades Práticas

Este repositório contém as implementações e exercícios práticos da disciplina de **Estruturas de Dados**, focando em estruturas lineares fundamentais: **Stack (Pilha)**, **Queue (Fila)** e **Deque (Fila Dupla)**.

## 📚 Sobre o Projeto

Atividade acadêmica que implementa e demonstra o uso de estruturas de dados lineares através de exercícios práticos. Cada questão está organizada em arquivos separados com implementações específicas e testes demonstrativos.

## 🚀 Como Executar

### Executar todas as questões:

```bash
python main.py
```

### Executar uma questão específica:

```bash
python question_X.py  # onde X é o número da questão (2-15)
```

## 🏗️ Estruturas de Dados Implementadas

### 📚 **ArrayStack** (`stack.py`)

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

### 🚶 **ArrayQueue** (`queue.py`)

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

### ↔️ **ArrayDeque** (`deque.py`)

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

## 📁 Estrutura do Projeto

```
├── main.py              # Executor principal de todas as questões
├── stack.py             # Implementação da pilha
├── queue.py             # Implementação da fila
├── deque.py             # Implementação do deque
├── question_2.py        # Exercício 2: Operações de pilha
├── question_3.py        # Exercício 3: Função transfer entre pilhas
├── question_4.py        # Exercício 4: Remoção recursiva de pilha
├── question_5.py        # Exercício 5: Inversão de lista com pilha
├── question_6.py        # Exercício 6: Operações de fila
├── question_7.py        # Exercício 7: Operações de deque
├── question_8.py        # Exercício 8: Verificação de parênteses
└── README.md            # Este arquivo
```

## 🎯 Conceitos Demonstrados

- **Implementação de TADs** (Tipos Abstratos de Dados)
- **Arrays circulares** e redimensionamento dinâmico
- **Complexidade temporal O(1)** para operações básicas
- **Algoritmos clássicos** usando estruturas lineares
- **Balanceamento de parênteses** com pilhas
- **Inversão de sequências** usando pilhas
- **Transferência entre estruturas**

## 🛠️ Requisitos

- **Python 3.6+**
- Nenhuma dependência externa (apenas biblioteca padrão)

---

**Autor:** Eduardo Inácio  
**Matricula:** 1612611  
**Disciplina:** Estruturas de Dados  
**Instituição:** Universidade Estadual do Ceará
