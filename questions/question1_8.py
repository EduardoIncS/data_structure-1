from stack import ArrayStack

def verificar_parenteses(expressao):
    """
    Verifica se em uma string contendo uma expressão aritmética, 
    os parênteses de abertura e fechamento estão bem formados ou não.
    """
    pilha = ArrayStack()
    
    for caractere in expressao:
        if caractere == '(':
            pilha.push(caractere)
        elif caractere == ')':
            if pilha.is_empty():
                return False  # Parêntese de fechamento sem correspondente
            pilha.pop()
    
    # Se a pilha estiver vazia, todos os parênteses foram balanceados
    return pilha.is_empty()

def exercicio_8():
    """
    Escreve um programa para verificar se em uma string contendo uma expressão aritmética,
    os parênteses de abertura e fechamento estão bem formados ou não.
    """
    print("=== Exercício 8 - Verificação de Parênteses Bem Formados ===")
    
    # Casos de teste
    expressoes_teste = [
        "2 + 3 * (4 - 1)",
        "((2 + 3) * 4)",
        "(2 + 3) * (4 - 1)",
        "2 + 3 * 4",
        "((2 + 3)",
        "2 + 3) * 4",
        "(2 + (3 * 4))",
        "((()))",
        "((())",
        "()())",
        "",
        "(((2 + 3) * 4) - 1)",
        "2 + 3 * (4 - (1 + 2))"
    ]
    
    for i, expressao in enumerate(expressoes_teste, 1):
        resultado = verificar_parenteses(expressao)
        status = "✓ BEM FORMADA" if resultado else "✗ MAL FORMADA"
        
        print(f"{i:2d}. '{expressao}' -> {status}")
        
        # Mostrando o processo para algumas expressões
        if i <= 3:  # Apenas para as primeiras 3 expressões
            print(f"     Processo:")
            pilha_demo = ArrayStack()
            for j, char in enumerate(expressao):
                if char == '(':
                    pilha_demo.push(char)
                    print(f"       Pos {j}: '{char}' -> empilha, pilha: {pilha_demo._data}")
                elif char == ')':
                    if not pilha_demo.is_empty():
                        pilha_demo.pop()
                        print(f"       Pos {j}: '{char}' -> desempilha, pilha: {pilha_demo._data}")
                    else:
                        print(f"       Pos {j}: '{char}' -> erro! pilha vazia")
                        break
            print(f"       Final: pilha {pilha_demo._data} -> {'vazia (OK)' if pilha_demo.is_empty() else 'não vazia (ERRO)'}")
            print()
    
    print(f"\n--- Como funciona o algoritmo ---")
    print("1. Para cada '(' encontrado: empilha na pilha")
    print("2. Para cada ')' encontrado: verifica se há '(' na pilha para desempilhar")
    print("3. Se tentar desempilhar com pilha vazia: expressão mal formada")
    print("4. No final, se pilha estiver vazia: expressão bem formada")
    print("5. Se sobrar '(' na pilha: expressão mal formada")

if __name__ == "__main__":
    exercicio_8()