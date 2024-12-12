import streamlit as st
import openai

# ChatGPT API 키 설정
openai.api_key = "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"

def get_optimization_hint(query, schema):
    """GPT API를 활용해 쿼리 최적화 힌트를 얻는 함수"""
    prompt = f"""
    The following is a TPC-H database schema:
    {schema}
    
    Based on this schema, optimize the following SQL query:
    {query}
    
    Provide a detailed explanation and an optimized version of the query.
    """
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']

# Streamlit UI
st.title("📊 TPC-H SQL Optimizer")
st.markdown("AutoSteer를 활용하여 TPC-H 데이터셋의 쿼리를 최적화하는 도구입니다.")

# Step 1: DB Schema 입력
st.subheader("1️⃣ DB 스키마 입력")
schema_input_method = st.radio("스키마 입력 방법을 선택하세요:", ("텍스트 입력", "파일 업로드"))

if schema_input_method == "텍스트 입력":
    schema = st.text_area("TPC-H 스키마를 입력하세요.")
elif schema_input_method == "파일 업로드":
    uploaded_file = st.file_uploader("TPC-H 스키마 파일 업로드", type=["txt", "sql"])
    if uploaded_file:
        schema = uploaded_file.read().decode("utf-8")
    else:
        schema = ""

# Step 2: SQL 쿼리 입력
st.subheader("2️⃣ SQL 쿼리 입력")
query = st.text_area("최적화하고자 하는 SQL 쿼리를 입력하세요.")

# Step 3: 최적화 실행
if st.button("🚀 Optimize"):
    if schema and query:
        with st.spinner("ing..."):
            result = get_optimization_hint(query, schema)
        st.subheader("최적화 결과")
        st.text_area("Autosteer의 최적화 힌트", result, height=300)
    else:
        st.error("DB 스키마와 SQL 쿼리를 모두 입력하세요.")

# Step 4: 결과 다운로드
if "result" in locals():
    st.download_button(
        label="💾 최적화 결과 다운로드",
        data=result,
        file_name="optimized_query.txt",
        mime="text/plain",
    )
