from tkinter import *
from random import *

root=Tk()
root.geometry('600x600')
root.configure(bg="#F1D3B2")
global l1
#exit function
def exit():
    root.destroy()
l1=["1","2","3","4","5","6","7","8"," "]

#win function
def win():
    if (b1["text"]=="1" and b2["text"]=="4"and b3["text"]=="7" and b4["text"]=="2" and b5["text"]=="5"
    and b6["text"]=="8" and b7["text"]=="3" and b8["text"]=="6"and b9["text"]==" "):
        b10=Button(root,height=2 ,width= 20 ,text="you won,click to exit",command=exit)
        b10.place(x=200,y=400)
        

#will assign number to button
def num_assign():
    assign=choice(l1)
    l1.remove(assign)
    return assign
#will swap the buttons
def swap(button_1,button_2):
    temp=button_1["text"]
    button_1["text"]=button_2["text"]
    button_2["text"]=temp

#movement for corner tiles
def corner_tiles(clicked_button,move1,move2):
    if (move1["text"]==" " ):
            swap(move1,clicked_button)
    if (move2["text"]==" "):
            swap(move2,clicked_button)
#movement for middle tiles
def middle_tiles(clicked_button,move1,move2,move3):
    if (move1["text"]==" " ):
            swap(move1,clicked_button)
    if (move2["text"]==" "):
            swap(move2,clicked_button)
    if (move3["text"]==" "):
            swap(move3,clicked_button)
#movement for center tiles
def center_tiles(clicked_button,move1,move2,move3,move4):
    if (move1["text"]==" " ):
            swap(clicked_button,move1)
    if (move2["text"]==" "):
            swap(clicked_button,move2)
    if (move3["text"]==" "):
            swap(clicked_button,move3)
    if (move4["text"]==" "):
            swap(clicked_button,move4)

#main movement function
def move(button_id):
    
    if button_id==1:
        corner_tiles(b1,b2,b4)

    if button_id==2:
        middle_tiles(b2,b1,b3,b5)
    if button_id==3:
        corner_tiles(b3,b2,b6)
        
    if button_id==4:
        middle_tiles(b4,b1,b7,b5)
    if button_id==5:
       center_tiles(b5,b2,b4,b6,b8)
    if button_id==6:
        middle_tiles(b6,b3,b9,b5)
    if button_id==7:
        corner_tiles(b7,b8,b4)
    if button_id==8:
         middle_tiles(b8,b7,b9,b5)
    if button_id==9:
        corner_tiles(b9,b8,b6)
    win()


b1=Button(root,text=num_assign(),height=5,width=10,fg="white",font=('times 10 bold'),activebackground="#A43820",bg="#46211A" ,command=lambda:move(1))
b1.place(x=100,y=100)
img_label= Label(image=click_btn)
b2=Button(root,text=num_assign(),height=5,width=10,fg="white",font=('times 10 bold'),activebackground="#A43820",bg="#46211A",command=lambda:move(2))
b2.place(x=100,y=200)

b3=Button(root,text=num_assign(),height=5,width=10,fg="white",font=('times 10 bold'),activebackground="#A43820",bg="#46211A",command=lambda:move(3))
b3.place(x=100,y=300)

b4=Button(root,text=num_assign(),height=5,width=10,fg="white",font=('times 10 bold'),activebackground="#A43820",bg="#46211A",command=lambda:move(4))
b4.place(x=200,y=100)

b5=Button(root,text=num_assign(),height=5,width=10,fg="white",font=('times 10 bold'),activebackground="#A43820",bg="#46211A",command=lambda:move(5))
b5.place(x=200,y=200)

b6=Button(root,text=num_assign(),height=5,width=10,fg="white",font=('times 10 bold'),activebackground="#A43820",bg="#46211A",command=lambda:move(6))
b6.place(x=200,y=300)

b7=Button(root,text=num_assign(),height=5,width=10,fg="white",font=('times 10 bold'),activebackground="#A43820",bg="#46211A",command=lambda:move(7))
b7.place(x=300,y=100)

b8=Button(root,text=num_assign(),height=5,width=10,fg="white",font=('times 10 bold'),activebackground="#A43820",bg="#46211A",command=lambda:move(8))
b8.place(x=300,y=200)

b9=Button(root,text=num_assign(),height=5,width=10,fg="white",font=('times 10 bold'),activebackground="#A43820",bg="#46211A",command=lambda:move(9))
b9.place(x=300,y=300)



root.mainloop()