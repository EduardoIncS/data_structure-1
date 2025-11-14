from queue import ArrayQueue

def exercicio_6():
    """
    Execute a seguinte série de operações de fila, assumindo uma fila inicialmente vazia:
    enqueue(5), enqueue(3), dequeue(), enqueue(2), enqueue(8), dequeue(), dequeue(), enqueue(9),
    enqueue(1), dequeue(), enqueue(7), dequeue(), enqueue(6), dequeue(), enqueue(4), dequeue(), dequeue().
    """
    print("=== Exercício 6 - Sequência de Operações de Fila ===")
    
    # Criando fila inicialmente vazia
    fila = ArrayQueue()
    
    # Executando as operações uma por uma
    operacoes = [
        ('enqueue', 5), ('enqueue', 3), ('dequeue',), ('enqueue', 2), ('enqueue', 8),
        ('dequeue',), ('dequeue',), ('enqueue', 9), ('enqueue', 1), ('dequeue',),
        ('enqueue', 7), ('dequeue',), ('enqueue', 6), ('dequeue',), ('enqueue', 4),
        ('dequeue',), ('dequeue',)
    ]
    
    for i, operacao in enumerate(operacoes, 1):
        if operacao[0] == 'enqueue':
            valor = operacao[1]
            fila.enqueue(valor)
            # Mostrando elementos válidos na fila (do front até size)
            elementos = []
            for j in range(fila._size):
                pos = (fila._front + j) % len(fila._data)
                elementos.append(fila._data[pos])
            print(f"{i:2d}. enqueue({valor}) -> Fila: {elementos}")
        else:  # dequeue
            if not fila.is_empty():
                valor_removido = fila.dequeue()
                # Mostrando elementos válidos na fila após remoção
                elementos = []
                for j in range(fila._size):
                    pos = (fila._front + j) % len(fila._data)
                    elementos.append(fila._data[pos])
                print(f"{i:2d}. dequeue() -> {valor_removido} removido, Fila: {elementos}")
            else:
                print(f"{i:2d}. dequeue() -> Fila vazia!")
    
    # Estado final
    elementos_finais = []
    for j in range(fila._size):
        pos = (fila._front + j) % len(fila._data)
        elementos_finais.append(fila._data[pos])
    
    print(f"\nEstado final da fila: {elementos_finais}")
    print(f"Tamanho final: {len(fila)}")
    
    if not fila.is_empty():
        print(f"Primeiro elemento (front): {fila.first()}")
    else:
        print("Fila está vazia")