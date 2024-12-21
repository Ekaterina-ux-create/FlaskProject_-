from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('gifts.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/gifts', methods=['GET'])

def show_gifts():
    conn = get_db_connection()
    gifts = conn.execute('SELECT * FROM gifts WHERE status = "Не куплен"').fetchall()#извлекаю только подарки, которые еще не куплены
    conn.close()
    return render_template('gifts.html', gifts=gifts)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
