import mysql.connector

connection = mysql.connector.connect(user='wojtek', password='wojtek', host='127.0.0.1', database='flask-python', auth_plugin='mysql_native_password')

cursor = connection.cursor()

insertQuery = "INSERT INTO users(username, city) VALUES(%(username)s, %(city)s)"
insertData = {
    'username': 'Mariusz',
    'city': 'Warszawa'
}
cursor.execute(insertQuery, insertData)
connection.commit()

query = 'SELECT username, city FROM users'
cursor.execute(query)

for (id, username, city) in cursor:
    print(f"{id} - {username} from {city}")
connection.close()