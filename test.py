# -*- coding: utf-8 -*-
import sqlite3
connection = sqlite3.connect('db.sqlite3')
cursor = connection.execute('select word from word')
wordlist=[i[0] for i in cursor.fetchall()]
print('\n'.join(wordlist))
print("จำนวนคำ : "+str(len(wordlist)))
connection.close()