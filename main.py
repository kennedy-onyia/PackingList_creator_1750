from flask import Flask, render_template
import sqlite3
app = Flask(__name__)

test = "Something to add"

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/1750")
def create_1750():
    conn = sqlite3.connect('/Users/justinmutinta/Documents/Python/PackingList_creator_1750_from_BidDawg/python_files/DatabaseManagement/PackingListCreator.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM product")
    data = cur.fetchall()
    cur.close()
    return render_template('html_files/1750_Generator.html', data = data, test = test)


@app.route("/17501")
def create_17501():
    return render_template('html_files/mutinta_position_test.html')

if __name__ == '__main__':
    app.run(debug=True)