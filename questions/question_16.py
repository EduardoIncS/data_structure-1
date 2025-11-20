from linkedStack import LinkedStack

def contar_nos_lista_circular(tail):
    """
    Função que conta o número de nós em uma lista circularmente encadeada.
    
    Args:
        tail: Referência ao último nó da lista circular (ou None se vazia)
    
    Returns:
        Número de nós na lista circular
    """
    # Se a lista estiver vazia
    if tail is None:
        return 0
    
    # Se há apenas um nó (aponta para si mesmo)
    if tail._next == tail:
        return 1
    
    # Percorre a lista circular contando os nós
    count = 1  # Conta o nó tail
    current = tail._next  # Começa do primeiro nó
    
    # Percorre até voltar ao tail
    while current != tail:
        count += 1
        current = current._next
    
    return count

def criar_lista_circular(elementos):
    """Função auxiliar para criar uma lista circularmente encadeada."""
    if not elementos:
        return None
    
    # Cria o primeiro nó
    head = LinkedStack._Node(elementos[0], None)
    current = head
    
    # Adiciona os demais elementos
    for elemento in elementos[1:]:
        current._next = LinkedStack._Node(elemento, None)
        current = current._next
    
    # Faz a ligação circular: último nó aponta para o primeiro
    tail = current
    tail._next = head
    
    return tail  # Retorna referência ao último nó

def imprimir_lista_circular(tail, max_rotacoes=2):
    """Função auxiliar para imprimir a lista circular."""
    if tail is None:
        return "Lista vazia"
    
    elementos = []
    current = tail._next  # Começa do primeiro nó
    count = 0
    max_elementos = contar_nos_lista_circular(tail) * max_rotacoes
    
    # Imprime alguns elementos para mostrar a circularidade
    for _ in range(max_elementos):
        elementos.append(str(current._element))
        current = current._next
        count += 1
        
        # Para evitar loop infinito na impressão
        if count >= max_elementos:
            break
    
    return " -> ".join(elementos) + " -> ..."

def exercicio_16():
    print("Exercício 16: Contar nós em lista circularmente encadeada")
    
    # Teste 1: Lista com vários elementos
    lista1 = criar_lista_circular([1, 2, 3, 4, 5])
    count1 = contar_nos_lista_circular(lista1)
    print(f"Lista circular: {imprimir_lista_circular(lista1, 1)}")
    print(f"Número de nós: {count1}")
    print()
    
    # Teste 2: Lista com um elemento
    lista2 = criar_lista_circular([10])
    count2 = contar_nos_lista_circular(lista2)
    print(f"Lista circular: {imprimir_lista_circular(lista2, 2)}")
    print(f"Número de nós: {count2}")
    print()
    
    # Teste 3: Lista vazia
    lista3 = criar_lista_circular([])
    count3 = contar_nos_lista_circular(lista3)
    print(f"Lista vazia - Número de nós: {count3}")
    print()
    
    # Teste 4: Lista com dois elementos
    lista4 = criar_lista_circular([100, 200])
    count4 = contar_nos_lista_circular(lista4)
    print(f"Lista circular: {imprimir_lista_circular(lista4, 2)}")
    print(f"Número de nós: {count4}")
    print()
    
    # Teste 5: Lista maior
    lista5 = criar_lista_circular([1, 2, 3, 4, 5, 6, 7])
    count5 = contar_nos_lista_circular(lista5)
    print(f"Lista circular: {imprimir_lista_circular(lista5, 1)}")
    print(f"Número de nós: {count5}")