
import collections
#from nltk.corpus import stopwords

file = open('98-0.txt')
punctuations = set(['.', ':', '(', '/', ')', '\\', '"', '-', ','])
#stopwords = set(stopwords.words('english'))
wordcount = {}

for word in file.read().lower().split(): 
#    for punctuation in punctuations:
#        word = word.replace(punctuation, "")
    # if word in stopwords
#         continue;
    word = word.replace(".","")
    word = word.replace(",","")
    word = word.replace("\"","")
    word = word.replace("“","")
    
    if word in wordcount:
        wordcount[word] +=1
    else: 
        wordcount[word] = 1
    
d = collections.Counter(wordcount)

for word, count in d.most_common(10):
    print (word, ": ", count)
