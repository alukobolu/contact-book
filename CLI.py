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

def submit_record(name, email, phone, address):
    global cursor
    

    if name=='' or email=='' or phone=='' or address=='':
        print("Error! Please fill all the fields!")
    else:
        cursor.execute(
        "INSERT INTO CONTACT_BOOK (NAME, EMAIL, PHONE_NUMBER, ADDRESS) VALUES (?,?,?,?)", (name, email, phone, address))
        connector.commit()
        print('We have stored the contact successfully!')
        list_contacts()

def delete_record(name):
    global  connector, cursor

    if not name:
        print( "You have not selected any item!")

    cursor.execute('DELETE FROM CONTACT_BOOK WHERE NAME = ?', (name,))
    connector.commit()

    print( 'The desired contact has been deleted')
    list_contacts()
exiting = False
while exiting ==False:
    choice = input("\nWelcome Please enter the values \n add , del , show , x to \n 1. update your contact book ,\n 2. delete a contact or \n 3. show all contacts \n 4. to exit  respectively \n == :")
    if choice =='add':
        name = input("name: ")
        email = input("email: ")
        phone = input("phone: ")
        address = input("address: ")
        submit_record(name, email, phone, address)
    elif choice == 'del':
        name = input("name: ")
        delete_record(name)
    elif choice == "show":
        list_contacts()
    elif choice == "x":
        exiting = True
    else:
        print("Error invalid command valid commands are add,del,show to update your contact book ,delete a contact or show all contacts respectively ,please start the program to try again")