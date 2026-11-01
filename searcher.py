import tkinter as tk

root = tk.Tk()

root.title("Searcher")
root.attributes('-fullscreen', True)

x = [
    "Terry A. Davis is the greatest programmer ever.",
    "Tesla is a genius.",
    "I'm a genius too.",
    "Dawid Piotrowski is a young chess player.",
    "Potency"
]


def search():
    ent_txt = ent.get()
    for i in x:
         if ent_txt in i:
            txt.insert(tk.END, i)
        
text = tk.Label(root, text="Enter a phrase")
text.pack(pady=30)

ent = tk.Entry(root)
ent.pack()

btn = tk.Button(root, text="OK", command=search)
btn.pack()

txt = tk.Text(root)
txt.pack(pady=20)

root.mainloop()