from tkinter import Tk,Button,Label,Frame,Entry,OptionMenu,StringVar,PhotoImage,Spinbox,Toplevel
from pickle import load,dump
from math import ceil
from tkvalidate import float_validate




root=Tk()
root.geometry('700x550')
root.config(background="white")
root.title("Profitability of LPG Distributership")
root.resizable(0,0)
root.iconbitmap('download.ico')

def Show_Developers():
    window = Toplevel()
    window.geometry('150x70')
    window.iconbitmap('download.ico')
    newlabel = Label(window, text = "Tamojit Das\nArshia Mitra\nAnunita Bhattacharya\nArya Bhattacharya")
    newlabel.pack()

def refresh_values():
    global EXPENSES,TARGET_CYLINDER,DATABASE,PROFIT_PER_CYLINDER
    PROFIT_PER_CYLINDER=int(Profit_Per_Cylinder.get())
    Expense_Label.config(text=str(EXPENSES))
    TARGET_CYLINDER=ceil(EXPENSES/PROFIT_PER_CYLINDER)
    Target_Cylinder_Label.config(text=str(TARGET_CYLINDER))
    DATABASE['EXPENSES']=EXPENSES
    DATABASE['TARGET_CYLINDER']=TARGET_CYLINDER
    DATABASE['PROFIT_PER_CYLINDER']=PROFIT_PER_CYLINDER


def one_home():
    fixed_frame.place_forget()
    main_frame.place(x=50,y=80)

def second_home():
    monthly_frame.place_forget()
    main_frame.place(x=50,y=80)

def third_home():
    recovery_frame.place_forget()
    main_frame.place(x=50,y=80)

def fourth_home():
    analysis_frame.place_forget()
    main_frame.place(x=50,y=80)

def add_expense_main_frame():
    global DATABASE
    if DATABASE=={}:
        main_frame.place_forget()
        fixed_frame.place(x=50,y=80)
    else:
        main_frame.place_forget()
        monthly_frame.place(x=50,y=80)

def add_recovery_main_frame():
    global DATABASE
    if True:
        main_frame.place_forget()
        recovery_frame.place(x=50,y=80)

def add_analysis_main_frame():
    main_frame.place_forget()
    analysis_frame.place(x=50,y=80)

def load_db():
    global DATABASE,EXPENSES,TARGET_CYLINDER,PROFIT_PER_CYLINDER
    try:
        f=open('Database.dat','rb')
        DATABASE=load(f)
        f.close()
        EXPENSES=DATABASE['EXPENSES']
        TARGET_CYLINDER=DATABASE['TARGET_CYLINDER']
        PROFIT_PER_CYLINDER=DATABASE['PROFIT_PER_CYLINDER']
    except:
        DATABASE={}
    return DATABASE

def write_db():
    global DATABASE
    f=open('Database.dat','wb')
    dump(DATABASE,f)
    f.close()

def predict_time():
    try:
        ans=ceil(TARGET_CYLINDER/int(Working_Days.get())/int(Sales_Per_Day.get()))
        Expected_Time.delete(0,'end')
        Expected_Time.insert(0,str(ans))
    except:
        pass

def predict_sales():
    try:
        ans=ceil(TARGET_CYLINDER/int(Working_Days.get())/int(Expected_Time.get()))
        Sales_Per_Day.delete(0,'end')
        Sales_Per_Day.insert(0,str(ans))
    except:
        pass

def f():
    pass

def Custom_Spinbox(root):
    w=Spinbox(root,from_=10,to=100,relief='groove')
    return w


def Custom_Entry(root):
    entry=Entry(root,bg='white',bd=1,relief='groove')
    float_validate(entry,from_=0,to=10000000)
    return entry

def Custom_Label(root,display_text):
    label=Label(root,bg='white',anchor='e',bd=0,relief='groove',text=display_text)
    return label

def Custom_Dropdown(root,var,arr):
    option=OptionMenu(root,var,*arr)
    option.config(bg='white',relief='groove')
    return option

def Custom_Button(root,txt,func):
    button=Button(root,text=txt,command=func,relief='groove',bg='white')
    return button

def one_add():
    global EXPENSES
    total=  float(Office.get()) \
            +float(Office_Extras.get()) \
            +float(Advertisement.get()) \
            +float(Office_License.get()) \
            +Dict[var.get()]


    EXPENSES+=total
    refresh_values()
    write_db()
    monthly_frame.place(x=50,y=80)
    fixed_frame.place_forget()

def add_two():
    global EXPENSES
    total=float(Employees_Salary.get()) + float(Electric_Bill.get()) + float(Transportation.get()) + float(License_Renew.get()) + float(Mobile_Internet.get())
    EXPENSES+=total
    monthly_frame.place_forget()
    refresh_values()
    write_db()
    main_frame.place(x=50,y=80)


def add_three():
    global EXPENSES
    EXPENSES-=float(Cylinder_Sold.get())
    main_frame.place(x=50,y=80)
    refresh_values()
    write_db()
    recovery_frame.place_forget()



fixed_frame=Frame(root,width=600,height=400,highlightbackground="blue",highlightthickness=1,background='white',relief='groove')

# Custom_Label(fixed_frame,'Godown Land Lease Registration').place(x=70,y=50)
# Godown=Custom_Entry(fixed_frame)
# Godown.place(x=400,y=50)

Custom_Label(fixed_frame,'Land Registration ( Office + Godown )').place(x=70,y=100)
Office=Custom_Entry(fixed_frame)
Office.place(x=400,y=100)

Custom_Label(fixed_frame,'Miscellaneous').place(x=70,y=150)
Office_Extras=Custom_Entry(fixed_frame)
Office_Extras.place(x=400,y=150)

Custom_Label(fixed_frame,'Advertisement').place(x=70,y=200)
Advertisement=Custom_Entry(fixed_frame)
Advertisement.place(x=400,y=200)

Custom_Label(fixed_frame,'Licensing Cost').place(x=70,y=250)
Office_License=Custom_Entry(fixed_frame)
Office_License.place(x=400,y=250)

Custom_Label(fixed_frame,'IOCL Security Deposit').place(x=70,y=300)
var=StringVar(fixed_frame)
var.set('SC-ST')
Security_Deposit=Custom_Dropdown(fixed_frame,var,['SC-ST','OBC','GENERAL'])
Security_Deposit.place(x=400,y=300)
Dict={'SC-ST':300000,'OBC':600000,'GENERAL':500000}

Custom_Button(fixed_frame,'Add to one time investment',one_add).place(x=400,y=350)
Custom_Button(fixed_frame,'Home',one_home).place(x=70,y=350)




monthly_frame=Frame(root,width=600,height=400,highlightbackground="blue",highlightthickness=1,background='white',relief='groove')

Custom_Label(monthly_frame,'Employees Salary').place(x=70,y=50)
Employees_Salary=Custom_Entry(monthly_frame)
Employees_Salary.place(x=400,y=50)

Custom_Label(monthly_frame,'Electric Bill').place(x=70,y=100)
Electric_Bill=Custom_Entry(monthly_frame)
Electric_Bill.place(x=400,y=100)

Custom_Label(monthly_frame,'Transpotation ( vehicle + fuel )').place(x=70,y=150)
Transportation=Custom_Entry(monthly_frame)
Transportation.place(x=400,y=150)

Custom_Label(monthly_frame,'License Renew ( once every 2 yrs )').place(x=70,y=200)
License_Renew=Custom_Entry(monthly_frame)
License_Renew.place(x=400,y=200)

Custom_Label(monthly_frame,'Mobile + Internet + Food + Water').place(x=70,y=250)
Mobile_Internet=Custom_Entry(monthly_frame)
Mobile_Internet.place(x=400,y=250)



Custom_Button(monthly_frame,'Add to monthly investment',add_two).place(x=400,y=350)
Custom_Button(monthly_frame,'Home',second_home).place(x=70,y=350)



recovery_frame=Frame(root,width=600,height=400,highlightbackground="blue",highlightthickness=1,background='white',relief='groove')

Custom_Label(recovery_frame,'Money recovered / Income / Earnings').place(x=70,y=50)
Cylinder_Sold=Custom_Entry(recovery_frame)
Cylinder_Sold.place(x=400,y=50)

Custom_Button(recovery_frame,'Add to monthly recovery',add_three).place(x=400,y=350)
Custom_Button(recovery_frame,'Home',third_home).place(x=70,y=350)



analysis_frame=Frame(root,width=600,height=400,highlightbackground="blue",highlightthickness=1,background='white',relief='groove')

Custom_Label(analysis_frame,'Sales per day').place(x=70,y=50)
Sales_Per_Day=Custom_Entry(analysis_frame)
Sales_Per_Day.place(x=400,y=50)

Custom_Label(analysis_frame,'Working days').place(x=70,y=100)
Working_Days=Custom_Entry(analysis_frame)
Working_Days.place(x=400,y=100)

Custom_Label(analysis_frame,'Expected Break Even Time in months').place(x=70,y=150)
Expected_Time=Custom_Entry(analysis_frame)
Expected_Time.place(x=400,y=150)


Custom_Button(analysis_frame,'Home',fourth_home).place(x=70,y=350)
Custom_Button(analysis_frame,'Predict B.E.T in months',predict_time).place(x=280,y=350)
Custom_Button(analysis_frame,'Predict Sales/day',predict_sales).place(x=430,y=350)




main_frame=Frame(root,width=600,height=400,highlightbackground="blue",highlightthickness=1,background='white',relief='groove')
bg = PhotoImage(file = "bg2.png")
useless_label = Label( main_frame, image = bg)
useless_label.place(x = 0, y = 0)

Custom_Button(main_frame,'Add Expense',add_expense_main_frame).place(x=150,y=350)
Custom_Button(main_frame,'Add Recovery',add_recovery_main_frame).place(x=300,y=350)
Custom_Button(main_frame,'Analysis',add_analysis_main_frame).place(x=450,y=350)




###########################################################################################################

EXPENSES=0.0
TARGET_CYLINDER=0
DATABASE=load_db()
PROFIT_PER_CYLINDER=61

if DATABASE!={}:
    EXPENSES=DATABASE['EXPENSES']
    TARGET_CYLINDER=DATABASE['TARGET_CYLINDER']
    PROFIT_PER_CYLINDER=DATABASE['PROFIT_PER_CYLINDER']

Custom_Label(root,'Expense:').place(x=450,y=15)
Expense_Label=Custom_Label(root,str(EXPENSES))
Expense_Label.place(x=600,y=15)

Custom_Label(root,'Target Cylinder:').place(x=450,y=35)
Target_Cylinder_Label=Custom_Label(root,str(TARGET_CYLINDER))
Target_Cylinder_Label.place(x=600,y=40)
Custom_Label(root,'( Break Even Volume )').place(x=450,y=57)

Custom_Label(root,'Profit per Cylinder: ').place(x=100,y=15)
Profit_Per_Cylinder=Custom_Spinbox(root)
Profit_Per_Cylinder.place(x=100,y=40)
Profit_Per_Cylinder.delete(0,3)
Profit_Per_Cylinder.insert(index=0, s=str(PROFIT_PER_CYLINDER))


Custom_Button(root,'Developers',Show_Developers).place(x=50,y=500)

main_frame.place(x=50,y=80)

##fixed_frame.place(x=50,y=50)


##monthly_frame.place(x=50,y=50)


##recovery_frame.place(x=50,y=50)



root.mainloop()
