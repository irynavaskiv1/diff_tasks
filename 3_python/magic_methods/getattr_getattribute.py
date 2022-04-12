class GetAttr:
    """
    check diff with __getattr__ and __getattribute, where
    attr1 - attribute class
    attr2 - attribute instance
    attr3 - attribute dynamic

    __getattribute__  call for each objects
    __getattr__ only for dynamic objects
    """

    attr1 = 1

    def __init__(self):
        self.attr2 = 2

    def __getattr__(self, attr):
        print('__getattr__: ' + attr)
        return 3


class GetAttribute(object):
    attr1 = 1

    def __init__(self):
        self.attr2 = 2

    def __getattribute__(self, attr):
        print('__getattribute__ :' + attr)
        if attr == 'attr3':
            return 3
        else:
            return object.__getattribute__(self, attr)


X = GetAttr()
Y = GetAttribute()

print('attr class', X.attr1)
print('attribute class', Y.attr1)
print('-' * 40)
print('attr instance', X.attr2)
print('attribute instance', Y.attr2)
print('-' * 40)
print('attr dynamic', X.attr3)
print('attribute dynamic', X.attr3)
