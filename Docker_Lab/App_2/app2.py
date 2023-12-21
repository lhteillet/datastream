# Simple Flask Application: app.py

from flask import Flask 
# import mysql.connector


app = Flask(__name__)

# mydb = mysql.connector.connect(
#     host="db",
#     user="root",
#     passwd="e6d808b728e243ed26ac20dc6be6bd6977caa31414cded955dfa55ba79d6aedc",
# )

@app.route('/') 
def hello_world():
    return 'Hello, World! You are in App 2'

if __name__ == "__main__": 
    app.run(debug=True, host="0.0.0.0",port=5001)
 