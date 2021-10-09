'''
check diff with __getattr__ and __getattribute, where
attr1 - attribute class
attr2 - attribute instance
attr3 - attribute dynamic
'''


class GetAttr:
    attr1 = 1

    def __init__(self):
        self.attr2 = 2

    def __getattr__(self, attr):
        print('get: ' + attr)
        return 3


X = GetAttr()
print(X.attr1)
print(X.attr2)
print(X.attr3)
print('-' * 40)


class GetAttribute(object):
    attr1 = 1

    def __init__(self):
        self.attr2 = 2

    def __getattribute__(self, attr):
        print('get: ' + attr)
        if attr == 'attr3':
            return 3
        else:
            return object.__getattribute__(self, attr)


Y = GetAttribute()
print(Y.attr1)
print(Y.attr2)
print(Y.attr3)
