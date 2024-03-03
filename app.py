from flask import Flask, render_template, request, jsonify

import mysql.connector

app = Flask(__name__)

# Connect to MySQL (replace 'your_username' and 'your_password' with your MySQL credentials)
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="@Alexander07",
    database="mydb"
)

cursor = db.cursor()

# Define routes
@app.route('/')
def index():
    return render_template('ind.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']

        # Insert data into the database
        query = "INSERT INTO users (username, email) VALUES (%s, %s)"
        cursor.execute(query, (username, email))
        db.commit()

        return jsonify({"message": "Data submitted successfully"})

if __name__ == '__main__':
    app.run(debug=True)
