import random

def main():
    dice = [(a,b,c,d,e) for a in range(1,7) for b in range(1,7) for c in range(1,7) for d in range(1,7) for e in range(1,7)]

    print(len(dice))

    dice2 = [(a,b,c,d,e) for a in range(1,7) for b in range(a,7) for c in range(b,7) for d in range(c,7) for e in range(d,7)]

    print(len(dice2))
    print(random.choice(dice2))

if __name__ == '__main__':
    main()