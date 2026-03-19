from transformers import pipeline

generator = None

def load_model():
    global generator
    if generator is None:
        generator = pipeline("text-generation", model="google/flan-t5-base")

def generate_sql(user_input):
    user_input = user_input.lower()

    # 🔥 Rule-based overrides (smart layer)

    if "customer" in user_input:

    # 🔥 ID condition FIRST
     if "id" in user_input:
        words = user_input.split()
        for i, word in enumerate(words):
            if word == "id":
                for j in range(i+1, len(words)):
                    if words[j].isdigit():
                        return f"SELECT * FROM customers WHERE id = {words[j]};"

    # 🔥 City condition
    if "mumbai" in user_input:
        return "SELECT * FROM customers WHERE city = 'Mumbai';"

    # 🔥 Default (LAST)
    return "SELECT * FROM customers;"
    if "orders" in user_input:
        if "above" in user_input or "greater" in user_input:
            words = user_input.split()
            for word in words:
                if word.isdigit():
                    return f"SELECT * FROM orders WHERE amount > {word};"
        return "SELECT * FROM orders;"

    # fallback to AI
    return "SELECT * FROM customers;"