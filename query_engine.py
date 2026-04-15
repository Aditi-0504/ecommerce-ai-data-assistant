from utils import normalize_query, apply_filters

def generate_sql(user_query, state, year, category):
    user_query = normalize_query(user_query)

    if "revenue" in user_query and ("state" in user_query or "top" in user_query):
        base_query = """
        SELECT c.customer_state, SUM(f.price + f.freight_value) AS revenue
        FROM public.fact_sales f
        JOIN public.dim_customers c ON f.customer_id = c.customer_id
        JOIN public.dim_time t ON DATE(f.order_date) = t.date
        JOIN public.dim_products p ON f.product_id = p.product_id
        GROUP BY c.customer_state
        ORDER BY revenue DESC
        LIMIT 5
        """
        return apply_filters(base_query)

    elif "customer" in user_query and "top" in user_query:
        return """
        SELECT customer_id, SUM(price + freight_value) AS revenue
        FROM public.fact_sales
        GROUP BY customer_id
        ORDER BY revenue DESC
        LIMIT 10;
        """

    elif "top" in user_query and "revenue" in user_query:
        base_query = """
        SELECT c.customer_state, SUM(f.price + f.freight_value) AS revenue
        FROM public.fact_sales f
        JOIN public.dim_customers c ON f.customer_id = c.customer_id
        JOIN public.dim_time t ON DATE(f.order_date) = t.date
        JOIN public.dim_products p ON f.product_id = p.product_id
        GROUP BY c.customer_state
        ORDER BY revenue DESC
        LIMIT 5
        """
        return apply_filters(base_query)

    elif "monthly" in user_query:
        return """
        SELECT t.year, t.month, SUM(f.price + f.freight_value) AS revenue
        FROM public.fact_sales f
        JOIN public.dim_time t
        ON DATE(f.order_date) = t.date
        GROUP BY t.year, t.month
        ORDER BY t.year, t.month;
        """

    elif "revenue" in user_query:
        base_query = """
        SELECT SUM(price + freight_value) AS total_revenue
        FROM public.fact_sales
        """
        return base_query
    
    elif "category" in user_query:
        return """
        SELECT p.product_category_name, SUM(f.price) AS revenue
        FROM public.fact_sales f
        JOIN public.dim_products p
        ON f.product_id = p.product_id
        GROUP BY p.product_category_name
        ORDER BY revenue DESC
        LIMIT 10;
        """

    elif "yearly" in user_query:
        return """
        SELECT t.year, SUM(f.price + f.freight_value) AS revenue
        FROM public.fact_sales f
        JOIN public.dim_time t
        ON DATE(f.order_date) = t.date
        GROUP BY t.year
        ORDER BY t.year;
        """

    elif "segment" in user_query:
        return """
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

    return None