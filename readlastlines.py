n = int(input("enter no of lines:"))
f =open("sumeet.txt","r")

for line in (f.readlines()[-n]):
    print(line, end="")
f.close()