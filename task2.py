#!python3

"""
Create a variable that contains an empyy list.
Ask a user to enter 5 words.  Add the words into the list.
Print the list
inputs:
string 
string
string
string
string

outputs:
string

example:
Enter a word: apple
Enter a word: worm
Enter a word: dollar
Enter a word: shingle
Enter a word: virus

['apple', 'worm', 'dollar', 'shingle', 'virus']
"""
i = 0 
words = []

while i != 5: 
    i+=1
    word = str(input("Enter a word : "))
    words.append(word)
else :
    print(words)



