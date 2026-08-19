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

def hasGamelog(table, player_id, season):
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(
        f"SELECT 1 FROM {table} WHERE player_id = ? AND season = ? LIMIT 1",
        (player_id, season),
    )
    found = cursor.fetchone() is not None
    connection.close()
    return found

