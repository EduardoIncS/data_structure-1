class ArrayDeque:
    DEFAULT_CAPACITY = 10
    
    def __init__(self):
        self._data = [None] * ArrayDeque.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0
    
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def first(self):
        """Retorna o primeiro elemento (frente) sem removê-lo"""
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self._data[self._front]
    
    def last(self):
        """Retorna o último elemento (traseira) sem removê-lo"""
        if self.is_empty():
            raise IndexError("Deque is empty")
        back = (self._front + self._size - 1) % len(self._data)
        return self._data[back]
    
    def back(self):
        """Alias para last() - retorna o último elemento sem removê-lo"""
        return self.last()
    
    def add_first(self, e):
        """Adiciona elemento na frente do deque"""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        self._front = (self._front - 1) % len(self._data)
        self._data[self._front] = e
        self._size += 1
    
    def add_last(self, e):
        """Adiciona elemento na traseira do deque"""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1
    
    def delete_first(self):
        """Remove e retorna o primeiro elemento"""
        if self.is_empty():
            raise IndexError("Deque is empty")
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)
        return answer
    
    def delete_last(self):
        """Remove e retorna o último elemento"""
        if self.is_empty():
            raise IndexError("Deque is empty")
        back = (self._front + self._size - 1) % len(self._data)
        answer = self._data[back]
        self._data[back] = None
        self._size -= 1
        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)
        return answer
    
    def _resize(self, cap):
        """Aumenta a capacidade do array da fila após o último elemento"""
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0
