word = 'Ê Ñ Ç ð Ð ¡ Ñ G'
encodings = ['utf-8', 'cp1252', 'iso-8859-1', 'ascii']
for encoding in encodings:
    print(word.encode(encoding, errors='replace'))
print(word.encode('ascii',errors='xmlcharrefreplace'))