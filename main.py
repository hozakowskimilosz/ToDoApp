import tkinter as tk

root = tk.Tk()
root.title("To-Do List")

root.config(bg="#333333")

# Stworzenie kontenera do wyświetlania czynności
listbox = tk.Listbox(root, width=50, bg="#cccccc", fg="#333333", font=("Arial", 12))
listbox.pack(pady=10, padx=10)

# Ładowanie czynności z pliku
try:
    with open("todos.txt", "r") as f:
        for line in f:
            item = line.strip()
            if item != "":
                listbox.insert(tk.END, item)
except:
    pass

# Dodawanie nowej czynności do kontenera
def add_item():
    item = entry.get()
    if item != "":
        listbox.insert(tk.END, item)
        entry.delete(0, tk.END)
        save_items()

# Tworzenie przycisku i pola tekstowego do wprowadzania czynności
entry = tk.Entry(root, width=30, bg="#ffffff", fg="#333333", font=("Arial", 12))
entry.pack(pady=5)
button = tk.Button(root, text="Dodaj czynność", command=add_item, bg="#90ee90", fg="#333333", font=("Arial", 12, "bold"))
button.pack(pady=5)

# Usuwanie nowej czynności do kontenera
def remove_item():
    index = listbox.curselection()
    if index:
        listbox.delete(index)
        save_items()

# Tworzenie przycisku do usuwania czynności
button = tk.Button(root, text="Usuń czynność", command=remove_item, bg="#ffcccb", fg="#333333", font=("Arial", 12, "bold"))
button.pack()

# Zapisywanie czynności do pliku
def save_items():
    with open("todos.txt", "w") as f:
        for i in range(listbox.size()):
            item = listbox.get(i)
            f.write(item + "\n")

root.geometry("400x400")

root.mainloop()
