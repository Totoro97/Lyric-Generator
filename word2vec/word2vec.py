import pickle
from gensim.models.word2vec import Word2Vec

f = open('sents.pkl', 'rb')
sents = pickle.load(f)
f.close()

model = Word2Vec(sents, min_count=1)

f = open('word2vec.pkl', 'wb')
pickle.dump(model, f, -1)
f.close()

