# 🧠 Text-to-SQL Web App

A web-based application that converts natural language queries into SQL and executes them on a database in real-time.

## 🚀 Features

* Convert plain English to SQL queries
* Supports filtering (id, city, amount)
* Handles multiple conditions
* JOIN queries between tables
* Safe query execution (prevents harmful SQL)
* Interactive UI using Streamlit

## 🛠️ Tech Stack

* Python
* SQLite
* Streamlit
* Transformers (HuggingFace)

## 📌 Example Queries

* show all customers
* show customer with id 1
* show orders above 5000
* show orders for customer id 1
* show customers with their orders

## 📷 Screenshots

(Add your screenshots here)

## ⚙️ How to Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

## 💡 Future Improvements

* Add support for more complex SQL queries
* Improve LLM accuracy
* Deploy as a web app
