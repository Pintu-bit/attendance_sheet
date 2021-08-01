from tkinter import * 
import tkinter as tk
import xlsxwriter as xl
import pandas as pd
import os

pg_root=Tk();
pg_root.geometry("744x623")
pg_root.title("My first gui")

def Take_input():
    if os.path.exists('E:\Python Software\Example.xlsx'):
        os.remove("Example.xlsx")
        
    workbook=xl.Workbook('Example.xlsx')
    worksheet=workbook.add_worksheet()
    row=0
    col=0
    lst=[]
    INPUT = inputtxt.get("1.0", "end-1c")
    print(INPUT)
    lst=INPUT.split(" ")
    print(lst[0])
    for item in lst:
        worksheet.write(row,col,item)
        row+=1
    workbook.close()    
    #print(lst)
    
    #file=open("temp.txt","a")
    #file.writelines(INPUT)
    
   # if(file!=None):
        #inpt1.insert(END,"Successfull")
        #inpt1.pack()
        
    #file.close()
   
    
def view_data():
    path='E:\Python Software\Example.xlsx'
    isExst=os.path.exists(path)
    if isExst:        
        df=pd.read_excel("Example.xlsx")
        inpt1.insert(END,df)
        inpt1.pack()
    else:
        inpt1.insert(END,"There is no any containt availabel at now!")
        inpt1.pack()
         
   

title_lebel=Label(text="PLEASE INPUT THE DATA ",font="comicsense 14 bold")
inputtxt = Text(pg_root,height = 5,width = 80,bg = "light yellow",fg="black",borderwidth=3,relief=SUNKEN)
inpt1=Text(pg_root,height=7,width=50,bg="green",fg="white",borderwidth=3,relief=SUNKEN,padx=0)

b1 = Button(pg_root,text="Submit",width = 30,bg = "light cyan",
            command = lambda:Take_input())
b2 = Button(pg_root, text = "Exit",width =30,bg = "light cyan",
            command = pg_root.destroy) 

#Output = Text(pg_root, height = 5,width =50,bg = "lightcyan")
b3=Button(pg_root,text="Export the excel data Sheet",width=50,bg="lightcyan",command=lambda:view_data())


title_lebel.pack(pady=20)
inputtxt.pack(pady=70)
b1.pack(padx=180,pady=30)
b2.pack(padx=100)
b3.pack(pady=30)


pg_root.mainloop()



