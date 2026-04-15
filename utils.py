def normalize_query(user_query):
    return user_query.lower()\
        .replace("categories", "category")\
        .replace("states", "state")


def apply_filters(query, state, year, category):
    conditions = []

    if state != "All":
        conditions.append(f"c.customer_state = '{state}'")

    if year != "All":
        conditions.append(f"t.year = {year}")

    if category != "All":
        conditions.append(f"p.product_category_name = '{category}'")

    if conditions:
        return query.replace(
            "GROUP BY",
            "WHERE " + " AND ".join(conditions) + " GROUP BY"
        )

    return query