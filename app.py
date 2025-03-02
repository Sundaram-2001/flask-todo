from flask import Flask, request, jsonify
from routes import routes_blueprint
#import subprocess as sp
#from pymongo import MongoClient 
#from mongopass import mongopass
app = Flask(__name__)

app.register_blueprint(routes_blueprint)
if __name__ == "__main__":
    print("Server started..")
    app.run(debug=True)