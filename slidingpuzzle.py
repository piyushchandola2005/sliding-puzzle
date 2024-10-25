from tkinter import *
from random import *

root=Tk()
root.geometry('600x600')
root.configure(bg="grey")
global l1
def exit():
    root.destroy()
l1=["1","2","3","4","5","6","7","8"," "]
def win():
    if (b1["text"]=="1" and b2["text"]=="4"and b3["text"]=="7" and b4["text"]=="2" and b5["text"]=="5"
    and b6["text"]=="8" and b7["text"]=="3" and b8["text"]=="6"and b9["text"]==" "):
        b10=Button(root,height=2 ,width= 20 ,text="you won,click to exit",command=exit)
        b10.place(x=200,y=400)
        


def num_assign():
    assign=choice(l1)
    l1.remove(assign)
    return assign
def swap(button_1,button_2):
    temp=button_1["text"]
    button_1["text"]=button_2["text"]
    button_2["text"]=temp

def corner_tiles(clicked_button,move1,move2):
    if (move1["text"]==" " ):
            swap(clicked_button,move1)
    if (move2["text"]==" "):
            swap(move2,clicked_button)
    
def move(button_id):
    
    if button_id==1:
        corner_tiles(b1,b2,b4)

    if button_id==2:
        if (b1["text"]==" " ):
            swap(b1,b2)
        if (b3["text"]==" "):
            swap(b2,b3)
        if (b5["text"]==" "):
            swap(b2,b5)

    if button_id==3:
        corner_tiles(b3,b2,b6)
        
    if button_id==4:
        if (b1["text"]==" " ):
            swap(b1,b4)
        if (b7["text"]==" "):
            swap(b7,b4)
        if (b5["text"]==" "):
            swap(b4,b5)
    if button_id==5:
        if (b4["text"]==" " ):
            swap(b5,b4)
        if (b2["text"]==" "):
            swap(b2,b5)
        if (b6["text"]==" "):
            swap(b6,b5)
        if (b8["text"]==" "):
            swap(b5,b8)
    if button_id==6:
        if (b9["text"]==" " ):
            swap(b9,b6)
        if (b3["text"]==" "):
            swap(b6,b3)
        if (b5["text"]==" "):
            swap(b6,b5)
    if button_id==7:
        corner_tiles(b7,b8,b4)
    if button_id==8:
        if (b9["text"]==" " ):
            swap(b9,b8)
        if (b7["text"]==" "):
            swap(b7,b8)
        if (b5["text"]==" "):
            swap(b8,b5)
    if button_id==9:
        corner_tiles(b9,b8,b6)
    win()



b1=Button(root,text=num_assign(),height=5,width=10,activebackground="light green",bg="dark grey" ,command=lambda:move(1))
b1.place(x=100,y=100)

b2=Button(root,text=num_assign(),height=5,width=10,activebackground="light green",bg="dark grey",command=lambda:move(2))
b2.place(x=100,y=200)

b3=Button(root,text=num_assign(),height=5,width=10,activebackground="light green",bg="dark grey",command=lambda:move(3))
b3.place(x=100,y=300)

b4=Button(root,text=num_assign(),height=5,width=10,activebackground="light green",bg="dark grey",command=lambda:move(4))
b4.place(x=200,y=100)

b5=Button(root,text=num_assign(),height=5,width=10,activebackground="light green",bg="dark grey",command=lambda:move(5))
b5.place(x=200,y=200)

b6=Button(root,text=num_assign(),height=5,width=10,activebackground="light green",bg="dark grey",command=lambda:move(6))
b6.place(x=200,y=300)

b7=Button(root,text=num_assign(),height=5,width=10,activebackground="light green",bg="dark grey",command=lambda:move(7))
b7.place(x=300,y=100)

b8=Button(root,text=num_assign(),height=5,width=10,activebackground="light green",bg="dark grey",command=lambda:move(8))
b8.place(x=300,y=200)

b9=Button(root,text=num_assign(),height=5,width=10,activebackground="light green",bg="dark grey",command=lambda:move(9))
b9.place(x=300,y=300)



root.mainloop()