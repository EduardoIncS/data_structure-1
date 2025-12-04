from stack import ArrayStack

def transfer(S, T):
    """
    Transfere todos os elementos da pilha S para a pilha T,
    de modo que o elemento que começou no topo de S seja o primeiro
    a ser inserido em T, e o elemento na parte inferior de S termine no topo de T.
    """
    while not S.is_empty():
        elemento = S.pop()
        T.push(elemento)

def exercicio_3():
    """
    Implementa e testa a função transfer(S, T) que transfere todos os elementos
    da pilha S para a pilha T.
    """
    print("=== Exercício 3 - Função Transfer(S, T) ===")
    
    # Criando duas pilhas
    S = ArrayStack()
    T = ArrayStack()
    
    # Populando a pilha S com alguns elementos
    elementos = [1, 2, 3, 4, 5]
    print("Adicionando elementos na pilha S:")
    for elem in elementos:
        S.push(elem)
        print(f"  push({elem}) -> S: {S._data}")
    
    print(f"\nEstado inicial:")
    print(f"  Pilha S: {S._data} (topo: {S.top() if not S.is_empty() else 'vazia'})")
    print(f"  Pilha T: {T._data} (topo: {T.top() if not T.is_empty() else 'vazia'})")
    
    # Executando a transferência
    print(f"\nExecutando transfer(S, T)...")
    transfer(S, T)
    
    print(f"\nEstado após transferência:")
    print(f"  Pilha S: {S._data} (topo: {S.top() if not S.is_empty() else 'vazia'})")
    print(f"  Pilha T: {T._data} (topo: {T.top() if not T.is_empty() else 'vazia'})")
    
    # Verificando a ordem dos elementos em T
    print(f"\nVerificando ordem em T (removendo elementos):")
    while not T.is_empty():
        elemento = T.pop()
        print(f"  pop() -> {elemento}, T restante: {T._data}")
    
    print(f"\n--- Demonstração adicional ---")
    print("Testando com pilha S contendo: [A, B, C] (onde C está no topo)")

if __name__ == "__main__":
    exercicio_3()