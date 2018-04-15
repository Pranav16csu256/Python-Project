from tkinter import *
win=Tk()
count=0


def first():
    global count
    f=open("python2.txt","r")
    l=f.readlines()
    m=l[0].split()
    s1.set(m[0])
    s2.set(m[1])
    s3.set(m[2])
    s4.set(m[3])
    s5.set(m[4])
    count=1
def last():
    global count
    f=open("python2.txt","r")
    l=f.readlines()
    k=len(l)
    m=l[-1].split()
    s1.set(m[0])
    s2.set(m[1])
    s3.set(m[2])
    s4.set(m[3])
    s5.set(m[4])
    count=k
def addrec():
    flag=0
    s6.set("")
    f=open("python2.txt","r")
    lines=f.readlines()
    f.close()
    print(lines)
    f=open("python2.txt","a")
    CustomerID=s1.get()
    name=s2.get()
    address=s3.get()
    MobileNO=s4.get()
    bill=s5.get()
    try:
        
        for i in lines:
            j=i.split()
    
            if(CustomerID==(j[0])):
                flag=1
                print("*")

    except:
        print("first record")
    if(flag==0):
        if(len(MobileNO)==10):

            f.writelines(CustomerID.ljust(5)+name.ljust(20)+address.ljust(20)+MobileNO.ljust(20)+bill.ljust(5)+"\n")
            clear()
            s6.set("Record added")
            
        else:
           s6.set("Incorrect Mobile no")
    else:
        s6.set("Id already exist")
    f.close()
       
def nextrec():
    r=""
    s6.set(r)
    global count
    i=0
    f=open("python2.txt","r")
    try:
        
        while(i<=count):
            l=f.readline()
            i=i+1

        m=l.split()
        s1.set(m[0])
        s2.set(m[1])
        s3.set(m[2])
        s4.set(m[3])
        s5.set(m[4])
        print(m)
        count=count+1
    except:
        m=""
        s1.set(m)
        s2.set(m)
        s3.set(m)
        s4.set(m)
        s5.set(m)
        
        s6.set("No More Record Found")
        
    
    f.close()
def prev():
    r=""
    s6.set(r)
    global count
    i=0
    print(count)
    f=open("python2.txt","r")
    try:
    
        while(count-1>i):
            l=f.readline()
            i=i+1
        m=l.split()
        s1.set(m[0])
        s2.set(m[1])
        s3.set(m[2])
        s4.set(m[3])
        s5.set(m[4])
        print(m)
        count=count-1 
    except:
        
        m=""
        s1.set(m)
        s2.set(m)
        s3.set(m)
        s4.set(m)
        s5.set(m)
        s6.set("you cant go back")
        count=0
          
def delrec():
    k=[s1.get(),s2.get(),s3.get(),s4.get(),s5.get()]
    f=open("python2.txt","r")
    lines=f.readlines()
    print(lines)
    print(k)
    f.close()
    f=open("python2.txt","w")
    for i in lines:
        m=i.split()
        print(m)
        if(m!=k):
             f.writelines(m[0].ljust(3)+m[1].ljust(20)+m[2].ljust(20)+m[3].ljust(20)+m[4].ljust(5)+"\n")
             s6.set("Record Deleted")
    f.close()
def search():
    k=s1.get()
  
    f=open("python2.txt","r")
    h=f.readlines()
    for i in h:
        j=i.split()
        if(j[0]==k):
            print("customer found") 
            print(j)
            s1.set(j[0])
            s2.set(j[1])
            s3.set(j[2])
            s4.set(j[3])
            s5.set(j[4])
            
    f.close()        
def update():
    a1=s1.get()
    a2=s2.get()
    a3=s3.get()
    a4=s4.get()
    a5=s5.get()
    f=open("python2.txt","r")
    h=f.readlines()
    f.close()
    f=open("python2.txt","w")
    flag=0
    for i in h:
        j=i.split()
        if(j[0]!=a1):
            f.writelines(j[0].ljust(3)+j[1].ljust(20)+j[2].ljust(20)+j[3].ljust(20)+j[4].ljust(5)+"\n")
    
        else:
            f.writelines(a1.ljust(3)+a2.ljust(20)+a3.ljust(20)+a4.ljust(20)+a5.ljust(5)+"\n")
            flag=1
            s6.set("record updated")
    if(flag==0):
        s6.set("You cannot update id")
        
    
    
def clear():
    global count
    count=0 
    m=""
    s1.set(m)
    s2.set(m)
    s3.set(m)
    s4.set(m)
    s5.set(m)
    s6.set(m)
s1=StringVar()
s2=StringVar()
s3=StringVar()
s4=StringVar()
s5=StringVar()
s6=StringVar()
l1=Label(win,text="CustomerID")
l2=Label(win,text="Name")
l3=Label(win,text="Address")
l4=Label(win,text="Mobile No.")
l5=Label(win,text="Bill")
t1=Entry(win,textvariable=s1)
t2=Entry(win,textvariable=s2)
t3=Entry(win,textvariable=s3)
t4=Entry(win,textvariable=s4)
t5=Entry(win,textvariable=s5)
t6=Entry(win,textvariable=s6)

b1=Button(win,text="add",command=addrec)
b4=Button(win,text=">",command=nextrec)
b2=Button(win,text="del",command=delrec)
b7=Button(win,text="search",command=search)
b5=Button(win,text="update",command=update)
b3=Button(win,text="<",command=prev)
b8=Button(win,text="|<",command=first)
b9=Button(win,text=">|",command=last)
b6=Button(win,text="clear",command=clear)
l1.grid(row=1,column=1)
l2.grid(row=2,column=1)
l3.grid(row=1,column=3)
l4.grid(row=2,column=3)
l5.grid(row=3,column=1)
t1.grid(row=1,column=2)
t2.grid(row=2,column=2)
t3.grid(row=1,column=4)
t4.grid(row=2,column=4)
t5.grid(row=3,column=2)
t6.grid(row=3,column=7)
b1.grid(row=5,column=1)
b2.grid(row=5,column=2)
b3.grid(row=5,column=3)
b4.grid(row=5,column=4)
b5.grid(row=5,column=5)
b7.grid(row=5,column=7)
b6.grid(row=7,column=3)
b8.grid(row=7,column=2)
b9.grid(row=7,column=4)
win.mainloop()
