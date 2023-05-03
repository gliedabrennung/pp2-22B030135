import psycopg2
import re

def main():
    connection = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password= "sss13.08"
    )
    
    running = True
    mode = 'ASC'
    connection.autocommit = True

    with connection.cursor() as cursor:
        cursor.execute("""CREATE TABLE IF NOT EXISTS phonebook(
        first_name VARCHAR(20) NOT NULL,
        phone_number VARCHAR(20) NOT NULL
        ) """)
        
    while running:
        selection = int(input("""
                      Select mode:
                      1 - Add
                      2 - Delete
                      3 - Edit
                      4 - Look
                      5 - Clear book
                      6 - Resort
                      7 - Import from CSV
                      """
                      ))
        
        if selection == 1:
            name_to_insert = input("Enter name: ")
            number_to_insert=input("enter phone number: ")
            with connection.cursor() as cursor:
                cursor.execute(f"""INSERT INTO phonebook(first_name,phone_number)
                VALUES ('{name_to_insert}','{number_to_insert}')""")
                
        elif selection == 2:
            name_to_delete=input("enter to delete: ")
            with connection.cursor() as cursor:
                cursor.execute(f"DELETE FROM phonebook WHERE first_name = '{name_to_delete}' OR phone_number = '{name_to_delete}'")                
                
        elif selection == 3:
            editing_name=input("Select the contact to edit: ")
            new_name=input("New name: ")
            new_number=input("New phone number: ")
            with connection.cursor() as cursor:
                cursor.execute(f"UPDATE phonebook SET first_name='{new_name}' WHERE first_name='{editing_name}'")
                cursor.execute(f"UPDATE phonebook SET phone_number='{new_number}' WHERE first_name='{new_name}'")                
                
        elif selection == 4:
            with connection.cursor() as cursor:
                if mode =='ASC':
                    cursor.execute(f"""SELECT * FROM phonebook ORDER BY first_name ASC""")
                    
                if mode =='DESC':
                    cursor.execute(f"""SELECT * FROM phonebook ORDER BY first_name DESC""")
                    
                all=cursor.fetchall()
                for _,name,phone in all:
                    print("|"+name+"---"+phone+"|")

        elif selection == 5:
            with connection.cursor() as cursor:
                cursor.execute("TRUNCATE TABLE phonebook;")
                
        elif selection == 6:
            mode_change=input("1 - [A-Z], 2 - [Z-A]")
            if mode_change == 1:
                mode = 'ASC'
            else:
                mode = 'DESC'
                
        elif selection == 7:
            with connection.cursor() as cursor:
                cursor.execute(f"""
                                COPY phonebook(first_name, phone_number)
                                FROM 'C:\\Users\\Acer\\Desktop\\pp2\\pp2-22B030135\\tsis10\\phones.csv'
                                DELIMITER ','
                                CSV HEADER;
                               """)

    connection.close()

if __name__ == "__main__":
    main()