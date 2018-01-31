import pickle
import jieba
import random

f = open('lyrics.pkl', 'rb')
data = pickle.load(f)
f.close()

cnt = 0
test_data = []
data = list(data.items())
print(len(data))
random.shuffle(data)

for _, text in data :
    lis = list(jieba.cut(text)) 
    while ('\n' in lis) :
        lis.remove('\n')
    if (len(lis) < 102) : 
        continue
    test_data.append((lis[:100], lis[100: 102]))
    print(lis[: 100])
    cnt += 1
    print(cnt)
    if (cnt >= 500) :
        break
f = open('test_data_long.pkl', 'wb')
pickle.dump(test_data, f, -1)
f.close()
