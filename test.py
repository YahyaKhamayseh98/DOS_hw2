from flask import Flask 
import requests, json
import timeit
app = Flask(__name__)

@app.route('/')
def main():
    print("")
    print("Welcome to Bazar.come") 
    while 1>0:
       print("")
       print("Store services:")
       print("1. Buy ")
       print("2. Lookup ")
       print("3. Search ")
       print("")
       index = input("Please enter the index of the service to proceed it:")
       if int(index) == 1:
          print("")
          _id = input("please enter the number of the book you want to buy:")
          code_to_test="""
import requests 
_id="5"
response = requests.get("http://127.0.0.1:5002/buy/"+_id)
          """
          elapsed_time = timeit.timeit(code_to_test,number=100)/100
          print("")
          print("latency :")
          print(elapsed_time)
          print("")
          response = requests.get("http://127.0.0.1:5002/buy/"+_id)
          
          print("")
          print(response.json())
          print("")
       if int(index) == 2:
          print("")
          _id = input("please enter the number of the book you want to lookup on:")
          code_to_test="""
import requests 
_id="2"
response = requests.get("http://127.0.0.1:5002/lookup/"+_id)
          """
          elapsed_time = timeit.timeit(code_to_test,number=100)/100
          print("")
          print("latency :")
          print(elapsed_time)
          print("")
          response = requests.get("http://127.0.0.1:5002/lookup/"+_id)
          print(response.json())
          print("")
       if int(index) == 3:
          print("")
          _topic = input("please enter the topic of the books you want to search for:")
          code_to_test="""
import requests 
_topic="graduate_school"
response = requests.get("http://127.0.0.1:5002/search/"+_topic)
          """
          elapsed_time = timeit.timeit(code_to_test,number=100)/100
          print("")
          print("latency :")
          print(elapsed_time)
          print("")
          response = requests.get("http://127.0.0.1:5002/search/"+_topic)
          print("")
          print(response.json())
     
    return 'Bazar.com'
    
    
