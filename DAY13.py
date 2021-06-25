#DAY13
# 1. Write a Python program for all the cases which can check a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).

print("check a string contains only a certain set of characters") 
import re
def is_allowed_specific_char(string):
    charRe = re.compile(r'[^a-zA-Z0-9.]')
    string = charRe.search(string)
    return not bool(string)

print(is_allowed_specific_char("Karthuiknr2021")) 
print(is_allowed_specific_char("*&%@#!}{"))

#***************************************************************************
# 2. Write a Python program that matches a word containing 'ab'.
print(" ")
print("program that matches a word containing 'ab'")
def text_match(text):
        patterns = '\w*ab.\w*'
        if re.search(patterns,  text):
                return ('Found a match!')
        else:
                return('Not matched!')

print(text_match("abdul"))
print(text_match("bala"))

#*******************************************************************************
# 3. Write a Python program to check for a number at the end of a word/sentence
print(" ")
print("program to check for a number at the end of a word/sentence")
def end_num(string):
    text = re.compile(r".*[0-9]$")
    if text.match(string):
        return True
    else:
        return False

print(end_num('abcdef'))
print(end_num('abcdef6'))

#***************************************************************************
# 4. Write a Python program to search the numbers (0-9) of length between 1 to 3 in a given string

print(" ")
print("program to search the numbers (0-9) of length between 1 to 3 in a given string")
results = re.finditer(r"([0-9]{1,3})", "Exercises number 1, 12, 13, and 345 are important")
print("Number of length 1 to 3")
for n in results:
     print(n.group(0))

#***********************************************************************************
# 5. Write a Python program to match a string that contains only uppercase letters
def text_match(text):
        patterns = '^[\w*A-Z.*\w]*$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("The quick brown fox jumps over the lazy dog."))
print(text_match("KINGKOHLI"))




















