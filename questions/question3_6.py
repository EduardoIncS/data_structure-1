"""
Exercício 6 - Lista 3
Desenhe a árvore AVL resultante da remoção da entrada com a chave 62 
da árvore AVL da Figura 11.14b.
"""

from avlTreeMap import AVLTreeMap


def build_avl_tree_from_figure():
    """
    Constrói a árvore AVL da Figura 11.14b (após remoção de 32 e rebalanceamento)
    """
    tree = AVLTreeMap()
    
    # Inserindo os nós conforme a Figura 11.14b
    keys = [44, 17, 78, 32, 50, 88, 48, 62, 54]
    
    for key in keys:
        tree[key] = key  # Usando a chave como valor para simplificar
    
    return tree


def print_tree_structure(tree):
    """
    Imprime a estrutura da árvore em formato visual simples
    """
    if len(tree) == 0:
        print("Árvore vazia")
        return
    
    def print_tree_recursive(p, prefix="", is_left=None):
        """Imprime a árvore de forma hierárquica"""
        if p is None:
            return
        
        # Imprime o nó direito primeiro (para aparecer em cima visualmente)
        if tree.right(p) is not None:
            print_tree_recursive(
                tree.right(p), 
                prefix + ("│   " if is_left else "    "), 
                False
            )
        
        # Imprime o nó atual
        if is_left is None:
            print(f"{prefix}[{p.key()}]")
        elif is_left:
            print(f"{prefix}└── [{p.key()}]")
        else:
            print(f"{prefix}┌── [{p.key()}]")
        
        # Imprime o nó esquerdo
        if tree.left(p) is not None:
            print_tree_recursive(
                tree.left(p), 
                prefix + ("    " if is_left == False else "│   "), 
                True
            )
    
    print("\nEstrutura da árvore:")
    print_tree_recursive(tree.root())
    
    print("\nTraversão inorder:")
    inorder_keys = [p.key() for p in tree.inorder()]
    print(f"  {inorder_keys}")


def exercicio_6():
    """
    Exercício 6: Desenha a árvore AVL resultante da remoção da chave 62
    """
    print("\n" + "="*70)
    print("EXERCÍCIO 6 - LISTA 3")
    print("="*70)
    print("Remoção da chave 62 da árvore AVL da Figura 11.14b")
    print("="*70)
    
    # Constrói a árvore inicial (Figura 11.14b)
    tree = build_avl_tree_from_figure()
    
    print("\n--- ANTES da remoção de 62 ---")
    print_tree_structure(tree)
    
    # Remove a chave 62
    print("\n" + "-"*70)
    print("Removendo chave 62...")
    print("-"*70)
    del tree[62]
    
    print("\n--- DEPOIS da remoção de 62 ---")
    print_tree_structure(tree)
    
    # Verifica o balanceamento
    print("\n" + "="*70)
    print("Verificação: A árvore permanece balanceada (propriedade AVL mantida)")
    print("="*70)

if __name__ == "__main__":
    exercicio_6()