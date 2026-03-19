def generate_sql(user_input):
    user_input = user_input.lower()

    if "customers" in user_input:
        if "mumbai" in user_input:
            return "SELECT * FROM customers WHERE city='Mumbai';"
        return "SELECT * FROM customers;"

    if "orders" in user_input:
        if "above" in user_input or "greater" in user_input:
            return "SELECT * FROM orders WHERE amount > 5000;"
        return "SELECT * FROM orders;"

    return "SELECT * FROM customers;"