def chain_sum0(input_number):
    result = input_number

    def wrapper(input_number2=None):
        nonlocal result
        if input_number2 is None:
            return result
        result += input_number2
        return wrapper
    return wrapper


def chain_sum1(input_number):
    ''' create without if statement '''
    result = input_number

    def wrapper(input_number2=None):
        nonlocal result
        try:
            input_number2 == int(input_number2)
        except TypeError:
            return result
        result += input_number2
        return wrapper
    return wrapper


def chain_sum(input_number):
    ''' create without if statement '''
    result = input_number

    def wrapper(input_number2=None):
        nonlocal result
        try:
            input_number2 == int(input_number2)
        except TypeError:
            return result
        result += input_number2
        return wrapper
    return wrapper


print(chain_sum(10)())   # 10
print(chain_sum(10)(23)())  # 23
print(chain_sum(10)(45)(-10)())  # 45
