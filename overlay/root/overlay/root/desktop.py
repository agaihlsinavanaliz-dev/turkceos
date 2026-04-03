import tkinter as tk

root = tk.Tk()
root.title("TürkçeOS")
root.attributes("-fullscreen", True)

def ac_not():
    w = tk.Toplevel(root)
    w.title("Not")
    tk.Text(w).pack()

tk.Button(root, text="Not Aç", command=ac_not).pack(pady=20)

root.mainloop()
