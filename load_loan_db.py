# import os
import psycopg2

conn = psycopg2.connect(
    '''host=ec2-54-225-241-25.compute-1.amazonaws.com dbname=d4mmfd28jhu33d user=pkvdgzetxertgh password=8ea6dd1dda6f7b947adf2a378d2494bed62cd58e7b3bf14baa55a16117a2ce90''')
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS loan_data(
    Customer_ID integer,
    Status_Checking_Acc text,
    Duration_in_Months integer,
    Credit_History text,
    Purposre_Credit_Taken text,
    Credit_Amount integer,
    Savings_Acc text,
    Years_At_Present_Employment text,
    Inst_Rt_Income integer,
    Marital_Status_Gender text,
    Other_Debtors_Guarantors text,
    Current_Address_Yrs integer,
    Property text,
    Age integer,
    Other_Inst_plans text,
    Housing text,
    Num_CC integer,
    Job text,
    Dependents integer,
    Telephone text,
    Foreign_Worker text,
    Default_On_Payment integer,
    Count integer
)
""")

conn.commit()

with open('data/bank_loan_defaults.csv', 'r') as f:
    # Notice that we don't need the `csv` module.
    next(f)  # Skip the header row.
    cur.copy_from(f, 'loan_data', sep=',')

conn.commit()
