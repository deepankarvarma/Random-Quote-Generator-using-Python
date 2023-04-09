import streamlit as st
import requests

def fetch_quote():
    response = requests.get("https://api.quotable.io/random")
    data = response.json()
    return data['content'], data['author']

def main():
    quote, author = fetch_quote()

    quote_display = st.empty() # Create an empty element to hold the quote text

    quote_display.write(f"{quote} — {author}")

    if st.button("Get Another"):
        quote, author = fetch_quote()
        quote_display.write(f"{quote} — {author}")

if __name__ == '__main__':
    main()
