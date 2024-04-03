name = input("")
vowels = ['a', 'e', 'i', 'o', 'u']
length = len(name)
name = name.lower()
vowel_count = 0
consonant_count = 0
def fun(name):
    global vowel_count,consonant_count
    for i in range(length):
        if name[i] in vowels:
           vowel_count += 1
        else:
           consonant_count += 1
    result = {"vowels": vowel_count, "consonants": consonant_count}
    return result
print(fun(name))