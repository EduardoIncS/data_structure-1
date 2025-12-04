from linkedBinaryTree import LinkedBinaryTree

def are_identical(tree1, tree2):
    """
    Verifica se duas árvores binárias são idênticas.
    Duas árvores são idênticas se tiverem a mesma estrutura e o mesmo conteúdo.
    """
    return _are_identical_recursive(tree1.root(), tree2.root(), tree1, tree2)


def _are_identical_recursive(p1, p2, tree1, tree2):
    """
    Função auxiliar recursiva para verificar se duas subárvores são idênticas.
    """
    # Se ambas as posições são None, as subárvores são idênticas
    if p1 is None and p2 is None:
        return True
    
    # Se apenas uma das posições é None, as árvores são diferentes
    if p1 is None or p2 is None:
        return False
    
    # Verifica se os elementos são iguais
    if p1.element() != p2.element():
        return False
    
    # Verifica recursivamente os filhos esquerdo e direito
    left_identical = _are_identical_recursive(tree1.left(p1), tree2.left(p2), tree1, tree2)
    right_identical = _are_identical_recursive(tree1.right(p1), tree2.right(p2), tree1, tree2)
    
    return left_identical and right_identical


def exercicio_4():
    """Exercício 4: Verificar se duas árvores binárias são idênticas."""
    print("Exercício 4: Verificação de Árvores Binárias Idênticas\n")
    
    # Criar primeira árvore
    #       1
    #      / \
    #     2   3
    #    /
    #   4
    tree1 = LinkedBinaryTree()
    root1 = tree1._add_root(1)
    left1 = tree1._add_left(root1, 2)
    tree1._add_right(root1, 3)
    tree1._add_left(left1, 4)
    
    # Criar segunda árvore (idêntica à primeira)
    #       1
    #      / \
    #     2   3
    #    /
    #   4
    tree2 = LinkedBinaryTree()
    root2 = tree2._add_root(1)
    left2 = tree2._add_left(root2, 2)
    tree2._add_right(root2, 3)
    tree2._add_left(left2, 4)
    
    # Criar terceira árvore (diferente)
    #       1
    #      / \
    #     2   3
    #      \
    #       5
    tree3 = LinkedBinaryTree()
    root3 = tree3._add_root(1)
    left3 = tree3._add_left(root3, 2)
    tree3._add_right(root3, 3)
    tree3._add_right(left3, 5)
    
    # Criar quarta árvore (mesma estrutura, valores diferentes)
    #       1
    #      / \
    #     2   4
    #    /
    #   4
    tree4 = LinkedBinaryTree()
    root4 = tree4._add_root(1)
    left4 = tree4._add_left(root4, 2)
    tree4._add_right(root4, 4)
    tree4._add_left(left4, 4)
    
    # Testes
    print("Árvore 1: [1, 2, 3, 4] (estrutura: 1 como raiz, 2 à esquerda com filho 4, 3 à direita)")
    print("Árvore 2: [1, 2, 3, 4] (mesma estrutura e valores)")
    print("Árvore 3: [1, 2, 3, 5] (estrutura diferente: 2 tem filho direito 5)")
    print("Árvore 4: [1, 2, 4, 4] (mesma estrutura, valores diferentes)\n")
    
    print(f"Árvore 1 e Árvore 2 são idênticas? {are_identical(tree1, tree2)}")
    print(f"Árvore 1 e Árvore 3 são idênticas? {are_identical(tree1, tree3)}")
    print(f"Árvore 1 e Árvore 4 são idênticas? {are_identical(tree1, tree4)}")
    print(f"Árvore 2 e Árvore 3 são idênticas? {are_identical(tree2, tree3)}")
    
    # Testar com árvore vazia
    tree_empty1 = LinkedBinaryTree()
    tree_empty2 = LinkedBinaryTree()
    print(f"\nDuas árvores vazias são idênticas? {are_identical(tree_empty1, tree_empty2)}")
    print(f"Árvore 1 e árvore vazia são idênticas? {are_identical(tree1, tree_empty1)}")


if __name__ == "__main__":
    exercicio_4()
