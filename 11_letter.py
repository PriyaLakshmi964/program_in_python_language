letter = '''dear <|Name|>
you are selected
 Date : <|Date|>
'''

name = input("enter your name ")
date = input("enter date ")
letter = letter.replace("<|Name|>" , name)
letter = letter.replace("<|Date|>" , date)
print(letter)