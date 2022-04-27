import mysql.connector
from flask import Flask
from flask import jsonify
from flask import request
from mysql.connector import cursor

def get_connection_to_database():
    connection = mysql.connector.connect(
        user='wojtek',
        password='wojtek',
        host='127.0.0.1',
        database='python',
        auth_plugin='mysql_native_password'
    )

    return connection

class User:
    def __init__(self, user_id, username, city):
        self.user_id = user_id
        self.username = username
        self.city = city

app = Flask(__name__)

@app.route('/users', methods=['GET'])
def get_users():
    users = []
    connection = get_connection_to_database()
    cursor = connection.cursor()
    query = 'SELECT id, username, city FROM users'
    cursor.execute(query)

    for row in cursor:
        users.append(User(row['id'], row['username'], row['city']))

    connection.close()

    return jsonify(users)


app.run(port=8000)