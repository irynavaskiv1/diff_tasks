import pickle

from init_data import db

dbfile = open('people-pickle', 'wb')
pickle.dump(db, dbfile)
dbfile.close()
