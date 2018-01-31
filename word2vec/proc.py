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
        lis += list(jieba.cut(text)) + ['。']
    f = open('words.pkl', 'wb')
    pickle.dump(lis, f, -1)
    f.close()
    cnt += 1
    print(cnt)
