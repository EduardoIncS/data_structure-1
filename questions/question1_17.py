from linkedStack import LinkedStack

def reverter_lista_recursivo(head):
    """
    Algoritmo recursivo rápido para reverter uma lista encadeada simples.
    
    Args:
        head: Referência ao primeiro nó da lista original
    
    Returns:
        Referência ao primeiro nó da lista revertida (antigo último nó)
    """
    # Caso base: lista vazia ou com um elemento
    if head is None or head._next is None:
        return head
    
    # Recursão: reverte o resto da lista
    new_head = reverter_lista_recursivo(head._next)
    
    # Inverte a ligação: o próximo nó aponta de volta para o atual
    head._next._next = head
    head._next = None  # O antigo primeiro se torna o último
    
    return new_head

def criar_lista_encadeada(elementos):
    """Função auxiliar para criar uma lista encadeada a partir de uma lista Python."""
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
    """Função auxiliar para imprimir a lista."""
    if head is None:
        return "Lista vazia"
    
    elementos = []
    current = head
    while current is not None:
        elementos.append(str(current._element))
        current = current._next
    return " -> ".join(elementos) + " -> None"

def lista_para_array(head):
    """Converte lista encadeada para array Python para facilitar comparação."""
    elementos = []
    current = head
    while current is not None:
        elementos.append(current._element)
        current = current._next
    return elementos

def exercicio_17():
    print("\n" + "="*70)
    print("EXERCÍCIO 17 - LISTA 1")
    print("="*70)
    print("Reversão recursiva de lista encadeada")
    print("="*70)
    
    # Teste 1: Lista com vários elementos
    print("Teste 1: Lista [1, 2, 3, 4, 5]")
    lista1 = criar_lista_encadeada([1, 2, 3, 4, 5])
    print(f"Original: {imprimir_lista(lista1)}")
    lista1_revertida = reverter_lista_recursivo(lista1)
    print(f"Revertida: {imprimir_lista(lista1_revertida)}")
    print(f"Array resultado: {lista_para_array(lista1_revertida)}")
    print()
    
    # Teste 2: Lista com um elemento
    print("Teste 2: Lista [42]")
    lista2 = criar_lista_encadeada([42])
    print(f"Original: {imprimir_lista(lista2)}")
    lista2_revertida = reverter_lista_recursivo(lista2)
    print(f"Revertida: {imprimir_lista(lista2_revertida)}")
    print()
    
    # Teste 3: Lista vazia
    print("Teste 3: Lista vazia")
    lista3 = criar_lista_encadeada([])
    print(f"Original: {imprimir_lista(lista3)}")
    lista3_revertida = reverter_lista_recursivo(lista3)
    print(f"Revertida: {imprimir_lista(lista3_revertida)}")
    print()
    
    # Teste 4: Lista com dois elementos
    print("Teste 4: Lista [10, 20]")
    lista4 = criar_lista_encadeada([10, 20])
    print(f"Original: {imprimir_lista(lista4)}")
    lista4_revertida = reverter_lista_recursivo(lista4)
    print(f"Revertida: {imprimir_lista(lista4_revertida)}")
    print()
    
    # Teste 5: Lista maior
    print("Teste 5: Lista [1, 2, 3, 4, 5, 6, 7, 8]")
    lista5 = criar_lista_encadeada([1, 2, 3, 4, 5, 6, 7, 8])
    print(f"Original: {imprimir_lista(lista5)}")
    lista5_revertida = reverter_lista_recursivo(lista5)
    print(f"Revertida: {imprimir_lista(lista5_revertida)}")
    print(f"Array resultado: {lista_para_array(lista5_revertida)}")