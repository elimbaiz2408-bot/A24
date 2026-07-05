import tkinter as tk
start=tk.Tk()
start.title("калькулятор")
start.geometry("450x300")
def note():
    pass
def clear():
    панель.config(state="normal")
    панель.delete(len(панель.get())-1,tk.END)
    панель.config(state="readonly")
def стереть_ошибку():
    if not k in список_кнопок:
        панель.config(state="normal")
        панель.delete(0,tk.END)
        панель.config(state="readonly")
    elif k in список_кнопок:
        pass
def равно():
    try:
        панель.config(state="normal")
        выражение=панель.get().replace("×","*").replace("÷","/")
        ответ=eval(выражение)
        панель.delete(0,tk.END)
        панель.insert(tk.END,str(ответ))
        панель.config(state="readonly")
    except ZeroDivisionError:
        панель.config(state="normal")
        панель.delete(0,tk.END)
        панель.insert(tk.END,"нельзя делить на 0")
        панель.config(state="readonly")
        панель.after(2000,стереть_ошибку) 
    except Exception:
        панель.config(state="normal")
        панель.delete(0,tk.END)
        панель.insert(tk.END,"ошибка")
        панель.config(state="readonly")
        панель.after(2000,стереть_ошибку)
def hh(option):
    панель.config(state="normal")
    панель.insert(tk.END,option)
    панель.config(state="readonly")
список_кнопок={
    ("7",1,0),("8",1,1),("9",1,2),("DEL",1,3),
    ("4",2,0),("5",2,1),("6",2,2),("÷",4,3),
    ("1",3,2),("2",3,1),("3",3,0),("×",5,3),
    ("0",4,0),(".",4,1),("=",4,2),("-",2,3),
    ("+",3,3)
}
панель=tk.Entry(start,width=50,state="readonly");панель.grid(row=0,column=0,columnspan=9999)
for k,ro,colu in список_кнопок:
    if k == "DEL":
        command=clear
    elif k == "=":
        command=равно
    else:
        панель.config(state="readonly")
        command=lambda x=k: hh(x)

    кнопки=tk.Button(start,text=k,command=command,width=7,height=5,bd=3);кнопки.grid(row=ro,column=colu);
start.mainloop()