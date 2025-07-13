import streamlit as st
from scrape import scrape_website

st.title("AI Web Scrapper")
url=st.text_input("Enter the website URL:")

if st.button("Scrape Site"):
    st.write(f"Scrapping the websiter:{url}")
    result=scrape_website(url)
    