import sqlite3

with sqlite3.connect(database='gt.db') as con : 
    cur = con.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS main_cat (
        id INTEGER PRIMARY KEY,
        cat_name TEXT


    )""")


    cur.execute("""CREATE TABLE IF NOT EXISTS sub_cat (
        id INTEGER PRIMARY KEY,
        sub_cat_name TEXT,
        main_cat_id INTEGER, 
        FOREIGN KEY(main_cat_id) REFERENCES main_cat (id)
        

    )""")
    con.commit()