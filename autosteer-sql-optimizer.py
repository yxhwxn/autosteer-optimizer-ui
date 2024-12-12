import streamlit as st
import openai

# ChatGPT API 키 설정

def get_optimization_hint(query, schema):
    prompt = f"""
    You are the role of optimizing the query used by the TPC-H database about 10GB from now on.

    However, you should derive the query optimization result based on the Autosteer open source.
    
    The following is a TPC-H database schema:
    {schema}
    
    Based on this schema, optimize the following SQL query:
    {query}
    
    Provide a detailed explanation and an optimized version of the query. 
    
    Please note that the lineitem table is a heavy table with a size of about 7GB.

    I hope the main flow of the answer is as follows.

    1. Autosteer에서 사용한 힌트셋

    2. 해당 힌트가 적용된 튜닝된 쿼리

    3. 튜닝된 쿼리에 대한 설명

    답변은 한국어로 해줘.
    """
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",  # 'gpt-4' 또는 'gpt-3.5-turbo' 사용
        messages=[
            {"role": "system", "content": "You are a database query optimization expert."},
            {"role": "user", "content": prompt},
        ]
    )
    return response['choices'][0]['message']['content']

def format_markdown_response(response):
    """GPT 응답을 Markdown 형식으로 포맷"""
    return f"""
## 📊 SQL 쿼리 최적화 결과

{response}
"""

# Streamlit UI
st.title("📊 SQL Optimizer with AutoSteer")
st.markdown("TCNN 모델이 탑재된 AutoSteer를 활용하여 TPC-H 데이터셋의 쿼리를 최적화하는 도구입니다.")

# Step 1: DB Schema 입력
st.subheader("1️⃣ DB Schema Input")
schema_input_method = st.radio("Schema input method:", ("text", "file-upload"))

if schema_input_method == "text":
    schema = st.text_area("Input TPC-H schema info.")
elif schema_input_method == "file-upload":
    uploaded_file = st.file_uploader("Upload TPC-H schema info.", type=["txt", "sql"])
    if uploaded_file:
        schema = uploaded_file.read().decode("utf-8")
    else:
        schema = ""

# Step 2: SQL 쿼리 입력
st.subheader("2️⃣ SQL Query Input")
query = st.text_area("Enter the SQL query you want to optimize.")

# Step 3: 최적화 실행
if st.button("🚀 Optimize"):
    if schema and query:
        with st.spinner("in progress..."):
            raw_result = get_optimization_hint(query, schema)
            markdown_result = format_markdown_response(raw_result)
        st.subheader("[Optimized Result]")
        st.markdown(markdown_result, unsafe_allow_html=True)  # Markdown 형식으로 출력
    else:
        st.error("DB 스키마와 SQL 쿼리를 모두 입력하세요.")

# Step 4: 결과 다운로드
if "raw_result" in locals():
    st.download_button(
        label="💾 download",
        data=raw_result,
        file_name="optimized_query.md",  # Markdown 파일로 저장
        mime="text/markdown",
    )
