text = 'Hello world. Hello Python. Hello again.'

import string

words = text.lower().translate(str.maketrans(",.!'-", '     ', string.digits)).split()
uniq_words = list()
uniq_words.extend(element for element in words if element not in uniq_words)
res = [(word, words.count(word)) for word in uniq_words]
res.sort(key=lambda x: (x[1]), reverse=True)
res = res[:10]
print(res)
