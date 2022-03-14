db_file_name = 'peopleDB'
ENDDB = 'enddb.'
ENDREC = 'endrec.'
RECSEP = '=>'


def store_base(db, db_file_name=db_file_name):
    dbfile = open(db_file_name, 'w')
    for key in db:
        print(key, dbfile)
        for (key, values) in db[key].items():
            print(key, RECSEP, values, file=dbfile)
    dbfile.close()


if __name__ == '__main__':
    from init_data import db
    store_base(db)

