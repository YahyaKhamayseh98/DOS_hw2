from flask import Flask, jsonify 
from flask_cache import Cache 
import requests, json 
app = Flask(__name__)
cache = Cache(app,config={'CACHE_TYPE':'simple'})
@app.route('/')
def hello():
    return 'hello'
    
load_balancer = 2    
load_balancer2 = 2      
@app.route('/buy/<_id>')
@cache.memoize(timeout=50)
def buy(_id):
    global load_balancer
    if (load_balancer > 1):
        response = requests.get("http://127.0.0.1:5003/buy/"+_id) 
        load_balancer = load_balancer - 1
    else: 
        response = requests.get("http://127.0.0.1:5004/buy/"+_id)  
        load_balancer = load_balancer + 1
    
    if(response.json()>0):
       return jsonify("THe Purchase is Done !")
    return jsonify("The Ordered book is not existed in the stock any more !")
    
@app.route('/invalidate/<_id>')
def invalidate(_id):
    cache.delete_memoized('buy',_id)
    cache.delete_memoized('lookup',_id)
    cache.delete_memoized('search')
    return "OK" 
       
@app.route('/lookup/<_id>')
@cache.memoize(timeout=50)
def lookup(_id):
    global load_balancer2
    if (load_balancer2 > 1):
        response = requests.get("http://127.0.0.1:5005/query_item/"+_id)
        load_balancer2 = load_balancer2 - 1
    else: 
        response = requests.get("http://127.0.0.1:5006/query_item/"+_id) 
        load_balancer2 = load_balancer2 + 1
    
    return response.json()
    
@app.route('/search/<_topic>')
@cache.memoize(timeout=50)
def search(_topic):
    global load_balancer2
    if (load_balancer2 > 1):
        response = requests.get("http://127.0.0.1:5005/query_sub/"+_topic)
        load_balancer2 = load_balancer2 - 1
    else: 
        response = requests.get("http://127.0.0.1:5006/query_sub/"+_topic)
        load_balancer2 = load_balancer2 + 1
    
    return response.json()
