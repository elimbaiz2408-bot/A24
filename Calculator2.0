import customtkinter as ctk
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
root=ctk.CTk()
root.title("calculatro")
root.geometry("300x400")
root.resizable(False,False)
entry=ctk.CTkEntry(root,height=60,font=("Arial",28),justify="right",state="readonly")
entry.pack(fill="x",padx=10,pady=10)
def press(value):
    entry.configure(state="normal")
    entry.insert("end",value)
    entry.configure(state="readonly")
def clear():
    entry.configure(state="normal")
    entry.delete(0,"end")
    entry.configure(state="readonly")
def equal():
    try:
        entry.configure(state="normal")
        op=eval(entry.get())
        entry.delete(0,"end")
        entry.insert(0,str(op))
        entry.configure(state="readonly")
    except ZeroDivisionError:
        entry.delete(0,"end")
        entry.insert(0,"ZeroDivisionError")
    except SyntaxError:
        entry.delete(0,"end")
        entry.insert(0,"SyntaxError")
    except TypeError:
        entry.delete(0,"end")
        entry.insert(0,"TypeError")
button=[
    ["7","8","9","/"],
    ["4","5","6","*"],
    ["1","2","3","-"],
    ["C","0","=","+"]
]
frame=ctk.CTkFrame(root)
frame.pack(expand=True,fill="both",padx=10,pady=10)
for r,row in enumerate(button):
    frame.grid_rowconfigure(r,weight=1)
for c in range(4):
    frame.grid_columnconfigure(c,weight=1)
for r,row in enumerate(button):
    for c,text in enumerate(row):
        if text == "C":
            cmd=clear
        elif text == "=":
            entry.configure(state="normal")
            cmd=equal
            entry.configure(state="readonly")
        else:
            cmd=lambda t=text:press(t)
        btn=ctk.CTkButton(frame,text=text,command=cmd,height=60,corner_radius=20,font=("Arial",22))
        btn.grid(row=r,column=c,padx=5,pady=5,sticky="nsew")

root.mainloop()
