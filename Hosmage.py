from tkinter import *
from tkinter import ttk
from hsbdalgo import get_priority
from tkinter import messagebox




patient_list = []

dicty = {}

app = Tk()

    

def click():
    try:
        name = str(entry1.get())

        age = int(entry2.get())

        category = str(entry3.get())

        condition = entry4.get()
        if condition == "True":
            condition = True
        else:
            condition = False

        global dicty
        global patient_list 

        dicty["NAME"] = name
        dicty["CATEGORY"] = category
        dicty["AGE"] = age
        dicty["SELDOM_SICK"] = condition
        patient_list.append(dicty)
        dicty = dict()
    except ValueError:
            messagebox.showerror("Missing Details","Error: AGE cannot be EMPTY and SHOULD contain ONLY numbers!")
       
    
    
def empty(patient_list):
     if patient_list == []:
          messagebox.showerror("Empty Patients","Error: Admission List is empty. You need to admit AT LEAST ONE patient first.")        

        
        
def get_list():
    empty(patient_list)
    print(patient_list)

    
        
def sort():
    empty(patient_list)
    window = Tk.winfo_toplevel(app)
    sorted_patient_list = sorted(patient_list, key=get_priority, reverse=True)
    print(sorted_patient_list)
app.geometry("500x450")



"""""PATIENT NAME"""
label1 = Label(app,text="Patient Name")
label1.pack(padx=5,pady=5 )

entry1 = Entry(master=app)
entry1.pack(padx=10,pady=10)

""""PATIENT AGE"""
label2 = Label(app,text="Patient Age")
label2.pack(padx=5,pady=5)

entry2 = Entry(master=app)
entry2.pack(padx=10,pady=10)


"""""PATIENT CATEGORY"""
cat = ["A","B","C"]

label3 = Label(app,text="Patient Category")
label3.pack(padx=5,pady=5 )

entry3 = ttk.Combobox(app,values=cat,width=10)
entry3.pack(padx=10,pady=10)
entry3.current(0)

"""""PATIENT SELDOM_SICK"""
seldom = [True,False]

label4 = Label(app,text="Patient Seldomly falls sick")
label4.pack(padx=5,pady=5)

entry4 = ttk.Combobox(app,values=seldom,width=10)
entry4.pack(padx=10,pady=10)
entry4.current(0)


admit = Button(app,text='ADMIT',background="purple",activebackground="black",activeforeground="white",command=click).pack(padx=10,pady=10)

get_patients = Button(app,text="list",background="blue",command=get_list).pack(padx=10,pady=10)

assign = Button(app,text="ASSIGN BED",background="blue",command=sort).pack(padx=10,pady=10)

app.mainloop()
