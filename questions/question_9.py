from stack import ArrayStack

def eh_operador(char):
    """Verifica se o caractere é um operador"""
    return char in ['+', '-', '*', '/', '^']

def eh_operando(char):
    """Verifica se o caractere é um operando (número ou letra)"""
    return char.isalnum()

def prefixa_para_infixa(expressao_prefixa):
    """Converte uma expressão prefixa para infixa"""
    pilha = ArrayStack()
    
    # Processa a expressão da direita para a esquerda
    for i in range(len(expressao_prefixa) - 1, -1, -1):
        char = expressao_prefixa[i]
        
        if char == ' ':
            continue
            
        if eh_operando(char):
            pilha.push(char)
        elif eh_operador(char):
            # Desempilha dois operandos
            operando1 = pilha.pop()
            operando2 = pilha.pop()
            # Cria expressão infixa com parênteses
            expressao_infixa = f"({operando1}{char}{operando2})"
            pilha.push(expressao_infixa)
    
    return pilha.top()

def prefixa_para_posfixa(expressao_prefixa):
    """Converte uma expressão prefixa para pós-fixa"""
    pilha = ArrayStack()
    
    # Processa a expressão da direita para a esquerda
    for i in range(len(expressao_prefixa) - 1, -1, -1):
        char = expressao_prefixa[i]
        
        if char == ' ':
            continue
            
        if eh_operando(char):
            pilha.push(char)
        elif eh_operador(char):
            # Desempilha dois operandos
            operando1 = pilha.pop()
            operando2 = pilha.pop()
            # Cria expressão pós-fixa
            expressao_posfixa = f"{operando1}{operando2}{char}"
            pilha.push(expressao_posfixa)
    
    return pilha.top()

def exercicio_9():
    """
    Escreva um programa para converter uma expressão aritmética na forma prefixa para
    formas infixas e pós-fixadas equivalentes.
    """
    print("=== Exercício 9 - Conversão de Expressão Prefixa ===")
    
    # Casos de teste com expressões prefixas
    expressoes_prefixas = [
        "+ A B",
        "- * A B C",
        "+ * A B * C D",
        "* + A B - C D",
        "/ + A B * C D",
        "+ - A B * C / D E"
    ]
    
    for i, exp_prefixa in enumerate(expressoes_prefixas, 1):
        print(f"\nTeste {i}:")
        print(f"  Prefixa:  {exp_prefixa}")
        
        # Mostra o processo de conversão para infixa (primeiro exemplo)
        if i == 1:
            print(f"  Processo para infixa:")
            pilha_demo = ArrayStack()
            tokens = exp_prefixa.replace(' ', '')
            for j in range(len(tokens) - 1, -1, -1):
                char = tokens[j]
                if eh_operando(char):
                    pilha_demo.push(char)
                    print(f"    '{char}' -> empilha operando, pilha: {pilha_demo._data}")
                elif eh_operador(char):
                    op1 = pilha_demo.pop()
                    op2 = pilha_demo.pop()
                    resultado = f"({op1}{char}{op2})"
                    pilha_demo.push(resultado)
                    print(f"    '{char}' -> cria ({op1}{char}{op2}), pilha: {pilha_demo._data}")
        
        # Conversões
        infixa = prefixa_para_infixa(exp_prefixa)
        posfixa = prefixa_para_posfixa(exp_prefixa)
        
        print(f"  Infixa:   {infixa}")
        print(f"  Pós-fixa: {posfixa}")
    
    print(f"\n--- Como funciona o algoritmo ---")
    print("PREFIXA → INFIXA:")
    print("1. Processa expressão da direita para a esquerda")
    print("2. Operandos: empilha diretamente")
    print("3. Operadores: desempilha 2 operandos, cria (op1 oper op2)")
    print()
    print("PREFIXA → PÓS-FIXA:")
    print("1. Processa expressão da direita para a esquerda") 
    print("2. Operandos: empilha diretamente")
    print("3. Operadores: desempilha 2 operandos, cria op1 op2 oper")

if __name__ == "__main__":
    exercicio_9()