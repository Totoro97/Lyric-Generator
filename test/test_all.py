import pickle
import jieba
import re
import numpy
import math

test_lis = ['fdist', 'fdist_word', 'char_rnn', 'word_rnn']
data = dict()
cost = dict()

for meth in test_lis :
    cost[meth] = 0.0
    
for meth in test_lis :
    f = open('ans_' + meth + '.pkl', 'rb')
    data[meth] = list(pickle.load(f))
    f.close()
    
f = open('word2vec.pkl', 'rb')
model = pickle.load(f)
f.close()

f = open('test_data.pkl', 'rb')
test_data = pickle.load(f)
f.close()

for index in range(1000) :
    for meth in test_lis :
        ans = re.sub('\n', '。', data[meth][index][1])
        print(ans)
        in_data, out_data = test_data[index]
        #print(out_data)
        in_data = ''.join(in_data)
        ans = re.sub(in_data, '', ans)
        ans = list(jieba.cut(ans))
        for _ in range(2) : 
            an = ans[_]
            if (an in model) :
                cost[meth] += math.sqrt(float(sum((model[an] - model[out_data[_]]) ** 2)))
            else :
                #pass
                cost[meth] += math.sqrt(float(sum(model[out_data[_]] ** 2))) 
    for meth in test_lis :
        print(meth, cost[meth])
    print(index)
        
