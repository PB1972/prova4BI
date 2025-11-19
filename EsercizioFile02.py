# Scrivi un programma che chieda all’utente di inserire una serie di parole separate da spazio e le
# scriva in un file, una parola per riga.

# parole = input("Inserisci una sequenza di 5 parole separate da uno spazio")
# lista_parole = parole.split()

# with open("parole.txt","a") as file:
#     for parola in lista_parole:
#         file.write(parola + "\n")

def scriviFile(nomeFile):
    with open(nomeFile,"a") as file:
        for parola in lista_parole:
            file.write(parola + "\n")

parole = input("Inserisci una sequenza di 5 parole separate da uno spazio")
lista_parole = parole.split()
mioFile = "parole.txt"
scriviFile(mioFile)