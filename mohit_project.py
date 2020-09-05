from Tkinter import *
from tkMessageBox import *
import sqlite3
con=sqlite3.Connection('master')
cur=con.cursor()
cur.execute("create table if not exists user(user_id varchar2(10) primary key,first varchar2(10),last varchar2(10))")
root=Tk()
root.geometry('1000x620')
root.resizable(width=False,height=False)
Label(root,text='Welcome to Master Type',font='algerian 55').grid(row=0,column=0,columnspan=5,padx=25)
Label(root,text='Enter your user name:',font='times 20').grid(row=1,column=0,pady=30)
e1=Entry(root,font='times 20',bd=5,bg='light grey')
e1.grid(row=1,column=3,pady=30)
s=0
m=5
ans=0
wro=0
i=0
a=0
acc=0
def login():
    global name
    cur.execute("select first,last from user where user_id=(?)",(e1.get(),))
    f=cur.fetchall()
    name=f
    if len(f)==0:
        showerror('Error','Invalid user name')
        return
    root.destroy()
    root1=Tk()
    root1.geometry('1000x620')
    root1.resizable(width=False,height=False)
    
    def games():

        root1.destroy()
        root0 = Tk()
        root0.resizable(width=False,height=False)
        photo = PhotoImage(file = "try.gif")
        w0 = Label(root0, image=photo)
        w0.pack()
        root0.mainloop()
        
    def test():
        root1.destroy()
        root2=Tk()
        root2.geometry('1000x620')
        root2.resizable(width=False,height=False)
        t=Text(root2,font='times',width=80,height=10,bd=5)
        t.grid(row=0,column=0,columnspan=11)
        p='The graphical user interface is a form of user interface that allows users to interact with electronic devices through graphical icons and visual indicators such as secondary notation, instead of text   based user interface, typed command labels or text navigation. GUIs were introduced in reaction to the perceived steep learning curve of command-line interfaces,which require commands to be typed on a computer keyboard.'
        lenth=len(p)
        for i in p:
            t.insert(INSERT,i)

        def result():
            global i,ans,wro,acc
            text=t1.get(1.0,END)
            if len(text)>=len(p):
                for j in p:
                    if j==text[i]:
                        ans=ans+1
                    else:
                        wro=wro+1
                    i=i+1
            elif len(text)<len(p):
                for j in text:
                    if j==p[i]:
                        ans=ans+1
                    else:
                        wro=wro+1
                    i=i+1
            acc=(ans*1.0/(ans+wro)*1.0)*100
            root2.destroy()
            root4=Tk()
            Label(root4,text='Result',font='algerian 25 bold').grid(row=0,column=0,columnspan=2)
            Label(root4,text='Name:').grid(row=1,column=0)
            Label(root4,text=name[0]).grid(row=1,column=1)
            Label(root4,text='Correct keystrokes:').grid(row=2,column=0)
            Label(root4,text='%s' % (ans)).grid(row=2,column=1)
            Label(root4,text='Wrong keystrokes:').grid(row=3,column=0)
            Label(root4,text='%s' % (wro)).grid(row=3,column=1)
            Label(root4,text='Your accuracy(%):').grid(row=4,column=0)
            Label(root4,text='%s' % (acc)).grid(row=4,column=1)
            if m==0 and s==0:
                d1=4
                d2=59
            elif m==0 and s!=0:
                d1=4
                d2=59-s
            elif m!=0 and s==0:
                d1=4-m
                d2=59
            else:
                d1=4-m
                d2=59-s
            d1=d1+((d2*1.0)/60)
            d1=int((ans+wro)/d1)
            Label(root4,text='Your speed:').grid(row=5,column=0)
            Label(root4,text='%s keystrokes per minutes' % (d1)).grid(row=5,column=1)
            root4.mainloop()
                
        
        def run():
            global s,m
            Label(root2,text="%s:%s" % (m,s),font='times 20').grid(row=0,column=12)
            if s!=0:
                s-=1
            if m==0 and s==0:
                root2.after(100,result)
                return
            if s==0:
                m-=1; s=59
            root2.after(1000,run)
                
        t1=Text(root2,font='times',width=80,height=10,bd=5)
        t1.grid(row=1,column=0,columnspan=11)
        Button(root2,text='Start',command=run,width=15,height=3,bg='white',activebackground='blue').grid(row=1,column=12,padx=30)
        Button(root2,text='Quit',command=result,width=15,height=3,bg='white',activebackground='blue').grid(
            row=1,column=13)
        #Label(root2,text='please do not click on text box').grid(row=1,column=14)
        def change():
            a1.configure(bg='white')
            a2.configure(bg='white')
            a3.configure(bg='white')
            a4.configure(bg='white')
            a5.configure(bg='white')
            a6.configure(bg='white')
            a7.configure(bg='white')
            a8.configure(bg='white')
            a9.configure(bg='white')
            a10.configure(bg='white')
            a11.configure(bg='white')
            a12.configure(bg='white')
            a13.configure(bg='white')
            a14.configure(bg='white')
            a15.configure(bg='white')
            a16.configure(bg='white')
            a17.configure(bg='white')
            a18.configure(bg='white')
            a19.configure(bg='white')
            a20.configure(bg='white')
            a21.configure(bg='white')
            a22.configure(bg='white')
            a23.configure(bg='white')
            a24.configure(bg='white')
            a25.configure(bg='white')
            a26.configure(bg='white')
            a27.configure(bg='white')
            a28.configure(bg='white')
            a29.configure(bg='white')
            a30.configure(bg='white')
            a31.configure(bg='white')
            a32.configure(bg='white')
            a33.configure(bg='white')
            a34.configure(bg='white')
            
        def Q(_event=None):
            t1.insert(END,'q')
            a1.configure(bg='blue')
            a1.after(100,change)
        def W(_event=None):
            t1.insert(END,'w')
            a2.configure(bg='blue')
            a2.after(100,change)
        def E(_event=None):
            t1.insert(END,'e')
            a3.configure(bg='blue')
            a3.after(100,change)
        def R(_event=None):
            t1.insert(END,'r')
            a4.configure(bg='blue')
            a4.after(100,change)
        def T(_event=None):
            t1.insert(END,'t')
            a5.configure(bg='blue')
            a5.after(100,change)
        def Y(_event=None):
            t1.insert(END,'y')
            a6.configure(bg='blue')
            a6.after(100,change)
        def U(_event=None):
            t1.insert(END,'u')
            a7.configure(bg='blue')
            a7.after(100,change)
        def I(_event=None):
            t1.insert(END,'i')
            a8.configure(bg='blue')
            a8.after(100,change)
        def O(_event=None):
            t1.insert(END,'o')
            a9.configure(bg='blue')
            a9.after(100,change)
        def P(_event=None):
            t1.insert(END,'p')
            a10.configure(bg='blue')
            a10.after(100,change)
        def backspace(_event=None):
            #s=s+(t.get()[:-1])
            a11.configure(bg='blue')
            a11.after(1000,change)
        def A(_event=None):
            t1.insert(END,'a')
            a13.configure(bg='blue')
            a13.after(100,change)
        def S(_event=None):
            t1.insert(END,'s')
            a14.configure(bg='blue')
            a14.after(100,change)
        def D(_event=None):
            t1.insert(END,'d')
            a15.configure(bg='blue')
            a15.after(100,change)
        def F(_event=None):
            t1.insert(END,'f')
            a16.configure(bg='blue')
            a16.after(100,change)
        def G(_event=None):
            t1.insert(END,'g')
            a17.configure(bg='blue')
            a17.after(100,change)
        def H(_event=None):
            t1.insert(END,'h')
            a18.configure(bg='blue')
            a18.after(100,change)
        def J(_event=None):
            t1.insert(END,'j')
            a19.configure(bg='blue')
            a19.after(100,change)
        def K(_event=None):
            t1.insert(END,'k')
            a20.configure(bg='blue')
            a20.after(100,change)
        def L(_event=None):
            t1.insert(END,'l')
            a21.configure(bg='blue')
            a21.after(100,change)
        def enter(_event=None):
            #s=s+(t.get()[:-1])
            a22.configure(bg='blue')
            a22.after(100,change)
        def Z(_event=None):
            t1.insert(END,'z')
            a24.configure(bg='blue')
            a24.after(100,change)
        def X(_event=None):
            t1.insert(END,'x')
            a25.configure(bg='blue')
            a25.after(100,change)
        def C(_event=None):
            t1.insert(END,'c')
            a26.configure(bg='blue')
            a26.after(100,change)
        def V(_event=None):
            t1.insert(END,'v')
            a27.configure(bg='blue')
            a27.after(100,change)
        def B(_event=None):
            t1.insert(END,'b')
            a28.configure(bg='blue')
            a28.after(100,change)
        def N(_event=None):
            t1.insert(END,'n')
            a29.configure(bg='blue')
            a29.after(100,change)
        def M(_event=None):
            t1.insert(END,'m')
            a30.configure(bg='blue')
            a30.after(100,change)
        def comma(_event=None):
            t1.insert(END,',')
            a31.configure(bg='blue')
            a31.after(100,change)
        def dot(_event=None):
            t1.insert(END,'.')
            a32.configure(bg='blue')
            a32.after(100,change)
        def space(_event=None):
            t1.insert(END,' ')
            a34.configure(bg='blue')
            a34.after(100,change)
        def backspace(_event=None):
            a=t1.get(0.1,END)
            b=a[:-1]
            
        a1=Button(root2,text='Q',command=Q,width=7,height=2)
        a1.grid(row=2,column=0)
        root2.bind('q',Q)
        a2=Button(root2,text='W',command=W,width=7,height=2)
        root2.bind('w',W)
        a2.grid(row=2,column=1)
        a3=Button(root2,text='E',command=E,width=7,height=2)
        root2.bind('e',E)
        a3.grid(row=2,column=2)
        a4=Button(root2,text='R',command=R,width=7,height=2)
        root2.bind('r',R)
        a4.grid(row=2,column=3)
        a5=Button(root2,text='T',command=T,width=7,height=2)
        root2.bind('t',T)
        a5.grid(row=2,column=4)
        a6=Button(root2,text='Y',command=Y,width=7,height=2)
        root2.bind('y',Y)
        a6.grid(row=2,column=5)
        a7=Button(root2,text='U',command=U,width=7,height=2)
        root2.bind('u',U)
        a7.grid(row=2,column=6)
        a8=Button(root2,text='I',command=I,width=7,height=2)
        root2.bind('i',I)
        a8.grid(row=2,column=7)
        a9=Button(root2,text='O',command=O,width=7,height=2)
        root2.bind('o',O)
        a9.grid(row=2,column=8)
        a10=Button(root2,text='P',command=P,width=7,height=2)
        root2.bind('p',P)
        a10.grid(row=2,column=9)
        a11=Button(root2,text='backspace',command=backspace,width=7,height=2)
        #root2.bind('<backspace>',backspace)
        a11.grid(row=2,column=10)

        a12=Button(root2,text='caps lock',width=7,height=2)
        a12.grid(row=3,column=0)
        a13=Button(root2,text='A',command=A,width=7,height=2)
        root2.bind('a',A)
        a13.grid(row=3,column=1)
        a14=Button(root2,text='S',command=S,width=7,height=2)
        root2.bind('s',S)
        a14.grid(row=3,column=2)
        a15=Button(root2,text='D',command=D,width=7,height=2)
        root2.bind('d',D)
        a15.grid(row=3,column=3)
        a16=Button(root2,text='F',command=F,width=7,height=2)
        root2.bind('f',F)
        a16.grid(row=3,column=4)
        a17=Button(root2,text='G',command=G,width=7,height=2)
        root2.bind('g',G)
        a17.grid(row=3,column=5)
        a18=Button(root2,text='H',command=H,width=7,height=2)
        root2.bind('h',H)
        a18.grid(row=3,column=6)
        a19=Button(root2,text='J',command=J,width=7,height=2)
        root2.bind('j',J)
        a19.grid(row=3,column=7)
        a20=Button(root2,text='K',command=K,width=7,height=2)
        root2.bind('k',K)
        a20.grid(row=3,column=8)
        a21=Button(root2,text='L',command=L,width=7,height=2)
        root2.bind('l',L)
        a21.grid(row=3,column=9)
        a22=Button(root2,text='enter',command=enter,width=7,height=2)
        #root2.bind('<enter>',enter)
        a22.grid(row=3,column=10)
        a23=Button(root2,text='shift',width=7,height=2)
        a23.grid(row=4,column=0)
        a24=Button(root2,text='Z',command=Z,width=7,height=2)
        root2.bind('z',Z)
        a24.grid(row=4,column=1)
        a25=Button(root2,text='X',command=X,width=7,height=2)
        root2.bind('x',X)
        a25.grid(row=4,column=2)
        a26=Button(root2,text='C',command=C,width=7,height=2)
        root2.bind('c',C)
        a26.grid(row=4,column=3)
        a27=Button(root2,text='V',command=V,width=7,height=2)
        root2.bind('v',V)
        a27.grid(row=4,column=4)
        a28=Button(root2,text='B',command=B,width=7,height=2)
        root2.bind('b',B)
        a28.grid(row=4,column=5)
        a29=Button(root2,text='N',command=N,width=7,height=2)
        root2.bind('n',N)
        a29.grid(row=4,column=6)
        a30=Button(root2,text='M',command=M,width=7,height=2)
        root2.bind('m',M)
        a30.grid(row=4,column=7)
        a31=Button(root2,text=',',command=comma,width=7,height=2)
        root2.bind(',',comma)
        a31.grid(row=4,column=8)
        a32=Button(root2,text='.',command=dot,width=7,height=2)
        root2.bind('.',dot)
        a32.grid(row=4,column=9)
        a33=Button(root2,text='shift',width=7,height=2)
        a33.grid(row=4,column=10)
        a34=Button(root2,text='space',width=92,height=2,command=space)
        a34.grid(row=5,column=0,columnspan=11)
        root2.bind('<space>',space)        
        root2.mainloop()

    Label(root1,text='Welcome sir').grid(row=0,column=0)
    Button(root1,text='Tutorial',font='Arial 76 bold',width=16,bd=5,command=games).grid(row=1,column=0,sticky=N+S+E+W)
    Button(root1,text='Start Test',font='Arial 74 bold',command=test,width=16,bd=5).grid(row=2,column=0,sticky=N+S+E+W)
    Button(root1,text='Games',font='Arial 76 bold',width=16,bd=5,command=games).grid(row=3,column=0,sticky=N+S+E+W)
    root1.mainloop()

def new():
    root3=Tk()
    root3.resizable(width=False,height=False)
    Label(root3,text='Enter your first name:').grid(row=0,column=0)
    n1=Entry(root3)
    n1.grid(row=0,column=1)
    Label(root3,text='Enter your Last name:').grid(row=1,column=0)
    n2=Entry(root3)
    n2.grid(row=1,column=1)
    Label(root3,text='Enter your user name:').grid(row=2,column=0)
    n3=Entry(root3)
    n3.grid(row=2,column=1)
    def insert():
        try:
            cur.execute("insert into user values (?,?,?)",(n3.get(),n1.get(),n2.get()))
            con.commit()
            showinfo('Information','Successfully account created,login again')
            root3.destroy()
        except:
            showerror('Error','user id already taken,please insert another details')
    Button(root3,text='Submit',command=insert).grid(row=3,column=0)
    root3.mainloop()

Button(root,text='Login',font='times 25',command=login).grid(row=2,column=2,pady=70)
Label(root,text='If you are new user:',font='times 30').grid(row=3,column=0,pady=10)
Button(root,text='Create account',font='times 25',command=new).grid(row=4,column=2,pady=40)
root.mainloop()
