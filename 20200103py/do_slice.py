L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print (L[0:3])
print (L[:3])
print (L[1:3])
print (L[-1])
def trim(num):
    if num[:1] == ' ':
        return trim(num[1:])
    elif num[-1:] == ' ':
        return trim(num[:-1])
    else:
        return num
print (trim(' 123 '))