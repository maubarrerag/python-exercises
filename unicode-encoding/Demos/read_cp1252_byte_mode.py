with open('./unicode-encoding/Demos/characters_dos.txt', 'rb') as f:
    contents = f.read()
    print(contents)
    print(contents.decode('cp1252'))