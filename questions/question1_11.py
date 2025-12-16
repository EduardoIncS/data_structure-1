from stack import ArrayStack
from queue import ArrayQueue

def eh_palindromo_pilha_fila(string):
    """
    Crie um sistema usando uma pilha e uma fila para testar se uma determinada string é um
    palíndromo (ou seja, se os caracteres são lidos da mesma forma, tanto para a frente quanto
    para trás).
    """
    # Remove espaços e converte para minúsculas para comparação
    string_limpa = string.replace(" ", "").lower()
    
    pilha = ArrayStack()
    fila = ArrayQueue()
    
    # Adiciona cada caractere tanto na pilha quanto na fila
    for char in string_limpa:
        pilha.push(char)
        fila.enqueue(char)
    
    # Compara caracteres: pilha (reverso) vs fila (ordem normal)
    while not pilha.is_empty() and not fila.is_empty():
        char_pilha = pilha.pop()      # Último inserido (do final para início)
        char_fila = fila.dequeue()    # Primeiro inserido (do início para final)
        
        if char_pilha != char_fila:
            return False
    
    return True

def exercicio_11():
    """
    Crie um sistema usando uma pilha e uma fila para testar se uma determinada string é um
    palíndromo (ou seja, se os caracteres são lidos da mesma forma, tanto para a frente quanto
    para trás).
    """
    print("\n" + "="*70)
    print("EXERCÍCIO 11 - LISTA 1")
    print("="*70)
    print("Teste de Palíndromo com Pilha e Fila")
    print("="*70)
    
    # Casos de teste
    strings_teste = [
        "arara",
        "ovo",
        "casa",
        "socos",
        "A base do teto desaba",
        "hello",
        "racecar",
        "python",
    ]
    
    for i, string in enumerate(strings_teste, 1):
        resultado = eh_palindromo_pilha_fila(string)
        status = "✓ É PALÍNDROMO" if resultado else "✗ NÃO É PALÍNDROMO"
        
        print(f"{i:2d}. '{string}' -> {status}")
        
        # Mostrar processo detalhado para os primeiros exemplos
        if i <= 3:
            string_limpa = string.replace(" ", "").lower()
            print(f"     String limpa: '{string_limpa}'")
            
            pilha_demo = ArrayStack()
            fila_demo = ArrayQueue()
            
            print(f"     Preenchendo estruturas:")
            for char in string_limpa:
                pilha_demo.push(char)
                fila_demo.enqueue(char)
                print(f"       '{char}' -> Pilha: {pilha_demo._data}, Fila: [elementos internos]")
            
            print(f"     Comparação:")
            chars_pilha = []
            chars_fila = []
            
            while not pilha_demo.is_empty():
                chars_pilha.append(pilha_demo.pop())
            
            # Reconstruir fila para demonstração
            fila_demo = ArrayQueue()
            for char in string_limpa:
                fila_demo.enqueue(char)
            
            while not fila_demo.is_empty():
                chars_fila.append(fila_demo.dequeue())
            
            print(f"       Pilha (reverso): {chars_pilha}")
            print(f"       Fila (normal):   {chars_fila}")
            print(f"       São iguais? {chars_pilha == chars_fila}")
            print()
    
    print("--- Como funciona o algoritmo ---")
    print("1. PILHA: armazena caracteres em ordem LIFO (Last In, First Out)")
    print("   - Ao desempilhar: obtém caracteres do FINAL para o INÍCIO")
    print("2. FILA: armazena caracteres em ordem FIFO (First In, First Out)")  
    print("   - Ao desenfileirar: obtém caracteres do INÍCIO para o FINAL")
    print("3. COMPARAÇÃO: se pilha e fila produzem a mesma sequência,")
    print("   significa que a string é igual lida de frente e de trás")
    print("4. PALÍNDROMO: string que lida normalmente = string lida ao contrário")

if __name__ == "__main__":
    exercicio_11()