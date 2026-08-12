from flask import Flask
import requests
url='http://127.0.0.1:1000'
app =Flask(__name__)
@app.route('/')
def home():
    return "Hello duniya"
@app.route('/api')
def api():
    response=requests.get(url+'/api')
    return response.json()
@app.route('/api1')
def api1():
    response=requests.get(url+'/api1')
    return response.json()

if __name__ =='__main__':
    app.run()
