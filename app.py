from flask import Flask, request
import redis
import psycopg2
from utils import get_secret

app = Flask(__name__)

# Load secrets
rds = get_secret("my-rds-secret")
rds_conn = psycopg2.connect(
    host=rds["host"],
    database=rds["dbname"],
    user=rds["username"],
    password=rds["password"],
    port=rds["port"]
)
cursor = rds_conn.cursor()

# Redis connection
redis_secret = get_secret("my-redis-secret")
r = redis.Redis(
    host=redis_secret["host"],
    port=redis_secret["port"],
    password=redis_secret.get("password"),
    decode_responses=True
)

@app.route("/add")
def add_name():
    name = request.args.get("name")
    if not name:
        return "Missing 'name' parameter", 400

    cursor.execute("INSERT INTO names (name) VALUES (%s)", (name,))
    rds_conn.commit()
    r.set("latest_name", name)
    return f"Added {name}!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
