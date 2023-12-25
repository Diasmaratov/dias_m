import psycopg2 as psy
try:
    conn = psy.connect(host= '78.141.227.124',
                        user= 'postgres',
                        database= 'GITHUB',
                        password= '123')
    cur = conn.cursor()
    cur.execute('SELECT COUNT(*) FROM students WHERE age > 15')
    
    data = cur.fetchall()
    print(data)

except Exception as err:
    print('something wrong',err)
