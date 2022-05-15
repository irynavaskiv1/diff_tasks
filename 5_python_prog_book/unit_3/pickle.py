import pickle

data = {'a': 'a', 1: '1'}
path = 'mydata.pc1'

# pickle.load()   # convert a str to object (deserialization)
# pickle.dumps()  # convert an object to str (serialization)

# with open(path, 'wb') as file:
#     date_new = pickle.dumps(data)
#     print(date_new)
#     pickle.dump(data, file=file)
#
#
# with open(path, 'rb') as file:
#     pickle.load(data, file=file)
