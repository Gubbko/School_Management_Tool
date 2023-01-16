import tkinter as tk


root = tk.Tk()
root.title("Database")

tb_manu = tk.Entry(root)
tb_manu.grid(row=0, column=1)
tb_modl = tk.Entry(root)
tb_modl.grid(row=1, column=0)
tb_type = tk.Entry(root)
tb_type.grid(row=1, column=1)
tb_sern = tk.Entry(root)
tb_sern.grid(row=2, column=0)
tb_inve = tk.Entry(root)
tb_inve.grid(row=2, column=1)
tb_clas = tk.Entry(root)
tb_clas.grid(row=3, column=0)

root.mainloop()

