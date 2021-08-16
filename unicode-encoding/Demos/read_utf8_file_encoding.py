with open('./unicode-encoding/Demos/characters_utf.txt', encoding='utf-8') as f:
    contents = f.read()
    print(contents)
    print(contents.encode('utf-8'))