import psycopg2
import csv

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password= "sss13.08"
    )

cur = conn.cursor()
conn.autocommit = True

with conn.cursor() as cursor:
    cursor.execute("""CREATE TABLE IF NOT EXISTS phonebook(
    name VARCHAR(20) NOT NULL,
    phone VARCHAR(20) NOT NULL
    ) """)
    
run = True    
while run:
    print(
        "[0] Quit\n[1] Add Contact\n[2] Update Contact\n[3] Delete Contact\n[4] Print Data\n[5] Add CSV - file")
    select = int(input())
    
    if select == 0:
        run = False
        
    if select == 1:
        print("Insert name:")
        name = input()
        
        print("Insert number:")
        phone = input()
        
        cur.execute(f"INSERT INTO phonebook (name, phone) VALUES ('{name}', '{phone}')")

    if select == 2:
        print("Select the contact to update:")
        name = input()
        new_name=input("New name: ")
        new_number=input("New phone number: ")
        with conn.cursor() as cursor:
            cursor.execute(f"UPDATE phonebook SET name='{new_name}' WHERE name='{name}'")
            cursor.execute(f"UPDATE phonebook SET phone='{new_number}' WHERE name='{new_name}'") 
        
    if select == 3:
        print("Select the contact name to delete:")
        name = input()
        
        print("Select the contact number to delete:")
        phone = input()
        
        cur.execute(f"DELETE FROM phonebook where ('{name}', '{phone}')")
        
    if select == 4:
        print("Select 0 to [A - Z]\nSelect 1 to [Z - A]")
        sorting = int(input())
        
        if sorting == 0:
            cur.execute("SELECT * FROM phonebook ORDER BY name ASC")
            data = cur.fetchall()
            
        if sorting == 1:
            cur.execute("SELECT * FROM phonebook ORDER BY name DESC")
            data = cur.fetchall()
            
        for i in data:
            print(i)
            
    if select == 5:
        with open('table.csv') as file:
            reader = csv.reader(file, delimiter=',')
            
            for i in reader:
                name = i[0]
                phone = i[1]
                
                cur.execute(f"INSERT INTO phonebook (name, phone) VALUES ('{name}', '{phone}')")
                
    conn.commit()