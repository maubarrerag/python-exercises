with open('./unicode-encoding/Demos/characters_dos.txt', encoding='cp1252') as f:
    contents = f.read()
    print(contents.encode('cp1252'))
    print(contents)