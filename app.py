import streamlit as st
import pandas as pd

# Correct the formation of the URL
sheet_id = "1PmOf1bjCpLGm7DiF7dJsuKBne2XWkmHyo20BS4xgizw"
sheet_name = "charlas"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

# Read the data from the URL and perform data cleaning
df = pd.read_csv(url)

# Function to filter data based on user input
def filter_data(user_input):
    filtered_df = df[df["対象事業者"].str.contains(user_input)]
    return filtered_df

# Streamlit app
def main():
    # Set Streamlit page title
    st.set_page_config(page_title="CSV Chatbot")

    # Display title and instructions
    st.title("CSV Chatbot")
    st.markdown("Enter a keyword to search for matching data in the CSV.")

    # User input textbox
    user_input = st.text_input("Enter a keyword")

    # Filter and display the data
    if st.button("Search"):
        if user_input:
            filtered_data = filter_data(user_input)
            st.dataframe(filtered_data)

# Run the Streamlit app
if __name__ == "__main__":
    main()
