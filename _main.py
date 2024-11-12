from tkinter import Tk, ttk


root: Tk = Tk(screenName='Network GUI', baseName='Network GUI management')
frm = ttk.Frame(root, padding=200, height=500)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()
