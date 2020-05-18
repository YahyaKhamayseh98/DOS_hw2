from flask import Flask, jsonify, json
from flask import request
import requests , json
import sqlite3


app = Flask(__name__)

@app.route('/')
def root():
    # Connect to db
    db = sqlite3.connect('books.db')  
    cursor = db.cursor()
    #cursor.execute('CREATE TABLE books(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,topic TEXT, cost INTEGER, ammount INTEGER)')
    # Connect to db
   

    # Insert data into db
    #cursor.execute('INSERT INTO books(topic,name, cost, ammount) VALUES("distributed_systems","How to finish Project 3 on time",20 ,5 )')
    #db.commit()
    #cursor.execute('INSERT INTO books(topic,name, cost, ammount) VALUES("graduate_school","Why theory classes are so hard", 10,4 )')
    #db.commit()
    #cursor.execute('INSERT INTO books(topic,name, cost, ammount) VALUES("graduate_school","Spring in the Pioneer Valley",15 ,7 )')
    #db.commit()
    #cursor.execute('INSERT INTO books(topic,name, cost, ammount) VALUES("graduate_school","Cooking for the Impatient Graduate Student",17 ,6 )')
    #db.commit()

    # Get data from db
    result=cursor.execute('SELECT * FROM books')
    items = []
    for row in result:
            items.append({'id': row[0], 'name': row[1], 'topic': row[2] , 'cost': row[3] , 'ammount': row[4]})
    # Close db connection
    db.close()
    return jsonify({'books': items})
  

@app.route('/query_sub/<_tpc>')
def query_sub(_tpc):
    # Connect to db
    db = sqlite3.connect('books.db')  
    cursor = db.cursor()
    
    result=cursor.execute('SELECT * FROM books WHERE topic ="%s"'%(_tpc))
    items = []
    for row in result:
            items.append({'id': row[0], 'name': row[1], 'topic': row[2] , 'cost': row[3] , 'ammount': row[4]})
    # Close db connection
    db.close()
    return jsonify({'books': items})

@app.route('/query_item/<_id>')
def query_item(_id):
    # Connect to db
    db = sqlite3.connect('books.db')  
    cursor = db.cursor()
    
    result=cursor.execute('SELECT * FROM books WHERE id ="%s"'%(_id))
    items = []
    for row in result:
            items.append({'id': row[0], 'name': row[1], 'topic': row[2] , 'cost': row[3] , 'ammount': row[4]})
    # Close db connection
    db.close()
    return jsonify({'books': items})

@app.route('/update_cost/<_id>')
def update_cost(_id):
    # Connect to db
    db = sqlite3.connect('books.db')  
    cursor = db.cursor()
    
    # Get request args
    cost = request.args.get('cost')
    #post = request.args.get('post')
    
    # Update data in db
    cursor.execute('UPDATE books SET cost="%s" WHERE id=%s' % (cost, _id))
    db.commit()
    result=cursor.execute('SELECT * FROM books WHERE id ="%s"'%(_id))
    items = []
    for row in result:
            items.append({'id': row[0], 'name': row[1], 'topic': row[2] , 'cost': row[3] , 'ammount': row[4]})
    # Close db connection
    db.close()
    response = requests.get("http://127.0.0.1:5002/invalidate/"+_id) 
    return jsonify({'books': items})

@app.route('/update_inc_ammount/<_id>')
def update_inc_ammount(_id):
    # Connect to db
    db = sqlite3.connect('books.db')  
    cursor = db.cursor()
    
    # Get request args
    #cost = request.args.get('cost')
    #post = request.args.get('post')
    
    result1=cursor.execute('SELECT ammount FROM books WHERE id ="%s"'%(_id))
    for row in result1:
        ammount = row[0]
    
    int_ammount = int(ammount)   
    int_ammount = int_ammount + 1
    str_ammount = str(int_ammount)
    print(ammount)
    # Update data in db
    cursor.execute('UPDATE books SET ammount="%s" WHERE id=%s' % (str_ammount, _id))
    db.commit()
    result=cursor.execute('SELECT * FROM books WHERE id ="%s"'%(_id))
    items = []
    for row in result:
            items.append({'id': row[0], 'name': row[1], 'topic': row[2] , 'cost': row[3] , 'ammount': row[4]})
    # Close db connection
    db.close()
    response = requests.get("http://127.0.0.1:5002/invalidate/"+_id)
    return jsonify({'books': items})

@app.route('/update_dec_ammount/<_id>')
def update_dec_ammount(_id):
    # Connect to db
    db = sqlite3.connect('books.db')  
    cursor = db.cursor()
    
    # Get request args
    #cost = request.args.get('cost')
    #post = request.args.get('post')
    
    result1=cursor.execute('SELECT ammount FROM books WHERE id ="%s"'%(_id))
    for row in result1:
        ammount = row[0]
    
    int_ammount = int(ammount)   
    int_ammount = int_ammount - 1
    str_ammount = str(int_ammount)
    print(ammount)
    # Update data in db
    cursor.execute('UPDATE books SET ammount="%s" WHERE id=%s' % (str_ammount, _id))
    db.commit()
    result=cursor.execute('SELECT * FROM books WHERE id ="%s"'%(_id))
    items = []
    for row in result:
            items.append({'id': row[0], 'name': row[1], 'topic': row[2] , 'cost': row[3] , 'ammount': row[4]})
    # Close db connection
    db.close()
    response = requests.get("http://127.0.0.1:5002/invalidate/"+_id)
    return jsonify({'books': items})

if __name__ == '__main__':
    app.run(debug=True, threaded=True,host= '127.0.0.1')
