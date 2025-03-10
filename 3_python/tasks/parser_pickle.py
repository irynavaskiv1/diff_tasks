import pickle

data = {1: "1", 2: "two"}
file = "file_pickle.pc"


with open(file, "wb") as f:
    str_repr = pickle.dumps(data)
    print(str_repr)
    pickle.dump(data, file=f)


with open(file, "rb") as f:
    data1 = pickle.load(file=f)
    data2 = pickle.loads(str_repr)

print(data1, data2)
