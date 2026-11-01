# Repeat program 4 for a list of such words to be censored.
students = ["uzair" , "mehatab" , "uzair", "muddassir"]
with open("file.txt" , "r")as f:
    reads = f.read()
    print(reads)

for student in students:
    reads = reads.replace(student , "*****")
print(reads)
    


with open("file.txt" , "w") as f :
    f.write(reads)
# with open("file1.txt" , "w") as f :
#     f.read()