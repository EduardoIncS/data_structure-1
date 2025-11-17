from linkedStack import LinkedStack

def concatenar_listas(lista_L, lista_M):
    """
    Algoritmo para concatenar duas listas encadeadas simples L e M, dadas
    apenas referências ao primeiro nó de cada lista, em uma única lista L que contém todos os
    nós de L seguidos por todos os nós de M.
    """
    # Se L estiver vazia, retorna M
    if lista_L is None:
        return lista_M
    
    # Se M estiver vazia, retorna L
    if lista_M is None:
        return lista_L
    
    # Encontra o último nó de L
    current = lista_L
    while current._next is not None:
        current = current._next
    
    # Liga o último nó de L ao primeiro nó de M
    current._next = lista_M
    
    return lista_L

def criar_lista(elementos):
    if not elementos:
        return None
    
    head = LinkedStack._Node(elementos[0], None)
    current = head
    
    for elemento in elementos[1:]:
        current._next = LinkedStack._Node(elemento, None)
        current = current._next
    
    return head

def imprimir_lista(head):
    if head is None:
        return "None"
    
    elementos = []
    current = head
    while current is not None:
        elementos.append(str(current._element))
        current = current._next
    return " -> ".join(elementos) + " -> None"

def exercicio_14():
    """
    Implementa um algoritmo para concatenar duas listas encadeadas simples L e M.
    """
    print("=== Exercício 14 - Concatenar Duas Listas Encadeadas ===")
    
    casos_teste = [
        ([1, 2, 3], [4, 5, 6]),
        ([1], [2, 3, 4]),
        ([1, 2, 3], []),
        ([], [1, 2, 3]),
        ([], []),
        (['A', 'B'], ['C', 'D', 'E']),
        ([10, 20], [30]),
    ]
    
    for i, (elementos_L, elementos_M) in enumerate(casos_teste, 1):
        print(f"\nTeste {i}:")
        
        # Criando as listas L e M
        lista_L = criar_lista(elementos_L)
        lista_M = criar_lista(elementos_M)
        
        print(f"  Lista L: {imprimir_lista(lista_L)}")
        print(f"  Lista M: {imprimir_lista(lista_M)}")
        
        # Concatenando as listas
        lista_concatenada = concatenar_listas(lista_L, lista_M)
        
        print(f"  Resultado (L + M): {imprimir_lista(lista_concatenada)}")
        
        # Demonstração do processo para casos pequenos
        if i <= 3 and elementos_L and elementos_M:
            print(f"  Processo:")
            print(f"    1. Percorre L até o último nó")
            print(f"    2. Liga último nó de L ao primeiro nó de M")
            print(f"    3. Retorna referência do início de L")
    
    print(f"\nAlgoritmo:")
    print("1. Se L vazia → retorna M")
    print("2. Se M vazia → retorna L") 
    print("3. Caso geral:")
    print("   - Percorre L até encontrar o último nó (next == None)")
    print("   - Liga o último nó de L ao primeiro nó de M")
    print("   - Retorna a referência do início de L")
    print("Complexidade: O(|L|) tempo, O(1) espaço")

if __name__ == "__main__":
    exercicio_14()