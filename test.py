# -*- coding: utf-8 -*-
import sqlite3
connection = sqlite3.connect('db.sqlite3')
cursor = connection.execute('select word from word')
wordlist=[i[0] for i in cursor.fetchall()]
#print('\n'.join(wordlist))
print("จำนวนคำ : "+str(len(wordlist)))
connection.close()
from pythainlp.tokenize import dict_word_tokenize,create_custom_dict_trie,word_tokenize
dictthai=create_custom_dict_trie(wordlist)
while True:
    text=input("text : ")
    if text=="exit":
        break
    print("ผลจาก dict : \t"+'|'.join(dict_word_tokenize(text,dictthai)))
    print("ผลจาก PyThaiNLP : \t"+'|'.join(word_tokenize(text)))