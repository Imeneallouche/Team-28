from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

# Initialize the database
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT,
            password TEXT
        )
    ''')
    cursor.execute("INSERT INTO users (username, password) VALUES ('admin', 'shellmates{secure_password}')")
    conn.commit()
    conn.close()

# Vulnerable login function
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
        cursor.execute(query)
        user = cursor.fetchone()
        conn.close()

        if user:
            return f"Welcome, {user[1]}! The flag is: shellmates{{sql_injection_success}}"
        else:
            return "Invalid inputs!"
    return render_template('index.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)