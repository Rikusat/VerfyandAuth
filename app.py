import streamlit as st
from langchain.agents import create_pandas_dataframe_agent
from langchain.chat_models import ChatOpenAI
from langchain.agents.agent_types import AgentType
import pandas as pd

# Correct the formation of the URL
sheet_id = "1PmOf1bjCpLGm7DiF7dJsuKBne2XWkmHyo20BS4xgizw"
sheet_name = "charlas"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

# Read the data from the URL and perform data cleaning
df = pd.read_csv(url, dtype=str).fillna("")

# Create a Pandas Dataframe Agent
agent = create_pandas_dataframe_agent(df)

# Create a ChatOpenAI agent
chat_agent = ChatOpenAI(
    langchain_agent=agent,
    model_name="gpt-3.5-turbo-0613",
    max_tokens=100,
    temperature=0.6
)

# Function to interact with the chatbot
def chat_with_bot(user_input):
    # Generate a response from the chatbot
    response = chat_agent.reply(user_input)
    return response

# Streamlit app
def main():
    # Set Streamlit page title
    st.set_page_config(page_title="CSV Chatbot")

    # Display title and instructions
    st.title("CSV Chatbot")
    st.markdown("Enter your question and the chatbot will provide a response based on the CSV data.")

    # User input textbox
    user_input = st.text_input("User Input")

    # Chatbot response
    if st.button("Ask"):
        if user_input:
            bot_response = chat_with_bot(user_input)
            st.text_area("Chatbot Response", value=bot_response, height=200)

# Run the Streamlit app
if __name__ == "__main__":
    main()
