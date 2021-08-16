with open('./unicode-encoding/Demos/characters_utf.txt', 'rb') as f:
    contents = f.read()
    print(contents)
    print(contents.decode('utf-8'))