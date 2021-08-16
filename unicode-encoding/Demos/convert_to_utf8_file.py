with open('./unicode-encoding/Demos/characters_dos.txt', encoding='cp1252') as f1:
    with open('./unicode-encoding/Demos/characters_utf.txt','w', encoding='utf-8') as f2:
        f2.write( f1.read() )