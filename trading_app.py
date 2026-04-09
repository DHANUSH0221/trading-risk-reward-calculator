import streamlit as st

st.title("Trading Risk Reward Calculator")

price = st.number_input("Enter current price", min_value=0.0)
sl_percent = st.number_input("Enter stop loss %", min_value=0.0)
target_percent = st.number_input("Enter target %", min_value=0.0)

if st.button("Analyze"):
    stop_loss = price * (1 - sl_percent / 100)
    target = price * (1 + target_percent / 100)

    risk = price - stop_loss
    reward = target - price
    rr = reward / risk if risk != 0 else 0

    st.write("Current Price:", price)
    st.write("Stop Loss:", round(stop_loss, 2))
    st.write("Target:", round(target, 2))
    st.write("Risk Reward Ratio:", round(rr, 2))

    if rr >= 1.5:
        st.success("GOOD TRADE")
    else:
        st.error("AVOID TRADE")
