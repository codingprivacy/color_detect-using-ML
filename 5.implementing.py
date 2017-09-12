
import numpy as np
import Tkinter as tk
from untested_tkdnd_wrapper import TkDND
import pickle
import cv2

f=open("theta","rb")
theta=pickle.load(f)
f.close()
count=0
class main(tk.Tk):
    def __init__(self,*args,**kwargs):
        def move_window(event):
               self.geometry('+{0}+{1}'.format(event.x_root, event.y_root))

        tk.Tk.__init__(self,*args,**kwargs)
        container=tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        #tk.Tk.title(self,"File Transfer")
        tk.Tk.wm_overrideredirect(self,True)
        tk.Tk.wm_resizable(self,0,0)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0,weight=1)
        self.bind('<B1-Motion>', move_window)

        def enterb(event):
            btn_close.configure(text="X",background="#C60000")
        def leaveb(event):
            btn_close.configure(text="X",background="#04202C")

        w = tk.Canvas(self, width=1000, height=520,bd=0,highlightthickness=0)
        w.place(x=0,y=465)
        w.create_line(0, 0, 700, 0, fill="#04202C",width=20)


        w = tk.Canvas(self, width=50, height=500,bd=0,highlightthickness=0)
        w.place(x=697,y=0)
        w.create_line(0, 0, 0, 500, fill="#04202C",width=6)

        w = tk.Canvas(self, width=4, height=500,bd=0,highlightthickness=0)
        w.place(x=0,y=0)
        w.create_line(1, 0, 1, 500, fill="#04202C",width=5)

        upper=tk.Canvas(self,width=700,height=39,bd=0,highlightthickness=0,background="#04202C")
        upper.place(x=0,y=0)
        upper.create_rectangle(0,0,900,42,outline="#04202C")
        upper.create_line(10,44,100,44,fill="#04202C")

        btn_close=tk.Button(self,width=3,text="X",relief="flat",bg="#04202c",fg="White",bd=0,activebackground="#777777",command=self.destroy,font=('Berlin Sans FB',15))
        btn_close.bind("<Enter>",enterb)
        btn_close.bind("<Leave>",leaveb)
        btn_close.place(x=660,y=2)

        self.frames = {}

        for F in (first_frame,second_frame):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(first_frame)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()
        frame.winfo_toplevel().geometry("700x470")

class first_frame(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        label1=tk.Label(self,text="Drag and Drop your image here",font=("Verdana",12))
        label1.place(x=20,y=48)

        frame = tk.Frame(self)
        frame.pack()

        listbox1 = tk.Listbox(self,width="50",height="18",selectmode="Multiple")
        scrollbar = tk.Scrollbar(frame, orient="vertical")
        scrollbar.config(command=listbox1.yview)
        scrollbar.place(x=70,y=70)

        listbox1.place(x=20,y=90)
        listbox1.config(yscrollcommand=scrollbar.set)


        label2=tk.Label(self,text="Output Box",font=("Verdana",12))
        label2.place(x=400,y=48)

        listbox2=tk.Listbox(self,width="50",height="18",yscrollcommand=scrollbar.set)
        listbox2.place(x=370,y=90)
        scrollbar.config(command=listbox2.yview)

        dnd=TkDND(self)
        def handle(event):
              event.widget.insert(0, event.data)
        dnd.bindtarget(listbox1, handle, 'text/uri-list')

        def sigmoid(z):
                den = 1.0 + np.e ** (-1.0 * z)
                d = 1.0 / den
                return d

        def testing(X):
                count=0

                X=np.array(X)
                X=X/1000.0
                X=np.insert(X,0,[1],axis=0)
                p=100*(sigmoid(X.dot(theta)))
                #print("probability:",p)
                if(p>=70):
                    listbox2.insert(count,"Given Image is Red")
                    count+=1

                elif(p<60):
                    listbox2.insert(count,"Image is Not Red")
                    count+=1

                else:
                    listbox2.insert(count,"Unsure about result ,but has some percentage of Red")
                    count+=1




        def compute(value):
                img=cv2.imread(value)
                height,width,type=img.shape
                a=0
                b=0
                c=0
                for i in range(height):   #going through each column pixel

                        for j in range(width):  #taking all the pixels of that column i.e. all row pixels of i
                            #print(img1[i][j])#printing each one
                            a+=img[i][j][0]

                            b+=img[i][j][1]
                            c+=img[i][j][2]
                total=height*width
                avga=(a/total)
                avgb=(b/total)
                avgc=(c/total)
                to_test=[avga,avgb,avgc]
                testing(to_test)

        def select():
            listbox2.delete(0,tk.END)
            for item in (listbox1.get(0,tk.END)):
                compute(item)

        def entera(enter=1):
            butn1.config(bg="lavender")

        def leavea(enter=1):
            butn1.config(bg="#5BC8AC")

        butn1=tk.Button(self,text="RESULT",command=lambda:select(),relief="flat",bd=0,bg="#5BC8AC",fg="gray4",height=2,width=18,font=("Helvetica",13))
        butn1.place(x=260,y=400)
        butn1.bind("<Enter>",entera)
        butn1.bind("<Leave>",leavea)

class second_frame(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller


app=main()
app.mainloop()
