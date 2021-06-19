# list of letters
letters = ['a', 'b', 'd', 'e', 'i', 'j', 'o']


# function that filters vowels
def filter_vowels(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']

    return True if letter in vowels else False


filtered_vowels = filter(filter_vowels, letters)

print('The filtered vowels are:')
for vowel in filtered_vowels:
    print(vowel)
