def generate_sql(user_input):
    user_input = user_input.lower()
    words = user_input.split()

    # 🚨 Safety
    if any(word in words for word in ["drop", "delete", "update"]):
        return None

    # 🔗 JOIN
    if "customer" in words and "order" in words:
        return """
        SELECT customers.name, orders.amount, orders.date
        FROM customers
        JOIN orders ON customers.id = orders.customer_id;
        """

    # 👤 CUSTOMERS (CHECK FIRST!)
    if "customers" in words or "customer" in words:

        if "id" in words:
            for i, word in enumerate(words):
                if word == "id":
                    if i+1 < len(words) and words[i+1].isdigit():
                        return f"SELECT * FROM customers WHERE id = {words[i+1]};"

        if "mumbai" in words:
            return "SELECT * FROM customers WHERE city = 'Mumbai';"

        return "SELECT * FROM customers;"

    # 📦 ORDERS
    if "orders" in words or "order" in words:

        conditions = []

        if "above" in words or "greater" in words:
            for word in words:
                if word.isdigit():
                    conditions.append(f"amount > {word}")
                    break

        if "customer" in words and "id" in words:
            for i, word in enumerate(words):
                if word == "id":
                    if i+1 < len(words) and words[i+1].isdigit():
                        conditions.append(f"customer_id = {words[i+1]}")

        if "date" in words:
            return "SELECT id, customer_id, amount, date FROM orders;"

        if conditions:
            return f"SELECT * FROM orders WHERE {' AND '.join(conditions)};"

        return "SELECT * FROM orders;"

    return None