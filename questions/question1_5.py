from stack import ArrayStack

def inverter_lista(lista):
    """
    Implementa uma função que inverte uma lista de elementos colocando-os em uma pilha
    em uma ordem e escrevendo-os de volta na lista na ordem inversa.
    """
    # Criando uma pilha auxiliar
    pilha = ArrayStack()
    
    # Colocando todos os elementos da lista na pilha
    for elemento in lista:
        pilha.push(elemento)
    
    # Removendo elementos da pilha e colocando de volta na lista
    for i in range(len(lista)):
        lista[i] = pilha.pop()
    
    return lista

def exercicio_5():
    """
    Implementa e testa uma função que inverte uma lista usando uma pilha.
    """
    print("=== Exercício 5 - Inverter Lista usando Pilha ===")
    
    # Testando com diferentes tipos de listas
    listas_teste = [
        [1, 2, 3, 4, 5],
        ['A', 'B', 'C', 'D'],
        [10, 20, 30],
        [100]
    ]
    
    for i, lista_original in enumerate(listas_teste, 1):
        print(f"\nTeste {i}:")
        lista_copia = lista_original.copy()  # Fazendo uma cópia para preservar o original
        
        print(f"  Lista original: {lista_original}")
        
        # Mostrando o processo da pilha
        pilha_demo = ArrayStack()
        print(f"  Adicionando na pilha:")
        for elem in lista_copia:
            pilha_demo.push(elem)
            print(f"    push({elem}) -> pilha: {pilha_demo._data}")
        
        print(f"  Removendo da pilha:")
        resultado = []
        while not pilha_demo.is_empty():
            elem = pilha_demo.pop()
            resultado.append(elem)
            print(f"    pop() -> {elem}, pilha: {pilha_demo._data}")
        
        print(f"  Lista invertida: {resultado}")
        
        # Testando a função principal
        lista_invertida = inverter_lista(lista_copia)
        print(f"  Resultado da função: {lista_invertida}")

if __name__ == "__main__":
    exercicio_5()