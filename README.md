# 📊 TPC-H SQL Optimizer

**TPC-H SQL Optimizer** is a web application designed to optimize SQL queries for the **TPC-H dataset** using the **GPT API**. The tool analyzes user-provided database schemas and SQL queries to propose **optimization strategies** and generates optimized SQL queries along with detailed explanations.

---

## 🛠️ Features

1. **Database Schema Input**:
   - Users can input the TPC-H database schema either as text or by uploading a `.sql` file.

2. **SQL Query Input**:
   - Allows users to input SQL queries they want to optimize.

3. **SQL Optimization Using AutoSteer**:
   - Optimize SQL queries for better performance.

4. **Markdown-formatted Optimization Results**:
   - Displays optimization results in a structured Markdown format for readability.

5. **Download Optimization Results**:
   - Users can download the optimized queries and explanations as a `.md` file.

---

## 💡 Project Goals

- **SQL Performance Optimization**:
  - Help users optimize SQL queries for better execution efficiency on TPC-H or similar databases.

- **Automated SQL Analysis**:
  - Provide a tool to analyze and optimize SQL queries without requiring extensive database expertise.

- **Showcasing GPT Capabilities**:
  - Demonstrate the application of OpenAI's GPT models in database query optimization tasks.

---

## 🔧 Technologies Used

- **Frontend/UI**: [Streamlit](https://streamlit.io/)
- **Database**: TPC-H dataset schema
- **Language**: Python

---

## 🚀 Installation and Setup

### 1. **Clone the Repository**
```bash
git clone https://github.com/username/tpch-sql-optimizer.git
cd tpch-sql-optimizer
### 2. **Create and Activate a Virtual Environment**

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

```

### 3. **Install Required Packages**

```bash
pip install -r requirements.txt

```

### 4. **Set Up API Key**

Set your OpenAI API key as an environment variable or directly in the code:

```bash
export OPENAI_API_KEY="your_openai_api_key"

```

### 5. **Run the Application**

```bash
streamlit run app.py

```

### 6. **Access the Application**

Open your browser and navigate to [http://localhost:8501](http://localhost:8501/) to use the application.

---

## 📋 Usage Example

### **Input**

1. **TPC-H Schema**:
    
    ```sql
    CREATE TABLE customer (
        c_custkey INT NOT NULL,
        c_name VARCHAR(25) NOT NULL,
        ...
    );
    
    ```
    
2. **SQL Query**:
    
    ```sql
    SELECT c_name, o_orderdate, o_totalprice
    FROM customer c
    JOIN orders o
    ON c.c_custkey = o.o_custkey
    WHERE c.c_mktsegment = 'AUTOMOBILE'
      AND o.o_orderdate >= '1995-01-01'
      AND o.o_orderdate < '1996-01-01';
    
    ```
    

### **Output**

- GPT-generated optimization strategies and optimized query:
    
    ```markdown
    ## 📊 SQL Query Optimization Results
    
    ### Optimization Strategies and Reasoning
    1. Add indexes to improve join and filtering performance.
    2. Use a subquery to pre-filter rows for the join operation.
    3. Rearrange query execution order for better performance.
    
    ### Optimized SQL Query
    ```sql
    SELECT c.c_name, o.o_orderdate, o.o_totalprice
    FROM customer c
    JOIN (
        SELECT o_custkey, o_orderdate, o_totalprice
        FROM orders
        WHERE o.o_orderdate >= '1995-01-01'
          AND o.o_orderdate < '1996-01-01'
    ) o
    ON c.c_custkey = o.o_custkey
    WHERE c.c_mktsegment = 'AUTOMOBILE';
    
    ```

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](https://chatgpt.com/c/LICENSE) file for details.
