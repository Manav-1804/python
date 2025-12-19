from tkinter import *
import mysql.connector
import tkinter.messagebox as msg


# ---------------- DATABASE CONNECTION ----------------
def create_conn():
    return mysql.connector.connect(
        host="localhost",
        database="python",
        user="root",
        password=""
    )


# ---------------- FUNCTIONS ----------------
def clear():
    e_fname.delete(0, END)
    e_lname.delete(0, END)
    e_email.delete(0, END)
    e_mobile.delete(0, END)


def data_insert():
    if e_fname.get()=="" or e_lname.get()=="" or e_email.get()=="" or e_mobile.get()=="":
        msg.showinfo("Insert Status","All Fields Are Mandatory")
    else:
        conn=create_conn()
        cursor=conn.cursor()
        query="insert into student(fname,lname,email,mobile) values(%s,%s,%s,%s)"
        cursor.execute(query,(e_fname.get(),e_lname.get(),e_email.get(),e_mobile.get()))
        conn.commit()
        clear()
        msg.showinfo("Insert Status","Data Inserted Successfully")
        conn.close()


def data_search():
    if e_id.get()=="":
        msg.showinfo("Search Status","ID Mandatory")
    else:
        clear()
        conn=create_conn()
        cursor=conn.cursor()
        cursor.execute("select * from student where id=%s",(e_id.get(),))
        row=cursor.fetchone()
        if row:
            e_fname.insert(0,row[1])
            e_lname.insert(0,row[2])
            e_email.insert(0,row[3])
            e_mobile.insert(0,row[4])
        else:
            msg.showinfo("Search Status","ID Not Found")
        conn.close()


def data_update():
    if e_id.get()=="" or e_fname.get()=="" or e_lname.get()=="" or e_email.get()=="" or e_mobile.get()=="":
        msg.showinfo("Update Status","All Fields Are Mandatory")
    else:
        conn=create_conn()
        cursor=conn.cursor()
        cursor.execute(
            "update student set fname=%s,lname=%s,email=%s,mobile=%s where id=%s",
            (e_fname.get(),e_lname.get(),e_email.get(),e_mobile.get(),e_id.get())
        )
        conn.commit()
        clear()
        msg.showinfo("Update Status","Data Updated Successfully")
        conn.close()


def data_delete():
    if e_id.get()=="":
        msg.showinfo("Delete Status","ID Mandatory")
    else:
        conn=create_conn()
        cursor=conn.cursor()
        cursor.execute("delete from student where id=%s",(e_id.get(),))
        conn.commit()
        clear()
        msg.showinfo("Delete Status","Data Deleted Successfully")
        conn.close()


# ---------------- UI DESIGN ----------------
root = Tk()
root.geometry("420x600")
root.title("Student Registration Form")
root.resizable(False,False)
root.configure(bg="#ecf0f1")

# Header
Label(root,text="Student Registration",
      bg="#2c3e50",fg="white",
      font=("Segoe UI",18,"bold"),
      pady=15).pack(fill=X)

# Main Frame
frame = Frame(root,bg="#ecf0f1",width=380,height=300)
frame.place(x=20,y=90)

font_lbl=("Segoe UI",11,"bold")
font_ent=("Segoe UI",11)

def lbl(txt,y):
    Label(frame,text=txt,font=font_lbl,bg="#ecf0f1").place(x=20,y=y)

def ent(y):
    e=Entry(frame,font=font_ent,bd=2,relief=RIDGE)
    e.place(x=150,y=y,width=200,height=30)
    return e

# Labels & Entries
lbl("ID",20)
lbl("First Name",70)
lbl("Last Name",120)
lbl("Email",170)
lbl("Mobile",220)

e_id = ent(20)
e_fname = ent(70)
e_lname = ent(120)
e_email = ent(170)
e_mobile = ent(220)

# Buttons
btn_font=("Segoe UI",11,"bold")

Button(root,text="INSERT",bg="#27ae60",fg="white",
       font=btn_font,width=12,command=data_insert).place(x=40,y=420)

Button(root,text="SEARCH",bg="#2980b9",fg="white",
       font=btn_font,width=12,command=data_search).place(x=220,y=420)

Button(root,text="UPDATE",bg="#f39c12",fg="white",
       font=btn_font,width=12,command=data_update).place(x=40,y=470)

Button(root,text="DELETE",bg="#c0392b",fg="white",
       font=btn_font,width=12,command=data_delete).place(x=220,y=470)

root.mainloop()
