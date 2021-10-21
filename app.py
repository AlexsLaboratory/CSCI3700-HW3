from flask import Flask, render_template
import psycopg2
import psycopg2.extras

app = Flask(__name__)

username = "postgres"
password = "test"
host = "192.168.160.139"
port = "5432"
database = "dvdrental"

conn = psycopg2.connect(dbname=database, user=username, password=password, host=host)

cur = conn.cursor()


@app.route("/api/update_basket_a")
def update_basket_a():
	try:
		cur.execute("""INSERT INTO basket_a VALUES (5, 'Cherry');""")
		conn.commit()
		return "Success"
	except psycopg2.Error as e:
		return e


@app.route("/api/unique")
def get_unique():
	try:
		cur.execute("""SELECT DISTINCT
basket_a.fruit_a,
basket_b.fruit_b
from basket_a
inner join basket_b
on basket_a.a = basket_b.b;""")
		record = cur.fetchall()
		return render_template('index.html', sql_table=record)
	except psycopg2.Error as e:
		return e


if __name__ == "__main__":
	app.run()
