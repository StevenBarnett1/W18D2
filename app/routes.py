from flask import Blueprint, render_template
import os
import psycopg2


bp = Blueprint("main",__name__,"/")

CONNECTION_PARAMETERS = {
    "user": os.environ.get("DB_USER"),
    "password": os.environ.get("DB_PASS"),
    "dbname": os.environ.get("DB_NAME"),
    "host": os.environ.get("DB_HOST"),
}

@bp.route('/')
def main():
    with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
        with conn.cursor() as curs:
            rows = curs.execute(
                """
                SELECT *
                FROM appointments
                """
            )
    print(rows[0])
    return render_template('main.html', rows = [row for row in rows])
