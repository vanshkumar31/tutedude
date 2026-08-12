from flask import Flask,request,jsonify
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

load_dotenv()

app =Flask(__name__)

MONGODB_URI =os.getenv('mongodb_uri')
client = MongoClient(MONGODB_URI, server_api=ServerApi('1'))

db =client.test
collection=db['flask-demo']



@app.route("/submit" , methods=[ 'POST'])
def submit():
        # Check if the user submitted the contact form
        if request.method == 'POST':
            form_data=dict(request.json)
            print(form_data)
            try:
                collection.insert_one(form_data)
                return jsonify({
                    "success": True,
                    "message": "Data submitted successfully"
                }), 201
            except Exception as e:
                print(e)
                return jsonify({
            "success": False,
            "message": "Failed to save data"
        }), 500

        else:
            return jsonify({
    "success": False,
    "message": "Invalid request method"
}), 405

@app.route('/test')
def test():
    try:
        client.admin.command('ping')
        return "Pinged your deployment. You successfully connected to MongoDB!"
        
    except Exception as e:
        return e
     

if __name__ =='__main__':
    app.run(port=9000)
