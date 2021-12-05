# for files

f = open('filename.txt', 'w')
f.write('sometext')
f.flush()
f.close()

# same as, doing flush and close by himself
with open('filename_second.txt', 'w') as file:
    """ use __enter__ and __exit__ magic methods"""
    file.write('sometext_second')
