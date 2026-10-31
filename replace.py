"""4. A file contains a word “Donkey” multiple times. You need to write a program which
replaces this word with ##### by updating the same file."""


file = open("word.txt" , "r")
word = file.read()
a = word.replace("donkey" , "*******")
with open("word.txt" , "w")as f:
    f.write(a) 



