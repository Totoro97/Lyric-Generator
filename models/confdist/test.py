import nltk
import pickle
import os
import numpy as np

if os.path.exists('fdist.pkl') :
    f = open('fdist.pkl', 'rb')
    fdist = pickle.load(f)
    f.close()
else :    
    f = open('lyrics.pkl', 'rb')
    data = pickle.load(f)
    f.close()
    lis = []
    cnt = 0
    for _ in data :
        js = [__ for __ in data[_]]
        lis += js
        cnt += 1
        print(cnt)

    bigram = list(nltk.bigrams(lis))
    fdist = nltk.ConditionalFreqDist(bigram)
    f = open('fdist.pkl', 'wb')
    pickle.dump(fdist, f, -1)
    f.close()
    
f = open('test_data.pkl', 'rb')
test_data = pickle.load(f)
f.close()

Ans = []
cnt = 0

for in_data, out_data in test_data :
    ans = ''.join(in_data)
    bg = in_data[-1][-1]
    for _ in range(20) :
        a = []
        p = []
        for key, value in fdist[bg].items() :
            a.append(key)
            p.append(value)
        a = np.array(a)
        p = np.array(p, dtype = np.float32)
        p /= sum(p)
        bg = np.random.choice(a = a, p = p)
        ans += bg
        
    Ans.append(ans)
    cnt += 1
    print(cnt)
    print(''.join(in_data), ans)
data = zip(test_data, Ans)
f = open('ans_fdist.pkl', 'wb')
pickle.dump(data, f, -1)
f.close()
