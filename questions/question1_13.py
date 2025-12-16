from linkedStack import LinkedStack

def encontrar_penultimo(head):
    """
    Algoritmo para encontrar o penúltimo nó em uma lista encadeada simples na
    qual o último nó é indicado por uma próxima referência de None.
    """
    if head is None or head._next is None:
        return None
    
    current = head
    while current._next._next is not None:
        current = current._next
    
    return current

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

def imprimir_lista_encadeada(head):
    if head is None:
        return "None"
    
    elementos = []
    current = head
    while current is not None:
        elementos.append(str(current._element))
        current = current._next
    return " -> ".join(elementos) + " -> None"

def exercicio_13():
    """
    Implementa um algoritmo para encontrar o penúltimo nó em uma lista encadeada simples.
    Utiliza a estrutura de nós do LinkedStack para manter consistência com o projeto.
    """
    print("\n" + "="*70)
    print("EXERCÍCIO 13 - LISTA 1")
    print("="*70)
    print("Encontrar Penúltimo Nó em Lista Encadeada")
    print("="*70)
    
    casos_teste = [
        [],
        [1],
        [1, 2],
        [1, 2, 3],
        [1, 2, 3, 4, 5],
        ['A', 'B', 'C', 'D'],
    ]
    
    for i, elementos in enumerate(casos_teste, 1):
        print(f"\nTeste {i}: {elementos}")
        
        head = criar_lista_encadeada(elementos)
        print(f"  Lista: {imprimir_lista_encadeada(head)}")
        
        penultimo = encontrar_penultimo(head)
        
        if penultimo:
            print(f"  Penúltimo nó: {penultimo._element}")
        else:
            print(f"  Penúltimo nó: None")
        
        # Processo detalhado para listas pequenas
        if len(elementos) <= 3 and elementos:
            print(f"  Percurso:")
            current = head
            posicao = 0
            while current:
                if current._next is None:
                    print(f"    Nó {posicao}: {current._element} (último)")
                elif current._next._next is None:
                    print(f"    Nó {posicao}: {current._element} (penúltimo)")
                else:
                    print(f"    Nó {posicao}: {current._element}")
                current = current._next
                posicao += 1
    
    print(f"\nAlgoritmo:")
    print("- Percorre a lista até encontrar um nó onde next.next == None")
    print("- Esse nó é o penúltimo da lista")
    print("- Complexidade: O(n) tempo, O(1) espaço")

if __name__ == "__main__":
    exercicio_13()