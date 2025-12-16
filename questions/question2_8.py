from linkedBinaryTree import LinkedBinaryTree

def convert_to_sum_tree(tree):
    """
    Substitui o valor de cada nó pela soma de todos os elementos
    presentes em suas subárvores esquerda e direita.
    O valor de um nó filho vazio é considerado 0.
    """
    
    if len(tree) == 0:
        return
    
    _convert_to_sum_tree_recursive(tree.root(), tree)


def _convert_to_sum_tree_recursive(p, tree):
    """
    Função auxiliar recursiva que converte a árvore em árvore soma.
    Retorna a soma de todos os elementos da subárvore (incluindo o nó atual antes da conversão).
    """
    if p is None:
        return 0
    
    # Se é folha, retorna o valor atual (será substituído por 0)
    if tree.num_children(p) == 0:
        old_value = p.element()
        tree.replace(p, 0)
        return old_value
    
    # Processa recursivamente as subárvores
    left_sum = _convert_to_sum_tree_recursive(tree.left(p), tree)
    right_sum = _convert_to_sum_tree_recursive(tree.right(p), tree)
    
    # Guarda o valor antigo do nó
    old_value = p.element()
    
    # Substitui o valor do nó pela soma das subárvores
    new_value = left_sum + right_sum
    tree.replace(p, new_value)
    
    # Retorna a soma total incluindo o valor antigo do nó
    return old_value + left_sum + right_sum


def print_tree_inorder(tree):
    """Imprime a árvore em ordem (inorder traversal)."""
    if len(tree) == 0:
        print("Árvore vazia")
        return
    
    elements = []
    _collect_inorder(tree.root(), tree, elements)
    print(" ".join(map(str, elements)))


def _collect_inorder(p, tree, elements):
    """Coleta elementos em ordem."""
    if p is None:
        return
    
    _collect_inorder(tree.left(p), tree, elements)
    elements.append(p.element())
    _collect_inorder(tree.right(p), tree, elements)


def exercicio_8():
    """Exercício 8: Converter árvore para árvore soma."""
    
    print("\n" + "="*70)
    print("EXERCÍCIO 8 - LISTA 2")
    print("="*70)
    print("Conversão para Árvore Soma")
    print("="*70)
    print()
    
    # Criar árvore do exemplo
    #         1
    #        / \
    #       2   3
    #        \  / \
    #        4 5   6
    #         / \
    #        7   8
    tree1 = LinkedBinaryTree()
    root = tree1._add_root(1)
    node2 = tree1._add_left(root, 2)
    node3 = tree1._add_right(root, 3)
    tree1._add_right(node2, 4)
    node5 = tree1._add_left(node3, 5)
    tree1._add_right(node3, 6)
    tree1._add_left(node5, 7)
    tree1._add_right(node5, 8)
    
    print("Árvore Original:")
    print("         1")
    print("        / \\")
    print("       2   3")
    print("        \\  / \\")
    print("        4 5   6")
    print("         / \\")
    print("        7   8")
    print("\nInorder (antes):", end=" ")
    print_tree_inorder(tree1)
    
    # Converter para árvore soma
    convert_to_sum_tree(tree1)
    
    print("\nÁrvore Soma:")
    print("         35")
    print("        /  \\")
    print("       4    26")
    print("        \\   /  \\")
    print("        0 15   0")
    print("         /  \\")
    print("        0    0")
    print("\nInorder (depois):", end=" ")
    print_tree_inorder(tree1)
    
    # Criar árvore simples
    print("\n" + "="*50)
    print("\nÁrvore 2 Original:")
    print("       10")
    print("      /  \\")
    print("     5    15")
    
    tree2 = LinkedBinaryTree()
    root2 = tree2._add_root(10)
    tree2._add_left(root2, 5)
    tree2._add_right(root2, 15)
    
    print("Inorder (antes):", end=" ")
    print_tree_inorder(tree2)
    
    convert_to_sum_tree(tree2)
    
    print("\nÁrvore 2 Soma:")
    print("       20")
    print("      /  \\")
    print("     0    0")
    print("Inorder (depois):", end=" ")
    print_tree_inorder(tree2)
    
    # Criar árvore com único nó
    print("\n" + "="*50)
    print("\nÁrvore 3: Apenas raiz (42)")
    
    tree3 = LinkedBinaryTree()
    tree3._add_root(42)
    
    print("Inorder (antes):", end=" ")
    print_tree_inorder(tree3)
    
    convert_to_sum_tree(tree3)
    
    print("Árvore 3 após conversão: 0 (folha)")
    print("Inorder (depois):", end=" ")
    print_tree_inorder(tree3)


if __name__ == "__main__":
    exercicio_8()
