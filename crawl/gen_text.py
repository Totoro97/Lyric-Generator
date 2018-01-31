import pickle
import re
f = open('backup/lyrics.pkl', 'rb')
data = pickle.load(f)
f.close()

text = ''
for _ in data :
    text += data[_]

text = re.sub('作[词曲]', '', text)
f = open('text.txt', 'w')
f.write(text)
f.close()
