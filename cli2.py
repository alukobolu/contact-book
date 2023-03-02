import sqlite3

# Connecting and Initializing the Database where we will store all the data
connector = sqlite3.connect('contacts.db')
cursor = connector.cursor()

cursor.execute(
"CREATE TABLE IF NOT EXISTS CONTACT_BOOK (S_NO INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, NAME TEXT, EMAIL TEXT, PHONE_NUMBER TEXT, ADDRESS TEXT)"
)


#defininting functions 
def list_contacts():
    curr = connector.execute('SELECT  NAME, EMAIL, PHONE_NUMBER, ADDRESS FROM CONTACT_BOOK')
    fetch = curr.fetchall()
    
    for data in fetch:
        print(f"{data}\n")

def save_details(name, email, phone, address):
    global cursor
    

    if name=='' or email=='' or phone=='' or address=='':
        print("Error! Please fill all the fields required!")
    else:
        cursor.execute(
        "INSERT INTO CONTACT_BOOK (NAME, EMAIL, PHONE_NUMBER, ADDRESS) VALUES (?,?,?,?)", (name, email, phone, address))
        connector.commit()
        print('Your contact has been stored successfully!')
        list_contacts()
        
def Update():
    Database()

    fname1=fname.get()
    lname1=lname.get()
    email1=email.get()
    address1=address.get()
    contact1=contact.get()

    if fname1=='' or lname1==''or email1=='' or address1==''or contact1=='':
        print("Warning","Please fill the empty field!!!")
    else:

        curItem = tree.focus()
        contents = (tree.item(curItem))
        selecteditem = contents['values']
      
        conn.execute('UPDATE REGISTRATION SET FNAME=?,LNAME=?,EMAIL=?,ADDRESS=?,CONTACT=? WHERE RID = ?',(fname1,lname1,email1,address1,contact1, selecteditem[0]))
        conn.commit()
        print("Message"," Details Updated successfully")
        

def delete(name):
    global  connector, cursor

    if not name:
        print( "Please ou have not selected any item!")

    cursor.execute('DELETE FROM CONTACT_BOOK WHERE NAME = ?', (name,))
    connector.commit()

    print( 'Sucess! The contact has been deleted')
    list_contacts()

choice = input("Welcome Please enter the values add contact,delete contact,list saved, to update your contact book ,delete a contact or show all contacts respectively :")
if choice =='add contact':
    name = input("name: ")
    email = input("email: ")
    phone = input("phone: ")
    address = input("address: ")
    submit_record(name, email, phone, address)
elif choice == 'delete contact':
    name = input("name: ")
    delete_record(name)
elif choice == "list saved":
    list_contacts()
    
else:
    print("Error invalid command valid commands are add contact,delete contact,list saved, to update your contact book ,delete a contact or show all contacts respectively ,please start the program to try again")