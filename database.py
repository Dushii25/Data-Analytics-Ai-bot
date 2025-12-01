import psycopg2
from config import DBCONFIG
from datetime import datetime

def get_db_connection():
    return psycopg2.connect(**DBCONFIG)


def log_user_data(username, file_name):
    conn = get_db_connection()
    cursor = conn.cursor()
    now = datetime.now()
    cursor.execute(
        "INSERT INTO user_logs (username, file_name, upload_date, upload_time) VALUES (%s, %s, %s, %s)",
        (username, file_name, now.date(), now.time())
    )
    conn.commit()
    cursor.close()
    conn.close()

def get_all_user_logs():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user_logs ORDER BY upload_date DESC, upload_time DESC")
    logs = cursor.fetchall()
    cursor.close()
    conn.close()
    return logs



