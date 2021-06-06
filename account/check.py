# importing the important library.
import nltk
import sys
import pandas as pd
import numpy as np
import os
from os import listdir
from os.path import isfile, join
import time
import re
from nltk.tokenize import sent_tokenize, word_tokenize
from spellchecker import SpellChecker
"""from termcolor import colored
from colorama import Fore
from sty import fg, rs"""

'''
def load_book(path):
    """Load a book from its file"""
    input_file = os.path.join(path)
    with open(input_file) as f:
        book = f.read()
    return book

path = "E:\\extra\\big.txt"

'''

book = sys.argv[1]

def clean_text(text):
    '''Remove unwanted characters and extra spaces from the text'''
    text = re.sub(r'\n', ' ', text) 
    text = re.sub(r'[{}@_*>()\\#%+=\[\]]','', text)
    text = re.sub('a0','', text)
    text = re.sub('\'92t','\'t', text)
    text = re.sub('\'92s','\'s', text)
    text = re.sub('\'92m','\'m', text)
    text = re.sub('\'92ll','\'ll', text)
    text = re.sub('\'91','', text)
    text = re.sub('\'92','', text)
    text = re.sub('\'93','', text)
    text = re.sub('\'94','', text)
    text = re.sub('\.','. ', text)
    text = re.sub('\!','! ', text)
    text = re.sub('\?','? ', text)
    text = re.sub(' +',' ', text)
    return text


book = clean_text(book)

#TGREEN =  '\033[32m'
spell = SpellChecker()
array = []
right = 0
wrong = 0
for word in word_tokenize(book):
    if spell.correction(word) == word:
        array.append(word)
        right = right + 1
    else:
        array.append("[" + word + "]")
        wrong = wrong + 1
        

file = open("C:\\Users\\DIVESH\\projects\\Essay checker\\media\\div1.txt", "w+")
for f in array:
    file.write(f+' ') 

# giving the marks

# givin marks basis of wrong word 
total_marks = 100
total_word = right + wrong
wrong_percent = wrong / total_word 
m = total_marks/2 *wrong_percent 
fm_1 = 50 - m

# giving marks basis of the desired keyword present 
keyword = sys.argv[2]
list = keyword.split(",")

def is_group_member(group_data, n):
    for value in group_data:
        if n == value:
            return True
    return False
match = 0
for i in list:
    if is_group_member(word_tokenize(book),i):
        match = match + 1

len_keyword = len(list)
match_percent1 = match/len_keyword
match_percent = (match/len_keyword) * 100
fm_2 = 50 * match_percent1
fm = fm_1 + fm_2


file = open("C:\\Users\\DIVESH\\projects\\Essay checker\\media\\div1.txt", "r")
file = file.read()
print("your given keyword match",match_percent,"%  percent \n\n\n")
print("The final marks is",format(fm, ".2f"))
print(print(file))


    
