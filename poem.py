"""1. Write a program to read the text from a given file ‘poems.txt’ and find out whether it
contains the word ‘twinkle’."""


with open("poem.txt" , "r")as f :
   read_file =  f.read()

if "Twinkle" in read_file:
   print("yes")

    

