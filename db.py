import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="ecommerce_dw",
        user="postgres",
        password="newpassword123",
        host="localhost",
        port="5432"
    )