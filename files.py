file_name = "x-file.txt"
fd = open(file_name, "a") # a for apenddi w for write r for read
while True:
    line = input("Enter a line (or just press enter to quit): ")
    if line:
        fd.write(line + "\n", "")
    else
        break



