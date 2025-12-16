from linkedStack import LinkedStack

def contar_nos_recursivo(head):
    """
    Algoritmo recursivo que conta o número de nós em uma lista encadeada simples.
    
    Args:
        head: Referência ao primeiro nó da lista
    
    Returns:
        Número de nós na lista
    """
    # Caso base: se a lista estiver vazia
    if head is None:
        return 0
    
    # Caso recursivo: 1 (nó atual) + contagem do resto da lista
    return 1 + contar_nos_recursivo(head._next)

def criar_lista_encadeada(elementos):
    if not elementos:
        return None
    
    # Cria o primeiro nó
    head = LinkedStack._Node(elementos[0], None)
    current = head
    
    # Adiciona os demais elementos
    for elemento in elementos[1:]:
        current._next = LinkedStack._Node(elemento, None)
        current = current._next
    
    return head

def imprimir_lista(head):
    if head is None:
        return "Lista vazia"
    
    elementos = []
    current = head
    while current is not None:
        elementos.append(str(current._element))
        current = current._next
    return " -> ".join(elementos)

def exercicio_15():
    print("\n" + "="*70)
    print("EXERCÍCIO 15 - LISTA 1")
    print("="*70)
    print("Contar nós em lista encadeada (recursivo)")
    print("="*70)
    
    # Teste 1: Lista com vários elementos
    lista1 = criar_lista_encadeada([1, 2, 3, 4, 5])
    count1 = contar_nos_recursivo(lista1)
    print(f"Lista: {imprimir_lista(lista1)}")
    print(f"Número de nós: {count1}")
    print()
    
    # Teste 2: Lista com um elemento
    lista2 = criar_lista_encadeada([10])
    count2 = contar_nos_recursivo(lista2)
    print(f"Lista: {imprimir_lista(lista2)}")
    print(f"Número de nós: {count2}")
    print()
    
    # Teste 3: Lista vazia
    lista3 = criar_lista_encadeada([])
    count3 = contar_nos_recursivo(lista3)
    print(f"Lista: {imprimir_lista(lista3)}")
    print(f"Número de nós: {count3}")
    print()
    
    # Teste 4: Lista maior
    lista4 = criar_lista_encadeada([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    count4 = contar_nos_recursivo(lista4)
    print(f"Lista: {imprimir_lista(lista4)}")
    print(f"Número de nós: {count4}")
    print()