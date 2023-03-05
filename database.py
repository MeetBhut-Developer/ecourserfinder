from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'MyLocal@pass@8155'
app.config['MYSQL_DB'] = 'ineuron_data'

mysql = MySQL(app)

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM category_list;')
    data = cur.fetchall()
    cur.close()
    return str(data)

if __name__ == '__main__':
    app.run()
