'''
Names: Gaby Ramon and Maddie Chan
Date: 3.31.2024
Title: TMS PHASE 3 WINDOWS
'''

from tkinter import *
import tkinter as tk
from tkinter import messagebox
import tkmacosx as tkmac
import csv


############################### LOGIN WINDOW ###############################

def login():
    pass

def exit():
    pass

wdLogin=tk.Tk()
wdLogin.title('Login')
wdLogin.geometry('700x375')
wdLogin.resizable(width=False,height=False)

body=tk.Frame(wdLogin,bg='white',height=375,width=750)
body.grid(row=0,column=0)


lblUsername=tk.Label(body,text='Username: ',bg='white',fg='black')
lblUsername.config(font=('Times New Roman',20))
lblUsername.place(x=150,y=120)

entUsername=tk.Entry(body,bg='#ddf2fd',fg='black')
entUsername.config(font=('Times New Roman',20))
entUsername.place(x=300,y=120,width=300,height=40)


lblPassword=tk.Label(body,text='Password: ',bg='white',fg='black')
lblPassword.config(font=('Times New Roman',20))
lblPassword.place(x=150,y=190)

entPassword=tk.Entry(body,bg='#ddf2fd',fg='black')
entPassword.config(font=('Times New Roman',20),show='*')
entPassword.place(x=300,y=190,width=300,height=40)


loginTitle=tk.Label(body,text='Task Management System',bg='white',fg='black')
loginTitle.config(font=('Times New Roman',28))
loginTitle.place(x=200,y=30)


btnLogin=tk.Button(body,text='Login',command=login,width=5)
btnLogin.place(x=350,y=260)
btnLogin.config(font=('Times New Roman',20))

btnExit=tk.Button(body,text='Exit',command=exit,width=5)
btnExit.place(x=500,y=260)
btnExit.config(font=('Times New Roman',20))

wdLogin.mainloop()


#################### MAIN PAGE WINDOW  ######################


def addTask():
    pass

def editTask():
    pass

def removeTask():
    pass

def searchTask():
    pass

def calendar():
    pass

def settings():
    pass

def exit():
    pass

wdMain=Tk()
wdMain.title('Main Menu Page')
wdMain.geometry('720x500')
wdMain.resizable(width=False,height=False)

mainBody=tk.Frame(bg='white',height=500,width=720)
mainBody.grid(row=0,column=0)

#Main Title
lblMainTitle=tk.Label(mainBody,text = 'Task Management System', bg='white',fg='black')
lblMainTitle.config(font=('Times New Roman',28))
lblMainTitle.place(x=200,y=30)

#Action Buttons
btnMainAdd=tkmac.Button(mainBody,text='Add Task',bg='pink')
btnMainAdd.config(font=('Times New Roman',20))
btnMainAdd.place(x=185,y=130)

btnMainEdit=tkmac.Button(mainBody,text='Edit Task',bg='gold')
btnMainEdit.config(font=('Times New Roman',20))
btnMainEdit.place(x=185,y=210)

btnMainRemove=tkmac.Button(mainBody,text='Remove Task',bg='sandybrown')
btnMainRemove.config(font=('Times New Roman',20))
btnMainRemove.place(x=175,y=290)

btnMainSearch=tkmac.Button(mainBody,text='Search',bg='lightgreen')
btnMainSearch.config(font=('Times New Roman',20))
btnMainSearch.place(x=400,y=130)

btnMainCalendar=tkmac.Button(mainBody,text='Calendar',bg='lightskyblue')
btnMainCalendar.config(font=('Times New Roman',20))
btnMainCalendar.place(x=395,y=210)

btnMainSettings=tkmac.Button(mainBody,text='Settings',bg='mediumpurple')
btnMainSettings.config(font=('Times New Roman',20))
btnMainSettings.place(x=400,y=290)

btnExit=tkmac.Button(mainBody,text='Exit',bg='#ddf2fd')
btnExit.config(font=('Times New Roman',18))
btnExit.place(x=310,y=400)


############################### ADD TASK WINDOW ###############################

wdAdd=tk.Tk()
wdAdd.title('Add Task')
wdAdd.geometry('1000x500')
wdAdd.resizable(width=False,height=False)

addBody=tk.Frame(wdAdd,bg='#ffcccb',height=500,width=1000)
addBody.grid(row=0,column=0)


addTitle=tk.Label(addBody,text='Add Task',bg='#ffcccb',fg='black')
addTitle.config(font=('Times New Roman',28))
addTitle.place(x=445,y=30)


lblTaskName=tk.Label(addBody,text='Task Name: ',bg='#ffcccb',fg='black')
lblTaskName.config(font=('Times New Roman',18))
lblTaskName.place(x=250,y=120)

entTaskName=tk.Entry(addBody,bg='#C0C5CE',fg='black')
entTaskName.config(font=('Times New Roman',14))
entTaskName.place(x=400,y=120,width=300)


lblDate=tk.Label(addBody,text='Date: ',bg='#ffcccb',fg='black')
lblDate.config(font=('Times New Roman',18))
lblDate.place(x=250,y=170)

entDate=tk.Entry(addBody,bg='#C0C5CE',fg='black')
entDate.config(font=('Times New Roman',14))
entDate.place(x=400,y=170,width=300)


lblDuration=tk.Label(addBody,text='Duration: ',bg='#ffcccb',fg='black')
lblDuration.config(font=('Times New Roman',18))
lblDuration.place(x=250,y=220)

entDuration=tk.Entry(addBody,bg='#C0C5CE',fg='black')
entDuration.config(font=('Times New Roman',14))
entDuration.place(x=400,y=220,width=300)


lblDescrip=tk.Label(addBody,text='Description: ',bg='#ffcccb',fg='black')
lblDescrip.config(font=('Times New Roman',18))
lblDescrip.place(x=250,y=270)

entDescrip=tk.Entry(addBody,bg='#C0C5CE',fg='black')
entDescrip.config(font=('Times New Roman',14))
entDescrip.place(x=400,y=270,width=400,height=100)


def add():
    pass

btnAddTask=tk.Button(addBody,text='Add',command=add,width=5)
btnAddTask.place(x=450,y=420)
btnAddTask.config(font=('Times New Roman',20))


def home():
    pass

btnHome=tkmac.Button(addBody,text='Main Page',command=home,
                  bg='#ffcccb')
btnHome.place(x=10,y=5)
btnHome.config(font=('Times New Roman',14))

wdAdd.mainloop()


############################### REMOVE TASK WINDOW ###############################

wdRemove=tk.Tk()
wdRemove.title('Remove Task')
wdRemove.geometry('700x400')
wdRemove.resizable(width=False,height=False)

removeBody=tk.Frame(wdRemove,bg='#ffe6cb',height=500,width=1000)
removeBody.grid(row=0,column=0)


removeTitle=tk.Label(removeBody,text='Remove Task',bg='#ffe6cb',fg='black')
removeTitle.config(font=('Times New Roman',28))
removeTitle.place(x=270,y=40)


lblTaskNameR=tk.Label(removeBody,text='Task Name: ',bg='#ffe6cb',fg='black')
lblTaskNameR.config(font=('Times New Roman',18))
lblTaskNameR.place(x=160,y=120)

entTaskNameR=tk.Entry(removeBody,bg='#C0C5CE',fg='black')
entTaskNameR.config(font=('Times New Roman',14))
entTaskNameR.place(x=290,y=120,width=300)


lblDateR=tk.Label(removeBody,text='Date: ',bg='#ffe6cb',fg='black')
lblDateR.config(font=('Times New Roman',18))
lblDateR.place(x=160,y=180)

entDateR=tk.Entry(removeBody,bg='#C0C5CE',fg='black')
entDateR.config(font=('Times New Roman',14))
entDateR.place(x=290,y=180,width=300)


def remove():
    pass

btnRemoveTask=tk.Button(removeBody,text='Remove',command=remove,width=5)
btnRemoveTask.place(x=300,y=260)
btnRemoveTask.config(font=('Times New Roman',20))


def home():
    pass

btnHome=tkmac.Button(removeBody,text='Main Page',command=home,
                  bg='#ffe6cb')
btnHome.place(x=10,y=5)
btnHome.config(font=('Times New Roman',14))

wdRemove.mainloop()


############################### EDIT TASK WINDOW ###############################

wdEdit=tk.Tk()
wdEdit.title('Edit Task')
wdEdit.geometry('1000x500')
wdEdit.resizable(width=False,height=False)

editBody=tk.Frame(wdEdit,bg='#ece0ba',height=500,width=1000)
editBody.grid(row=0,column=0)


editTitle=tk.Label(editBody,text='Edit Task',bg='#ece0ba',fg='black')
editTitle.config(font=('Times New Roman',28))
editTitle.place(x=445,y=30)


lblTaskNameE=tk.Label(editBody,text='Task Name:',bg='#ece0ba',fg='black')
lblTaskNameE.config(font=('Times New Roman',18))
lblTaskNameE.place(x=20,y=120)

entTaskNameE=tk.Entry(editBody,bg='#C0C5CE',fg='black')
entTaskNameE.config(font=('Times New Roman',14))
entTaskNameE.place(x=120,y=120,width=300)

lblDateE=tk.Label(editBody,text='Date: ',bg='#ece0ba',fg='black')
lblDateE.config(font=('Times New Roman',18))
lblDateE.place(x=20,y=180)

entDateE=tk.Entry(editBody,bg='#C0C5CE',fg='black')
entDateE.config(font=('Times New Roman',14))
entDateE.place(x=120,y=180,width=300)


lblNewTask=tk.Label(editBody,text='New Task Name: ',bg='#ece0ba',fg='black')
lblNewTask.config(font=('Times New Roman',18))
lblNewTask.place(x=500,y=120)

entNewTask=tk.Entry(editBody,bg='#C0C5CE',fg='black')
entNewTask.config(font=('Times New Roman',14))
entNewTask.place(x=650,y=120,width=300)


lblNewDate=tk.Label(editBody,text='New Date: ',bg='#ece0ba',fg='black')
lblNewDate.config(font=('Times New Roman',18))
lblNewDate.place(x=500,y=180)

entNewDate=tk.Entry(editBody,bg='#C0C5CE',fg='black')
entNewDate.config(font=('Times New Roman',14))
entNewDate.place(x=650,y=180,width=300)


lblNewDuration=tk.Label(editBody,text='New Duration: ',bg='#ece0ba',fg='black')
lblNewDuration.config(font=('Times New Roman',18))
lblNewDuration.place(x=500,y=240)

entNewDuration=tk.Entry(editBody,bg='#C0C5CE',fg='black')
entNewDuration.config(font=('Times New Roman',14))
entNewDuration.place(x=650,y=240,width=300)


lblNewDescrip=tk.Label(editBody,text='New Description: ',bg='#ece0ba',fg='black')
lblNewDescrip.config(font=('Times New Roman',18))
lblNewDescrip.place(x=500,y=300)

entNewDescrip=tk.Entry(editBody,bg='#C0C5CE',fg='black')
entNewDescrip.config(font=('Times New Roman',14))
entNewDescrip.place(x=650,y=300,width=300,height=100)


def submit():
    pass

btnSubmit=tk.Button(editBody,text='Submit',command=submit,width=5)
btnSubmit.place(x=865,y=425)
btnSubmit.config(font=('Times New Roman',20))


def home():
    pass

btnHome=tkmac.Button(editBody,text='Main Page',command=home,
                  bg='#ece0ba')
btnHome.place(x=10,y=5)
btnHome.config(font=('Times New Roman',14))

wdEdit.mainloop()


#################### SEARCH WINDOW ######################


def search():
    pass

wdSearch=Tk()
wdSearch.title('Search Page')
wdSearch.geometry('700x500')
wdSearch.resizable(width=False,height=False)

searchBody=tk.Frame(wdSearch,bg='#dcedc1',width=700,height=500)
searchBody.grid(row=0,column=0)

#Title
lblSearchTitle=tk.Label(searchBody,text = 'Search Task', bg='#dcedc1',fg='black')
lblSearchTitle.config(font=('Times New Roman',28))
lblSearchTitle.place(x=280,y=70)

btnTMS=tkmac.Button(searchBody, text = 'Task Management System',command=home, bg='#dcedc1')
btnTMS.config(font=('Times New Roman',16))
btnTMS.place(x=1,y=1)

#Search
entSearch=tk.Entry(searchBody,bg='#ddf2fd',fg='black')
entSearch.place(x=40,y=130,height=25,width=185)

btnSearch=tkmac.Button(searchBody,text='Search',command=search,bg='grey',fg='white')
btnSearch.config(font=('Times New Roman',13))
btnSearch.place(x=230,y=130)


txtResults=tk.Text(searchBody,height=20,width=30,bg='gainsboro')
txtResults.place(x=40,y=165)

txtTaskName=tk.Text(searchBody,height=2,width=20,bg='#dcedc1')
txtTaskName.place(x=450,y=150)

lblSearchTitle=tk.Label(searchBody,text="Title: ",bg='#dcedc1',fg='black')
lblSearchTitle.config(font=("Times New Roman",18))
lblSearchTitle.place(x=350,y=200)
entSearchTitle = tk.Entry(searchBody,bg='#ddf2fd',fg='black')
entSearchTitle.place(x=480,y=200,height=30,width=200)

lblSearchDate=tk.Label(searchBody,text="Date: ",bg='#dcedc1',fg='black')
lblSearchDate.config(font=("Times New Roman",18))
lblSearchDate.place(x=350,y=245)
entSearchDate = tk.Entry(searchBody,bg='#ddf2fd',fg='black')
entSearchDate.place(x=480,y=245,height=30,width=200)

lblSearchDuration=tk.Label(searchBody,text="Duration: ",bg='#dcedc1',fg='black')
lblSearchDuration.config(font=("Times New Roman",18))
lblSearchDuration.place(x=350,y=290)
entSearchDuration = tk.Entry(searchBody,bg='#ddf2fd',fg='black')
entSearchDuration.place(x=480,y=290,height=30,width=200)

lblSearchDescription=tk.Label(searchBody,text="Description: ",bg='#dcedc1',fg='black')
lblSearchDescription.config(font=("Times New Roman",18))
lblSearchDescription.place(x=350,y=335)
entSearchDescription = tk.Entry(searchBody,bg='#ddf2fd',fg='black')
entSearchDescription.place(x=480,y=335,height=70,width=200)

wdSearch.mainloop()

#################### SETTINGS WINDOW  ######################

wdSettings=Tk()
wdSettings.title('Settings Page')
wdSettings.geometry('700x500')
wdSettings.resizable(width=False,height=False)

settingsBody=tk.Frame(wdSettings,bg='thistle',width=700,height=500)
settingsBody.grid(row=0,column=0)

#Title
lblSettingsTitle=tk.Label(settingsBody,text = 'Settings', bg='thistle')
lblSettingsTitle.config(font=('Times New Roman',28))
lblSettingsTitle.place(x=300,y=75)

#Buttons

def adduser():
    pass

def removeuser():
    pass

def changeun():
    pass

def changepass():
    pass

btnTMS=tk.Button(settingsBody,text = 'Task Management System',bg='thistle')
btnTMS.config(font=('Times New Roman',16))
btnTMS.place(x=1,y=1)

btnAddUser=tk.Button(settingsBody,text='Add User',command=adduser,width=15,height=1)
btnAddUser.config(font=('Times New Roman',20))
btnAddUser.place(x=250,y=150)

btnRemoveUser=tk.Button(settingsBody,text='Remove User',command=removeuser,width=15,height=1)
btnRemoveUser.config(font=('Times New Roman',20))
btnRemoveUser.place(x=250,y=220)

btnChangeUn=tk.Button(settingsBody,text='Change Username',command=changeun,width=15,height=1)
btnChangeUn.config(font=('Times New Roman',20))
btnChangeUn.place(x=250,y=290)

btnChangePass=tk.Button(settingsBody,text='Change Password',command=changepass,width=15,height=1)
btnChangePass.config(font=('Times New Roman',20))
btnChangePass.place(x=250,y=360)

wdSettings.mainloop()

#################### CALENDAR PAGE WINDOW  ######################

def exit():
    pass

def show_cal():
    pass

wdCalendar=Tk()
wdCalendar.title('Calendar Page')
wdCalendar.geometry('700x500')
wdCalendar.resizable(width=False,height=False)

calBody=tk.Frame(wdCalendar,bg='lightskyblue',width=700,height=500)
calBody.grid(row=0,column=0)

#Title
lblCalendarTitle=tk.Label(calBody,text = 'Calendar', bg='lightskyblue')
lblCalendarTitle.config(font=('Times New Roman',28))
lblCalendarTitle.place(x=300,y=70)

btnTMS=tkmac.Button(calBody,text = 'Task Management System',command=home,bg='lightskyblue')
btnTMS.config(font=('Times New Roman',16))
btnTMS.place(x=1,y=1)

#Calendar Labels/Buttons
lblMonth=tk.Label(calBody,text='Month: ',bg='lightskyblue')
lblMonth.config(font=("Times New Roman",18))
lblMonth.place(x=60,y=125)
entMonth = tk.Entry(calBody,bg='#ddf2fd',fg='black')
entMonth.config(font=("Times New Roman", 18))
entMonth.place(x=130,y=125)

lblYear=tk.Label(calBody,text='Year: ',bg='lightskyblue')
lblYear.config(font=("Times New Roman",18))
lblYear.place(x=380,y=125)
entYear = tk.Entry(calBody,bg='#ddf2fd',fg='black')
entYear.config(font=('Times New Roman',18))
entYear.place(x=450,y=125)

btnShow=tk.Button(calBody,text='Show Calendar',command=show_cal,bg='dimgray',fg='black')
btnShow.config(font=('Times New Roman',16))
btnShow.place(x=290,y=400)

btnClose=tk.Button(calBody,text='Close',command=exit,bg='dimgray',fg='black')
btnClose.config(font=('Times New Roman',16))
btnClose.place(x=320,y=450)


wdCalendar.mainloop()
