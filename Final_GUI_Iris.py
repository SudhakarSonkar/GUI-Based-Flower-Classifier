# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 23:05:14 2021

@author: Sudhakar
"""


from tkinter import *
from sklearn.datasets import load_iris
root=Tk()
root.geometry("400x600")
root.configure(background="light green")

Label(root,text="GUI BASED FLOWER CLASSIFIER",
      font=('Helvetica',15,'bold'),bg="light green",
      relief="solid").pack()
Label(root,text="Application Version 1.1",relief="solid",
      bg="light green").pack(side=BOTTOM)

Label(root,text="=================================================",bg="light green").pack(fill='both')
#----------------------------------------------
Label(root,text="Sepal length in Cm",font=('Helvetica',10,'bold'),bg="light green",
      relief="solid",width=18).place(x=40,y=80)
Label(root,text="Sepal width in Cm",font=('Helvetica',10,'bold'),bg="light green",
      relief="solid",width=18).place(x=40,y=130)
Label(root,text="Petal length in Cm",font=('Helvetica',10,'bold'),bg="light green",
      relief="solid",width=18).place(x=40,y=180)
Label(root,text="Petal width in Cm",font=('Helvetica',10,'bold'),bg="light green",
      relief="solid",width=18).place(x=40,y=230)

Label(root,text="Predicted Result is",font=('Helvetica',10,'bold'),bg="light green",
      relief="solid",width=18).place(x=40,y=320)

#--------------------------------------------------------------------------------------
sl=StringVar()
sw=StringVar()
pl=StringVar()
pw=StringVar()
Entry(root,text=sl,width=25).place(x=200,y=80)
Entry(root,text=sw,width=25).place(x=200,y=130)
Entry(root,text=pl,width=25).place(x=200,y=180)
Entry(root,text=pw,width=25).place(x=200,y=230)

Label(root,text="Information",font=('Helvetica',10,'bold'),
      bg="light green",relief="solid",width=18).place(x=40,y=279)

def info():
    n=Tk()
    n.geometry("300x300")
    n.configure(background="light green")
    
    n.resizable(0,0)
    n.mainloop()


Button(root,text="info",width=18,command=info).place(x=200,y=279)


def model():
    data=load_iris()
    x=data.data
    y=data.target
    #data training
    from sklearn.neighbors import KNeighborsClassifier
    model=KNeighborsClassifier(n_neighbors=3, metric='euclidean')
    model.fit(x,y)
    x_test=[float(sl.get()),float(sw.get()),float(pl.get()),float(pw.get())]
    y_pred=model.predict([x_test,])

    Label(root,text=str(data.target_names[y_pred[0]]),font=('Helvetica',10,'bold'),bg="light green",
      relief="solid",width=18).place(x=200,y=320)

Button(root,text="Prediction",width=18,command=model).place(x=40,y=400)

Button(root,text="Termination",width=18,command=root.destroy).place(x=200,y=400)

Button(root,text="Clear Prediction",width=18,command=clear).place(x=100,y=450)

def clear():
    Label(root,text=" "*30,font=('Helvetica',10,'bold'),bg="light green",
      relief="solid",width=18).place(x=200,y=320)

root.resizable(0,0)
root.mainloop()
