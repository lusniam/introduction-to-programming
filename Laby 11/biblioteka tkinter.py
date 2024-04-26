from tkinter import *
from tkinter.ttk import Combobox
from tkinter.messagebox import showinfo

def komunikat():
    showinfo("Piwo","Piwo moment")

root=Tk()
root.title("Piwo")

swidth = root.winfo_screenwidth()
sheight = root.winfo_screenheight()
root.geometry(f'1000x600+{int((swidth-1000)/2)}+{int((sheight-600)/2)}')

#piwo=Button(root,text="Piwo?",command=komunikat)
#piwo.pack(anchor=N,ipadx=5,ipady=5,expand=True)

message=Label(root,text="Podaj numer telefonu:")
message.pack(ipadx=5,ipady=5,)

telefony=[]
for i in range(1000000):
    x="503"
    while(len(x+str(i))<9):
        x+='0'
    x+=str(i)
    telefony.append(x)

wartosc=StringVar()
#tel=Scale(root,from_=0,to=999999999,orient='horizontal',variable=wartosc,sliderlength=5)
#tel.pack(fill=X)

tel2=Combobox(root,textvariable=wartosc)
tel2['values']=telefony
tel2.pack(padx=5,pady=5)

tel2.bind('<<ComboboxSelected>>',showinfo(title='Nie no kurwa', message="Jakis jebniety gosciu jestes"))

root.mainloop()