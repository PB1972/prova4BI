# Scrivi un programma che crei un file di testo chiamato “prova.txt” e ci scriva dentro la frase “Questo
# è un file di prova.”.

with open("prova.txt",'a') as file:
    file.write("questo è un file di prova\n")

with open("prova.txt",'r') as file:
    contenuto = file.read()
    print(contenuto)

    
