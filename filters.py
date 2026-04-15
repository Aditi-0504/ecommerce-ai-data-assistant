import streamlit as st

def load_filters(cursor):
    st.sidebar.header("Filters")

    cursor.execute("SELECT DISTINCT customer_state FROM public.dim_customers")
    states = [row[0] for row in cursor.fetchall()]

    cursor.execute("SELECT DISTINCT year FROM public.dim_time ORDER BY year")
    years = [row[0] for row in cursor.fetchall()]

    cursor.execute("SELECT DISTINCT product_category_name FROM public.dim_products")
    categories = [row[0] for row in cursor.fetchall()]

    selected_state = st.sidebar.selectbox("State", ["All"] + states)
    selected_year = st.sidebar.selectbox("Year", ["All"] + [str(y) for y in years])
    selected_category = st.sidebar.selectbox("Category", ["All"] + categories)

    return selected_state, selected_year, selected_category


def view_controls():
    st.sidebar.header("View Options")

    show_sql = st.sidebar.checkbox("Show SQL", True)
    show_table = st.sidebar.checkbox("Show Table", True)
    show_chart = st.sidebar.checkbox("Show Charts", True)
    show_insight = st.sidebar.checkbox("Show Insight", True)

    chart_type = st.sidebar.selectbox("Chart Type", ["Auto", "Bar", "Line", "Pie"])

    return show_sql, show_table, show_chart, show_insight, chart_type