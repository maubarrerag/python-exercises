with open('URLs.txt', encoding='utf-8') as f:
    urls = f.read().splitlines()
def is_ascii(c):
    """Returns boolean indicating if c is ascii
    
    Keyword arguments:
    c (str) - one-character string to check
    """
    return ord(c) < 256
        
def contains_confusables(s):
    """Searches string for confusables.
    Returns 2-element tuple:
     t[0]: Boolean - indicates if s contains one or more confusables.
     t[1]: String - copy of original string, but with confusables utf-8 encoded.
    
    Keyword arguments:
    s (str) - string to check 
    """
    u = []
    confusable = False
    for c in s:
        if is_ascii(c):
            u.append(c)
        else:
            u.append('[' + str(c.encode('utf-8')) + ']')
            confusable = True
    s2 = ''.join(u)
    
    return (confusable, s2)
def main():    
    for url in urls:
        t = contains_confusables(url)
        if t[0]:
            print(url,  '*' + t[1], sep='\n\t', end='\n\n')
        else:
            print(url, end='\n\n')
main()