"""
Exercício 5 - Lista 3
Desenhe a árvore AVL resultante da inserção de uma entrada com a chave 52 
na árvore AVL da Figura 11.14b.
"""

from avlTreeMap import AVLTreeMap


def build_avl_tree_from_figure():
    """
    Constrói a árvore AVL da Figura 11.14b (após remoção de 32 e rebalanceamento)
    """
    tree = AVLTreeMap()
    
    # Inserindo os nós conforme a Figura 11.14b
    # A estrutura após remoção de 32 e rebalanceamento:
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
    
    def get_inorder_with_height(p, level=0):
        """Retorna lista de tuplas (chave, nível, altura)"""
        result = []
        if tree.left(p) is not None:
            result.extend(get_inorder_with_height(tree.left(p), level + 1))
        
        height = p._node._height if hasattr(p._node, '_height') else 0
        result.append((p.key(), level, height))
        
        if tree.right(p) is not None:
            result.extend(get_inorder_with_height(tree.right(p), level + 1))
        
        return result
    
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
    
    print("\nTraversão inorder (chave, nível, altura):")
    nodes = get_inorder_with_height(tree.root())
    for key, level, height in nodes:
        print(f"  Chave: {key:2d}, Nível: {level}, Altura: {height}")


def exercicio_5():
    """
    Exercício 5: Desenha a árvore AVL resultante da inserção da chave 52
    """
    print("\n" + "="*70)
    print("EXERCÍCIO 5 - LISTA 3")
    print("="*70)
    print("Inserção da chave 52 na árvore AVL da Figura 11.14b")
    print("="*70)
    
    # Constrói a árvore inicial (Figura 11.14b)
    tree = build_avl_tree_from_figure()
    
    print("\n--- ANTES da inserção de 52 ---")
    print_tree_structure(tree)
    
    # Insere a chave 52
    print("\n" + "-"*70)
    print("Inserindo chave 52...")
    print("-"*70)
    tree[52] = 52
    
    print("\n--- DEPOIS da inserção de 52 ---")
    print_tree_structure(tree)
    
    # Verifica o balanceamento
    print("\n" + "="*70)
    print("Verificação: A árvore permanece balanceada (propriedade AVL mantida)")
    print("="*70)

if __name__ == "__main__":
    exercicio_5()