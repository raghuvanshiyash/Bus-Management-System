from tkinter import *
from tkinter import messagebox
import sqlite3 

class Pages:
    def __init__(self):
        self.conn = sqlite3.connect('busnew.db')
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS BUSDATA (BUSNO VARCHAR PRIMARY KEY, AgencyName text, Fromdes VARCHAR, TODES VARCHAR, FROMT VARCHAR, TOT VARCHAR, SEATS INT, DAY VARCHAR, TYPE INT)")
        self.conn.commit()

    def agent(self):
        obj = Toplevel(root)
        obj.title('AGENT LOGIN')
        obj.geometry('500x800')
        self.BUSNO = StringVar()
        self.AgencyName = StringVar()
        self.Fromdes = StringVar()
        self.Todes = StringVar()
        self.Fromt = StringVar()
        self.Tot = StringVar()
        self.Seats = IntVar()
        self.Day = StringVar()
        self.Ac = IntVar()


        label_0 = Label(obj, text="ADD BUS HERE",font=("Constantia", 40))
        label_0.place(x=90,y=23)
        label_1 = Label(obj, text="BUSNO",font=("Constantia", 20))
        label_1.place(x=80,y=130)
        entry_1 = Entry(obj,textvar=self.BUSNO)
        entry_1.place(x=240,y=130)
        label_2 = Label(obj, text="AgencyName:",font=("Constantia", 20))
        label_2.place(x=68,y=180)
        entry_2 = Entry(obj,textvar=self.AgencyName)
        entry_2.place(x=240,y=180)
        label_3 = Label(obj, text="From:",font=("Constantia", 20))
        label_3.place(x=68,y=240)
        entry_3 = Entry(obj,textvar=self.Fromdes)
        entry_3.place(x=240,y=240)
        label_4 = Label(obj, text="To:",font=("Constantia", 20))
        label_4.place(x=68,y=290)
        entry_4 = Entry(obj,textvar=self.Todes)
        entry_4.place(x=240,y=290)
        label_5 = Label(obj, text="Start time:",font=("Constantia", 20))
        label_5.place(x=68,y=330)
        entry_5 = Entry(obj,textvar=self.Fromt)
        entry_5.place(x=240,y=330)
        label_6 = Label(obj, text="End Time:",font=("Constantia", 20))
        label_6.place(x=68,y=380)
        entry_6 = Entry(obj,textvar=self.Tot)
        entry_6.place(x=240,y=380)
        label_7 = Label(obj, text="Seats:",font=("Constantia", 20))
        label_7.place(x=68,y=430)
        entry_7 = Entry(obj,textvar=self.Seats)
        entry_7.place(x=240,y=430)
        label_8 = Label(obj, text="DAYS:",font=("Constantia", 20))
        label_8.place(x=68,y=480)
        entry_8 = Entry(obj,textvar=self.Day)
        entry_8.place(x=240,y=480)
        radio = Radiobutton(obj,value = 1, text = 'AC',variable = self.Ac).place(x = 250,y = 550)
        radio2 = Radiobutton(obj,text = 'NON AC', value = 0,variable = self.Ac).place(x =250 ,y = 510)
        self.regbutton = Button(obj,text = 'Register',command = self.insert).place(x = 290,y = 600)
        #self.fetchbutton = Button(obj,text = 'Fetch',command = self.fetch).place(x = 300,y = 650)
        

        
    def booking(self):
        self.Pick = StringVar()
        self.Dep = StringVar()
        self.day = StringVar()

        obj2 = Toplevel(root)
        obj2.title("BOOK A RIDE")
        obj2.geometry('500x500')
        search = Label(obj2, text = 'Search BUSES',fg = 'White', font=("Constantia", 40)).place(x = 120, y = 50)
        label0 = Label(obj2, text='FROM', font=("Constantia", 20))
        label0.place(x=140,y=135)
        entry_0 = Entry(obj2, textvar = self.Pick,width = 20)
        entry_0.place(x=140,y=180)
        label1 = Label(obj2, text='TO', font=("Constantia", 20))
        label1.place(x=140,y=225)
        entry_1 = Entry(obj2, textvar = self.Dep,width = 20)
        entry_1.place(x=140,y=280)
        label2 = Label(obj2, text='DAY',font=("Constantia", 20))
        label2.place(x=140,y=325)
        entry_2 = Entry(obj2, textvar = self.day,width = 20)
        entry_2.place(x=140,y=380)
        button1 = Button(obj2, text = 'Search',command = self.search, font=("Constantia", 20)).place(x = 150,y = 420)



    def maint(self,root1): 
        root1.destroy() 

    def splash(self,root1):
        root1.title("Introduction")
        root1.geometry('900x500')
        Label(root1,text="Project Title: Bus Booking System",font=("Times New Roman",18),fg="Black").place(x=280,y=80)
        Label(root1,text="Developed as part of the course Advanced Programming Lab & DBMS",font=("Times New Roman",18),fg="Black").place(x=100,y=140)
        Label(root1,text="Developed By",font=("Times New Roman",13),fg="Blue").place(x=140,y=200)
        Label(root1,text="Yash Raghuvanshi 191B292",font=("Times New Roman",18),fg="Blue").place(x=310,y=240)
        Label(root1,text="Project Supervisors : Dr. Mahesh Kumar Singh & Nilesh Patel",font=("Times New Roman",13),fg="Brown").place(x=220,y=280)

        root1.update()
        root1.after(5000)
        self.maint(root1)

    #def message(self):

    def mainwindow(self,root):
        root.title("Welcome to BUS BOOKING SERVICE")
        root.configure(bg='black')
        root.resizable(1, 1)
        l = Frame( root, bg='grey', height = 103, width = 1600, relief = RAISED).place(x = 0, y= 0)
        text1 = Label(l,bg = 'grey',fg = 'black', text = 'BUS BOOKING SERVICE',width = 40,font=("Constantia", 50)).place(x = 0, y = 0)
        self.background_image = PhotoImage(file="bus.gif")
        self.background_image = self.background_image.subsample(1,1)
        l1 = Label(root, image = self.background_image, relief = RAISED).place(x = 800, y = 250)
        text2 = Label(root, text = "YOUR JOURNEY \n IS OUR PRIORITY", height = 10, font = ('constantia', 30), fg = 'white', bg = 'black').place(x = 250, y = 100)
        button1 = Button(root, text='AGENT LOGIN',bg = 'blue', height = 2, width = 20,font = ("Times new roman", 15),fg = 'yellow', command = self.agent).place(x = 450, y = 450)
        button2 = Button(root, text = 'BOOK TICKETS', height = 2, width = 20,bg = 'blue', command = self.booking,fg = 'yellow',font = ('Times new roman',15)).place(x = 150, y = 450)
        
        width, height = root.winfo_screenwidth(), root.winfo_screenheight()
        root.geometry('%dx%d+0+0' % (width,height))
    '''
    def fetch(self):
        self.cur.execute(
            "SELECT * FROM BUSDATA WHERE Fullname LIKE ?", ('%'+self.full+'%',))
        rows = self.cur.fetchall()
        return rows
    
    def fetch(self):
        obj2 = Toplevel(root)
        obj2.geometry('500x400')
        self.cur.execute(
            'SELECT * FROM BUSDATA ')
        rows = self.cur.fetchall()
        Lb1 = Listbox(obj2)
        i = 1
        for item in rows:
            Lb1.insert(i,item)
            i = i + 1
        Lb1.pack()
    '''
    def search(self):
        self.seats_to_book = IntVar()
        self.choice = IntVar()
        obj3 = Toplevel(root)
        obj3.geometry('800x800')
        self.cur.execute('SELECT * FROM BUSDATA WHERE Fromdes = ? and TODES = ? and DAY = ?',(self.Pick.get(), self.Dep.get(),self.day.get()))
        row = self.cur.fetchall()
        number = len(row)
        L = Label(obj3, text = "BUSNO, AgencyName , From , TODES ,FROMT, TOT, SEATS, DAY, TYPE AC=1:NON AC = 0", font = ('Constantia',10)).place(x = 100, y = 160)
        for i in range(0,number):
            self.str = " BUS %s" % (row[i],)
            Radiobutton(obj3, text = self.str,value = i,font = ('constantia', 10), variable = self.choice).place(x = 100, y = 200+100*i)
            i = i + 1
        self.ID = row[self.choice.get()][0]
        L1 = Label(obj3, text="No of Seats you want = ", font = ('Constantia', 20)).place(x = 100, y = 200+100*i+100)
        E1 = Entry(obj3, textvar = self.seats_to_book).place(x = 400, y = 200+100*i+100)
        b = Button(obj3, text = 'Book', font = ('Constantia', 20), command  = self.update).place(x = 100, y = 200+100*i+200)
        
    

    def insert(self):
        self.cur.execute('INSERT OR IGNORE INTO BUSDATA (BUSNO, AgencyName , Fromdes , TODES ,FROMT, TOT, SEATS, DAY, TYPE) VALUES (?,?,?,?,?,?,?,?,?)',(self.BUSNO.get(),self.AgencyName.get(), self.Fromdes.get(), self.Todes.get(), self.Fromt.get(), self.Tot.get(), self.Seats.get(), self.Day.get(), self.Ac.get()))
        self.conn.commit()
        messagebox.showinfo("showinfo", "BUS REGISTERED") 

    
    def update(self):
        self.cur.execute('UPDATE BUSDATA SET SEATS = SEATS - ? WHERE BUSNO = ?',(self.seats_to_book.get(), self.ID))
        self.conn.commit()
        messagebox.showinfo("showinfo", "SEAT BOOKED") 

    def __del__(self):
        self.conn.close()



root1 = Tk()
fron = Pages()
fron.splash(root1)


front = Pages()
root = Tk()
root.tk_setPalette('black')
front.mainwindow(root)

mainloop()