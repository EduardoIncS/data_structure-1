from stack import ArrayStack

def remover_todos_recursivo(pilha):
    """
    Método recursivo para remover todos os elementos de uma pilha.
    """
    if not pilha.is_empty():
        elemento = pilha.pop()
        print(f"Removendo: {elemento}")
        remover_todos_recursivo(pilha)

def exercicio_4():
    """
    Fornece um método recursivo para remover todos os elementos de uma pilha.
    """
    print("=== Exercício 4 - Método Recursivo para Remover Todos os Elementos ===")
    
    # Criando e populando uma pilha
    pilha = ArrayStack()
    elementos = [10, 20, 30, 40, 50]
    
    print("Adicionando elementos na pilha:")
    for elem in elementos:
        pilha.push(elem)
        print(f"  push({elem}) -> Pilha: {pilha._data}")
    
    print(f"\nPilha antes da remoção: {pilha._data}")
    print(f"Tamanho: {len(pilha)}")
    
    print(f"\nExecutando remoção recursiva:")
    remover_todos_recursivo(pilha)
    
    print(f"\nPilha após remoção: {pilha._data}")
    print(f"Tamanho: {len(pilha)}")
    print(f"Pilha está vazia: {pilha.is_empty()}")