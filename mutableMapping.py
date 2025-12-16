from collections.abc import MutableMapping as ABCMutableMapping


class MutableMapping(ABCMutableMapping):
    def __getitem__(self, k):
        """Retorna o valor associado à chave k."""
        raise NotImplementedError("Must be implemented by subclass")
    
    def __setitem__(self, k, v):
        """Associa o valor v à chave k."""
        raise NotImplementedError("Must be implemented by subclass")
    
    def __delitem__(self, k):
        """Remove o item com chave k."""
        raise NotImplementedError("Must be implemented by subclass")
    
    def __len__(self):
        """Retorna o número de itens no mapa."""
        raise NotImplementedError("Must be implemented by subclass")
    
    def __iter__(self):
        """Gera uma iteração sobre as chaves do mapa."""
        raise NotImplementedError("Must be implemented by subclass")
    
    def __contains__(self, k):
        """Retorna True se a chave k está no mapa."""
        try:
            self[k]
            return True
        except KeyError:
            return False
    
    def get(self, k, default=None):
        """Retorna o valor para a chave k, ou default se k não está no mapa."""
        try:
            return self[k]
        except KeyError:
            return default
    
    def setdefault(self, k, default=None):
        """Se k está no mapa, retorna seu valor; caso contrário, define e retorna default."""
        try:
            return self[k]
        except KeyError:
            self[k] = default
            return default
    
    def pop(self, k, *args):
        """Remove e retorna o valor para a chave k.
        Se k não está no mapa, retorna default se fornecido, caso contrário levanta KeyError.
        """
        try:
            value = self[k]
            del self[k]
            return value
        except KeyError:
            if args:
                return args[0]
            raise
    
    def popitem(self):
        """Remove e retorna um par (chave, valor) arbitrário do mapa."""
        try:
            k = next(iter(self))
        except StopIteration:
            raise KeyError("popitem(): map is empty")
        value = self[k]
        del self[k]
        return (k, value)
    
    def clear(self):
        """Remove todos os itens do mapa."""
        while len(self) > 0:
            self.popitem()
    
    def keys(self):
        """Retorna uma visão das chaves do mapa."""
        return KeysView(self)
    
    def values(self):
        """Retorna uma visão dos valores do mapa."""
        return ValuesView(self)
    
    def items(self):
        """Retorna uma visão dos pares (chave, valor) do mapa."""
        return ItemsView(self)
    
    def update(self, other=None, **kwargs):
        """Atualiza o mapa com pares chave/valor de other e kwargs."""
        if other is not None:
            if hasattr(other, 'keys'):
                for k in other.keys():
                    self[k] = other[k]
            else:
                for k, v in other:
                    self[k] = v
        for k, v in kwargs.items():
            self[k] = v
    
    def __eq__(self, other):
        """Retorna True se o mapa é igual a other."""
        if not isinstance(other, type(self)):
            return False
        if len(self) != len(other):
            return False
        for k in self:
            if k not in other or self[k] != other[k]:
                return False
        return True
    
    def __ne__(self, other):
        """Retorna True se o mapa não é igual a other."""
        return not (self == other)

class KeysView:
    """Visão das chaves de um mapa."""
    
    def __init__(self, mapping):
        self._mapping = mapping
    
    def __len__(self):
        return len(self._mapping)
    
    def __iter__(self):
        return iter(self._mapping)
    
    def __contains__(self, k):
        return k in self._mapping


class ValuesView:
    """Visão dos valores de um mapa."""
    
    def __init__(self, mapping):
        self._mapping = mapping
    
    def __len__(self):
        return len(self._mapping)
    
    def __iter__(self):
        for key in self._mapping:
            yield self._mapping[key]
    
    def __contains__(self, v):
        for value in self:
            if value == v:
                return True
        return False


class ItemsView:
    """Visão dos pares (chave, valor) de um mapa."""
    
    def __init__(self, mapping):
        self._mapping = mapping
    
    def __len__(self):
        return len(self._mapping)
    
    def __iter__(self):
        for key in self._mapping:
            yield (key, self._mapping[key])
    
    def __contains__(self, item):
        k, v = item
        try:
            return self._mapping[k] == v
        except KeyError:
            return False
