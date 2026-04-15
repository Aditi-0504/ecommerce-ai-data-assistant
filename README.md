# 📊 E-Commerce AI Data Assistant

An interactive data analytics platform that enables users to query an e-commerce data warehouse using natural language and visualize insights instantly.

---

## 🚀 Overview

The **E-Commerce AI Data Assistant** is a Streamlit-based application built on top of a structured PostgreSQL data warehouse. It allows users to ask business questions in plain English and receive:

- SQL query generation (rule-based NLP)
- Structured data output
- Visual analytics (bar, line, pie charts)
- Automated business insights

This project bridges the gap between **technical SQL querying** and **non-technical business understanding**.

---

## 🧠 Key Features

### 🔍 Natural Language Querying
Users can type queries like:
- `top revenue`
- `monthly revenue`
- `top categories`
- `customer segmentation`

The system interprets intent and converts it into SQL queries.

---

### 🗄️ Data Warehouse Integration
- Built on a **star schema**
- Uses fact and dimension tables:
  - `fact_sales`
  - `dim_customers`
  - `dim_products`
  - `dim_time`

---

### 📊 Interactive Dashboard
- Built using **Streamlit**
- Clean UI with real-time results
- Sidebar controls for filtering and visualization

---

### 🎛️ Dynamic Filters
Users can filter data by:
- State
- Year
- Product Category

All queries dynamically adjust based on selected filters.

---

### 📈 Visualizations
- Bar charts → category/state comparisons  
- Line charts → time-based trends  
- Pie charts → distribution analysis  

---

### 💡 Automated Insights
Each query result is accompanied by a business-level interpretation, making outputs easier to understand.

---

## 🏗️ Project Structure
```
ai_sql_project/
│
├── app.py              # Main Streamlit application (UI + execution)
├── db.py               # Database connection setup
├── query_engine.py     # Natural language → SQL logic
├── filters.py          # Sidebar filters and view controls
├── insights.py         # Business insight generation
├── utils.py            # Helper functions (query normalization, filters)
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

---

## ⚙️ Installation & Setup


### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/ecommerce-ai-data-assistant.git
cd ecommerce-ai-data-assistant
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Setup PostgreSQL
- Create a database: **ecommerce_dw**
- Load your dataset
- Ensure these tables exist:
  -  `fact_sales`
  -  `dim_customers`
  -  `dim_products`
  -  `dim_time`

### 4. Update Database Credentials
In `db.py`, update:
```bash
dbname="ecommerce_dw"
user="postgres"
password="your_password"
host="localhost"
port="5432"
```

---

## ▶️ Running the Application

```bash
streamlit run app.py
```
The app will open automatically in your browser.

---

## 🧪 Example Queries

Try these in the app:
  -  `top revenue`
  -  `state revenue`
  -  `monthly revenue`
  -  `yearly revenue`
  -  `top categories`
  -  `customer segmentation`

---

## 🧩 How It Works

1. User enters a query in natural language
2. Query is normalized and parsed
3. SQL is generated using rule-based logic
4. Filters are applied dynamically
5. Query is executed on PostgreSQL
6. Results are displayed as:
-    `Table`
-    `Chart`
-    `Insight`

---

## ⚠️ Limitations
-  Rule-based NLP (not fully dynamic like LLMs)
-  Limited to predefined query patterns
-  Requires structured schema

---

## 🔮 Future Enhancements
-  LLM integration (OpenAI / local models)
-  Advanced NLP parsing
-  Deployment on cloud (Streamlit Cloud / AWS)
-  User authentication
-  Query suggestions & auto-complete

---

## 🛠️ Tech Stack
-  Python
-  PostgreSQL
-  Streamlit
-  Pandas
-  Matplotlib

---

## 🎯 Use Cases
-  Business analytics dashboards
-  Data warehouse querying tools
-  Educational SQL + BI projects
-  Demonstration of full-stack data systems

---
