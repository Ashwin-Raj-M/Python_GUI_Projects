from distutils.util import execute
from tkinter import *
from tkinter import messagebox
import sqlite3
import tkinter

root=Tk()
root.title("Profile")

Label(root,text="Fill the following").grid(row=0,columnspan=2,pady=10)

#function for saving edits
def save_edit():
    #create or connect to a data base
    data=sqlite3.connect("profile.db")

    #creating a cursor
    cur=data.cursor()

    #updating the info
    cur.execute("""UPDATE profile SET
            first_name = :first,
            last_name = :last,
            address = :add,
            pincode = :pin,
            contact_no = :contact
            
            WHERE oid = :oid""",
            {
             'first' : f_name_edit.get(),
             'last' :  l_name_edit.get(),
             'add' : address_edit.get(),
             'pin' : pincode_edit.get(),
             'contact' : contact_no_edit.get(),
             'oid' : 3
            })

    #commit changes
    data.commit()

    #close connection
    data.close()

    edit_window.destroy()

    #success message
    tkinter.messagebox.showinfo("Data Edit","Data Edited successfully")

#function to create edit window
def edit():
    global edit_window
    edit_window=Toplevel()
    edit_window.title("Edit Window")

    #create or connect to a data base
    data=sqlite3.connect("profile.db")

    #creating a cursor
    cur=data.cursor()

    global record_id
    #record_id=edit_id.get()
    #Selecting the data
    cur.execute("SELECT * from profile WHERE oid = 3")
    records=cur.fetchall()

    #globalizing the variyables
    global f_name_edit
    global l_name_edit
    global address_edit
    global pincode_edit
    global contact_no_edit

    #creating text boxes
    f_name_edit=Entry(edit_window,width=30)
    f_name_edit.grid(row=1,column=1,padx=20,pady=10)

    l_name_edit=Entry(edit_window,width=30)
    l_name_edit.grid(row=2,column=1,padx=20,pady=10)

    address_edit=Entry(edit_window,width=30)
    address_edit.grid(row=3,column=1,padx=20,pady=10)

    pincode_edit=Entry(edit_window,width=30)
    pincode_edit.grid(row=4,column=1,padx=20,pady=10)

    contact_no_edit=Entry(edit_window,width=30)
    contact_no_edit.grid(row=5,column=1,padx=20,pady=10)

    #creating label for text boxes
    f_name_label=Label(edit_window,text="First Name")
    f_name_label.grid(row=1,column=0,padx=20,pady=10)

    l_name_label=Label(edit_window,text="Last Name")
    l_name_label.grid(row=2,column=0,padx=20,pady=10)

    address_label=Label(edit_window,text="Address")
    address_label.grid(row=3,column=0,padx=20,pady=10)

    pincode_label=Label(edit_window,text="PIN code")
    pincode_label.grid(row=4,column=0,padx=20,pady=10)

    contact_no_label=Label(edit_window,text="Contact number")
    contact_no_label.grid(row=5,column=0,padx=20,pady=10)

    #creating button for edit
    Button(edit_window,text="Save Edit",command=save_edit).grid(row=6,columnspan=2,padx=20,pady=10,ipadx=100)

    #dispaly the previous info

    for record in records:
        f_name_edit.insert(0,record[0])
        l_name_edit.insert(0,record[1])
        address_edit.insert(0,record[2])
        pincode_edit.insert(0,record[3])
        contact_no_edit.insert(0,record[4])

    #commit changes
    data.commit()

    #close connection
    data.close()




#function for edit drop
def edit_drop():
    global edit_id
    edit_id=Entry(root,width=30).grid(row=11,column=1)
    edit_label=Label(root,text="ID to edited").grid(row=11,column=0)
    #creating button to enter edit window
    edit_btn=Button(root,text="Edit",command=edit).grid(row=12,column=1,padx=20,pady=10,ipadx=50)
    edit_id.delete(0,END)

#function for delete window
def det_win():

    def delete():
        
        #warning message
        responce=tkinter.messagebox.askokcancel("Warning","Your data will be deleted permanently")
    
        if responce==1:
            #create or connect to a data base
            data=sqlite3.connect("profile.db")

            #creating a cursor
            cur=data.cursor()

            #delete a record
            cur.execute("DELETE from profile WHERE oid = 1")
            tkinter.messagebox.showinfo("Delete","Data deleted successfully")

            #commit changes
            data.commit()

            #close connection
            data.close()
        else:
            tkinter.messagebox.showinfo("Delete","Data delete was unsuccessful")


    delete_window=Toplevel()
    delete_window.title("Deleting Window")

    #creating for text box to delete reord
    det_box=Entry(delete_window,width=30).grid(row=0,column=1,padx=20)

    #creating label for text box
    Label(delete_window,text="Id to be deleted").grid(row=0,column=0,padx=20)
    
    #creating button to open delete window
    Button(delete_window,text="Delete",command=delete).grid(row=1,columnspan=2,padx=20,pady=10,ipadx=100)


#defining function for submit btn
def submit():
    #create or connect to a data base
    data=sqlite3.connect("profile.db")

    #creating a cursor
    cur=data.cursor()

    #recording the inputs to database
    cur.execute("INSERT INTO profile VALUES(:f_name,:l_name,:address,:pincode,:contact_no)",
    {
        "f_name":f_name.get(),
        "l_name":l_name.get(),
        "address":address.get(),
        "pincode":pincode.get(),
        "contact_no":contact_no.get()
    })

    #deleting the text boxes
    f_name.delete(0,END),
    l_name.delete(0,END),
    address.delete(0,END),
    pincode.delete(0,END),
    contact_no.delete(0,END)

    #message box
    tkinter.messagebox.showinfo("Status","Your Info have been Saved.")

    #commit changes
    data.commit()

    #close connection
    data.close()


#show records
def show():
    #create or connect to a data base
    data=sqlite3.connect("profile.db")

    #creating a cursor
    cur=data.cursor()

    #selectig the details
    cur.execute("SELECT *,oid FROM profile")
    records=cur.fetchall()
    print(records)

    #printing records
    print_record=""
    for record in records:
        print_record+="Name : "+str(record[0])+" "+str(record[1])+"\t"+"Address : "+str(record[2])+"\t"+"PIN Code : "+str(record[3])+"\t"+"Contact .No : "+str(record[4])+"\t"+"O.I.D : "+str(record[5])+"\n\n"

    show=Toplevel()
    show.title("Data Window")
    Label(show,text=print_record).grid(padx=20)


    #commit changes
    data.commit()

    #close connection
    data.close()

#creating text boxes
f_name=Entry(root,width=30)
f_name.grid(row=1,column=1,padx=20,pady=10)

l_name=Entry(root,width=30)
l_name.grid(row=2,column=1,padx=20,pady=10)

address=Entry(root,width=30)
address.grid(row=3,column=1,padx=20,pady=10)

pincode=Entry(root,width=30)
pincode.grid(row=4,column=1,padx=20,pady=10)

contact_no=Entry(root,width=30)
contact_no.grid(row=5,column=1,padx=20,pady=10)

#creating label for text boxes
f_name_label=Label(root,text="First Name")
f_name_label.grid(row=1,column=0,padx=20,pady=10)

l_name_label=Label(root,text="Last Name")
l_name_label.grid(row=2,column=0,padx=20,pady=10)

address_label=Label(root,text="Address")
address_label.grid(row=3,column=0,padx=20,pady=10)

pincode_label=Label(root,text="PIN code")
pincode_label.grid(row=4,column=0,padx=20,pady=10)

contact_no_label=Label(root,text="Contact number")
contact_no_label.grid(row=5,column=0,padx=20,pady=10)

#creating button to submit
Button(root,text="Submit Form",command=submit).grid(row=6,columnspan=2,padx=20,pady=10,ipadx=100)

#creating button to show records
Button(root,text="Show Reords",command=show).grid(row=7,columnspan=2,padx=20,pady=10,ipadx=100)

#creating button to open delete window
Button(root,text="Delete Reords",command=det_win).grid(row=9,column=1,padx=2,pady=10,ipadx=30)

#creating a buttom to edit
Button(root,text="Edit Reords",command=edit_drop).grid(row=9,column=0,padx=20,pady=10,ipadx=30)

root.mainloop()