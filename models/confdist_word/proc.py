import nltk
import pickle
import os
import numpy as np
import sys

if os.path.exists('fdist.pkl') :
    f = open('fdist.pkl', 'rb')
    fdist = pickle.load(f)
    f.close()
else :    
    f = open('words.pkl', 'rb')
    data = pickle.load(f)
    f.close()
    lis = data

    bigram = list(nltk.bigrams(lis))
    fdist = nltk.ConditionalFreqDist(bigram)
    f = open('fdist.pkl', 'wb')
    pickle.dump(fdist, f, -1)
    f.close()

bg = sys.argv[1]

text = bg

for _ in range(100) :
    a = []
    p = []
    for key, value in fdist[bg].items() :
        a.append(key)
        p.append(value)
    a = np.array(a)
    p = np.array(p, dtype = np.float32)
    p /= sum(p)
    bg = np.random.choice(a = a, p = p)
    text += bg

print(text)
