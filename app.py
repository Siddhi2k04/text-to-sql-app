
import streamlit as st
import pandas as pd
from utils.llm import generate_sql
from utils.db import run_query

st.title("🧠 Text to SQL App")

# User input
user_input = st.text_input("Ask your question:")

# Button click
if st.button("Generate SQL"):

    # Generate SQL
    with st.spinner("🤖 Generating SQL... Please wait..."):
         sql_query = generate_sql(user_input)    
    st.subheader("Generated SQL:")
    st.code(sql_query, language="sql")

    # 🚨 Safety check
    if any(word in sql_query.lower() for word in ["drop", "delete", "update", "insert"]):
        st.error("⚠️ Unsafe query detected!")
    else:
        try:
            columns, results = run_query(sql_query)

            st.subheader("Results:")

            if results:
    # 🔥 Fix: ensure results is list of rows
             if isinstance(results[0], (int, str)):
              results = [results]

             df = pd.DataFrame(results)

             df = df.astype(str)

             if len(df.columns) == len(columns):
              df.columns = columns

             st.dataframe(df)
            else:
                st.write("No results found.")

        except Exception as e:
            st.error(f"Error: {e}")