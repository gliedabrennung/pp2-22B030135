import psycopg2
from sna import name, SCORE

connection = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password= "sss13.08"
)

connection.autocommit = True

with connection.cursor() as cursor:
    cursor.execute("""CREATE TABLE IF NOT EXISTS snake_table(
    username VARCHAR(25),
    score VARCHAR(25)
    ) """)

# поместить в функцию гейм офер -Ю
run = True
while run:    
    with connection.cursor() as cursor:
        insert = cursor.execute("INSERT INTO snake_table (username, score) VALUES (%s, %s)")
        cursor.execute(insert, (name, SCORE))

    with connection.cursor() as cursor:
        update = "UPDATE snake_table SET score = %s WHERE username = %s"
        cursor.execute(update, (str(SCORE), name))
    
connection.close()
