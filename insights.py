def generate_insight(user_query, results):
    if not results:
        return "No data found."

    if "state" in user_query:
        return f"Top state is {results[0][0]} with highest revenue."

    elif "category" in user_query:
        return f"Top category is {results[0][0]} showing strong demand."

    elif "monthly" in user_query:
        return "Revenue shows growth trend with fluctuations."

    elif "yearly" in user_query:
        return "Yearly revenue indicates business expansion."

    elif "segment" in user_query:
        return "Customer segmentation shows value distribution."

    return "Basic analysis complete."