import pyodbc
from utils.config import DB_CONFIG

def get_connection():
    conn_str = (
        f"DRIVER={DB_CONFIG['DRIVER']};"
        f"SERVER={DB_CONFIG['SERVER']};"
        f"DATABASE={DB_CONFIG['DATABASE']};"
        f"UID={DB_CONFIG['UID']};"
        f"PWD={DB_CONFIG['PWD']};"
    )
    return pyodbc.connect(conn_str)

def add_expense(email, category, amount, expense_date, thread_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Expenses (user_email, category, amount, expense_date,thread_id)
        VALUES (?, ?, ?, ?,?)
    """, (email, category, amount, expense_date, thread_id))
    conn.commit()
    conn.close()
    return {"status": "success", "message": f"Added {amount} for {category} on {expense_date}"}

def get_expense_summary(email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    select top 50 category,amount,expense_date, DATEPART(WEEK,expense_date) as week_number from expenses 
        WHERE user_email  = ?
        order by expense_date desc
    """, (email,))
    rows = cursor.fetchall()
    conn.close()

    result = [
        {
            "category": row.category,
            "amount": row.amount,
            "expense_date": row.expense_date.strftime("%Y-%m-%d"),
            "week_number": row.week_number
        }
        for row in rows
    ]

    print("result is \n", result)

    return result

def get_weekly_expense(email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT DATEPART(WEEK, expense_date) AS week_number,
               SUM(amount) AS total_spent
        FROM Expenses
        WHERE user_email = ?
        GROUP BY DATEPART(WEEK, expense_date)
        ORDER BY week_number
    """, (email,))
    rows = cursor.fetchall()
    conn.close()
    return {row[0]: row[1] for row in rows}


print(get_connection())