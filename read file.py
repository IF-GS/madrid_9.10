file_name = "x-file.txt"
fd = open(file_name) #read is implicit
print("here are the contentd of the file")
print(fd.read())
fd.close()

#other way
for line in fd:
    print(line, end="")

fd = open(file_name)
print("here is thr 3 letter words")
for line in fd:
    words = line.split()
    for words in words:
        if len(word) == 3
            print(word)

fd.close()