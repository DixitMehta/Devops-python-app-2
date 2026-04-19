from flask import Flask, request, jsonify
import mysql.connector
import os
from prometheus_client import start_http_server, Counter
requests_total = Counter('requests_total', 'Total requests')

@app.route('/')
def home():
    requests_total.inc()
    return "Hello"

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host=os.environ.get("DB_HOST"),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASS"),
        database="testdb"
    )

@app.route("/add", methods=["POST"])
def add():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (name VARCHAR(255))")
    cursor.execute("INSERT INTO users (name) VALUES (%s)", (data["name"],))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "User added"}

@app.route("/get", methods=["GET"])
def get():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(rows)

@app.route("/")
def home():
    return "DevOps Python App Running 🚀.....Stay Tuned...23:46 11-04-2026"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
