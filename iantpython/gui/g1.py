import tkinter as tk
window=tk.Tk()
a=tk.Label(
    text="WELCOME",
    foreground="white",
    background="black",
    height=2
)
a.pack(fill=tk.X)
# b=tk.Label(
#     text="submit",
#     foreground="white",
#     background="black",
#     # height=2,
#     # width=5
# )
# b.pack(fill=tk.X,side=tk.RIGHT)
# l=tk.Label(text="name")
# e=tk.Entry()
# l.pack()
# e.pack()
tb=tk.Text(
    height=30,
    width=40
)
tb.pack()
window.mainloop()

