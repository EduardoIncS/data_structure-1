from binaryTree import BinaryTree

class ArrayBinaryTree(BinaryTree):
    class Position(BinaryTree.Position):
        def __init__(self, container, index):
            self._container = container
            self._index = index
            
        def element(self):
            return self._container._data[self._index]
        
        def __eq__(self, other):
            return type(other) is type(self) and other._index == self._index and other._container is self._container
    
    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError("p must be of type Position")
        if p._container is not self:
            raise ValueError("p does not belong to this container")
        if p._index < 0 or p._index >= len(self._data):
            raise ValueError("p is no longer valid")
        if self._data[p._index] is None:
            raise ValueError("p is no longer valid")
        return p._index
    
    def _make_position(self, index):
        if index >= 0 and index < len(self._data) and self._data[index] is not None:
            return self.Position(self, index)
        return None
    
    def __init__(self, capacity=10):
        self._data = [None] * capacity
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def root(self):
        return self._make_position(0)
    
    def parent(self, p):
        index = self._validate(p)
        if index == 0:
            return None
        parent_index = (index - 1) // 2
        return self._make_position(parent_index)
    
    def left(self, p):
        index = self._validate(p)
        left_index = 2 * index + 1
        return self._make_position(left_index)
    
    def right(self, p):
        index = self._validate(p)
        right_index = 2 * index + 2
        return self._make_position(right_index)
    
    def num_children(self, p):
        index = self._validate(p)
        count = 0
        left_index = 2 * index + 1
        right_index = 2 * index + 2
        if left_index < len(self._data) and self._data[left_index] is not None:
            count += 1
        if right_index < len(self._data) and self._data[right_index] is not None:
            count += 1
        return count
    
    def _resize(self, new_capacity):
        old_data = self._data
        self._data = [None] * new_capacity
        for i in range(len(old_data)):
            self._data[i] = old_data[i]
    
    def _add_root(self, e):
        if self._data[0] is not None:
            raise ValueError("Root exists")
        self._data[0] = e
        self._size = 1
        return self._make_position(0)
    
    def _add_left(self, p, e):
        index = self._validate(p)
        left_index = 2 * index + 1
        if left_index >= len(self._data):
            self._resize(2 * len(self._data))
        if self._data[left_index] is not None:
            raise ValueError("Left child exists")
        self._data[left_index] = e
        self._size += 1
        return self._make_position(left_index)
    
    def _add_right(self, p, e):
        index = self._validate(p)
        right_index = 2 * index + 2
        if right_index >= len(self._data):
            self._resize(2 * len(self._data))
        if self._data[right_index] is not None:
            raise ValueError("Right child exists")
        self._data[right_index] = e
        self._size += 1
        return self._make_position(right_index)
    
    def replace(self, p, e):
        index = self._validate(p)
        old = self._data[index]
        self._data[index] = e
        return old
    
    def _delete(self, p):
        index = self._validate(p)
        if self.num_children(p) == 2:
            raise ValueError("p has two children")
        old = self._data[index]
        self._data[index] = None
        self._size -= 1
        return old
