class dict2:
    def __init__(self):
        self.store = []

    def __getitem__(self, key):
        for k, v in self.store:
            if k == key:
                return v

    def __setitem__(self, key, value):
        for i, (k, v) in enumerate(self.store):
            if k == key:
                self.store[i] = (key, value)
                return
        self.store.append((key, value))

    def __repr__(self):
        
        items = ', '.join(f"'{k}': {v}" for k, v in self.store)
        return f"{{ {items} }}"

# Example usage:
obj = dict2()
obj['a'] = 1
obj['b'] = 2
obj['c'] = 3

print(obj['a'])  # Output: 1
#print(obj['b'])  # Output: 2
#print(obj['c'])  # Output: 3

print(obj)       # Output: { 'a': 1, 'b': 2, 'c': 3 }
