from stack import ArrayStack

def exercicio_2():
    """
    Executa a seguinte série de operações de pilha, assumindo uma pilha inicialmente vazia:
    push(5), push(3), pop(), push(2), push(8), pop(), pop(), push(9), push(1), pop(), push(7),
    push(6), pop(), pop(), push(4), pop(), pop().
    """
    print("=== Exercício 2 - Sequência de Operações de Pilha ===")
    
    # Criando pilha inicialmente vazia
    pilha = ArrayStack()
    
    # Executando as operações uma por uma
    operacoes = [
        ('push', 5), ('push', 3), ('pop',), ('push', 2), ('push', 8),
        ('pop',), ('pop',), ('push', 9), ('push', 1), ('pop',),
        ('push', 7), ('push', 6), ('pop',), ('pop',), ('push', 4),
        ('pop',), ('pop',)
    ]
    
    for i, operacao in enumerate(operacoes, 1):
        if operacao[0] == 'push':
            valor = operacao[1]
            pilha.push(valor)
            print(f"{i:2d}. push({valor}) -> Pilha: {pilha._data}")
        else:  # pop
            if not pilha.is_empty():
                valor_removido = pilha.pop()
                print(f"{i:2d}. pop() -> {valor_removido} removido, Pilha: {pilha._data}")
            else:
                print(f"{i:2d}. pop() -> Pilha vazia!")
    
    print(f"\nEstado final da pilha: {pilha._data}")
    print(f"Tamanho final: {len(pilha)}")
    
    if not pilha.is_empty():
        print(f"Elemento no topo: {pilha.top()}")
    else:
        print("Pilha está vazia")

if __name__ == "__main__":
    exercicio_2()