import pickle
import random

f = open('sents.pkl', 'rb')
sents = pickle.load(f)
f.close()

long_sent = []

for sent in sents :
    if (len(sent) > 10) :
        long_sent.append(sent)
random.shuffle(long_sent)
print(len(long_sent))

long_sent = long_sent[:1000]
data = []

for sent in long_sent :
    data.append((sent[:-4], sent[-4:-2]))

f = open('test_data.pkl', 'wb')
pickle.dump(data, f, -1)
f.close()
