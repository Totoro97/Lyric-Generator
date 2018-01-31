import jieba
import pickle

f = open('lyrics.pkl', 'rb')
data = pickle.load(f)
f.close()

lis = []

cnt = 0
for _ in data :
    texts = data[_].strip().split('\n')
    for text in texts :
        lis.append(list(jieba.cut(text)) + ['。'])
    f.close()
    cnt += 1
    print(cnt)
    
f = open('sents.pkl', 'wb')
pickle.dump(lis, f, -1)
