def generate_sql(user_input):
    user_input = user_input.lower()
    words = user_input.split()

    # Safety check
    if any(word in words for word in ["drop", "delete", "update"]):
        return None

    # JOIN (customers + orders)
    if "customer" in words and "order" in words:
        return """
        SELECT customers.name, orders.amount, orders.date
        FROM customers
        JOIN orders ON customers.id = orders.customer_id;
        """

    # CUSTOMERS
    if "customers" in words or "customer" in words:

        # filter by id
        if "id" in words:
            for i, word in enumerate(words):
                if word == "id":
                    if i + 1 < len(words) and words[i + 1].isdigit():
                        return f"SELECT * FROM customers WHERE id = {words[i + 1]};"

        # filter by city
        if "mumbai" in words:
            return "SELECT * FROM customers WHERE city = 'Mumbai';"

        return "SELECT * FROM customers;"

    # ORDERS
    if "orders" in words or "order" in words:

        conditions = []  

        # extract number safely
        number = None
        for word in words:
            if word.isdigit():
                number = word
                break

        # amount conditions
        if number:
            if "above" in words or "greater" in words:
                conditions.append(f"amount > {number}")
            elif "below" in words or "less" in words:
                conditions.append(f"amount < {number}")

        # customer_id filter
        if "customer" in words and "id" in words:
            for i, word in enumerate(words):
                if word == "id":
                    if i + 1 < len(words) and words[i + 1].isdigit():
                        conditions.append(f"customer_id = {words[i + 1]}")

        # select date column (only if no filters)
        if "date" in words and not conditions:
            return "SELECT id, customer_id, amount, date FROM orders;"

        # apply conditions
        if conditions:
            return f"SELECT * FROM orders WHERE {' AND '.join(conditions)};"

        return "SELECT * FROM orders;"

    return None