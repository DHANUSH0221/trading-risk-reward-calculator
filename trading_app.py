import streamlit as st

st.title("My Trading Assistant")

price = st.number_input("Enter current price", min_value=0.0)

if st.button("Analyze"):
    st.write("Current Price:", price)