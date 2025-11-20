from linkedStack import LinkedStack

def separar_positivos_negativos(head):
    """
    Usando uma lista encadeada, escreve um programa para criar duas novas listas encadeadas, 
    uma contendo todos os números positivos e a outra contendo todos os números negativos.
    
    Args:
        head: Referência ao primeiro nó da lista original
    
    Returns:
        Tupla (lista_positivos, lista_negativos) com as referências às novas listas
    """
    # Inicializa as novas listas
    head_positivos = None
    tail_positivos = None
    head_negativos = None
    tail_negativos = None
    
    # Percorre a lista original
    current = head
    while current is not None:
        valor = current._element
        
        if valor > 0:  # Número positivo
            novo_no = LinkedStack._Node(valor, None)
            if head_positivos is None:
                head_positivos = novo_no
                tail_positivos = novo_no
            else:
                tail_positivos._next = novo_no
                tail_positivos = novo_no
                
        elif valor < 0:  # Número negativo
            novo_no = LinkedStack._Node(valor, None)
            if head_negativos is None:
                head_negativos = novo_no
                tail_negativos = novo_no
            else:
                tail_negativos._next = novo_no
                tail_negativos = novo_no
        
        # Nota: zero é ignorado (nem positivo nem negativo)
        current = current._next
    
    return head_positivos, head_negativos

def criar_lista_encadeada(elementos):
    """Função auxiliar para criar uma lista encadeada a partir de uma lista Python."""
    if not elementos:
        return None
    
    head = LinkedStack._Node(elementos[0], None)
    current = head
    
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
    """Converte lista encadeada para array Python."""
    elementos = []
    current = head
    while current is not None:
        elementos.append(current._element)
        current = current._next
    return elementos

def exercicio_18():
    print("Exercício 18: Separar números positivos e negativos")
    
    # Teste 1: Lista mista com positivos e negativos
    print("Teste 1: Lista [-5, 3, -2, 8, -1, 7, -9, 4]")
    lista1 = criar_lista_encadeada([-5, 3, -2, 8, -1, 7, -9, 4])
    print(f"Lista original: {imprimir_lista(lista1)}")
    
    positivos1, negativos1 = separar_positivos_negativos(lista1)
    print(f"Lista positivos: {imprimir_lista(positivos1)}")
    print(f"Lista negativos: {imprimir_lista(negativos1)}")
    print(f"Array positivos: {lista_para_array(positivos1)}")
    print(f"Array negativos: {lista_para_array(negativos1)}")
    print()
    
    # Teste 2: Lista só com positivos
    print("Teste 2: Lista [1, 5, 10, 15]")
    lista2 = criar_lista_encadeada([1, 5, 10, 15])
    print(f"Lista original: {imprimir_lista(lista2)}")
    
    positivos2, negativos2 = separar_positivos_negativos(lista2)
    print(f"Lista positivos: {imprimir_lista(positivos2)}")
    print(f"Lista negativos: {imprimir_lista(negativos2)}")
    print()
    
    # Teste 3: Lista só com negativos
    print("Teste 3: Lista [-1, -5, -10, -15]")
    lista3 = criar_lista_encadeada([-1, -5, -10, -15])
    print(f"Lista original: {imprimir_lista(lista3)}")
    
    positivos3, negativos3 = separar_positivos_negativos(lista3)
    print(f"Lista positivos: {imprimir_lista(positivos3)}")
    print(f"Lista negativos: {imprimir_lista(negativos3)}")
    print()
    
    # Teste 4: Lista com zeros (devem ser ignorados)
    print("Teste 4: Lista [-3, 0, 5, 0, -7, 2, 0]")
    lista4 = criar_lista_encadeada([-3, 0, 5, 0, -7, 2, 0])
    print(f"Lista original: {imprimir_lista(lista4)}")
    
    positivos4, negativos4 = separar_positivos_negativos(lista4)
    print(f"Lista positivos: {imprimir_lista(positivos4)}")
    print(f"Lista negativos: {imprimir_lista(negativos4)}")
    print(f"Nota: Zeros são ignorados (nem positivos nem negativos)")
    print()
    
    # Teste 5: Lista vazia
    print("Teste 5: Lista vazia")
    lista5 = criar_lista_encadeada([])
    print(f"Lista original: {imprimir_lista(lista5)}")
    
    positivos5, negativos5 = separar_positivos_negativos(lista5)
    print(f"Lista positivos: {imprimir_lista(positivos5)}")
    print(f"Lista negativos: {imprimir_lista(negativos5)}")