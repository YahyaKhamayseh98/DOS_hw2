from flask import Flask
import requests , json

app = Flask(__name__)

@app.route('/')
def root():
   # response = requests.get("http://127.0.0.1:5005/query_item/2")
    
    return ""

@app.route('/buy/<_id>')
def buy(_id):
    response = requests.get("http://127.0.0.1:5005/query_item/"+_id)
    obj = response.json()
    ammount = obj["books"][0]["ammount"]
    
    if (ammount>0):
       response2 = requests.get("http://127.0.0.1:5005/update_dec_ammount/"+_id)
       obj2 = response2.json()
       ammount2 = obj2["books"][0]["ammount"]
       response3 = requests.get("http://127.0.0.1:5006/update_dec_ammount/"+_id)
       obj3 = response3.json()
       ammount3 = obj3["books"][0]["ammount"]
       if (response2.json()!= None and response2.json()!= None and ammount2 == ammount3):
          return str(ammount2) 
          
    return str(ammount) 
