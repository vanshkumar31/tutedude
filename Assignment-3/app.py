'''
4 main types of databases:

1. Relational/SQL databases - databases > tables > rows > columns (MySQL, Postgres, Oracle, SQL Server, etc.)
2. NoSQL/Document databases - databases > collections > documents (MongoDB, CouchDB, etc.)
3. Graph databases - databases > nodes > edges (Neo4j, etc.)
4. key-value databases - databases > keys > values (Redis, Riak, etc.)
'''
# taking data from url
'''
@app.route('/user/<name>')
def user(name):
    return f" are you a user , \n{name}"

'''
# fetch data from json
'''
def home():
    name = request.values.get('name', 'someone')
    return render_template('index.html', name=name)
'''
from flask import Flask,request,render_template
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os
load_dotenv()

app =Flask(__name__)

uri =os.getenv('mongodb_uri')
client = MongoClient(uri, server_api=ServerApi('1'))

db =client.test
collection=db['fask-demo']
@app.route('/')
def home():
    name = request.values.get('name', 'someone')
    return render_template('index.html', name=name)
@app.route("/submit" , methods=['GET', 'POST'])
def submit():
        # Check if the user submitted the contact form
        if request.method == 'POST':
            form_data=dict(request.form)
            collection.insert_one(form_data)
            name = request.form.get('name')
            success_msg = "Thank you! We received your message."
            return render_template('submit.html', name=name, success=success_msg,data=form_data)


@app.route('/user')
def user():
    name=request.values.get('name',"Someone")
    return f" hey , \n{name}"


if __name__ =='__main__':
    app.run()
