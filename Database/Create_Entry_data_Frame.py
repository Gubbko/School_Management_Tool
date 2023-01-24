from tkinter import Label, Entry

"""
def Create_frame(root, x = 0, y = 0):
    frame = Frame(root).grid(row=x,column=y)
    List_for_Lables_and_Entry = [   "ID",
                                    "E-v.",      
                                    "Bilansikont",
                                    "Klass",
                                    "Vara nr.",
                                    "Alamnr.",
                                    "Inv.nr.",
                                    "Vara kirjeldus 1",
                                    "Kapit.Kp",
                                    "Soetusmaksumus",
                                    "Kulum perioodini",
                                    "Jääkv.per",
                                    "Aadress",
                                    "Aadressi text",
                                    "Ruum",
                                    "Kogus",
                                    "Ühik",
                                    "Töötaja",
                                    "Eesnimi",
                                    "Perenimi",
                                    "L. 2",
                                    "Vastutav isik",
                                    "Inventuuri kp.seisuga",
                                    "Inv.märkus"]
    return frame, List_for_Lables_and_Entry
"""

def Create_Labes(List_for_Lables_and_Entry, frame):
    List_for_Lables = []
    for index, lable in enumerate(List_for_Lables_and_Entry):
        new_label = Label(frame, text=lable, width=17).grid(row=index+1, column=1, pady=1)
        List_for_Lables.append(new_label)

def Create_Entry(List_for_Lables_and_Entry, frame):
    List_for_Entrys = []
    for index, _ in enumerate(List_for_Lables_and_Entry):
        List_for_Entrys.append(Entry(frame, width=17))
        List_for_Entrys[-1].grid(row=index+1, column=2)
    return List_for_Entrys

def loop(root):
    root.mainloop()

#Enter_data = Add_object_To_DB_Frame(1, 0)
#Enter_data.Create_Labes()
#Enter_data.Create_Entry()
#Enter_data.loop()