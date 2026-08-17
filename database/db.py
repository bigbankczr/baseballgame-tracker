import sqlite3

dbPath = "database/baseball.db"

def connect():
    return sqlite3.connect(dbPath)

def insertRows(table, rows):
    if not rows:
        return 0
    columns = ", ".join(rows[0].keys())
    placeholders = ", ".join(f":{k}"for k in rows[0].keys())
    sql = f"INSERT OR REPLACE INTO {table} ({columns}) VALUES ({placeholders})"

    connection = connect()
    cursor = connection.cursor()
    cursor.executemany(sql, rows)
    connection.commit()
    connection.close()
    return len(rows)

