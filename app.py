from langchain.chat_models import ChatOpenAI
from kor import create_extraction_chain
from kor.nodes import Object, Text
from dotenv import load_dotenv
import streamlit as st
import json
from schema import get_schema


def main():
    load_dotenv()
    st.set_page_config(page_title="Structure Data Extraction ChatBot")
    st.header("Tell me about the organizations you joined 💬")

    # chatbot setup
    chat_bot = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0, max_tokens=2000)

    person_schema = get_schema("person")

    extract_person_chain = create_extraction_chain(chat_bot, person_schema, encoder_or_encoder_class="json", input_formatter=None)

    if "messages" not in st.session_state:
        st.session_state.messages = []

    
    # print all previous messsages in the session
    for message in st.session_state.messages:
        st.chat_message(message["role"]).write(message["content"])


    # conversation UI setup
    if message_usr := st.chat_input("Say something"):
        st.chat_message("user").write(message_usr)
        st.session_state.messages.append({"role": "user", "content": message_usr})

        message_ai_extract = extract_person_chain.run(text=(message_usr))["data"]
        format_message_ai_extract = json.dumps(message_ai_extract, indent=2)

        st.chat_message("assistant").text(format_message_ai_extract)
        st.session_state.messages.append({"role": "assistant", "content": format_message_ai_extract})

if __name__ == "__main__":
    main()
