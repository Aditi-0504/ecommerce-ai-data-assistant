import psycopg2


conn = psycopg2.connect(
    dbname="ecommerce_dw",
    user="postgres",
    password="newpassword123",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()

user_query = input("Ask your question: ").lower()



if "state" in user_query and "revenue" in user_query:
    sql_query = """
    SELECT c.customer_state, SUM(f.price + f.freight_value) AS revenue
    FROM public.fact_sales f
    JOIN public.dim_customers c
    ON f.customer_id = c.customer_id
    GROUP BY c.customer_state
    ORDER BY revenue DESC
    LIMIT 5;
    """

elif "customer" in user_query and "top" in user_query:
    sql_query = """
    SELECT customer_id, SUM(price + freight_value) AS revenue
    FROM public.fact_sales
    GROUP BY customer_id
    ORDER BY revenue DESC
    LIMIT 10;
    """

elif "monthly" in user_query:
    sql_query = """
    SELECT t.year, t.month, SUM(f.price + f.freight_value) AS revenue
    FROM public.fact_sales f
    JOIN public.dim_time t
    ON DATE(f.order_date) = t.date
    GROUP BY t.year, t.month
    ORDER BY t.year, t.month;
    """

elif "category" in user_query:
    sql_query = """
    SELECT p.product_category_name, SUM(f.price) AS revenue
    FROM public.fact_sales f
    JOIN public.dim_products p
    ON f.product_id = p.product_id
    GROUP BY p.product_category_name
    ORDER BY revenue DESC
    LIMIT 10;
    """

elif "yearly" in user_query:
    sql_query = """
    SELECT t.year, SUM(f.price + f.freight_value) AS revenue
    FROM public.fact_sales f
    JOIN public.dim_time t
    ON DATE(f.order_date) = t.date
    GROUP BY t.year
    ORDER BY t.year;
    """

elif "segment" in user_query:
    sql_query = """
    SELECT 
        segment,
        COUNT(*) AS customers
    FROM (
        SELECT 
            customer_id,
            CASE 
                WHEN SUM(price) > 1000 THEN 'High Value'
                WHEN SUM(price) > 500 THEN 'Medium Value'
                ELSE 'Low Value'
            END AS segment
        FROM public.fact_sales
        GROUP BY customer_id
    ) sub
    GROUP BY segment;
    """

else:
    print("Sorry, I don't understand the query yet.")
    cursor.close()
    conn.close()
    exit()

print("\nGenerated SQL:\n", sql_query)

cursor.execute(sql_query)
results = cursor.fetchall()

print("\nResults:\n")
for row in results:
    print(row)

def generate_insight(user_query, results):
    if not results:
        return "No data found."

    if "state" in user_query:
        return f"Top performing state is {results[0][0]}, indicating strong regional demand concentration."

    elif "customer" in user_query:
        return "Revenue is widely distributed across customers, indicating a diversified customer base with low dependency risk."

    elif "monthly" in user_query:
        return "Revenue trend shows gradual growth with fluctuations, indicating stable business expansion over time."

    elif "category" in user_query:
        return f"Top category is {results[0][0]}, suggesting high demand in this product segment."

    elif "yearly" in user_query:
        return "Yearly revenue trend indicates overall business growth and increasing market adoption."

    elif "segment" in user_query:
        return "Customer segmentation shows distribution across value tiers, useful for targeted marketing strategies."

    return "Basic analysis completed."

insight = generate_insight(user_query, results)
print("\nInsight:\n", insight)

cursor.close()
conn.close()