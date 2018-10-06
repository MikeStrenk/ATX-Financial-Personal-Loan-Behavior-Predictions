# import os
import psycopg2

conn = psycopg2.connect(
    '''host=ec2-54-225-241-25.compute-1.amazonaws.com dbname=d4mmfd28jhu33d user=pkvdgzetxertgh password=8ea6dd1dda6f7b947adf2a378d2494bed62cd58e7b3bf14baa55a16117a2ce90''')
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS loan_history(
    id SERIAL PRIMARY KEY,
    age INT,
    occupation VARCHAR(50),
    years_at_job INT,
    salary INT,
    home VARCHAR(20),
    credit VARCHAR(20),
    approval VARCHAR(20)
)
""")

conn.commit()
