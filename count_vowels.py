vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Enter word: ")
count_vowels = 0
for letter in word:
    if letter in vowels:
        count_vowels += 1
print(count_vowels)

