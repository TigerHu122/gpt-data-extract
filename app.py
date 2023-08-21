from langchain.chat_models import ChatOpenAI
from langchain.memory.summary import ConversationSummaryMemory
from langchain.chains import ConversationChain

from dotenv import load_dotenv
import streamlit as st


def main():
    load_dotenv()
    st.set_page_config(page_title="Personal ChatBot")
    st.header("Have a Conversation 💬")

    # chatbot setup
    chat_bot = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0, max_tokens=2000)


    memory = ConversationSummaryMemory(llm=chat_bot)
    conversation_chain = ConversationChain(llm=chat_bot, memory=memory, verbose=True)



    if "messages" not in st.session_state:
        st.session_state.messages = []

    # print all previous messsages in the session
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # conversation UI setup
    if message_usr := st.chat_input("Say something"):
        with st.chat_message("user"):
            st.markdown(message_usr)
        st.session_state.messages.append({"role": "user", "content": message_usr})

        message_ai = conversation_chain.predict(input=message_usr)

        with st.chat_message("assistant"):
            st.markdown(message_ai)
        st.session_state.messages.append(
            {"role": "assistant", "content": message_ai})


if __name__ == "__main__":
    main()
