from matplotlib import pyplot as plt

fig=plt.figure(1)
ax1=plt.subplot(111)
costs = []
for index in range(4) :
    costs[index] /= 1000.0
        
meths = ['fdist', 'fdist_word', 'char_rnn', 'word_rnn']

rect=ax1.bar(left=range(4),height=costs,color="lightblue")
for rec in rect:
	x=rec.get_x()
	height=rec.get_height()
	ax1.text(x+0.1,1.02*height,str(height))
ax1.set_xticks(range(4))
ax1.set_xticklabels(meths)
plt.show()
