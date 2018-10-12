import io
from nltk.corpus import stopwords
import nltk
from collections import Counter
import pandas as pd
import csv

nltk.download('stopwords')
from nltk.tokenize import word_tokenize

stop_words = set(stopwords.words('english'))
file1 = open("document.txt")
line = file1.read()# Use this to read file content as a stream:
words = line.split()
document_without_stopwords=[]
for r in words:
    if not r in stop_words:
        document_without_stopwords.append(r)

count_frequency= Counter(document_without_stopwords)



dictionary_words=[]
with open('dictionary_of_legal_terms.csv') as f:
    reader = csv.reader(f, delimiter=";")
    for i in reader:
        dictionary_words.append(i[0])

count_relevant_words=0
for i in range(len(count_frequency)):
    if count_frequency.most_common()[i][0] in dictionary_words:
        count_relevant_words=count_relevant_words+int(count_frequency.most_common()[i][1])

print(count_relevant_words)

        
        


