# 🧠 Text-to-SQL App

🚀 **Live Demo:** https://text-to-sql-app-aavsvgi5gr5imyjppejujm.streamlit.app

---
A simple AI-powered application that converts natural language queries into SQL and executes them on a SQLite database using Streamlit.

---

## 🚀 Features

* Convert plain English into SQL queries
* Execute queries on a structured database
* Display results in a clean table format
* Built-in safety checks to block destructive queries (DROP, DELETE, UPDATE)
* Handles filtering conditions like:

  * customer id
  * city
  * order amount

---

## 🛠 Tech Stack

* Python
* Streamlit
* SQLite
* Pandas

---

## 📂 Project Structure

text-to-sql-app/
│
├── app.py
├── utils/
│   ├── db.py
│   ├── llm.py
│
├── database/
│   ├── db.sqlite
│   ├── init_db.py
│
├── screenshots/
├── requirements.txt
├── README.md

---

## ▶️ How to Run

1. Clone the repository

```bash
git clone <your-repo-link>
cd text-to-sql-app
```

2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Initialize database

```bash
python database/init_db.py
```

5. Run the app

```bash
streamlit run app.py
```


## ⚠️ Safety Feature

The app prevents execution of destructive queries such as:

* DROP
* DELETE
* UPDATE

---

## 💡 Future Improvements

* Integrate real LLM (OpenAI / HuggingFace)
* Add JOIN automation
* Improve query understanding
* Add authentication

---

## 👩‍💻 Author

Siddhi Bhalekar
