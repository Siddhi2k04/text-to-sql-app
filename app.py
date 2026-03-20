import streamlit as st
import pandas as pd
from utils.llm import generate_sql
from utils.db import run_query

st.markdown("""
    <style>
    .stTextInput > div > div > input {
        font-size: 16px;
        padding: 10px;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
        border-radius: 8px;
        padding: 10px 20px;
    }
    </style>
""", unsafe_allow_html=True)

# App Title
st.title("🧠 Text to SQL App")

# User Input
user_input = st.text_input("Ask your question:")

# Button Click
if st.button("Generate SQL"):

    # Handle empty input
    if not user_input.strip():
        st.warning("⚠️ Please enter a question.")
        st.stop()

    # Generate SQL with loading spinner
    with st.spinner("🤖 Generating SQL... Please wait..."):
        sql_query = generate_sql(user_input)

    # Safety fallback (VERY IMPORTANT)
    if not sql_query:
        sql_query = "SELECT * FROM orders;"

    # Show SQL
    st.subheader("Generated SQL:")
    st.code(sql_query, language="sql")

    # Prevent dangerous queries
    if any(word in sql_query.lower() for word in ["drop", "delete", "update"]):
        st.error("Unsafe query detected!")
    if not sql_query:
     st.error("Invalid or unsafe query!")
    
    else:
        try:
            columns, results = run_query(sql_query)

            st.subheader("Results:")

            if results:
                # ensure results is list of rows
                if isinstance(results[0], (int, str)):
                    results = [results]

                df = pd.DataFrame(results)

                # Convert all to string
                df = df.astype(str)

                # Assign column names if matching
                if len(df.columns) == len(columns):
                    df.columns = columns

                st.dataframe(df)

            else:
                st.info("No results found.")

        except Exception as e:
            st.error(f"Error: {e}")