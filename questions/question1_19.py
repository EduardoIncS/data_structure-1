from doublyLinkedBase import _DoublyLinkedBase

class ListaDuplamenteEncadeada(_DoublyLinkedBase):
    """Lista duplamente encadeada simples para demonstração."""
    
    def add_first(self, element):
        """Adiciona elemento no início da lista."""
        self._insert_between(element, self._header, self._header._next)
    
    def add_last(self, element):
        """Adiciona elemento no final da lista."""
        self._insert_between(element, self._trailer._prev, self._trailer)
    
    def delete_first(self):
        """Remove e retorna o primeiro elemento."""
        if self.is_empty():
            raise Exception("Lista vazia")
        return self._delete_node(self._header._next)
    
    def delete_last(self):
        """Remove e retorna o último elemento."""
        if self.is_empty():
            raise Exception("Lista vazia")
        return self._delete_node(self._trailer._prev)

def excluir_duplicados(lista):
    """
    Escreve um programa para excluir elementos duplicados em uma lista duplamente encadeada.
    
    Args:
        lista: Instância de ListaDuplamenteEncadeada
    
    Returns:
        Lista sem elementos duplicados (modifica a lista original)
    """
    if lista.is_empty():
        return lista
    
    # Usa um conjunto para rastrear elementos já vistos
    elementos_vistos = set()
    
    # Percorre a lista usando os nós internos
    current = lista._header._next  # Primeiro nó real (pula o header)
    
    while current != lista._trailer:  # Enquanto não chegar ao trailer
        elemento = current._element
        next_node = current._next  # Salva referência antes de possível remoção
        
        if elemento in elementos_vistos:
            # Elemento duplicado - remove da lista
            lista._delete_node(current)
        else:
            # Primeiro encontro - adiciona ao conjunto
            elementos_vistos.add(elemento)
        
        current = next_node
    
    return lista

def criar_lista_dupla(elementos):
    """Função auxiliar para criar uma lista duplamente encadeada."""
    lista = ListaDuplamenteEncadeada()
    for elemento in elementos:
        lista.add_last(elemento)
    return lista

def imprimir_lista_dupla(lista):
    """Função auxiliar para imprimir a lista duplamente encadeada."""
    if lista.is_empty():
        return "Lista vazia"
    
    elementos = []
    current = lista._header._next
    while current != lista._trailer:
        elementos.append(str(current._element))
        current = current._next
    return " <-> ".join(elementos)

def lista_dupla_para_array(lista):
    """Converte lista duplamente encadeada para array Python."""
    elementos = []
    current = lista._header._next
    while current != lista._trailer:
        elementos.append(current._element)
        current = current._next
    return elementos

def exercicio_19():
    print("\n" + "="*70)
    print("EXERCÍCIO 19 - LISTA 1")
    print("="*70)
    print("Excluir elementos duplicados em lista duplamente encadeada")
    print("="*70)
    
    # Teste 1: Lista com vários duplicados
    print("Teste 1: Lista [1, 2, 3, 2, 4, 1, 5, 3, 6]")
    lista1 = criar_lista_dupla([1, 2, 3, 2, 4, 1, 5, 3, 6])
    print(f"Lista original: {imprimir_lista_dupla(lista1)}")
    print(f"Tamanho original: {len(lista1)}")
    
    excluir_duplicados(lista1)
    print(f"Lista sem duplicados: {imprimir_lista_dupla(lista1)}")
    print(f"Tamanho após remoção: {len(lista1)}")
    print(f"Array resultado: {lista_dupla_para_array(lista1)}")
    print()
    
    # Teste 2: Lista com todos elementos iguais
    print("Teste 2: Lista [5, 5, 5, 5, 5]")
    lista2 = criar_lista_dupla([5, 5, 5, 5, 5])
    print(f"Lista original: {imprimir_lista_dupla(lista2)}")
    print(f"Tamanho original: {len(lista2)}")
    
    excluir_duplicados(lista2)
    print(f"Lista sem duplicados: {imprimir_lista_dupla(lista2)}")
    print(f"Tamanho após remoção: {len(lista2)}")
    print()
    
    # Teste 3: Lista sem duplicados
    print("Teste 3: Lista [1, 2, 3, 4, 5] (sem duplicados)")
    lista3 = criar_lista_dupla([1, 2, 3, 4, 5])
    print(f"Lista original: {imprimir_lista_dupla(lista3)}")
    print(f"Tamanho original: {len(lista3)}")
    
    excluir_duplicados(lista3)
    print(f"Lista sem duplicados: {imprimir_lista_dupla(lista3)}")
    print(f"Tamanho após remoção: {len(lista3)}")
    print()
    
    # Teste 4: Lista vazia
    print("Teste 4: Lista vazia")
    lista4 = criar_lista_dupla([])
    print(f"Lista original: {imprimir_lista_dupla(lista4)}")
    
    excluir_duplicados(lista4)
    print(f"Lista sem duplicados: {imprimir_lista_dupla(lista4)}")
    print()
    
    # Teste 5: Lista com strings duplicadas
    print("Teste 5: Lista ['a', 'b', 'c', 'a', 'd', 'b', 'e']")
    lista5 = criar_lista_dupla(['a', 'b', 'c', 'a', 'd', 'b', 'e'])
    print(f"Lista original: {imprimir_lista_dupla(lista5)}")
    print(f"Tamanho original: {len(lista5)}")
    
    excluir_duplicados(lista5)
    print(f"Lista sem duplicados: {imprimir_lista_dupla(lista5)}")
    print(f"Tamanho após remoção: {len(lista5)}")
    print(f"Array resultado: {lista_dupla_para_array(lista5)}")