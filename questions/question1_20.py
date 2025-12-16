from doublyLinkedBase import _DoublyLinkedBase

class DoublyLinkedBaseWithReverse(_DoublyLinkedBase):
    """
    Modifica a classe _DoublyLinkedBase para incluir um método reverse 
    que inverte a ordem da lista, mas sem criar ou destruir nenhum nó.
    """
    
    def reverse(self):
        """
        Inverte a ordem da lista duplamente encadeada sem criar ou destruir nós.
        Apenas reorganiza os ponteiros _prev e _next dos nós existentes.
        """
        if self.is_empty() or len(self) == 1:
            return  # Lista vazia ou com um elemento não precisa ser invertida
        
        # Percorre todos os nós (incluindo header e trailer) e inverte os ponteiros
        current = self._header
        
        while current is not None:
            # Troca os ponteiros _prev e _next do nó atual
            temp = current._prev
            current._prev = current._next
            current._next = temp
            
            # Move para o próximo nó (que agora está em _prev devido à troca)
            current = current._prev
        
        # Após inverter todos os ponteiros, troca header e trailer
        temp = self._header
        self._header = self._trailer
        self._trailer = temp

class ListaDuplaComReverse(DoublyLinkedBaseWithReverse):
    """Lista duplamente encadeada com funcionalidade de reversão."""
    
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

def criar_lista_com_reverse(elementos):
    """Função auxiliar para criar uma lista duplamente encadeada com reverse."""
    lista = ListaDuplaComReverse()
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

def verificar_integridade_lista(lista):
    """Verifica se os ponteiros da lista estão corretos após a reversão."""
    if lista.is_empty():
        return True
    
    # Verifica se header aponta corretamente
    if lista._header._next._prev != lista._header:
        return False
    
    # Verifica se trailer aponta corretamente
    if lista._trailer._prev._next != lista._trailer:
        return False
    
    # Verifica todos os nós intermediários
    current = lista._header._next
    while current != lista._trailer:
        if current._next._prev != current:
            return False
        if current._prev._next != current:
            return False
        current = current._next
    
    return True

def exercicio_20():
    print("\n" + "="*70)
    print("EXERCÍCIO 20 - LISTA 1")
    print("="*70)
    print("Método reverse em lista duplamente encadeada")
    print("="*70)
    
    # Teste 1: Lista com vários elementos
    print("Teste 1: Lista [1, 2, 3, 4, 5]")
    lista1 = criar_lista_com_reverse([1, 2, 3, 4, 5])
    print(f"Lista original: {imprimir_lista_dupla(lista1)}")
    print(f"Array original: {lista_dupla_para_array(lista1)}")
    print(f"Tamanho: {len(lista1)}")
    
    lista1.reverse()
    print(f"Lista invertida: {imprimir_lista_dupla(lista1)}")
    print(f"Array invertido: {lista_dupla_para_array(lista1)}")
    print(f"Tamanho após reversão: {len(lista1)}")
    print(f"Integridade dos ponteiros: {verificar_integridade_lista(lista1)}")
    print()
    
    # Teste 2: Lista com um elemento
    print("Teste 2: Lista [42]")
    lista2 = criar_lista_com_reverse([42])
    print(f"Lista original: {imprimir_lista_dupla(lista2)}")
    
    lista2.reverse()
    print(f"Lista invertida: {imprimir_lista_dupla(lista2)}")
    print(f"Integridade: {verificar_integridade_lista(lista2)}")
    print()
    
    # Teste 3: Lista vazia
    print("Teste 3: Lista vazia")
    lista3 = criar_lista_com_reverse([])
    print(f"Lista original: {imprimir_lista_dupla(lista3)}")
    
    lista3.reverse()
    print(f"Lista invertida: {imprimir_lista_dupla(lista3)}")
    print()
    
    # Teste 4: Lista com dois elementos
    print("Teste 4: Lista [10, 20]")
    lista4 = criar_lista_com_reverse([10, 20])
    print(f"Lista original: {imprimir_lista_dupla(lista4)}")
    
    lista4.reverse()
    print(f"Lista invertida: {imprimir_lista_dupla(lista4)}")
    print(f"Integridade: {verificar_integridade_lista(lista4)}")
    print()
    
    # Teste 5: Dupla reversão (deve voltar ao original)
    print("Teste 5: Dupla reversão [1, 2, 3, 4]")
    lista5 = criar_lista_com_reverse([1, 2, 3, 4])
    original = lista_dupla_para_array(lista5)
    print(f"Lista original: {imprimir_lista_dupla(lista5)}")
    
    lista5.reverse()
    print(f"Após 1ª reversão: {imprimir_lista_dupla(lista5)}")
    
    lista5.reverse()
    print(f"Após 2ª reversão: {imprimir_lista_dupla(lista5)}")
    final = lista_dupla_para_array(lista5)
    print(f"Voltou ao original? {original == final}")
    print(f"Integridade: {verificar_integridade_lista(lista5)}")
    print()
    
    # Teste 6: Lista com strings
    print("Teste 6: Lista ['a', 'b', 'c', 'd']")
    lista6 = criar_lista_com_reverse(['a', 'b', 'c', 'd'])
    print(f"Lista original: {imprimir_lista_dupla(lista6)}")
    
    lista6.reverse()
    print(f"Lista invertida: {imprimir_lista_dupla(lista6)}")
    print(f"Array invertido: {lista_dupla_para_array(lista6)}")
    print(f"Integridade: {verificar_integridade_lista(lista6)}")