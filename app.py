import streamlit as st
from llm import get_ai_messages
from dotenv import load_dotenv
import os

st.title("Streamlit 기본 예제")
st.write("잘 해봅시다.")
load_dotenv()

# 1. 스트림릿은 자동 재시작되면서 코드를 읽어서 이전의 내용 사라짐. 막으려고 리스트화
if "message_list" not in st.session_state:
    st.session_state.message_list = []
# 2. 기존의 내용 출력 [사용자]
for message in st.session_state.message_list:
    with st.chat_message(message["role"]):
        st.write(message["content"])
# print(f'before == {st.session_state.message_list}')       # 스트림릿 동작 원리 파악 로그
if user_question := st.chat_input(placeholder='소득세에 관련된 궁금한 내용들을 말씀하세요.'):
    # 4. 사용자 입력
    with st.chat_message("user"):
        st.write(user_question)
    st.session_state.message_list.append({"role":"user","content":user_question})
    # 5. AI 출력
    with st.spinner("답변을 생성하는 중입니다."):                # 스켈레톤 ui 같이 로딩창 생성
        ai_response=get_ai_messages(user_question)              # AI 출력 메세지
        with st.chat_message("ai"):
            ai_message=st.write_stream(ai_response)
    st.session_state.message_list.append({"role":"ai", "content":ai_message})
# print(f'after == {st.session_state.message_list}')        # 스트림릿 동작 원리 파악 로그
