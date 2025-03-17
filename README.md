# SQL GURU

SQL GURU is a Streamlit-powered application that utilizes the Google Gemini API to generate SQL queries from natural language input. The app supports SQLite and includes error handling for seamless query execution.

## Features
- Converts natural language questions into SQL queries.
- Uses the Google Gemini API for intelligent query generation.
- Executes queries on an SQLite database (`student.db`).
- Displays query results in a user-friendly format.
- Handles SQL errors gracefully.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/sql-guru.git
   cd sql-guru
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your API key:
   - Create a `.env` file in the project directory.
   - Add the following line, replacing `your_api_key` with your Google Gemini API key:
     ```
     GOOGLE_API_KEY=your_api_key
     ```

## Usage

1. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```
2. Enter a natural language question related to the `student` database.
3. View the generated SQL query and query results.

## Example Queries
**Input:**
```
How many records are there in the student table?
```
**Generated SQL:**
```sql
SELECT COUNT(*) FROM student;
```

**Input:**
```
What is the name of the student who scored the highest marks?
```
**Generated SQL:**
```sql
SELECT Name FROM student WHERE Marks = (SELECT MAX(Marks) FROM student);
```

## Dependencies
- Python 3.7+
- Streamlit
- SQLite
- Google Generative AI SDK
- Python-dotenv

## Contributing
Feel free to submit pull requests or raise issues to enhance the project.

## License
This project is licensed under the MIT License.

## Author
[Nandan](https://github.com/your-username)

