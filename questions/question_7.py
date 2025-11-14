from deque import ArrayDeque

def exercicio_7():
    """
    Execute a seguinte série de operações de deque, assumindo um deque inicialmente vazio:
    add_first(4), add_last(8), add_last(9), add_first(5), back(), delete_first(), delete_last(), add_last(7), 
    first(), last(), add_last(6), delete_first(), delete_first().
    """
    print("=== Exercício 7 - Sequência de Operações de Deque ===")
    
    # Criando deque inicialmente vazio
    deque = ArrayDeque()
    
    # Função auxiliar para mostrar o estado atual do deque
    def mostrar_deque():
        elementos = []
        for j in range(deque._size):
            pos = (deque._front + j) % len(deque._data)
            elementos.append(deque._data[pos])
        return elementos
    
    # Executando as operações uma por uma
    operacoes = [
        ('add_first', 4), ('add_last', 8), ('add_last', 9), ('add_first', 5), 
        ('back',), ('delete_first',), ('delete_last',), ('add_last', 7),
        ('first',), ('last',), ('add_last', 6), ('delete_first',), ('delete_first',)
    ]
    
    for i, operacao in enumerate(operacoes, 1):
        if operacao[0] == 'add_first':
            valor = operacao[1]
            deque.add_first(valor)
            print(f"{i:2d}. add_first({valor}) -> Deque: {mostrar_deque()}")
        elif operacao[0] == 'add_last':
            valor = operacao[1]
            deque.add_last(valor)
            print(f"{i:2d}. add_last({valor}) -> Deque: {mostrar_deque()}")
        elif operacao[0] == 'delete_first':
            if not deque.is_empty():
                valor_removido = deque.delete_first()
                print(f"{i:2d}. delete_first() -> {valor_removido} removido, Deque: {mostrar_deque()}")
            else:
                print(f"{i:2d}. delete_first() -> Deque vazio!")
        elif operacao[0] == 'delete_last':
            if not deque.is_empty():
                valor_removido = deque.delete_last()
                print(f"{i:2d}. delete_last() -> {valor_removido} removido, Deque: {mostrar_deque()}")
            else:
                print(f"{i:2d}. delete_last() -> Deque vazio!")
        elif operacao[0] == 'back':
            if not deque.is_empty():
                valor = deque.back()
                print(f"{i:2d}. back() -> {valor}, Deque: {mostrar_deque()}")
            else:
                print(f"{i:2d}. back() -> Deque vazio!")
        elif operacao[0] == 'first':
            if not deque.is_empty():
                valor = deque.first()
                print(f"{i:2d}. first() -> {valor}, Deque: {mostrar_deque()}")
            else:
                print(f"{i:2d}. first() -> Deque vazio!")
        elif operacao[0] == 'last':
            if not deque.is_empty():
                valor = deque.last()
                print(f"{i:2d}. last() -> {valor}, Deque: {mostrar_deque()}")
            else:
                print(f"{i:2d}. last() -> Deque vazio!")
    
    # Estado final
    print(f"\nEstado final do deque: {mostrar_deque()}")
    print(f"Tamanho final: {len(deque)}")
    
    if not deque.is_empty():
        print(f"Primeiro elemento (front): {deque.first()}")
        print(f"Último elemento (back): {deque.last()}")
    else:
        print("Deque está vazio")

if __name__ == "__main__":
    exercicio_7()