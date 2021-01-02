from dateutil.tz.win import valuestodict

teststr1 = "God"
teststr2 = "dog"

def ispermutation(str1, str2):
 str1 = str1.lower()
 str2 = str2.lower()
 if len(str1) != len(str2):
     return False
 str1 = ''.join(sorted(str1))
 str2 = ''.join(sorted(str2))
 size = len(str1)
 for i in range(size):
    if str1[i] != str2[i]:
         return False
    else:
         return True

print(ispermutation(teststr1, teststr2))

#other approch is given below
def otherapproch(str1, str2):
    d = dict()
    for i in str1:
        if i in d:
            d[i] -= 1
        else:
            d[i] = 1
    for i in str2:
        if i in d:
            d[i] -= 1
        else:
            d[i] = 1
    return all(value == 0 for value in d.values())



