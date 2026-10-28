import sqlite3 as sql 

db = sql.connect("database.db")
cr = db.cursor()
cr.execute("CREATE TABLE IF NOT EXISTS Students (ID INTEGER PRIMARY KEY , Name TEXT NOT NULL , Classes TEXT , Age INTEGER , Enrollment_Date DATE , Phone_Number_father TEXT , Phone_Number_mother TEXT , Status TEXT DEFAULT '------' )") 

results = cr.execute("SELECT * FROM Students")

print("\n ----------------Table------------------------------------------------------------------------------------------------------------------\n")
for row in results :
    print(f"ID : {row[0]} | Student Name : {row[1]} | Classes : {row[2]} | Age : {row[3]} | Enrollment Date : {row[4]} | Phone (Father) : {row[5]} | Phone (Mother) : {row[6]} | Status : {row[7]}")
print("\n----------------------------------------------------------------------------------------------------------------------------------------\n")

print(cr.fetchall())

input_massege = """
What do you want to do ? 
"s" : Show table all
"a" : Add items in table 
"u" : Update items in table
"d" : Delete items from table
"q" : Quit App
Choose your option : """

list_of_options = ["s" , "a" , "u" , "d" , "q"]

def show_students():
    results = cr.execute("SELECT * FROM Students")
    print("\n ----------------Table------------------------------------------------------------------------------------------------------------------\n")
    for row in results :
        print(f"ID : {row[0]} | Student Name : {row[1]} | Classes : {row[2]} | Age : {row[3]} | Enrollment Date : {row[4]} | Phone (Father) : {row[5]} | Phone (Mother) : {row[6]} | Status : {row[7]}")
    print("\n----------------------------------------------------------------------------------------------------------------------------------------\n")
    db.commit()

def add_student():
    input_add_name = input("Please Add your Student Name : ").strip().capitalize()
    input_add_classes = input("Please Add your Classes [ 1 , 2 , 3 , 4 , 5 , 6 , 7 ] : ").strip()
    input_add_age = int(input("Please Add your Age : ").strip())
    input_add_enrollment_date = input("Please Add your Enrollment Date (YYYY-MM-DD) : ").strip()
    input_add_phone_father = input("Please Add your Father's Phone Number : ").strip()
    input_add_phone_mother = input("Please Add your Mother's Phone Number : ").strip()
    input_add_status = input("Please Add your Status [Active / Inactive] : ").strip()

    cr.execute("""
        INSERT INTO Students (
            Name, Classes, Age, Enrollment_Date,
            Phone_Number_father, Phone_Number_mother, Status
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        input_add_name,
        input_add_classes,
        input_add_age,
        input_add_enrollment_date,
        input_add_phone_father,
        input_add_phone_mother,
        input_add_status
    ))
    
    input_add_again = input("Do you want to add another student? [yes (y) / no (n)] : ").lower().strip()
    if input_add_again == "y" or input_add_again == "yes":
        add_student()
    else:
        db.commit()
        print("Your has been added successfully")

def update_student():
    input_update_ID = int(input("Please update your ID : "))
    input_update_name = input("Please update your Student Name : ").strip().capitalize()
    input_update_classes = input("Please update your Classes [ 1 , 2 , 3 , 4 , 5 , 6 , 7 ] : ").strip()
    input_update_age = int(input("Please update your Age : ").strip())
    input_update_enrollment_date = input("Please update your Enrollment Date (YYYY-MM-DD) : ").strip()
    input_update_phone_father = input("Please update your Father's Phone Number : ").strip()
    input_update_phone_mother = input("Please update your Mother's Phone Number : ").strip()
    input_update_status = input("Please update your Status [Active / Inactive] : ").strip()

    cr.execute("""
        UPDATE Students
        SET Name = ?, Classes = ?, Age = ?, Enrollment_Date = ?,
            Phone_Number_father = ?, Phone_Number_mother = ?, Status = ?
        WHERE ID = ?
    """, (
        input_update_name,
        input_update_classes,
        input_update_age,
        input_update_enrollment_date,
        input_update_phone_father,
        input_update_phone_mother,
        input_update_status,
        input_update_ID
    ))

    input_update_again = input("Do you want to update another student? [yes (y) / no (n)] : ").lower().strip()
    db.commit()
    if input_update_again == "y" or input_update_again == "yes":
        update_student()
    else:
        db.commit()
        print("Your has been updated successfully")

def delete_student():
    while True:
        try:
            input_delete_ID = int(input("Please input the ID of the student you want to delete : "))
            cr.execute(
                "DELETE FROM Students WHERE ID = ?",
                (input_delete_ID,)
            )

            while True:
                input_delete_again = input("Do you want to delete another student? [yes (y) / no (n)] : ").lower().strip()
        
                if input_delete_again == "n" or input_delete_again == "no":
                    db.commit()
                    print("Your has been deleted successfully")
                    break  

                elif input_delete_again == "y" or input_delete_again == "yes":
                    delete_student()
                    # input_delete_other_ID = input("Please input the Number ID of the student you want to delete : ")
                    # cr.execute(f"DELETE FROM Students WHERE ID = {input_delete_other_ID}")
                    # db.commit()
                    # print("Your has been deleted successfully")
        
                elif input_delete_again != "y" and input_delete_again != "yes" and input_delete_again != "n" and input_delete_again != "no":
                    print("Please input your answer again")
        
        except:
            print("Please input a valid ID")
        break


def quit_app():
    print("Thanks for using our app")
    db.commit()

while True:   
    input_option = input(input_massege).lower().strip()

    if input_option in list_of_options:
        if input_option == "s":
            show_students()
        elif input_option == "a":
            add_student()
        elif input_option == "u":
            update_student() 
        elif input_option == "d":
            delete_student()
        elif input_option == "q":
            quit_app()
            break
    else :
        print("Your choose isn't in the list of options , Please input your choose again")
db.commit()
db.close()
