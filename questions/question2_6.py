from linkedBinaryTree import LinkedBinaryTree


def print_paths(tree):
    """
    Imprime todos os caminhos da raiz até cada folha da árvore binária.
    """
    
    if len(tree) == 0:
        print("Árvore vazia - nenhum caminho")
        return
    
    path = []
    _print_paths_recursive(tree.root(), tree, path)


def _print_paths_recursive(p, tree, path):
    """
    Função auxiliar recursiva que percorre a árvore e imprime os caminhos.
    """
    if p is None:
        return
    
    # Adiciona o elemento atual ao caminho
    path.append(p.element())
    
    # Se é uma folha, imprime o caminho
    if tree.num_children(p) == 0:
        print(" -> ".join(map(str, path)))
    else:
        # Continua a busca recursivamente
        _print_paths_recursive(tree.left(p), tree, path)
        _print_paths_recursive(tree.right(p), tree, path)
    
    # Remove o elemento atual do caminho (backtracking)
    path.pop()


def exercicio_6():
    """Exercício 6: Imprimir todos os caminhos da raiz até as folhas."""
    
    print("Exercício 6: Caminhos da Raiz até as Folhas\n")
    
    # Criar árvore do exemplo
    #         1
    #        / \
    #       2   3
    #      / \  / \
    #     4  5 6   7
    #          /     \
    #         8       9
    tree1 = LinkedBinaryTree()
    root = tree1._add_root(1)
    node2 = tree1._add_left(root, 2)
    node3 = tree1._add_right(root, 3)
    tree1._add_left(node2, 4)
    tree1._add_right(node2, 5)
    node6 = tree1._add_left(node3, 6)
    node7 = tree1._add_right(node3, 7)
    tree1._add_left(node6, 8)
    tree1._add_right(node7, 9)
    
    print("Árvore 1:")
    print("         1")
    print("        / \\")
    print("       2   3")
    print("      / \\  / \\")
    print("     4  5 6   7")
    print("          /     \\")
    print("         8       9")
    print("\nCaminhos da raiz até as folhas:")
    print_paths(tree1)
    
    # Criar árvore simples
    #       10
    #      /  \
    #     5    15
    tree2 = LinkedBinaryTree()
    root2 = tree2._add_root(10)
    tree2._add_left(root2, 5)
    tree2._add_right(root2, 15)
    
    print("\n" + "="*50)
    print("\nÁrvore 2:")
    print("       10")
    print("      /  \\")
    print("     5    15")
    print("\nCaminhos da raiz até as folhas:")
    print_paths(tree2)
    
    # Criar árvore com um único nó
    tree3 = LinkedBinaryTree()
    tree3._add_root(42)
    
    print("\n" + "="*50)
    print("\nÁrvore 3: Apenas raiz (42)")
    print("\nCaminhos da raiz até as folhas:")
    print_paths(tree3)
    
    # Criar árvore vazia
    tree4 = LinkedBinaryTree()
    
    print("\n" + "="*50)
    print("\nÁrvore 4: Vazia")
    print("\nCaminhos da raiz até as folhas:")
    print_paths(tree4)


if __name__ == "__main__":
    exercicio_6()
