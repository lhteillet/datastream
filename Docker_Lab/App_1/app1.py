from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)


def start_connection():
    config = {
        "host": "db",
        "user": "root",
        "passwd": "e6d808b728e243ed26ac20dc6be6bd6977caa31414cded955dfa55ba79d6aedc",
        "port": "3306",
        'database': 'customers'
        }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT customers_name, total_purchases FROM customers_data')
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    #return jsonify({'Customers Data': results}).get_data(as_text=True)
    s = ""
    for consumer in results:
        s += consumer['customers_name'] + ' ' + str(consumer['total_purchases']) + '<br>'
    return s


@app.route('/')
def hello_world():
    return start_connection()


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
