import streamlit as st
import openai

# OpenAI API 키 설정
openai.api_key = "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"

def generate_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message['content']

# Streamlit 앱 설정
st.title("AI 챗봇")

user_input = st.text_input("대화 입력:")

if st.button("전송"):
    if user_input:
        with st.spinner("응답 생성 중..."):
            response = generate_response(user_input)
            st.text_area("챗봇 응답:", value=response, height=200)
    else:
        st.warning("입력 필드를 비워둘 수 없습니다.")
