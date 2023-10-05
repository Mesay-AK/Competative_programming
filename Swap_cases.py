def swap_case(s):
    newS=''
    for i in s:
        if i .isupper():
            newS+=i.lower()
        else:
            newS+=i.upper()
        
    return newS

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
