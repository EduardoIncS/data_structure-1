from treeMap import TreeMap


def insert_and_print(tree, keys):
    """
    Insere chaves em uma árvore de busca binária vazia e imprime após cada inserção.
    """
    print("Inserindo chaves em uma árvore de busca binária:\n")
    
    for i, key in enumerate(keys, 1):
        # Inserir a chave (usando None como valor, pois só importa a estrutura)
        tree[key] = None
        
        print(f"Inserção {i}: chave {key}")
        print(f"Árvore em ordem (inorder): {get_inorder(tree)}")
        print(f"Altura da árvore: {get_height(tree)}")
        print("-" * 50)


def get_inorder(tree):
    """Retorna lista com as chaves em ordem (inorder traversal)."""
    if len(tree) == 0:
        return []
    
    result = []
    _inorder_helper(tree.root(), tree, result)
    return result


def _inorder_helper(p, tree, result):
    """Helper recursivo para percorrer a árvore em ordem."""
    if p is None:
        return
    
    _inorder_helper(tree.left(p), tree, result)
    result.append(p.key())
    _inorder_helper(tree.right(p), tree, result)


def get_height(tree):
    """Retorna a altura da árvore."""
    if len(tree) == 0:
        return -1
    return _height_helper(tree.root(), tree)


def _height_helper(p, tree):
    """Helper recursivo para calcular altura."""
    if p is None:
        return -1
    
    left_height = _height_helper(tree.left(p), tree)
    right_height = _height_helper(tree.right(p), tree)
    
    return 1 + max(left_height, right_height)


def exercicio_4():
    """Exercício 4: Inserir chaves em árvore de busca binária e imprimir após cada inserção."""
    print("\n" + "="*70)
    print("EXERCÍCIO 4 - LISTA 3")
    print("="*70)
    print("Inserção em Árvore de Busca Binária")
    print("="*70)
    
    # Chaves do exercício
    keys = [30, 40, 24, 58, 48, 26, 11, 13]
    
    # Criar árvore vazia
    tree = TreeMap()
    
    print(f"\nChaves a serem inseridas (nesta ordem): {keys}\n")
    print("="*50)
    
    # Inserir e imprimir
    insert_and_print(tree, keys)
    
    # Estado final
    print("\n" + "="*50)
    print("ESTADO FINAL DA ÁRVORE")
    print("="*50)
    print(f"Número de nós: {len(tree)}")
    print(f"Altura: {get_height(tree)}")
    print(f"Travessia em ordem: {get_inorder(tree)}")
    
    # Verificar se está ordenada (propriedade BST)
    inorder_list = get_inorder(tree)
    is_sorted = all(inorder_list[i] <= inorder_list[i+1] for i in range(len(inorder_list)-1))
    print(f"Propriedade BST mantida (ordem crescente): {is_sorted}")


if __name__ == "__main__":
    exercicio_4()
