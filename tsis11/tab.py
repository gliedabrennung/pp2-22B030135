import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password= "sss13.08"
    )
cur = conn.cursor()

conn.autocommit = True

cur.execute(''' CREATE OR REPLACE FUNCTION get_pagination(
                    _limit INT,
                    _offset INT)
                RETURNS TABLE(
                    name TEXT,
                    phone TEXT
                )
                LANGUAGE SQL
                AS $$
                    SELECT * FROM phonebook
                    LIMIT _limit
                    OFFSET _offset;
                $$''')
cur.execute(""" CREATE OR REPLACE PROCEDURE add_update_user(
                    _name TEXT,
                    _phone TEXT)
            LANGUAGE plpgsql
            AS $$
            BEGIN
                UPDATE phonebook SET phone = _phone WHERE name = _name;
                IF NOT FOUND THEN
                    INSERT INTO phonebook (name, phone) VALUES (_name, _phone);
                END IF;
            END
            $$
            """)
cur.execute(""" CREATE OR REPLACE PROCEDURE delete_user(
                _n TEXT,
                _m TEXT)
                LANGUAGE plpgsql
                AS $$
                BEGIN
                    IF _m = 'p' THEN
                        DELETE FROM phonebook WHERE phone = _n;
                    ELSE
                        DELETE FROM phonebook WHERE name = _n;
                    END IF;
                END
                $$""")

run = True
while run:
    print("[0] Quit\n[1] Data with pattern\n[2] I/U the User\n[3] Insert Many Users\n[4] Pagination\n[5] Delete the contact by name/phone")

    select = int(input("Insert number:"))
    if select == 0:
        run = False
        
    if select == 1:
        pattern = input("Insert the pattern")
        cur.execute("SELECT * FROM phonebook WHERE CONCAT(name, phone) LIKE '%"+pattern+"%'")
        result = cur.fetchall()
        for i in result:
            print(i)
            
    if select == 2:
        user = input("Insert name:")
        phone = input("Insert phone:")
        cur.execute("CALL add_update_user(%s, %s)",(user, phone))
        
    if select == 3:
            print('Insert many Users')
            values = input()
            values = values.split(" ")
            inc_v = {}
            a = {}
            i = 0
            while i != len(values):
                n, p = values[i], values[i + 1]
                try:
                    if type(int(p)) is int:
                        a[n] = p
                        cur.execute("CALL add_update_user(%s, %s)", (n, p))
                except:
                    inc_v[n] = p
                i += 2
                
    if select == 4:
        off = input("Insert Offset")
        lim = input("Insert Limit:")
        
        cur.execute('SELECT * FROM get_pagination(%s, %s)',(lim, off))
        result = cur.fetchall()
        for i in result:
            print(i)
            
    if select == 5:
        toDelete = input('p/n:')
        name_phone = input('Input Name or Phone to Delete:')
        
        cur.execute("CALL delete_user(%s, %s)",(name_phone, toDelete))
        
