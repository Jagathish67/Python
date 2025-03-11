def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = sum(1 for char in string if char in vowels)
    return count

user_input = input("Enter a string: ")

vowel_count = count_vowels(user_input)
print(f" The number of vowels in the given string is: {vowel_count}")



