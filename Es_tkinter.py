import tkinter as tk

# Crea la finestra principale
root = tk.Tk()

# Imposta il titolo della finestra
root.title("La mia prima finestra Tkinter")

label = tk.Label(root, text="Ciao, mondo!")
button = tk.Button(root, text="Cliccami")

label.pack()
button.pack()

# Avvia il ciclo degli eventi
root.mainloop()