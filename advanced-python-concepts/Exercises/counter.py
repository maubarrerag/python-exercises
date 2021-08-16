from collections import Counter

with open('Declaration_of_Independence.txt') as f:
    line = f.read()
    words = []
    words = [word.upper() for word in line.split() if len(word) > 5]
    c = Counter(words)
    print(c.most_common(10))
