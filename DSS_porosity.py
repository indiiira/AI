import numpy as np

import sqlite3

rows = [
    (0, 'Материал1', 12.0, 5.0, 0.1, 0.01),
    (1, 'Материал2', 9.00, 8.0, 0.15, 0.01),
    (2, 'Материал3', 15.0, 8.0, 0.2, 0.5),
    (3, 'Материал4', 14.0, 7.0, 0.3, 0.7),
]
conn = sqlite3.connect('C:/Users/Индира/PycharmProjects/AI/My_DB.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE Materials 
                (ID INTEGER NOT NULL PRIMARY KEY
                AUTOINCREMENT, NAME TEXT, 
                PORE_AREA_MEAN REAL NOT NULL, 
                PORE_AREA_STD REAL NOT NULL, 
                POROUS_MEAN REAL NOT NULL, 
                POROUS_STD REAL NOT NULL 
                )""")
cur.executemany("""INSERT INTO Materials values
(?,?,?,?,?,?)""", rows)
conn.commit()
conn.close()

