from stack import ArrayStack

def eh_numero(token):
    """Verifica se o token é um número"""
    try:
        int(token)
        return True
    except ValueError:
        return False

def eh_operador(token):
    """Verifica se o token é um operador"""
    return token in ['+', '-', '*', '/', '//', '%', '^', '**']

def calcular(operando1, operador, operando2):
    """Realiza a operação aritmética"""
    if operador == '+':
        return operando1 + operando2
    elif operador == '-':
        return operando1 - operando2
    elif operador == '*':
        return operando1 * operando2
    elif operador == '/':
        return operando1 // operando2  # Divisão inteira
    elif operador == '//':
        return operando1 // operando2
    elif operador == '%':
        return operando1 % operando2
    elif operador == '^' or operador == '**':
        return operando1 ** operando2
    else:
        raise ValueError(f"Operador desconhecido: {operador}")

def avaliar_posfixa(expressao):
    """Avalia uma expressão pós-fixa usando pilha"""
    pilha = ArrayStack()
    tokens = expressao.split()
    
    for token in tokens:
        if eh_numero(token):
            pilha.push(int(token))
        elif eh_operador(token):
            if len(pilha) < 2:
                raise ValueError("Expressão inválida: operandos insuficientes")
            operando2 = pilha.pop()
            operando1 = pilha.pop()
            resultado = calcular(operando1, token, operando2)
            pilha.push(resultado)
        else:
            raise ValueError(f"Token inválido: {token}")
    
    if len(pilha) != 1:
        raise ValueError("Expressão inválida: resultado incorreto")
    
    return pilha.pop()

def exercicio_10():
    """
    Implementa uma calculadora aritmética de inteiros usando pilhas.
    """
    print("\n" + "="*70)
    print("EXERCÍCIO 10 - LISTA 1")
    print("="*70)
    print("Calculadora Aritmética usando Pilhas")
    print("="*70)
    
    # Casos de teste com expressões pós-fixas
    expressoes_teste = [
        "3 4 +",           # 3 + 4 = 7
        "5 2 -",           # 5 - 2 = 3
        "6 3 *",           # 6 * 3 = 18
        "8 4 /",           # 8 / 4 = 2
        "10 3 %",          # 10 % 3 = 1
        "2 3 **",          # 2^3 = 8
        "15 7 + 1 1 + / 3 * 2 1 1 + + -",  # ((15+7)/(1+1))*3-(2+1+1) = 11*3-4 = 29
        "5 1 2 + 4 * + 3 -",              # 5+((1+2)*4)-3 = 5+12-3 = 14
    ]
    
    print("Avaliação de expressões pós-fixas:\n")
    
    for i, expressao in enumerate(expressoes_teste, 1):
        try:
            print(f"Teste {i}: {expressao}")
            
            # Mostrar processo detalhado para os primeiros exemplos
            if i <= 3:
                print(f"  Processo:")
                pilha_demo = ArrayStack()
                tokens = expressao.split()
                
                for token in tokens:
                    if eh_numero(token):
                        pilha_demo.push(int(token))
                        print(f"    '{token}' -> empilha, pilha: {pilha_demo._data}")
                    elif eh_operador(token):
                        op2 = pilha_demo.pop()
                        op1 = pilha_demo.pop()
                        resultado = calcular(op1, token, op2)
                        pilha_demo.push(resultado)
                        print(f"    '{token}' -> calcula {op1} {token} {op2} = {resultado}, pilha: {pilha_demo._data}")
            
            resultado = avaliar_posfixa(expressao)
            print(f"  Resultado: {resultado}")
            print()
            
        except Exception as e:
            print(f"  Erro: {e}")
            print()
    
    print("--- Algoritmo da Calculadora ---")
    print("1. Para cada token na expressão pós-fixa:")
    print("   - Se for número: empilha na pilha")
    print("   - Se for operador: desempilha 2 operandos, calcula e empilha resultado")
    print("2. Ao final, a pilha deve ter apenas 1 elemento (resultado)")
    print()
    print("Nota: Para usar interativamente, execute: python -m questions.question_10")

def calculadora_interativa():
    """Versão interativa da calculadora"""
    print("=== Calculadora Interativa ===")
    print("Digite expressões pós-fixas (ou 'sair' para terminar):")
    print("Exemplos: '3 4 +', '10 5 2 * -', '2 3 ** 1 +'")
    print()
    
    while True:
        try:
            entrada = input(">>> ").strip()
            
            if entrada.lower() in ['sair', 'exit', 'quit', '']:
                print("Calculadora encerrada!")
                break
                
            resultado = avaliar_posfixa(entrada)
            print(f"Resultado: {resultado}")
            
        except KeyboardInterrupt:
            print("\nCalculadora encerrada!")
            break
        except Exception as e:
            print(f"Erro: {e}")

if __name__ == "__main__":
    exercicio_10()
    print("\n" + "="*50 + "\n")
    calculadora_interativa()