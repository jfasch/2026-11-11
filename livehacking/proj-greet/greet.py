def greet(name):
    return f'Hi {name}, my name is Joerg'

if __name__ == '__main__':
    import sys
    names = sys.argv[1:]
    for name in names:
        print(greet(name))
