'''
Names: Gaby Ramon and Maddie Chan
Date: 4.22.2024
Title: TMS PHASE 5
'''

from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkmacosx import Button
import csv
import os
import pandas as pd
from datetime import date
from PIL import ImageTk, Image

CURRENTUSER=None
CURRENTPASS=None

############################### ADD TASK WINDOW ###############################
def addTaskWin(wdMain):
    wdAdd=tk.Toplevel()
    wdAdd.title('Add Task')
    wdAdd.geometry('1000x500')
    wdAdd.resizable(width=False,height=False)

    addBody=tk.Frame(wdAdd,bg='#ffcccb',height=500,width=1000)
    addBody.grid(row=0,column=0)

    logo=Image.open('CMPT 120 Logo.png')
    logo_resized=logo.resize((100,100))
    new_logo=ImageTk.PhotoImage(logo_resized)

    logo_label=tk.Label(addBody,image=new_logo,bg='#ffcccb')
    logo_label.place(x=890,y=10)

    addTitle=tk.Label(addBody,text='Add Task',bg='#ffcccb',fg='black')
    addTitle.config(font=('Times New Roman',28))
    addTitle.place(x=445,y=30)


    lblTaskName=tk.Label(addBody,text='Task Name: ',bg='#ffcccb',fg='black')
    lblTaskName.config(font=('Times New Roman',18))
    lblTaskName.place(x=250,y=120)

    global entTaskName
    entTaskName=tk.Entry(addBody,bg='#C0C5CE',fg='black')
    entTaskName.config(font=('Times New Roman',14))
    entTaskName.place(x=400,y=120,width=300)


    lblDate=tk.Label(addBody,text='Date: ',bg='#ffcccb',fg='black')
    lblDate.config(font=('Times New Roman',18))
    lblDate.place(x=250,y=170)

    global entDate
    entDate=tk.Entry(addBody,bg='#C0C5CE',fg='black')
    entDate.config(font=('Times New Roman',14))
    entDate.place(x=400,y=170,width=300)


    lblDuration=tk.Label(addBody,text='Duration: ',bg='#ffcccb',fg='black')
    lblDuration.config(font=('Times New Roman',18))
    lblDuration.place(x=250,y=220)

    global entDuration
    entDuration=tk.Entry(addBody,bg='#C0C5CE',fg='black')
    entDuration.config(font=('Times New Roman',14))
    entDuration.place(x=400,y=220,width=300)


    lblDescrip=tk.Label(addBody,text='Description: ',bg='#ffcccb',fg='black')
    lblDescrip.config(font=('Times New Roman',18))
    lblDescrip.place(x=250,y=270)

    global entDescrip
    entDescrip=tk.Entry(addBody,bg='#C0C5CE',fg='black')
    entDescrip.config(font=('Times New Roman',14))
    entDescrip.place(x=400,y=270,width=400,height=100)


    def add():
        file='%s.csv' % CURRENTUSER
        try:
            df = pd.read_csv(file)
        except FileNotFoundError:
            df=pd.DataFrame(columns=['Task Name','Date','Duration','Description'])
        new_row={
            'Task Name':entTaskName.get(),
            'Date':entDate.get(),
            'Duration':entDuration.get(),
            'Description':entDescrip.get()}
        df=pd.concat([df,pd.DataFrame([new_row])],ignore_index=True)
        df.to_csv(file,index=False)
        messagebox.showinfo('Add Task Success','Successfully Added Task')

    btnAddTask=Button(addBody,text='Add',command=add,bg='lightgrey')
    btnAddTask.place(x=450,y=420)
    btnAddTask.config(font=('Times New Roman',20))


    btnHome=Button(addBody,text='Main Page',command=lambda:[wdAdd.destroy(), wdMain.destroy(), mainmenuWin()],bg='#ffcccb')
    btnHome.place(x=10,y=5)
    btnHome.config(font=('Times New Roman',14))

    wdAdd.mainloop()


############################### REMOVE TASK WINDOW ###############################

def removeTaskWin(wdMain):

    filename=f'{CURRENTUSER}.csv'
    if os.path.exists(filename):
        wdRemove=tk.Toplevel()
        wdRemove.title('Remove Task')
        wdRemove.geometry('700x400')
        wdRemove.resizable(width=False,height=False)

        removeBody=tk.Frame(wdRemove,bg='#ffe6cb',height=500,width=1000)
        removeBody.grid(row=0,column=0)

        logo=Image.open('CMPT 120 Logo.png')
        logo_resized=logo.resize((100,100))
        new_logo=ImageTk.PhotoImage(logo_resized)
        logo_label=tk.Label(removeBody,image=new_logo,bg='#ffe6cb')
        logo_label.place(x=590,y=10)


        removeTitle=tk.Label(removeBody,text='Remove Task',bg='#ffe6cb',fg='black')
        removeTitle.config(font=('Times New Roman',28))
        removeTitle.place(x=270,y=40)


        lblTaskNameR=tk.Label(removeBody,text='Task Name: ',bg='#ffe6cb',fg='black')
        lblTaskNameR.config(font=('Times New Roman',18))
        lblTaskNameR.place(x=320,y=150)

        global entTaskNameR
        entTaskNameR=tk.Entry(removeBody,bg='#C0C5CE',fg='black')
        entTaskNameR.config(font=('Times New Roman',14))
        entTaskNameR.place(x=430,y=150,width=250)


        lblDateR=tk.Label(removeBody,text='Date: ',bg='#ffe6cb',fg='black')
        lblDateR.config(font=('Times New Roman',18))
        lblDateR.place(x=320,y=210)

        global entDateR
        entDateR=tk.Entry(removeBody,bg='#C0C5CE',fg='black')
        entDateR.config(font=('Times New Roman',14))
        entDateR.place(x=430,y=210,width=250)


        listbox_tasks=tk.Listbox(removeBody,bg='#C0C5CE', fg='black', font=('Times New Roman', 14), selectmode=tk.SINGLE)
        listbox_tasks.place(x=30, y=100, width=250, height=230)

        with open('%s.csv' % CURRENTUSER, 'r') as file:
            reader = csv.reader(file)
            next(reader)  
            for row in reader:
                listbox_tasks.insert('end', row[0])

                
        def remove():
            task_name= entTaskNameR.get()
            date=entDateR.get()
            selected_index=listbox_tasks.curselection()

            if task_name and date:
                with open('%s.csv' % CURRENTUSER,'r') as file:
                    content=csv.reader(file)
                    data=list(content)
                    
                removed=False
                for i,row in enumerate(data):
                    if row[0]==task_name and row[1]==date:
                        data.pop(i)
                        removed=True
                        break

                if removed:
                    with open('%s.csv' % CURRENTUSER,'w',newline='') as file:
                        writer=csv.writer(file)
                        writer.writerows(data)
                    messagebox.showinfo('RemoveTask Success','Task Successfully Removed')
                    if selected_index:
                        listbox_tasks.delete(selected_index)
                else:
                    messagebox.showerror('Error','Task not found!')
            else:
                if selected_index:
                    selected_task=listbox_tasks.get(selected_index)
                    listbox_tasks.delete(selected_index)
                    messagebox.showinfo('RemoveTask Success','Task Successfully Removed')

                    with open('%s.csv' % CURRENTUSER,'r') as file:
                        content=csv.reader(file)
                        data=list(content)

                    removed=False
                    for i, row in enumerate(data):
                        if row[0] == selected_task:
                            data.pop(i)
                            removed = True
                            break
                    if removed:
                        with open('%s.csv' % CURRENTUSER, 'w', newline='') as file:
                            writer = csv.writer(file)
                            writer.writerows(data)
                else:
                    messagebox.showerror('Error','Please enter both task name and date.')

        def on_select_task(event):
            selected_task=listbox_tasks.get(tk.ACTIVE)
            entTaskNameR.delete(0,'end')
            entTaskNameR.insert('end',selected_task)

        listbox_tasks.bind('<<ListboxSelect>>',on_select_task)
            
        btnRemoveTask=Button(removeBody,text='Remove',command=remove,bg='lightgrey')
        btnRemoveTask.place(x=300,y=360)
        btnRemoveTask.config(font=('Times New Roman',20))

        btnHome=Button(removeBody,text='Main Page',command=lambda:[wdRemove.destroy(), wdMain.destroy(), mainmenuWin()],bg='#ffe6cb')
        btnHome.place(x=10,y=5)
        btnHome.config(font=('Times New Roman',14))

        wdRemove.mainloop()
    else:
        messagebox.showerror('Error','No tasks added yet.')
        mainmenuWin()

############################### EDIT TASK WINDOW ###############################

def editTaskWin(wdMain):
    filename=f'{CURRENTUSER}.csv'
    if os.path.exists(filename):
        wdEdit=tk.Toplevel()
        wdEdit.title('Edit Task')
        wdEdit.geometry('1000x500')
        wdEdit.resizable(width=False,height=False)

        editBody=tk.Frame(wdEdit,bg='#ece0ba',height=500,width=1000)
        editBody.grid(row=0,column=0)

        logo=Image.open('CMPT 120 Logo.png')
        logo_resized=logo.resize((100,100))
        new_logo=ImageTk.PhotoImage(logo_resized)
        logo_label=tk.Label(editBody,image=new_logo,bg='#ece0ba')
        logo_label.place(x=890,y=10)

        def edit_select_task():
            selected_task=listbox_tasks.get(tk.ACTIVE)
            with open('%s.csv' % CURRENTUSER,'r') as file:
                reader=csv.reader(file)
                tasks=list(reader)
                for i, row in enumerate(tasks):
                    if row[0]==selected_task:
                        new_task_name=entNewTask.get().strip() if entNewTask.get().strip() else row[0]
                        new_date=entNewDate.get().strip() if entNewDate.get().strip() else row[1]
                        new_duration=entNewDuration.get().strip() if entNewDuration.get().strip() else row[2]
                        new_description=entNewDescrip.get().strip() if entNewDescrip.get().strip() else row[3]
                        tasks[i] = [new_task_name, new_date, new_duration, new_description]
                        break
            with open('%s.csv'% CURRENTUSER,'w',newline='') as file:
                writer=csv.writer(file)
                writer.writerow(["Task Name", "Date", "Duration", "Description"])
                writer.writerows(tasks[1:])

            messagebox.showinfo('Success','Task successfully edited!')
     
        listbox_tasks=tk.Listbox(editBody,bg='#C0C5CE',fg='black',font=('Times New Roman',14),selectmode=tk.SINGLE)
        listbox_tasks.place(x=50,y=100,width=300,height=350)

        with open('%s.csv' % CURRENTUSER, 'r') as file:
            reader = csv.reader(file)
            next(reader)  
            for row in reader:
                listbox_tasks.insert('end', row[0])

        btnSubmit=Button(editBody,text='Submit',command=edit_select_task)
        btnSubmit.place(x=865,y=425)
        btnSubmit.config(font=('Times New Roman',20))
        
        editTitle=tk.Label(editBody,text='Edit Task',bg='#ece0ba',fg='black')
        editTitle.config(font=('Times New Roman',28))
        editTitle.place(x=445,y=30)

        btnHome=Button(editBody,text='Main Page',command=lambda:[wdEdit.destroy(), wdMain.destroy(), mainmenuWin()],bg='#ece0ba')
        btnHome.place(x=10,y=5)
        btnHome.config(font=('Times New Roman',14))

        lblNewTask=tk.Label(editBody,text='New Task Name: ',bg='#ece0ba',fg='black')
        lblNewTask.config(font=('Times New Roman',20))
        lblNewTask.place(x=400,y=125)

        global entNewTask
        entNewTask=tk.Entry(editBody,bg='#C0C5CE',fg='black')
        entNewTask.config(font=('Times New Roman',16))
        entNewTask.place(x=570,y=120,width=350,height=50)

        lblNewDate=tk.Label(editBody,text='New Date: ',bg='#ece0ba',fg='black')
        lblNewDate.config(font=('Times New Roman',20))
        lblNewDate.place(x=400,y=185)

        global entNewDate
        entNewDate=tk.Entry(editBody,bg='#C0C5CE',fg='black')
        entNewDate.config(font=('Times New Roman',16))
        entNewDate.place(x=570,y=180,width=350,height=50)

        lblNewDuration=tk.Label(editBody,text='New Duration: ',bg='#ece0ba',fg='black')
        lblNewDuration.config(font=('Times New Roman',20))
        lblNewDuration.place(x=400,y=245)

        global entNewDuration
        entNewDuration=tk.Entry(editBody,bg='#C0C5CE',fg='black')
        entNewDuration.config(font=('Times New Roman',16))
        entNewDuration.place(x=570,y=240,width=350,height=50)


        lblNewDescrip=tk.Label(editBody,text='New Description: ',bg='#ece0ba',fg='black')
        lblNewDescrip.config(font=('Times New Roman',20))
        lblNewDescrip.place(x=400,y=305)

        global entNewDescrip
        entNewDescrip=tk.Entry(editBody,bg='#C0C5CE',fg='black')
        entNewDescrip.config(font=('Times New Roman',16))
        entNewDescrip.place(x=570,y=300,width=400,height=100)
        
        wdEdit.mainloop()
    else:
        messagebox.showerror('Error','No tasks added yet.')
        mainmenuWin()

#################### SEARCH WINDOW ######################

def searchTaskWin(wdMain):
    filename=f'{CURRENTUSER}.csv'
    if os.path.exists(filename):
        task_data=[]
        
        def search():

            searched_text = entSearch.get().lower()

            listbox_tasks.delete(0,'end')
            task_data.clear()

            with open('%s.csv' % CURRENTUSER,'r') as file:
                reader=csv.reader(file)
                next(reader)
                for row in reader:
                    task_name = row[0].lower()
                    date = row[1].lower()
                    duration = row[2].lower()
                    description=row[3]
                    if searched_text in task_name or searched_text in date or searched_text in duration:
                        listbox_tasks.insert('end',f'{task_name}, {date}')
                        task_data.append((task_name,date,duration,description))

        def show_task_info():
            selected_task_index=listbox_tasks.curselection()
            if selected_task_index:
                selected_task=listbox_tasks.get(selected_task_index[0])
                messagebox.showinfo('Task Information',selected_task)
            else:
                messagebox.showerror('Error','Please select a task from the list')

        def more_info():
            selected_task_index=listbox_tasks.curselection()
            if selected_task_index:
                selected_task=listbox_tasks.get(selected_task_index[0])
                task_name,date=selected_task.split(', ')
                task_info=[task for task in task_data if task[0] == task_name and task[1] == date]
                if task_info:
                    task_info=task_info[0]
                    entSearchName.delete(0,'end')
                    entSearchName.insert(0, task_info[0])
                    entSearchDate.delete(0, 'end')
                    entSearchDate.insert(0, task_info[1])
                    entSearchDuration.delete(0, 'end')
                    entSearchDuration.insert(0, task_info[2])
                    entDescrip.delete(0, 'end')
                    entDescrip.insert(0, task_info[3])
                else:
                    messagebox.showerror('Error', 'Task information not found.')
            else:
                messagebox.showerror('Error', 'Please select a task from the list.')


        wdSearch=tk.Toplevel()
        wdSearch.title('Search Page')
        wdSearch.geometry('700x500')
        wdSearch.resizable(width=False,height=False)

        searchBody=tk.Frame(wdSearch,bg='#dcedc1',width=700,height=500)
        searchBody.grid(row=0,column=0)

        logo=Image.open('CMPT 120 Logo.png')
        logo_resized=logo.resize((100,100))
        new_logo=ImageTk.PhotoImage(logo_resized)
        logo_label=tk.Label(searchBody,image=new_logo,bg='#dcedc1')
        logo_label.place(x=590,y=10)

        #Title
        lblSearchTitle=tk.Label(searchBody,text = 'Search Task', bg='#dcedc1',fg='black')
        lblSearchTitle.config(font=('Times New Roman',28))
        lblSearchTitle.place(x=280,y=50)

        btnTMS=Button(searchBody, text = 'Main Page',command=lambda:[wdSearch.destroy(), wdMain.destroy(), mainmenuWin()], bg='#dcedc1')
        btnTMS.config(font=('Times New Roman',16))
        btnTMS.place(x=1,y=1)

        #Search

        listbox_tasks=tk.Listbox(searchBody,bg='#C0C5CE', fg='black', font=('Times New Roman', 16))
        listbox_tasks.place(x=40,y=150,width=300,height=300)

        btnMoreInfo=Button(searchBody,text='More Info',command=more_info,bg='grey',fg='white')
        btnMoreInfo.config(font=('Times New Roman',13))
        btnMoreInfo.place(x=40,y=450,width=185)
        
        entSearch=tk.Entry(searchBody,bg='#ddf2fd',fg='black')
        entSearch.config(font=("Times New Roman",16))
        entSearch.place(x=40,y=125,height=25,width=185)

        btnSearch=Button(searchBody,text='Search',command=search,bg='grey',fg='white')
        btnSearch.config(font=('Times New Roman',13))
        btnSearch.place(x=230,y=125)


        lblSearchName=tk.Label(searchBody,text="Task Name: ",bg='#dcedc1',fg='black')
        lblSearchName.config(font=("Times New Roman",18))
        lblSearchName.place(x=350,y=150)
        entSearchName = tk.Entry(searchBody,bg='#ddf2fd',fg='black')
        entSearchName.config(font=("Times New Roman",16))
        entSearchName.place(x=480,y=150,height=30,width=200)

        lblSearchDate=tk.Label(searchBody,text="Date: ",bg='#dcedc1',fg='black')
        lblSearchDate.config(font=("Times New Roman",18))
        lblSearchDate.place(x=350,y=200)
        entSearchDate = tk.Entry(searchBody,bg='#ddf2fd',fg='black')
        entSearchDate.config(font=("Times New Roman",16))
        entSearchDate.place(x=480,y=200,height=30,width=200)

        lblSearchDuration=tk.Label(searchBody,text="Duration: ",bg='#dcedc1',fg='black')
        lblSearchDuration.config(font=("Times New Roman",18))
        lblSearchDuration.place(x=350,y=250)
        entSearchDuration = tk.Entry(searchBody,bg='#ddf2fd',fg='black')
        entSearchDuration.config(font=("Times New Roman",16))
        entSearchDuration.place(x=480,y=250,height=30,width=200)

        lblSearchDescrip=tk.Label(searchBody,text='Description: ',bg='#dcedc1',fg='black')
        lblSearchDescrip.config(font=("Times New Roman",18))
        lblSearchDescrip.place(x=350,y=300)
        entDescrip=tk.Entry(searchBody, bg='#ddf2fd', fg='black')
        entDescrip.config(font=("Times New Roman",16))
        entDescrip.place(x=480, y=300, height=70, width=200)


        wdSearch.mainloop()
    else:
        messagebox.showerror('Error','No tasks added yet.')
        mainmenuWin()

################ABOUT US PAGE##################################
def aboutUs(wdMain):
    wdAbout=tk.Toplevel()
    wdAbout.title('About Us Page')
    wdAbout.geometry('700x500')
    wdAbout.resizable(width=False,height=False)
    
    AboutBody=tk.Frame(wdAbout,bg='whitesmoke',width=700,height=500)
    AboutBody.grid(row=0,column=0)

    logo=Image.open('CMPT 120 Logo.png')
    logo_resized=logo.resize((100,100))
    new_logo=ImageTk.PhotoImage(logo_resized)
    logo_label=tk.Label(AboutBody,image=new_logo,bg='whitesmoke')
    logo_label.place(x=590,y=10)

    lblAboutTitle=tk.Label(AboutBody,text = 'About Us', bg='whitesmoke',fg='black')
    lblAboutTitle.config(font=('Times New Roman',35))
    lblAboutTitle.place(x=270,y=55)

    lblMadison=tk.Label(AboutBody,text='Madison Chan', bg='whitesmoke',fg='black')
    lblMadison.config(font=('Times New Roman',22))
    lblMadison.place(x=100,y=150)

    maddieInfo=('Madison is a sophomore at Marist College, majoring in Business Administration – Marketing and minoring in Graphic Design & Data Science and Analytics. You can contact her at madison.chan1@marist.edu.')

    txtMadison=Text(AboutBody,bg='whitesmoke',height=8,width=25,wrap='word',fg='black')
    txtMadison.insert('end',maddieInfo)
    txtMadison.config(font=('Times New Roman',16),state='disabled')
    txtMadison.place(x=80,y=200)

    lblGabriela=tk.Label(AboutBody,text='Gabriela Ramon', bg='whitesmoke',fg='black')
    lblGabriela.config(font=('Times New Roman',22))
    lblGabriela.place(x=410,y=150)

    gabyInfo=('Gabriela is a freshman at Marist College, studying Applied Mathematics with a minor in Data Science and Analytics. You can contact her at gabriela.ramon1@marist.edu.')

    txtGabriela=Text(AboutBody,bg='whitesmoke',height=8,width=25,wrap='word',fg='black')
    txtGabriela.insert('end',gabyInfo)
    txtGabriela.config(font=('Times New Roman',16),state='disabled')
    txtGabriela.place(x=390,y=200)


    btnBack = Button(AboutBody, text='Back', command=lambda:[wdAbout.destroy(), mainmenuWin()])
    btnBack.config(font=('Times New Roman', 16))
    btnBack.place(x=320, y=425)

    wdAbout.mainloop()


#####################ADD USER WINDOW####################
def addUserWin():
    def addUser():
        username=entUsername.get().strip()
        password=entPassword.get().strip()
        if username and password:
            with open('users.csv','r') as file:
                reader=csv.reader(file)
                for row in reader:
                    if row and row[0]==username:
                        messagebox.showerror('Error','Username already exists.')
                        return
            with open('users.csv','a',newline='') as file:
                writer=csv.writer(file)
                writer.writerow([username,password])

            messagebox.showinfo('Success',f'User "{username}" successfully added.')
            wdAddUser.destroy()
            loginWindow()
            
        else:
            messagebox.showerror('Error','Please enter both username and password.')


    wdAddUser=tk.Toplevel()
    wdAddUser.title('Add User')
    wdAddUser.geometry('400x200')
    wdAddUser.resizable(width=False, height=False)

    lblAddUserTitle=tk.Label(wdAddUser,text='Add User')
    lblAddUserTitle.config(font=('Times New Roman',20))
    lblAddUserTitle.place(x=155,y=10)

    lblUsername = tk.Label(wdAddUser, text='Username:')
    lblUsername.config(font=('Times New Roman', 16))
    lblUsername.place(x=40, y=50)

    entUsername = tk.Entry(wdAddUser, bg='white', fg='black')
    entUsername.config(font=('Times New Roman', 16))
    entUsername.place(x=160, y=50)

    lblPassword = tk.Label(wdAddUser, text='Password:')
    lblPassword.config(font=('Times New Roman', 16))
    lblPassword.place(x=40, y=100)

    entPassword = tk.Entry(wdAddUser, show='*', bg='white', fg='black')
    entPassword.config(font=('Times New Roman', 16))
    entPassword.place(x=160, y=100)

    btnAddUser = Button(wdAddUser, text='Add User', command=addUser)
    btnAddUser.config(font=('Times New Roman', 16))
    btnAddUser.place(x=100, y=150)

    btnBack = Button(wdAddUser, text='Back', command=lambda:[wdAddUser.destroy(), mainmenuWin()])
    btnBack.config(font=('Times New Roman', 16))
    btnBack.place(x=240, y=150)

    wdAddUser.mainloop()

###########REMOVE USER WINDOW##################
def removeUserWin():
    def removeUser():
        selected_user=users_listbox.get(tk.ACTIVE)
        users_listbox.delete(tk.ACTIVE)
        remove_user_from_csv(selected_user)

    def remove_user_from_csv(username):
        with open('users.csv','r') as file:
            lines=file.readlines()
        with open ('users.csv','w') as file:
            for line in lines:
                if line.strip() != username:
                    file.write(line)

    def load_users():
        with open('users.csv','r') as file:
            reader=csv.reader(file)
            next(reader)
            users=[row[0] for row in reader]
        return users

    wdRemoveUser=tk.Toplevel()
    wdRemoveUser.title('Remove User')
    wdRemoveUser.geometry('700x400')
    wdRemoveUser.resizable(width=False,height=False)

    remove_body=tk.Frame(wdRemoveUser,height=400,width=700)
    remove_body.grid(row=0,column=0)

    lblRemoveUser_Title=tk.Label(remove_body,text='Remove User')
    lblRemoveUser_Title.config(font=('Times New Roman',22))
    lblRemoveUser_Title.place(x=285,y=10)

    users_listbox=tk.Listbox(remove_body,width=50,height=15,font=('Times New Roman',16))
    users_listbox.place(x=150,y=70)

    users=load_users()
    for user in users:
        users_listbox.insert('end',user)

    btnRemoveUser=Button(remove_body,text='Remove User',command=removeUser)
    btnRemoveUser.config(font=('Times New Roman',16))
    btnRemoveUser.place(x=200,y=360)

    btnBack = Button(remove_body, text='Back', command=lambda:[wdRemoveUser.destroy(), mainmenuWin()])
    btnBack.config(font=('Times New Roman', 16))
    btnBack.place(x=450, y=360)

    wdRemoveUser.mainloop()

###############CHANGE USERNAME WINDOW##############
def changeUserWin():

    def update_user_in_csv(old_user,new_user):
        temp_file='temp_users.csv'
        with open('users.csv','r') as file, open(temp_file,'w',newline='') as temp:
            csvreader=csv.reader(file,delimiter=',')
            csvwriter=csv.writer(temp,delimiter=',')
            for row in csvreader:
                if row[0]==old_user:
                    row[0]=new_user
                csvwriter.writerow(row)
        os.replace(temp_file,'users.csv')
    
    def change_user():
        old_user=entOldUser.get().strip()
        new_user=entNewUser.get().strip()
        try:
            if old_user != CURRENTUSER:
                raise ValueError('You can only change your own username.')
            update_user_in_csv(old_user,new_user)
            messagebox.showinfo("Success", "Username changed successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    wdChangeUser=tk.Toplevel()
    wdChangeUser.title('Change Username')
    wdChangeUser.geometry('500x300')
    wdChangeUser.resizable(width=False, height=False)

    changeUserBody = tk.Frame(wdChangeUser, height=300, width=500)
    changeUserBody.grid(row=0, column=0)

    lblChangeUserTitle=tk.Label(changeUserBody,text='Change Username')
    lblChangeUserTitle.config(font=('Times New Roman', 22))
    lblChangeUserTitle.place(x=160, y=10)

    lblOldUsername = tk.Label(changeUserBody, text='Old Username:')
    lblOldUsername.config(font=('Times New Roman', 16))
    lblOldUsername.place(x=50, y=70)

    entOldUser = tk.Entry(changeUserBody, width=30, font=('Times New Roman', 16))
    entOldUser.place(x=200, y=70)

    lblNewUsername=tk.Label(changeUserBody,text='New Username: ')
    lblNewUsername.config(font=('Times New Roman',16))
    lblNewUsername.place(x=50,y=120)

    entNewUser=tk.Entry(changeUserBody,width=30,font=('Times New Roman',16))
    entNewUser.place(x=200,y=120)

    btnChangeUser=Button(changeUserBody,text='Change Username',command=change_user)
    btnChangeUser.config(font=('Times New Roman', 16))
    btnChangeUser.place(x=80, y=200)

    btnBack = Button(changeUserBody, text='Back', command=lambda:[wdChangeUser.destroy(), mainmenuWin()])
    btnBack.config(font=('Times New Roman', 16))
    btnBack.place(x=300, y=200)

    wdChangeUser.mainloop()


#################### CHANGE PASSWORD WINDOW ####################

def changePassWin():

    def update_pass_in_csv(old_pass,new_pass):
        temp_file='temp_users.csv'
        with open('users.csv','r') as file, open(temp_file,'w',newline='') as temp:
            csvreader=csv.reader(file,delimiter=',')
            csvwriter=csv.writer(temp,delimiter=',')
            for row in csvreader:
                if row[1]==old_pass:
                    row[1]=new_pass
                csvwriter.writerow(row)
        os.replace(temp_file,'users.csv')
    
    def change_pass():
        old_pass=entOldPass.get().strip()
        new_pass=entNewPass.get().strip()
        try:
            if old_pass != CURRENTPASS:
                raise ValueError('You can only change your own password.')
            update_pass_in_csv(old_pass,new_pass)
            messagebox.showinfo("Success", "Username changed successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    wdChangePass=tk.Toplevel()
    wdChangePass.title('Change Username')
    wdChangePass.geometry('500x300')
    wdChangePass.resizable(width=False, height=False)

    changePassBody = tk.Frame(wdChangePass, height=300, width=500)
    changePassBody.grid(row=0, column=0)

    lblChangePassTitle=tk.Label(changePassBody,text='Change Password')
    lblChangePassTitle.config(font=('Times New Roman', 22))
    lblChangePassTitle.place(x=160, y=10)

    lblOldPassword = tk.Label(changePassBody, text='Old Password:')
    lblOldPassword.config(font=('Times New Roman', 16))
    lblOldPassword.place(x=50, y=70)

    entOldPass = tk.Entry(changePassBody, width=30, font=('Times New Roman', 16))
    entOldPass.place(x=200, y=70)

    lblNewPassword=tk.Label(changePassBody,text='New Password: ')
    lblNewPassword.config(font=('Times New Roman',16))
    lblNewPassword.place(x=50,y=120)

    entNewPass=tk.Entry(changePassBody,width=30,font=('Times New Roman',16))
    entNewPass.place(x=200,y=120)

    btnChangePass=Button(changePassBody,text='Change Password',command=change_pass)
    btnChangePass.config(font=('Times New Roman', 16))
    btnChangePass.place(x=80, y=200)

    btnBack = Button(changePassBody, text='Back', command=lambda:[wdChangePass.destroy(), mainmenuWin()])
    btnBack.config(font=('Times New Roman', 16))
    btnBack.place(x=300, y=200)

    wdChangePass.mainloop()


#################### SETTINGS WINDOW  ######################

def settingsWin(wdMain):

    wdSettings=tk.Toplevel()
    wdSettings.title('Settings Page')
    wdSettings.geometry('700x500')
    wdSettings.resizable(width=False,height=False)

    settingsBody=tk.Frame(wdSettings,bg='thistle',width=700,height=500)
    settingsBody.grid(row=0,column=0)

    logo=Image.open('CMPT 120 Logo.png')
    logo_resized=logo.resize((100,100))
    new_logo=ImageTk.PhotoImage(logo_resized)
    logo_label=tk.Label(settingsBody,image=new_logo,bg='thistle')
    logo_label.place(x=590,y=10)

    #Title
    lblSettingsTitle=tk.Label(settingsBody,text = 'Settings', bg='thistle')
    lblSettingsTitle.config(font=('Times New Roman',28))
    lblSettingsTitle.place(x=300,y=75)

    #Buttons
    
    btnTMS=Button(settingsBody,text = 'Main Page',command=lambda:[wdSettings.destroy(), wdMain.destroy(), mainmenuWin()],bg='thistle')
    btnTMS.config(font=('Times New Roman',16))
    btnTMS.place(x=1,y=1)

    btnAddUser=Button(settingsBody,text='Add User',command=lambda:[wdSettings.destroy(), addUserWin()],bg='white')
    btnAddUser.config(font=('Times New Roman',20))
    btnAddUser.place(x=280,y=150)

    btnRemoveUser=Button(settingsBody,text='Remove User',command=lambda:[wdSettings.destroy(), removeUserWin()],bg='white')
    btnRemoveUser.config(font=('Times New Roman',20))
    btnRemoveUser.place(x=270,y=220)

    btnChangeUn=Button(settingsBody,text='Change Username',command=lambda:[wdSettings.destroy(), changeUserWin()],bg='white')
    btnChangeUn.config(font=('Times New Roman',20))
    btnChangeUn.place(x=250,y=290)

    btnChangePass=Button(settingsBody,text='Change Password',command=lambda:[wdSettings.destroy(), changePassWin()],bg='white')
    btnChangePass.config(font=('Times New Roman',20))
    btnChangePass.place(x=255,y=360)

    wdSettings.mainloop()


#################### CALENDAR PAGE WINDOW  ######################

global_logo=None

def calendarWin(wdMain):
    global global_logo
    y_position=210
    filename=f'{CURRENTUSER}.csv'
    if os.path.exists(filename):
        wdCalendar=Tk()
        wdCalendar.title('Calendar Page')
        wdCalendar.geometry('700x500')
        wdCalendar.resizable(width=False,height=False)

        calBody=tk.Frame(wdCalendar,bg='lightskyblue',width=700,height=500)
        calBody.grid(row=0,column=0)

                
        #Title
        lblCalendarTitle=tk.Label(calBody,text = 'Calendar', bg='lightskyblue')
        lblCalendarTitle.config(font=('Times New Roman',28))
        lblCalendarTitle.place(x=50,y=70)


        #Calendar Labels
        today=date.today().strftime('%B %d, %Y')
        lblToday=tk.Label(calBody,text=(f'Today: {today}'),bg='lightskyblue')
        lblToday.config(font=("Times New Roman",18))
        lblToday.place(x=50,y=125)

        lblUpcoming=tk.Label(calBody,text='Upcoming Tasks: ',bg='lightskyblue')
        lblUpcoming.config(font=("Times New Roman",18))
        lblUpcoming.place(x=50,y=170)

        with open(filename,'r') as f:
            reader=csv.reader(f)
            next(reader, None)
            for row in reader:
                show=row[1]
                task=row[0]
                lblDate=tk.Label(calBody, text=show,font=("Times New Roman",16))
                lblDate.config(padx=10)
                lblDate.place(x=75, y=y_position)
                lblTask=tk.Label(calBody, text=task,font=("Times New Roman",16),width=25,anchor='w')
                lblTask.config(padx=20)
                lblTask.place(x=155, y=y_position)
                y_position += 35
                
       
        btnHome=Button(calBody,text='Main Page',command=lambda:[wdCalendar.destroy(), wdMain.destroy(), mainmenuWin()],bg='lightskyblue')
        btnHome.place(x=1,y=1)
        btnHome.config(font=('Times New Roman',16))
  
        wdCalendar.mainloop()


##############LOGIN WINDOW AFTER MAIN MENU################

def loginWindowMM():
    global global_logo
    global new_logo
    os.chdir('/Users/MadisonChan_1/Downloads/Marist/Spring 2024/CMPT 120 - Intro to Programming/Final Project')

    
    def login():
        enteredUser=entUsername.get()
        enteredPass=entPassword.get()
        data=[]
        with open('users.csv') as csvfile:
            reader=csv.reader(csvfile)
            for row in reader:
                data.append(row)
        col0=[x[0] for x in data]
        col1=[x[1] for x in data]

        if enteredUser in col0:
            for k in range(0,len(col0)):
                if col0[k]==enteredUser and col1[k]==enteredPass:
                    messagebox.showinfo('Admin Login Success',f'    Welcome {enteredUser}    ')
                    global CURRENTUSER
                    CURRENTUSER = enteredUser
                    global CURRENTPASS
                    CURRENTPASS = enteredPass
                    wdLogin.destroy()
                    mainmenuWin()
                    return
            messagebox.showinfo('User Login Fail','Incorrect password')
        else:
            messagebox.showinfo('User Login Fail','Please enter a correct username and password')
    
    wdLogin=tk.Toplevel()
    wdLogin.title('Login')
    wdLogin.geometry('700x375')
    wdLogin.resizable(width=False,height=False)

    body=tk.Frame(wdLogin,bg='snow',height=375,width=750)
    body.grid(row=0,column=0)

    logo=Image.open('CMPT 120 Logo.png')
    logo_resized=logo.resize((100,100))
    new_logo=ImageTk.PhotoImage(logo_resized)
    
    logo_label=tk.Label(body,image=new_logo,bg='snow')
    logo_label.place(x=580,y=10)


    lblUsername=tk.Label(body,text='Username: ',bg='snow',fg='black')
    lblUsername.config(font=('Times New Roman',20))
    lblUsername.place(x=150,y=120)

    entUsername=tk.Entry(body,bg='lightblue',fg='black')
    entUsername.config(font=('Times New Roman',20))
    entUsername.place(x=300,y=120,width=300,height=40)


    lblPassword=tk.Label(body,text='Password: ',bg='snow',fg='black')
    lblPassword.config(font=('Times New Roman',20))
    lblPassword.place(x=150,y=190)

    entPassword=tk.Entry(body,bg='lightblue',fg='black')
    entPassword.config(font=('Times New Roman',20),show='*')
    entPassword.place(x=300,y=190,width=300,height=40)


    loginTitle=tk.Label(body,text='Task Management System',bg='snow',fg='black')
    loginTitle.config(font=('Times New Roman',28))
    loginTitle.place(x=200,y=30)


    btnLogin=Button(body,text='Login',command=login,bg='#ddf2fd')
    btnLogin.place(x=350,y=260)
    btnLogin.config(font=('Times New Roman',20))
    def exit_app():
        messagebox.showinfo('Exit','Thank you for using this application')
        wdLogin.destroy()

    btnExit=Button(body,text='Exit',command=exit_app,bg='#ddf2fd')
    btnExit.place(x=510,y=260)
    btnExit.config(font=('Times New Roman',20))

    btnNewUser=Button(body,text='New User',command=lambda:[wdLogin.destroy(), addUserWin()],bg='#ddf2fd')
    btnNewUser.place(x=510,y=310)
    btnNewUser.config(font=('Times New Roman',15))

    wdLogin.mainloop()

#################### MAIN PAGE WINDOW  ######################

def mainmenuWin():
    
    def exit_app_mm():
        messagebox.showinfo('Exit','Thank you for using this application')
        wdMain.destroy()
    
    wdMain=tk.Toplevel()
    wdMain.title('Main Menu Page')
    wdMain.geometry('720x500')
    wdMain.resizable(width=False,height=False)

    mainBody=tk.Frame(wdMain,bg='white',height=500,width=720)
    mainBody.grid(row=0,column=0)
    
    logo=Image.open('CMPT 120 Logo.png')
    logo_resized=logo.resize((100,100))
    new_logo=ImageTk.PhotoImage(logo_resized)
    logo_label1=tk.Label(mainBody,image=new_logo,bg='white')
    logo_label1.place(x=610,y=10)

    #Main Title
    lblMainTitle=tk.Label(mainBody,text = 'Task Management System', bg='white',fg='black')
    lblMainTitle.config(font=('Times New Roman',28))
    lblMainTitle.place(x=200,y=30)

    #Action Buttons
    btnMainAdd=Button(mainBody,text='Add Task',bg='pink',command=lambda:[wdMain.destroy(),addTaskWin(wdMain)])
    btnMainAdd.config(font=('Times New Roman',20))
    btnMainAdd.place(x=185,y=130)

    btnMainEdit=Button(mainBody,text='Edit Task',bg='gold',command=lambda:[wdMain.destroy(),editTaskWin(wdMain)])
    btnMainEdit.config(font=('Times New Roman',20))
    btnMainEdit.place(x=185,y=210)

    btnMainRemove=Button(mainBody,text='Remove Task',bg='sandybrown',command=lambda:[wdMain.destroy(),removeTaskWin(wdMain)])
    btnMainRemove.config(font=('Times New Roman',20))
    btnMainRemove.place(x=175,y=290)

    btnMainSearch=Button(mainBody,text='Search',bg='lightgreen',command=lambda:[wdMain.destroy(),searchTaskWin(wdMain)])
    btnMainSearch.config(font=('Times New Roman',20))
    btnMainSearch.place(x=400,y=130)

    btnMainCalendar=Button(mainBody,text='Calendar',bg='lightskyblue',command=lambda:[wdMain.destroy(),calendarWin(wdMain)])
    btnMainCalendar.config(font=('Times New Roman',20))
    btnMainCalendar.place(x=395,y=210)

    btnMainSettings=Button(mainBody,text='Settings',bg='mediumpurple',command=lambda:[wdMain.destroy(),settingsWin(wdMain)])
    btnMainSettings.config(font=('Times New Roman',20))
    btnMainSettings.place(x=400,y=290)

    btnAboutUs=Button(mainBody,text='About Us',bg='pink',command=lambda:[wdMain.destroy(),aboutUs(wdMain)])
    btnAboutUs.config(font=('Times New Roman',20))
    btnAboutUs.place(x=300,y=380)

    btnExit=Button(mainBody,text='Exit',bg='#ddf2fd',command=exit_app_mm)
    btnExit.config(font=('Times New Roman',18))
    btnExit.place(x=310,y=430)

    btnLogOut=Button(mainBody,text='Log Out',bg='#ddf2fd',command=lambda:[wdMain.destroy(),loginWindowMM()])
    btnLogOut.config(font=('Times New Roman',14))
    btnLogOut.place(x=20,y=5)

    wdMain.mainloop()


#################LOGIN WINDOW####################


def loginWindow():
    global global_logo
    global new_logo
    os.chdir('/Users/MadisonChan_1/Downloads/Marist/Spring 2024/CMPT 120 - Intro to Programming/Final Project')

    
    def login():
        enteredUser=entUsername.get()
        enteredPass=entPassword.get()
        data=[]
        with open('users.csv') as csvfile:
            reader=csv.reader(csvfile)
            for row in reader:
                data.append(row)
        col0=[x[0] for x in data]
        col1=[x[1] for x in data]

        if enteredUser in col0:
            for k in range(0,len(col0)):
                if col0[k]==enteredUser and col1[k]==enteredPass:
                    messagebox.showinfo('Admin Login Success',f'    Welcome {enteredUser}    ')
                    global CURRENTUSER
                    CURRENTUSER = enteredUser
                    global CURRENTPASS
                    CURRENTPASS = enteredPass
                    wdLogin.destroy()
                    mainmenuWin()
                    return
            messagebox.showinfo('User Login Fail','Incorrect password')
        else:
            messagebox.showinfo('User Login Fail','Please enter a correct username and password')
    
    wdLogin=tk.Tk()
    wdLogin.title('Login')
    wdLogin.geometry('700x375')
    wdLogin.resizable(width=False,height=False)

    body=tk.Frame(wdLogin,bg='snow',height=375,width=750)
    body.grid(row=0,column=0)

    logo1=Image.open('CMPT 120 Logo.png')
    logo_resized1=logo1.resize((100,100))
    new_logo=ImageTk.PhotoImage(logo_resized1)
    
    logo_label=tk.Label(body,image=new_logo,bg='snow')
    logo_label.place(x=580,y=10)


    lblUsername=tk.Label(body,text='Username: ',bg='snow',fg='black')
    lblUsername.config(font=('Times New Roman',20))
    lblUsername.place(x=150,y=120)

    entUsername=tk.Entry(body,bg='lightblue',fg='black')
    entUsername.config(font=('Times New Roman',20))
    entUsername.place(x=300,y=120,width=300,height=40)


    lblPassword=tk.Label(body,text='Password: ',bg='snow',fg='black')
    lblPassword.config(font=('Times New Roman',20))
    lblPassword.place(x=150,y=190)

    entPassword=tk.Entry(body,bg='lightblue',fg='black')
    entPassword.config(font=('Times New Roman',20),show='*')
    entPassword.place(x=300,y=190,width=300,height=40)


    loginTitle=tk.Label(body,text='Task Management System',bg='snow',fg='black')
    loginTitle.config(font=('Times New Roman',28))
    loginTitle.place(x=200,y=30)


    btnLogin=Button(body,text='Login',command=login,bg='#ddf2fd')
    btnLogin.place(x=350,y=260)
    btnLogin.config(font=('Times New Roman',20))
    def exit_app():
        messagebox.showinfo('Exit','Thank you for using this application')
        wdLogin.destroy()

    btnExit=Button(body,text='Exit',command=exit_app,bg='#ddf2fd')
    btnExit.place(x=510,y=260)
    btnExit.config(font=('Times New Roman',20))

    btnNewUser=Button(body,text='New User',command=lambda:[wdLogin.destroy(), addUserWin()],bg='#ddf2fd')
    btnNewUser.place(x=510,y=310)
    btnNewUser.config(font=('Times New Roman',15))

    wdLogin.mainloop()


loginWindow()


#tasks=[]

#def update_task_list(result=None):
    #listbox.delete(0,'end')
  #  #if result is None:
      #  for task in tasks:
     #       task_info
#

###################
