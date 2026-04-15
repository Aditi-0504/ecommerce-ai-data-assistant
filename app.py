import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from db import get_connection
from filters import load_filters, view_controls
from query_engine import generate_sql
from insights import generate_insight


st.title("E-Commerce AI Data Assistant")

conn = get_connection()
cursor = conn.cursor()

state, year, category = load_filters(cursor)
show_sql, show_table, show_chart, show_insight, chart_type = view_controls()

user_query = st.text_input("Enter your query")

if st.button("Run Query"):

    sql_query = generate_sql(user_query, state, year, category)

    if sql_query:
        cursor.execute(sql_query)
        results = cursor.fetchall()

        df = pd.DataFrame(results, columns=[desc[0] for desc in cursor.description])

        if show_sql:
            st.subheader("SQL")
            st.code(sql_query)

        if show_table:
            st.dataframe(df)

        if show_chart:
            if chart_type == "Pie":
                fig, ax = plt.subplots()
                ax.pie(df[df.columns[1]], labels=df[df.columns[0]], autopct='%1.1f%%')
                st.pyplot(fig)
            elif chart_type == "Line":
                st.line_chart(df.set_index(df.columns[0]))
            else:
                st.bar_chart(df.set_index(df.columns[0]))

        if show_insight:
            st.success(generate_insight(user_query, results))

    else:
        st.error("Query not understood")

cursor.close()
conn.close()