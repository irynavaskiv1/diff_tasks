def gen(param, start=0):
    for p in param:
        yield start, p
        yield from range(3)
        start += 1


for elem in gen(param="abc", start=10):
    print(elem)
