from tkinter import *
from tkcalendar import *

def grab_date():
    my_label.config(text=cal.get_date())

def on_select(v):
    print(v)

root = Tk()
cal = Calendar(root, selectmode = "day", year=2023, month = 5, day = 22)
cal.pack(pady = 20, fill="both", expand=True)
cal.bind('<<CalendarSelected>>', on_select)

my_btn = Button(root, text="Get Date", command=lambda:grab_date())
my_btn.pack(pady=20)

my_label = Label(root, text="")
my_label.pack(pady=20)

start = DateEntry(root, width=12, background='darkblue',
                  foreground='white', borderwidth=2)
start.pack(padx=10, pady=10)
end = DateEntry(root, width=12, background='darkblue',
                foreground='white', borderwidth=2)

end.pack(padx=10, pady=10)



root.mainloop()
