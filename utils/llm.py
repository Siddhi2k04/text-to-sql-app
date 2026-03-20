from transformers import pipeline

generator = None

def load_model():
    global generator
    if generator is None:
        generator = pipeline("text-generation", model="google/flan-t5-base")

def generate_sql(user_input):
    user_input = user_input.lower()

    if any(word in user_input for word in ["drop", "delete", "update"]):
     return None

    # JOIN
    if "customer" in user_input and "order" in user_input:
        return """
        SELECT customers.name, orders.amount, orders.date
        FROM customers
        JOIN orders ON customers.id = orders.customer_id;
        """

    # ORDERS
    if "order" in user_input:

        words = user_input.split()
        conditions = []

        # amount filter
        if "above" in user_input or "greater" in user_input:
            for word in words:
                if word.isdigit():
                    conditions.append(f"amount > {word}")
                    break

        # customer_id filter
        if "customer" in user_input and "id" in user_input:
            for i, word in enumerate(words):
                if word == "id":
                    for j in range(i+1, len(words)):
                        if words[j].isdigit():
                            conditions.append(f"customer_id = {words[j]}")
                            break

        # date column selection
        if "date" in user_input:
            return "SELECT id, customer_id, amount, date FROM orders;"

        if conditions:
            return f"SELECT * FROM orders WHERE {' AND '.join(conditions)};"

        return "SELECT * FROM orders;"

    # CUSTOMERS
    if "customer" in user_input:

        words = user_input.split()

        if "id" in user_input:
            for i, word in enumerate(words):
                if word == "id":
                    for j in range(i+1, len(words)):
                        if words[j].isdigit():
                            return f"SELECT * FROM customers WHERE id = {words[j]};"

        if "mumbai" in user_input:
            return "SELECT * FROM customers WHERE city = 'Mumbai';"

        

    return "SELECT * FROM customers;"
    return "SELECT * FROM orders;"