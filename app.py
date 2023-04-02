from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Qazxsw1122!@",
    database="users"
)

# Create a cursor object
cursor = db.cursor()


@app.route('/')
def index():
    # Execute a SQL query
    cursor.execute("SELECT * FROM `users`")
    result = cursor.fetchall()

    # Render a template with the query result
    return render_template('index.html', result=result)


# Close the database connection
db.close()

if __name__ == '__main__':
    app.run(debug=True)
