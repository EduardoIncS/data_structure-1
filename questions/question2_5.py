from linkedBinaryTree import LinkedBinaryTree


def is_sum_tree(tree):
    """
    Verifica se uma árvore binária é uma árvore soma.
    Em uma árvore soma, o valor de cada nó não folha é igual à soma de todos
    os elementos presentes em suas subárvores esquerda e direita.
    O valor de um nó filho vazio é considerado 0.
    """
    if len(tree) == 0:
        return True
    
    result, _ = _is_sum_tree_recursive(tree.root(), tree)
    return result


def _is_sum_tree_recursive(p, tree):
    """
    Função auxiliar recursiva que verifica se a subárvore é uma árvore soma.
    Retorna (is_sum, sum_subtree) onde:
    - is_sum: True se é uma árvore soma, False caso contrário
    - sum_subtree: soma de todos os elementos da subárvore
    """
    # Caso base: posição None
    if p is None:
        return (True, 0)
    
    # Caso folha: sempre válido, soma é o próprio valor
    # Verifica se é folha checando se não tem filhos
    if tree.num_children(p) == 0:
        return (True, p.element())
    
    # Verifica recursivamente as subárvores
    left_is_sum, left_sum = _is_sum_tree_recursive(tree.left(p), tree)
    right_is_sum, right_sum = _is_sum_tree_recursive(tree.right(p), tree)
    
    # Se alguma subárvore não é soma, retorna False
    if not left_is_sum or not right_is_sum:
        return (False, 0)
    
    # Verifica se o valor do nó atual é igual à soma das subárvores
    current_value = p.element()
    expected_sum = left_sum + right_sum
    
    if current_value == expected_sum:
        # É uma árvore soma, retorna a soma total incluindo o nó atual
        total_sum = current_value + left_sum + right_sum
        return (True, total_sum)
    else:
        return (False, 0)


def exercicio_5():
    """Exercício 5: Verificar se uma árvore binária é uma árvore soma."""
    
    print("\n" + "="*70)
    print("EXERCÍCIO 5 - LISTA 2")
    print("="*70)
    print("Verificação de Árvore Soma")
    print("="*70)
    print()
    
    # Criar árvore soma do exemplo
    #        44
    #       /  \
    #      9    13
    #     / \   / \
    #    4   5 6   7
    tree1 = LinkedBinaryTree()
    root1 = tree1._add_root(44)
    left1 = tree1._add_left(root1, 9)
    right1 = tree1._add_right(root1, 13)
    tree1._add_left(left1, 4)
    tree1._add_right(left1, 5)
    tree1._add_left(right1, 6)
    tree1._add_right(right1, 7)
    
    # Criar árvore que NÃO é soma
    #        10
    #       /  \
    #      3    5
    #     / \
    #    1   2
    tree2 = LinkedBinaryTree()
    root2 = tree2._add_root(10)
    left2 = tree2._add_left(root2, 3)
    tree2._add_right(root2, 5)
    tree2._add_left(left2, 1)
    tree2._add_right(left2, 2)
    
    # Criar árvore soma simples
    #       10
    #      /  \
    #     4    6
    tree3 = LinkedBinaryTree()
    root3 = tree3._add_root(10)
    tree3._add_left(root3, 4)
    tree3._add_right(root3, 6)
    
    # Criar árvore com um nó apenas
    tree4 = LinkedBinaryTree()
    tree4._add_root(5)
    
    # Criar árvore vazia
    tree5 = LinkedBinaryTree()
    
    # Testes
    print("Árvore 1: 44(4+5+9)+(6+7+13) = 44")
    print("         44")
    print("        /  \\")
    print("       9    13")
    print("      / \\   / \\")
    print("     4   5 6   7")
    print(f"É árvore soma? {is_sum_tree(tree1)}\n")
    
    print("Árvore 2: 10 ≠ (1+2+3)+5 = 11")
    print("         10")
    print("        /  \\")
    print("       3    5")
    print("      / \\")
    print("     1   2")
    print(f"É árvore soma? {is_sum_tree(tree2)}\n")
    
    print("Árvore 3: 10 = 4+6")
    print("         10")
    print("        /  \\")
    print("       4    6")
    print(f"É árvore soma? {is_sum_tree(tree3)}\n")
    
    print("Árvore 4: Apenas raiz (5)")
    print(f"É árvore soma? {is_sum_tree(tree4)}\n")
    
    print("Árvore 5: Vazia")
    print(f"É árvore soma? {is_sum_tree(tree5)}")


if __name__ == "__main__":
    exercicio_5()
