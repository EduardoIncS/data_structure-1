"""
Exercício 7 - Lista 3
Considere a sequência de chaves (5,16,22,45,2,10,18,30,50,12,1). 
Desenhe o resultado da inserção de entradas com essas chaves 
(na ordem dada) em uma árvore rubro-negra inicialmente vazia.
"""

from redBlackTreeMap import RedBlackTreeMap


def print_tree_structure(tree):
    """
    Imprime a estrutura da árvore rubro-negra com as cores
    """
    if len(tree) == 0:
        print("Árvore vazia")
        return
    
    def get_color(p):
        """Retorna a cor do nó"""
        if p._node._red:
            return "R"  # Red (Vermelho)
        return "B"  # Black (Preto)
    
    def print_tree_recursive(p, prefix="", is_left=None):
        """Imprime a árvore de forma hierárquica com cores"""
        if p is None:
            return
        
        # Imprime o nó direito primeiro (para aparecer em cima visualmente)
        if tree.right(p) is not None:
            print_tree_recursive(
                tree.right(p), 
                prefix + ("│   " if is_left else "    "), 
                False
            )
        
        # Imprime o nó atual com sua cor
        color = get_color(p)
        if is_left is None:
            print(f"{prefix}[{p.key()}:{color}]")
        elif is_left:
            print(f"{prefix}└── [{p.key()}:{color}]")
        else:
            print(f"{prefix}┌── [{p.key()}:{color}]")
        
        # Imprime o nó esquerdo
        if tree.left(p) is not None:
            print_tree_recursive(
                tree.left(p), 
                prefix + ("    " if is_left == False else "│   "), 
                True
            )
    
    print("\nEstrutura da árvore (R=Rubro/Vermelho, B=Negro/Preto):")
    print_tree_recursive(tree.root())
    
    print("\nTraversão inorder com cores:")
    nodes_info = []
    for p in tree.inorder():
        color = get_color(p)
        nodes_info.append(f"{p.key()}:{color}")
    print(f"  {', '.join(nodes_info)}")


def exercicio_7():
    """
    Exercício 7: Insere a sequência de chaves em uma árvore rubro-negra
    """
    print("\n" + "="*70)
    print("EXERCÍCIO 7 - LISTA 3")
    print("="*70)
    print("Inserção das chaves (5,16,22,45,2,10,18,30,50,12,1)")
    print("em uma árvore rubro-negra inicialmente vazia")
    print("="*70)
    
    # Cria uma árvore rubro-negra vazia
    tree = RedBlackTreeMap()
    
    # Sequência de chaves a serem inseridas
    keys = [5, 16, 22, 45, 2, 10, 18, 30, 50, 12, 1]
    
    print("\n--- Inserindo chaves sequencialmente ---\n")
    
    for key in keys:
        tree[key] = key  # Usando a chave como valor
        print(f"Inseriu chave: {key}")
        print_tree_structure(tree)
        print("-" * 70)
    
    print("\n" + "="*70)
    print("RESULTADO FINAL DA ÁRVORE RUBRO-NEGRA")
    print("="*70)
    print_tree_structure(tree)
    
    print("\n" + "="*70)
    print("Propriedades da árvore rubro-negra mantidas:")
    print("1. Raiz é preta")
    print("2. Todas as folhas (NIL) são pretas")
    print("3. Filhos de nós vermelhos são pretos")
    print("4. Todos os caminhos da raiz às folhas têm o mesmo número de nós pretos")
    print("="*70)


if __name__ == "__main__":
    exercicio_7()
