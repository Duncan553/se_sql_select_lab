# STEP 1A
# Import SQL Library and Pandas
import sqlite3
import pandas as pd

# STEP 1B
# Connect to the database
conn = sqlite3.connect("data.sqlite")

# Reference: all employee data
employee_data = pd.read_sql("""SELECT * FROM employees""", conn)
print("---------------------Employee Data---------------------")
print(employee_data)
print("-------------------End Employee Data-------------------")

# STEP 2
# Employee number and last name from all employees
df_first_five = pd.read_sql("""
    SELECT employeeNumber, lastName
    FROM employees
""", conn)

# STEP 3
# Last name before employee number
df_five_reverse = pd.read_sql("""
    SELECT lastName, employeeNumber
    FROM employees
""", conn)

# STEP 4
# Alias employeeNumber as 'ID'
df_alias = pd.read_sql("""
    SELECT lastName, employeeNumber AS ID
    FROM employees
""", conn)

# STEP 5
# CASE to bin job titles into Executive / Not Executive
df_executive = pd.read_sql("""
    SELECT *,
        CASE
            WHEN jobTitle = 'President'
              OR jobTitle = 'VP Sales'
              OR jobTitle = 'VP Marketing'
            THEN 'Executive'
            ELSE 'Not Executive'
        END AS role
    FROM employees
""", conn)

# STEP 6
# Length of last name as name_length
df_name_length = pd.read_sql("""
    SELECT LENGTH(lastName) AS name_length
    FROM employees
""", conn)

# STEP 7
# First two letters of job title as short_title
df_short_title = pd.read_sql("""
    SELECT SUBSTR(jobTitle, 1, 2) AS short_title
    FROM employees
""", conn)

# Reference: order details data
order_details = pd.read_sql("""SELECT * FROM orderDetails;""", conn)
print("------------------Order Details Data------------------")
print(order_details)
print("----------------End Order Details Data----------------")

# STEP 8
# Sum of rounded total prices (priceEach * quantityOrdered)
sum_total_price = pd.read_sql("""
    SELECT ROUND(priceEach * quantityOrdered) AS total_price
    FROM orderDetails
""", conn).sum()

# STEP 9
# Original orderDate + day, month, year columns
df_day_month_year = pd.read_sql("""
    SELECT
        orderDate,
        STRFTIME('%d', orderDate) AS day,
        STRFTIME('%m', orderDate) AS month,
        STRFTIME('%Y', orderDate) AS year
    FROM orderDetails
""", conn)

# Close the connection
conn.close()