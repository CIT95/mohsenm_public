# learnTogether Week 8

# https://www.w3resource.com/python-exercises/string/
# 2. Write a Python program to count the number of characters (character frequency) in a string.
def character_frequency(str):
    count = {}
    for character in str:
        count.setdefault(character, 0)
        count[character] = count[character] + 1
    
    return count

print('\nCounting the number of characters (character frequency) in a string.')
str = 'google.com'
print('Sample String :', str)
print('Expected Result :', character_frequency(str))


# https://www.w3resource.com/python-exercises/string/
# 3. Write a Python program to get a string made of the first 2 and the last 2 chars from a given 
#   a string. If the string length is less than 2, return instead of the empty string.
def string_first2_last2(str):
    if len(str) < 2:
        return ''
    else:
        return str[:2] + str[-2:]

print('\nMaking of the first 2 and the last 2 chars from a given string.')
str = 'w3resource'
print('Sample String :', str)
print('Expected Result :', string_first2_last2(str))


# https://www.w3resource.com/python-exercises/string/
# 5. Write a Python program to get a single string from two given strings, separated by a space and swap 
#   the first two characters of each string.
def string_mix_swap(str1, str2):
    return str2[:2] + str1[2:] + ' ' + str1[:2] + str2[2:]

print('\nGetting a string from two given strings, separated by a space, and swap the first two characters of each string.')
str1 = 'abc'
str2 = 'xyz'
print('Sample String :', str1, ',', str2)
print('Expected Result :', string_mix_swap(str1, str2))


# https://www.w3resource.com/python-exercises/string/
# 8. Write a Python function that takes a list of words and returns the longest word and 
#   the length of the longest one.
def longest_word_in_list(list):
    longest_word = ''
    for word in list:
        if len(word) > len(longest_word):
            longest_word = word
    
    return longest_word

print('\nLongest word and its length from the list')
list = ['congratulation', 'subtitution', 'engineering', 'definition', 'employment', 'appreciate']
print('Sample String :', list)
longest_word = longest_word_in_list(list)
print('Longest word :', longest_word)
print('Length of the longest word:', len(longest_word))


# https://www.w3resource.com/python-exercises/string/
# 12. Write a Python program to count the occurrences of each word in a given sentence.
def occurrences_words_in_sentences(sentence):
    list = sentence.split()

    count = {}
    for word in list:
        count.setdefault(word, 0)
        count[word] = count[word] + 1
    
    return count

print('\nCount the occurrences of each word in a given sentence.')
sentence = 'Python can be easy to pick up whether you are a first time programmer or you are experienced with other languages.'
print('Sentence :', sentence)
print('Occurrences of each word :', occurrences_words_in_sentences(sentence))


# https://www.w3resource.com/python-exercises/string/
# 20. Write a Python function to reverses a string if it's length is a multiple of 4.
def reverse_string(str):
    if len(str) % 4 == 0:
        return str[::-1]
    
    return str

print('\nReverses a string if it is length is a multiple of 4.')
str = 'Python'
print('Sample String :', str)
print('Expected Result :', reverse_string(str))
str = 'Exercise'
print('Sample String :', str)
print('Expected Result :', reverse_string(str))


# https://www.w3resource.com/python-exercises/string/
# 57.Write a Python program to remove spaces from a given string.
def remove_spaces_string(str):
    return str.replace(' ', '')

print('\nRemove spaces from a given string.')
str = 'w 3 res ou r ce'
print('Sample String :', str)
print('Expected Result :', remove_spaces_string(str))


# https://www.w3resource.com/python-exercises/string/
# 73. Write a Python program to count Uppercase, Lowercase, special character 
#   and numeric values in a given string.
def cout_characters(str):
    list = [0, 0, 0, 0]
    for char in str:
        if char >= 'A' and char <= 'Z':
            list[0] += 1
        elif char >= 'a' and char <= 'z':
            list[1] += 1
        elif char >= '0' and char <= '9':
            list[2] += 1
        else: 
            list[3] += 1
    
    return list

print('\nCount Uppercase, Lowercase, special character and numeric values in a given string.')
str = 'https://WWW.W3Resource.Com/Python-Exercises/String/'
list = cout_characters(str)
print('Sample String :', str)
print('Uppercase characters :', list[0])
print('Lowercase characters :', list[1])
print('Numeric value :', list[2])
print('Special characters :', list[3])


# https://pynative.com/python-string-exercise/
# Exercise 1: Given a string of odd length greater than 7, return a new string 
# made of the middle three characters of a given String.
def get_middle_three_chars(str):
    mid = len(str)//2

    return str[mid-1:mid+2]

print('\nNew string made of the middle three characters of a given String.')
str = 'PythonExercisesHome'
print('Sample String :', str)
print('Expected Result :', get_middle_three_chars(str))


# https://pynative.com/python-string-exercise/
# Exercise 4: Arrange string characters such that lowercase letters should come first.
def arrange_string_first_lowercase(str):
    for char in str:
        if char.isupper():
            str = str.replace(char, '') + char
    
    return str


print('\nArrange string characters such that lowercase letters should come first.')
str = 'PythonExercisesHome'
print('Sample String :', str)
print('Expected Result :', arrange_string_first_lowercase(str))

# https://pynative.com/python-string-exercise/
# Exercise 9: Given a string, return the sum and average of the digits that appear 
# in the string, ignoring all other characters.
def compute_sum_average(str):
    list = []
    digit = ''
    for char in str:
        if char.isdigit():
            digit += char
        if digit != '' and char == ' ':
            list.append(int(digit))
            digit = ''
    if digit != '':
        list.append(int(digit))

    return sum(list), sum(list)/len(list)

print('\nCompute sum and average of the digits in the string.')
str = 'English = 78 Science = 83 Math = 68 History = 65'
sum, average = compute_sum_average(str)
print('Sample String :', str)
print('Expected Result :  Sum is', sum, ', Average is', average)


# https://pynative.com/python-string-exercise/
# Exercise 11: Reverse a given string.
def reverse_string(str):
    reverse = ''
    for char in str:
        reverse = char + reverse

    return reverse

print('\nReverse a given string.')
str = 'Python'
print('Sample String :', str)
print('Expected Result :', reverse_string(str))


# https://pynative.com/python-string-exercise/
# Exercise 12: Find the last position of a substring "Emma" in a given string.
def find_last_position_substring(str):
    last_position = str.rfind('Emma')

    return last_position

print('\nFind the last position of a substring "Emma" in a given string.')
str = 'Emma is a data scientist who knows Python. Emma works at google.'
print('Sample String :', str)
print('Expected Result :', find_last_position_substring(str))


# https://pynative.com/python-string-exercise/
# Exercise 14: Remove empty strings from a list of strings.
def remove_empty_string_list(str_list):
    str_list[:] = [x for x in str_list if x]

    return str_list

print('\nRemove empty strings from a list of strings.')
str_list = ['Apple', 'Peach', '', 'Orange', 'Benana', '', 'Cherry', '']
print('Sample String :', str_list)
print('Expected Result :', remove_empty_string_list(str_list))


# https://pynative.com/python-string-exercise/
# Exercise 16: Removal all the characters other than integers from a string.
def removal_except_digit(str):
    digit = ''
    for char in str:
        if char.isdigit():
            digit += char

    return digit

print('\nRemoval all the characters other than integers from a string.')
str = 'I am 25 years and 10 months old'
print('Sample String :', str)
print('Expected Result :', removal_except_digit(str))


# https://pynative.com/python-string-exercise/
# Exercise 17: Find words with both alphabets and numbers.
def find_word_both_alphabets_numbers(str):
    list = []
    for word in str.split(' '):
        if word.isalnum() and not word.isalpha() and not word.isdigit():
            list.append(word)

    return list

print('\nFind words with both alphabets and numbers.')
str = 'his car number is ka99ap9999 and bike that met with accident is kl8ar888'
print('Sample String :', str)
print('Expected Result :', find_word_both_alphabets_numbers(str))
