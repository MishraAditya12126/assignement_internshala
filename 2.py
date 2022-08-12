var=list(input())

def checker(var):
    vowel = 'aeiou'
    final_word = ''

    first_word=var[0]

    for i in range(len(var)): # replacing first character with vowel
        if (var[0] not in vowel) and (var[i] in vowel):
            var[0]=var[i]
            var[i]=first_word
            break

    for k in range(len(var)): # replacing any special characters with "@" and alphabet with first occurence of the string
        if k==0:
            continue
        if var[k]==" ":
            continue
        if not ((ord("A") <= ord(var[k]) and ord(var[k]) <= ord("Z")) or (ord("a") <= ord(var[k]) and ord(var[k]) <= ord("z"))):
                var[k] = '@'
        if var[k] not in vowel and ((ord("A") <= ord(var[k]) and ord(var[k]) <= ord("Z")) or (ord("a") <= ord(var[k]) and ord(var[k]) <= ord("z"))):
                var[k] = first_word
        if var[k]==var[0]:
            var[k]=first_word

    for j in range(len(var)):
        final_word=final_word+var[j]

    return final_word

print(checker(var))