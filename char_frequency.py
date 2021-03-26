def char_frequency(string):
    my_dictionary=dict()
    keys=[]
    chars=[]
    for key in string:
        C=0
        for j in string:
                if key == j:
                    C += 1
                else:
                    continue
        my_dictionary[key]=C
    for a,b in my_dictionary.items():
        chars.append(a)
        keys.append(b)
    keys.sort()
    chars.sort()

    print(chars)
    print(keys)

def begin():
    string=input('enter a sentence or a word')
    char_frequency(string)
begin()
