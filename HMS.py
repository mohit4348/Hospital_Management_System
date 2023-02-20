from tkinter import *
import datetime
from tkinter import messagebox as tmsg
import mysql.connector
import _mysql_connector
from tkinter import ttk
import random
import time
from playsound import playsound
import pygame

            


class Hospital:
    def __init__(self,root):
        
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1550x700")
        lbltitle = Label(self.root,bd=10,text="+HOSPITAL MANAGEMENT SYSTEM",bg="green",fg="red",font="comicsans 50 bold",relief=RIDGE)
        root.iconbitmap(r"C:\Users\Mohit Sharma\OneDrive\Desktop\New folder\Hospital_Management_System\h.ico")
        lbltitle.pack(side=TOP,fill=X)
        pygame.mixer.init()
        


        # ****************************************Entryvariables******************************

        self.pname = StringVar()
        self.page = StringVar()
        self.padd= StringVar()
        self.pmob= StringVar()
        self.ptest= StringVar()
        self.presult= StringVar()
        self.pmed= StringVar()
        self.pdoc= StringVar()
        self.pref= StringVar()
        self.pfather= StringVar()
        self.pmother= StringVar()
        self.pamount= StringVar()
        self.ppaymode= StringVar()
        self.ppayby= StringVar()
        self.pballeft= StringVar()
        self.pdis = StringVar()

        

# *****************************************dataframes****************************

    

        Dataframe = Frame(self.root,relief=RIDGE,bd=10)
        Dataframe.place(x=0,y=100,width=1370,height=380)
        dataframeleft = LabelFrame(Dataframe,text="Patient Biodata",padx="20", font="comicsans 15 bold",bd=5,relief=RIDGE)
        dataframeleft.place(x=10,y=5,width=900,height=340)

        labelname = Label(dataframeleft,text="Patient Name",font="comicsans 10 bold")
        labelname.place(x=50,y=25)
        labelage = Label(dataframeleft,text="Patient's Age",font="comicsans 10 bold")
        labelage.place(x=50,y=60)
        labeladd = Label(dataframeleft,text="Address",font="comicsans 10 bold")
        labeladd.place(x=50,y=95)
        labelmob = Label(dataframeleft,text="Mobile No.",font="comicsans 10 bold")
        labelmob.place(x=50,y=130)
        labeltest = Label(dataframeleft,text="Test Name",font="comicsans 10 bold")
        labeltest.place(x=50,y=165)
        labelresult = Label(dataframeleft,text="Test Result",font="comicsans 10 bold")
        labelresult.place(x=50,y=200)
        labelmedicine = Label(dataframeleft,text="Medicine",font="comicsans 10 bold")
        labelmedicine.place(x=50,y=235)
        labeldoctor = Label(dataframeleft,text="Doctor Name",font="comicsans 10 bold")
        labeldoctor.place(x=50,y=270)


        


        dataframeright = LabelFrame(Dataframe,text="Prescribed",padx="20", font="comicsans 15 bold",bd=5,relief=RIDGE)
        dataframeright.place(x=920,y=5,width=420,height=340)


        referby = Label(dataframeleft,text="Refer By",font="comicsans 10 bold")
        referby.place(x=430,y=25)
        fathername = Label(dataframeleft,text="Father's Name",font="comicsans 10 bold")
        fathername.place(x=430,y=60)
        mothername = Label(dataframeleft,text="Mother's Name",font="comicsans 10 bold")
        mothername.place(x=430,y=95)
        amount = Label(dataframeleft,text="Amount",font="comicsans 10 bold")
        amount.place(x=430,y=130)
        paymentmode = Label(dataframeleft,text="Payment Mode",font="comicsans 10 bold")
        paymentmode.place(x=430,y=165)
        paymentby = Label(dataframeleft,text="Payment By",font="comicsans 10 bold")
        paymentby.place(x=430,y=200)
        balanceleft = Label(dataframeleft,text="Balance Left",font="comicsans 10 bold")
        balanceleft.place(x=430,y=235)
        discharge = Label(dataframeleft,text="Discharge",font="comicsans 10 bold")
        discharge.place(x=430,y=270)

        

        


        # *********************************Entryfields************************************


        entryname = Entry(dataframeleft,font="comicsans 10 bold",textvariable = self.pname , width=25)
        entryname.place(x=225,y=25)
        entryage = Entry(dataframeleft,font="comicsans 10 bold",textvariable=self.page,width=25)
        entryage.place(x=225,y=60)
        entryadd = Entry(dataframeleft,font="comicsans 10 bold",textvariable=self.padd, width=25)
        entryadd.place(x=225,y=95)
        entrymob = Entry(dataframeleft,font="comicsans 10 bold",textvariable=self.pmob, width=25)
        entrymob.place(x=225,y=130)
        testcombobox = ttk.Combobox(dataframeleft,font="comicsans 10 bold",textvariable=self.ptest, width=22,state="readonly",cursor="hand2")
        testcombobox["values"] = ("Lipid Profile Test","Chest X-Ray","ECG","CardioGraphy","Ultrasonography")
        testcombobox.current(0)
        testcombobox.place(x=225,y=165)
        entryresult = Entry(dataframeleft,font="comicsans 10 bold",textvariable=self.presult, width=25)
        entryresult.place(x=225,y=200)
        medicinecombobox = ttk.Combobox(dataframeleft,font="comicsans 10 bold",textvariable=self.pmed, width=22,state="readonly",cursor="hand2")
        medicinecombobox["values"] = ("None","Atorvastatin","Fluvastatin","Nitroglycerin","Thrombolytic drugs","Antidepressants")
        medicinecombobox.current(0)
        medicinecombobox.place(x=225,y=235)
        doctorcombobox = ttk.Combobox(dataframeleft,font="comicsans 10 bold",textvariable=self.pdoc, width=22,state="readonly",cursor="hand2")
        doctorcombobox["values"] = ("Dr. Mohit Sharma",)
        doctorcombobox.place(x=225,y=270)


        entryreferby = Entry(dataframeleft,font="comicsans 10 bold",textvariable=self.pref, width=25)
        entryreferby.place(x=610,y=25)
        entryfather = Entry(dataframeleft,font="comicsans 10 bold",textvariable=self.pfather, width=25)
        entryfather.place(x=610,y=60)
        entrymother = Entry(dataframeleft,font="comicsans 10 bold",textvariable=self.pmother, width=25)
        entrymother.place(x=610,y=95)
        entryamount = Entry(dataframeleft,font="comicsans 10 bold",textvariable=self.pamount, width=25)
        entryamount.place(x=610,y=130)
        paymentcombobox = ttk.Combobox(dataframeleft,font="comicsans 10 bold",textvariable=self.ppaymode, width=22,state="readonly",cursor="hand2")
        paymentcombobox["values"] = ("Cash","Cheque","UPI","Internet Banking")
        paymentcombobox.current(0)
        paymentcombobox.place(x=610,y=165)
        paymentbycombobox = ttk.Combobox(dataframeleft,font="comicsans 10 bold",textvariable=self.ppayby, width=22,state="readonly",cursor="hand2")
        paymentbycombobox["values"] = ("Patient","Family","Relative")
        paymentbycombobox.current(0)
        paymentbycombobox.place(x=610,y=200)
        entrybalance = Entry(dataframeleft,font="comicsans 10 bold",textvariable=self.pballeft, width=25)
        entrybalance.place(x=610,y=235)
        dischargecombobox = ttk.Combobox(dataframeleft,font="comicsans 10 bold",textvariable=self.pdis,width=22,state="readonly",cursor="hand2")
        dischargecombobox["values"] = ("Yes","No")
        dischargecombobox.current(0)
        dischargecombobox.place(x=610,y=270)


        self.txtprescribed = Text(dataframeright,font="comicsans 10",width=53,height=18)
        self.txtprescribed.place(x=0,y=0)

        


        # ******************************Button**********************




        dataframebutton = Frame(self.root,relief=RIDGE,cursor="hand2")
        dataframebutton.place(x=0,y=480,width=1368,height=50)
        # checkbuton = Button(dataframebutton,text="Fatch All",activebackground="green",activeforeground="white" , bg="green",fg="white",padx=72,pady=15,font="comicsans 12 bold",command=self.fatch_data,cursor="hand2")
        # checkbuton.pack(side=LEFT)
        resetbuton = Button(dataframebutton,text="Reset",activebackground="green",activeforeground="white",bg="green",fg="white",padx=72,pady=15,font="comicsans 12 bold",command=self.ireset,cursor="hand2",width=13)
        resetbuton.pack(side=LEFT)
        # deletebuton = Button(dataframebutton,text="Delete",activebackground="green",activeforeground="white",bg="green",fg="white",padx=72,pady=15,font="comicsans 12 bold",command=self.idelete,cursor="hand2")
        # deletebuton.pack(side=LEFT)
        insertbuton = Button(dataframebutton,text="Insert",activebackground="green",activeforeground="white",bg="green",fg="white",padx=72,pady=15,font="comicsans 12 bold",command=self.iinsert,cursor="hand2",width=13)
        insertbuton.pack(side=LEFT)
        printbuton = Button(dataframebutton,text="Print",activebackground="green",activeforeground="white",bg="green",fg="white",padx=72,pady=15,font="comicsans 12 bold",command=self.iprint,cursor="hand2",width=13)
        printbuton.pack(side=LEFT)
        exitbuton = Button(dataframebutton,text="Exit !",activebackground="green",activeforeground="white",bg="green",fg="white",padx=72,pady=15,font="comicsans 12 bold",command=self.rating,cursor="hand2",width=13)
        exitbuton.pack(side=LEFT)
        listenbuton = Button(dataframebutton,text="Listen It !",activebackground="green",activeforeground="white",bg="green",fg="white",padx=73,pady=15,font="comicsans 12 bold",command=self.listenit,cursor="hand2")
        listenbuton.pack(side=LEFT)





        # **********************************Bottomframe*********************





        dataframeinfo = Frame(self.root,bd=10,relief=RIDGE)
        dataframeinfo.place(x=0,y=530,width=1368,height=185)


        # *********************************Scrollbar*********************

        
        

        datascrollbarh = ttk.Scrollbar(dataframeinfo,orient=HORIZONTAL)
        datascrollbarv = ttk.Scrollbar(dataframeinfo,orient=VERTICAL)
        

        self.hospital_record = ttk.Treeview(dataframeinfo,columns=("Name","Age","Address","MobileNo.","Test","TestResult","Medicine","Doctor","ReferBy","FatherName","MotherName","Amount","PaymentMode","PaymentBy","BalanceLeft","Discharge"),xscrollcommand=datascrollbarh.set,yscrollcommand=datascrollbarv.set)

        datascrollbarh.pack(side=BOTTOM,fill=X)

        datascrollbarv.pack(side=RIGHT,fill=Y)

        datascrollbarh = ttk.Scrollbar(command=self.hospital_record.xview)
        datascrollbarv = ttk.Scrollbar(command=self.hospital_record.yview)

        # *********************************Heading*************************************

        self.hospital_record.heading("Name",text="Patient's Name")
        self.hospital_record.heading("Age",text="Age")
        self.hospital_record.heading("Address",text="Address")
        self.hospital_record.heading("MobileNo.",text="Mobile No.")
        self.hospital_record.heading("Test",text="Test")
        self.hospital_record.heading("TestResult",text="Test Result")
        self.hospital_record.heading("Medicine",text="Result")
        self.hospital_record.heading("Doctor",text="Doctor")
        self.hospital_record.heading("ReferBy",text="Refer By")
        self.hospital_record.heading("FatherName",text="Father Name")
        self.hospital_record.heading("MotherName",text="Mother Name")
        self.hospital_record.heading("Amount",text="Amount")
        self.hospital_record.heading("PaymentMode",text="Payment Mode")
        self.hospital_record.heading("PaymentBy",text="Payment By")
        self.hospital_record.heading("BalanceLeft",text="Balance Left")
        self.hospital_record.heading("Discharge",text="Discharge")

        self.hospital_record["show"] = "headings"
        self.hospital_record.pack(fill=BOTH,expand=1)

        # ***********************************ColumnWidth************************************

        self.hospital_record.column("Name",width=100)
        self.hospital_record.column("Age",width=100)
        self.hospital_record.column("Address",width=100)
        self.hospital_record.column("MobileNo.",width=100)
        self.hospital_record.column("Test",width=100)
        self.hospital_record.column("TestResult",width=100)
        self.hospital_record.column("Medicine",width=100)
        self.hospital_record.column("Doctor",width=100)
        self.hospital_record.column("ReferBy",width=100)
        self.hospital_record.column("FatherName",width=100)
        self.hospital_record.column("MotherName",width=100)
        self.hospital_record.column("Amount",width=100)
        self.hospital_record.column("PaymentMode",width=100)
        self.hospital_record.column("PaymentBy",width=100)
        self.hospital_record.column("BalanceLeft",width=100)
        self.hospital_record.column("Discharge",width=100)

        self.hospital_record.pack(fill=BOTH,expand=1)

        self.fatch_data()
        





        
    # **************************************Functionality**************************

    def rating(self):
        value = tmsg.askquestion("Feedback","Do You Want To Rate My Work?")
        if value == "yes":
            tmsg.showinfo("Contact Me!","Please Recruit Me! Thank You!")
        else:
            values = tmsg.showinfo("Feedback","Please! Let Me Know Where To Improve? Thank You!")
            if values == "ok":
                self.close()
                return
                     

    def close(self):
   #win.destroy()
        self.root.quit()

    def iinsert(self):
        if self.pname.get() == "" or self.pmob.get() == "":
            tmsg.showerror("Error","Name and Mobile No. can't be left blank")
        else:
            conn = mysql.connector.connect(host="localhost", username = "root", password = "mohit123",database = "mydata")
            my_cursor = conn.cursor()
            my_cursor.execute("Insert Into hospitalrecord values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                self.pname.get(),
                self.page.get(),
                self.padd.get(),
                self.pmob.get(),
                self.ptest.get(),
                self.presult.get(),
                self.pmed.get(),
                self.pdoc.get(),
                self.pref.get(),
                self.pfather.get(),
                self.pmother.get(),
                self.pamount.get(),
                self.ppaymode.get(),
                self.ppayby.get(),
                self.pballeft.get(),
                self.pdis.get(),
            
            ))
            conn.commit()
            self.fatch_data()
            conn.close()
            tmsg.showinfo("Success","Record Has Been Inserted!")

    def fatch_data(self):
        conn = mysql.connector.connect(host="localhost", username = "root", password = "mohit123", database = "mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("Select * from hospitalrecord")
        rows = my_cursor.fetchall()
        if len(rows)!=0:
            self.hospital_record.delete(*self.hospital_record.get_children())
            for i in rows:
                self.hospital_record.insert("",END,values=i)
            conn.commit()
        conn.close()

    def iprint(self):
            self.txtprescribed.insert(END,"Name:\t\t\t"+self.pname.get()+"\n")
            self.txtprescribed.insert(END,"Age:\t\t\t"+self.page.get()+"\n")
            self.txtprescribed.insert(END,"Address:\t\t\t"+self.padd.get()+"\n")
            self.txtprescribed.insert(END,"MobileNo:\t\t\t"+self.pmob.get()+"\n")
            self.txtprescribed.insert(END,"Test:\t\t\t"+self.ptest.get()+"\n")
            self.txtprescribed.insert(END,"TestResult:\t\t\t"+self.presult.get()+"\n")
            self.txtprescribed.insert(END,"Medicine:\t\t\t"+self.pmed.get()+"\n")
            self.txtprescribed.insert(END,"Doctor:\t\t\t"+self.pdoc.get()+"\n")
            self.txtprescribed.insert(END,"ReferBy:\t\t\t"+self.pref.get()+"\n")
            self.txtprescribed.insert(END,"FatherName:\t\t\t"+self.pfather.get()+"\n")
            self.txtprescribed.insert(END,"MotherName:\t\t\t"+self.pmother.get()+"\n")
            self.txtprescribed.insert(END,"Amount:\t\t\t"+self.pamount.get()+"\n")
            self.txtprescribed.insert(END,"PaymentMode:\t\t\t"+self.ppaymode.get()+"\n")
            self.txtprescribed.insert(END,"PaymentBy:\t\t\t"+self.ppayby.get()+"\n")
            self.txtprescribed.insert(END,"BalanceLeft:\t\t\t"+self.pballeft.get()+"\n")
            self.txtprescribed.insert(END,"Discharge:\t\t\t"+self.pdis.get()+"\n")
            tmsg.showinfo("Info","Print Successfully!")

    def ireset(self):
            self.pname.set("")
            self.page.set("")
            self.padd.set("")
            self.pmob.set("")
            # self.ptest.set("")
            self.presult.set("")
            # self.pmed.set("")
            self.pdoc.set("")
            self.pref.set("")
            self.pfather.set("")
            self.pmother.set("")
            self.pamount.set("")
            # self.ppaymode.set("")
            # self.ppayby.set("")
            self.pballeft.set("")
            # self.pdis.set("")
            self.txtprescribed.delete("1.0",END)


        
    def listenit(self):
            pygame.mixer.music.load("1.mp3")
            pygame.mixer.music.play(loops=0)
            value = tmsg.showwarning("Alert","Do You Want To Stop?")
            if value == "ok":
                pygame.mixer.music.stop()
            else:
                pass
        
    
        

root = Tk()
ob = Hospital(root)
root.mainloop()