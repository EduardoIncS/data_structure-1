from linkedBinaryTree import LinkedBinaryTree


def find_ancestors(tree, target):
    """
    Encontra todos os ancestrais de um nó específico na árvore binária.
    Retorna uma lista com os valores dos ancestrais do nó mais próximo ao mais distante.
    """
    
    if len(tree) == 0:
        return []
    
    ancestors = []
    found = _find_ancestors_recursive(tree.root(), tree, target, ancestors)
    
    if not found:
        return []
    
    return ancestors


def _find_ancestors_recursive(p, tree, target, ancestors):
    """
    Função auxiliar recursiva que busca o nó alvo e constrói a lista de ancestrais.
    Retorna True se o nó alvo foi encontrado na subárvore, False caso contrário.
    """
    if p is None:
        return False
    
    # Se encontrou o nó alvo
    if p.element() == target:
        return True
    
    # Busca recursivamente nas subárvores
    found_left = _find_ancestors_recursive(tree.left(p), tree, target, ancestors)
    found_right = _find_ancestors_recursive(tree.right(p), tree, target, ancestors)
    
    # Se o alvo foi encontrado em alguma subárvore, adiciona o nó atual aos ancestrais
    if found_left or found_right:
        ancestors.append(p.element())
        return True
    
    return False


def exercicio_7():
    """Exercício 7: Encontrar todos os ancestrais de um nó específico."""
    
    print("Exercício 7: Encontrar Ancestrais de um Nó\n")
    
    # Criar árvore do exemplo
    #         1
    #        / \
    #       2   3
    #      / \  / \
    #     4  5 6   7
    #        /     \
    #       8       9
    tree1 = LinkedBinaryTree()
    root = tree1._add_root(1)
    node2 = tree1._add_left(root, 2)
    node3 = tree1._add_right(root, 3)
    tree1._add_left(node2, 4)
    node5 = tree1._add_right(node2, 5)
    node6 = tree1._add_left(node3, 6)
    node7 = tree1._add_right(node3, 7)
    tree1._add_left(node5, 8)
    tree1._add_right(node7, 9)
    
    print("Árvore:")
    print("         1")
    print("        / \\")
    print("       2   3")
    print("      / \\  / \\")
    print("     4  5 6   7")
    print("        /     \\")
    print("       8       9")
    print()
    
    # Testes conforme o exemplo
    test_nodes = [9, 6, 5]
    
    for node_value in test_nodes:
        ancestors = find_ancestors(tree1, node_value)
        if ancestors:
            print(f"Os ancestrais do nó {node_value} são {', '.join(map(str, ancestors))}.")
        else:
            print(f"O nó {node_value} não foi encontrado ou não possui ancestrais.")
    
    # Teste adicional: nó raiz (não tem ancestrais)
    print(f"\nOs ancestrais do nó 1 (raiz) são {find_ancestors(tree1, 1)}.")
    
    # Teste adicional: nó que não existe
    print(f"Os ancestrais do nó 100 (não existe) são {find_ancestors(tree1, 100)}.")
    
    # Criar árvore simples para mais testes
    print("\n" + "="*50)
    print("\nÁrvore 2:")
    print("       10")
    print("      /  \\")
    print("     5    15")
    print("    /")
    print("   3")
    
    tree2 = LinkedBinaryTree()
    root2 = tree2._add_root(10)
    node5_2 = tree2._add_left(root2, 5)
    tree2._add_right(root2, 15)
    tree2._add_left(node5_2, 3)
    
    print(f"\nOs ancestrais do nó 3 são {', '.join(map(str, find_ancestors(tree2, 3)))}.")
    print(f"Os ancestrais do nó 15 são {', '.join(map(str, find_ancestors(tree2, 15)))}.")


if __name__ == "__main__":
    exercicio_7()
