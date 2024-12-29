# r+ read file and write new lines
# w+ write file and read new lines
with open("./texs.txt", "w+") as file:
    for line in file:
        print(line)
    file.write("nuevas cosas en este archivo\n")
    file.write("otra linea\n")
    file.write(" mas linea\n")
