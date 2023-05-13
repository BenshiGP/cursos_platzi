with open("./text.txt", "w+") as file:
    for line in file:
        print(line)
    file.write("Nuevas cosas en este archivo txt\n")    
    file.write("otra linea\n")    
    file.write("Nuevas cosas \n")    