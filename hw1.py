__author__ = 'pete'

import nltk
from nltk.corpus import gutenberg

import random

# dicts
words = {}
start_words = {}
last_words = {}
bigrams = {}
probabilities = {}
start_word_probs = {}
last_word_probs = {}

random.seed()

print 'importing text...'
# text
text_sents = gutenberg.sents('carroll-alice.txt')

print 'finding unique_words...'
# find the unique words in the text
unique_words = set([w.lower() for s in text_sents for w in s])

# hash table of words in text

print 'finding bigrams...'
# pairs of words in the text

for sent in text_sents:
    i = 0

    # hash first word
    first = sent[i].lower()

    if first in words:
        words[first] += 1
    else:
        words[first] = 1

    if first in start_words:
        start_words[first] += 1
    else:
        start_words[first] = 1

    # hash word 1 to n-1 and word pairs
    while i < len(sent)-2:

        word = sent[i].lower()
        follow_word = sent[i+1].lower()

        if word in words:
            words[word] += 1
        else:
            words[word] = 1

        if (word,follow_word) in bigrams:
            bigrams[word, follow_word] += 1
        else:
            bigrams[word, follow_word] = 1

        i+=1

    # hash last word
    last = sent[i].lower()

    if last in words:
        words[last] += 1
    else:
        words[last] = 1

    if last in last_words:
        last_words[last] += 1
    else:
        last_words[last] = 1

print 'calculating probabilities...'
j = 0
for (word,follow_word) in bigrams:
    probabilities[word, follow_word] =  float(bigrams[word, follow_word]) / float(words[word])
for word in start_words:
    start_word_probs[word] =  float(start_words[word]) / float(words[word])
for word in last_words:
    last_word_probs[word] = float(last_words[word]) / float(words[word])

# debug
#print 'Bigrams:'
#print bigrams
#print 'Probabilities'
#print probabilities

sorted_probs = sorted(probabilities.items(), key=lambda x:x[1], reverse=True)
#print sorted_probs
#print sorted_probs[0:10]

sorted_start_words_probs = sorted(start_word_probs.items(), key=lambda x:x[1], reverse=True)

sorted_last_words_probs = sorted(last_word_probs.items(), key=lambda x:x[1], reverse=True)

#output = str(sorted_start_words_probs[0]) #[0])#[1]
#i = 0
#while i < 5:
#    output += str(sorted_probs[i][0]) #[0]) + " " + str(sorted_probs[i][0][1])
#    i += 1 #[1] + sorted_probs[i]#[2]
#output += sorted_last_words_probs[0] #[1]#[1] + "."
#print output

print sorted_start_words_probs[0][0]
print sorted_probs[0][0][0]
print sorted_probs[0][0][1]
print sorted_last_words_probs[0][0]

i = 0
while i < 100:
    k = int(random.randint(0,100))
    j = int(random.randint(0,5))

    output = str(sorted_start_words_probs[k][0])[0].upper() + str(sorted_start_words_probs[k][0])[1:]
    while j < 6:
        output += " " + str(sorted_probs[k+j*j][0][0]) + " " + str(sorted_probs[k+j*j][0][1])
        j += 1
    output += " " + str(sorted_last_words_probs[k][0]) + ". "
    print output
    i += 1
#print sorted_probs
# print start_words
#first_words = [x for x in sorted_probs if x[0] == 'None']
#print first_words

#generated = ""
#start_words = sorted_probs['None']
#print start_words

