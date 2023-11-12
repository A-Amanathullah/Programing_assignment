from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root =  Tk()
root.geometry("500x300")
root.title("Student Record Management System")
root.iconbitmap('icon.ico')

tab_control = ttk.Notebook(root)

tab1= ttk.Frame(tab_control)
tab_control.add(tab1, text="add marks")
tab_control.pack(expand = 1 , fill= "both")

tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text="show marks")
tab_control.pack(expand = 1 , fill= "both")

tab3 = ttk.Frame(tab_control)
tab_control.add(tab3, text="about")
tab_control.pack(expand = 1 , fill= "both")

#################################### To add student marks #######################################################

def msg_succes():
	info = messagebox.showinfo("information","Add successfully... ")
	return info
def msg_fail():
	warrning = messagebox.showwarning("warrning","Fill all the Required feild")
	return warrning

def clear():
	for boxes in tab1.winfo_children():
		if isinstance(boxes,Entry):
			boxes.delete(0,"end")
		if isinstance(boxes,ttk.Combobox):
			boxes.set("")

def save():
	student_name = name_value.get()
	student_id = id_value.get()
	module = module_value.get()
	grade = grade_value.get()
	
	if student_name and student_id and module and grade:
		data = student_name + "  :  " + student_id + "  :  " + module + "  :  " + grade + '\n'
		file = open("Students_data.txt","a")
		file.write(data)
		file.close()
		clear()
		file = open("Students_data.txt","r")
		value2 = file.readlines()
		msg_succes()
			
		my_table.insert(parent='', index='end' , iid=len(value2) , values = (student_name , student_id , module , grade))

	else:
		msg_fail()
		



Label(tab1, text="Add Student Marks", font = "times 15 bold").grid(row=0,column=3)

st_name = Label(tab1, text="Student Nmae:")
st_name.grid(row=1 , column = 2)
st_id = Label(tab1, text = "Student ID:")
st_id.grid(row=2 , column=2)
module_name = Label(tab1, text="Module Nmae:")
module_name.grid(row=3,column=2)
module_grade = Label(tab1, text="Module Grade:")
module_grade.grid(row=4,column=2)

name_value = StringVar()
id_value = StringVar()
module_value = StringVar()
grade_value = StringVar()

name_box = Entry (tab1,textvariable = name_value).grid(row=1,column=3)
id_box = Entry (tab1, textvariable = id_value).grid(row=2, column=3)
module_box = Entry(tab1, textvariable= module_value).grid(row=3,column=3)

m_grades= ["Distinction","Merit","Pass","Re-do","Repeat"]
grade_box = ttk.Combobox(tab1,values = m_grades ,textvariable=grade_value, width = 17 ,state="readonly").grid(row= 4 , column=3)

empty = Label(tab1, text="")
empty.grid(row=5 , column = 2)

empty1 = Label(tab1, text="        ")
empty1.grid(row=7 , column = 1)

button_submit = Button(tab1,text="Submit", command = save).grid(row=7 ,column=2)
button_clear = Button(tab1,text="Clear", command = lambda:clear()).grid(row=7 ,column=3)

################################################################################################################

###################################### To display marks ########################################################

my_table = ttk.Treeview(tab2)

my_table['columns'] = ("St_Name", "St_id", "Module_nmae" , "Module_grade")

my_table.column("#0", width=0 ,stretch=NO)
my_table.column("St_Name", width=120,anchor=W)
my_table.column("St_id", width=100, anchor=W)
my_table.column("Module_nmae", width=150, anchor=W)
my_table.column("Module_grade", width=100, anchor=W)


my_table.heading("#0", text="not want", anchor=W)
my_table.heading("St_Name",text="Student Name", anchor=W)
my_table.heading("St_id",text="Student ID", anchor=W)
my_table.heading("Module_nmae",text="Module Name", anchor=W)
my_table.heading("Module_grade",text="Module Grade", anchor=W)


#read txt file
file = open("Students_data.txt","r")
value = file.readlines()


for loop in range(0,len(value)):
    info = value[loop]
    final = info.split("\n")
    succes=final[0].split(":")
    my_table.insert(parent='', index='end' , iid=loop , values = succes)


my_table.pack(pady=20)

#####################################################################################################


###################################  Developer infomation  ##########################################

about = Label(tab3, text="Student Record Management system \n Version 0.0.1 \n Developer:A M A N A T H U L L A H. \n FROM CSD-18 \n FOR PROGRAMMING ASSIGNMENT.\n \u00A9 2023 - 2025 AMANATHULLAH Inc. \n ", font = "times 20 bold" , justify="center")
about.pack()

########################################################################################################

root.mainloop()