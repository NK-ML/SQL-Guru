from dotenv import load_dotenv
import streamlit as st
import os
import sqlite3
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

def get_gemini_response(question, prompt):
    model = genai.GenerativeModel("gemini-1.5-pro")
    response = model.generate_content(question + "\n\n" + prompt)
    return response.text.strip()

def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
        rows = cursor.fetchall()
    except sqlite3.Error as e:
        rows = [("SQL Error:", str(e))]
    finally:
        conn.close()
    return rows    

prompt = """
You are an expert in converting English questions into SQL queries.
The database is student.db with columns: Name, Class, Section, Marks.
Example 1:
Q: How many records are there in the student table?
A: SELECT COUNT(*) FROM student;
Example 2:
Q: What is the name of the student who scored the highest marks?
A: SELECT Name FROM student WHERE Marks = (SELECT MAX(Marks) FROM student);
Your SQL query should:
- Be a single valid SQL statement.
- Not contain SQL keywords in explanations.
- Not include triple quotes at the start or end.
"""

st.set_page_config(page_title='SQL GURU', page_icon='🧠')
st.header('Gemini-powered SQL Query Generator')

question = st.text_input('Enter your question')
submit = st.button('Submit')

if submit and question:
    response = get_gemini_response(question, prompt)
    st.subheader("Generated SQL Query:")
    st.code(response, language="sql")
    
    data = read_sql_query(response, 'student.db')

    st.subheader("Query Results:")
    if data:
        if len(data) == 1 and len(data[0]) == 1:
            st.write(data[0][0])
        else:
            result_strings = []
            for row in data:
                result_strings.append("[" + ", ".join(map(str, row)) + "]") 
            st.write("\n".join(result_strings))
    else:
        st.write("No results found.")